"""Run the extracted student project and independently check the small summary."""
from pathlib import Path
import csv
import json
import statistics
import subprocess
import tempfile
import zipfile

import nbformat
import yaml
from assemble_notebooks import LESSONS, CELL_DISPLAY, read_cells

ROOT = Path(__file__).resolve().parents[1]


def rows(path):
    with path.open(newline="") as file:
        return list(csv.DictReader(file))


def run(code, project):
    result = subprocess.run(
        ["Rscript", "--vanilla", "-e", code], cwd=project,
        text=True, capture_output=True, timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return result.stdout


def main():
    executed = 0
    for name in LESSONS:
        notebook = nbformat.read(ROOT / "chapters" / f"{name}.ipynb", as_version=4)
        code = [cell for cell in notebook.cells if cell.cell_type == "code"]
        source = read_cells(ROOT / "scripts" / f"{name}.R")
        assert [cell.source for cell in code] == list(source.values())
        for cell, key in zip(code, source):
            assert cell.execution_count is not None
            assert not any(output.output_type == "error" for output in cell.outputs)
            assert cell.metadata.get("tags", []) == CELL_DISPLAY.get(name, {}).get(key, [])
        executed += len(code)

    config = yaml.safe_load((ROOT / "myst.yml").read_text())
    chapter_files = config["project"]["toc"][1]["children"]
    assert [entry["file"] for entry in chapter_files] == [
        "chapters/00-start-here.md", *(f"chapters/{name}.ipynb" for name in LESSONS)
    ]
    with tempfile.TemporaryDirectory(prefix="start-from-zero-student-") as temporary:
        with zipfile.ZipFile(ROOT / "downloads/start-from-zero-student.zip") as archive:
            assert archive.testzip() is None
            scripts = [Path(name).name for name in archive.namelist() if "/scripts/" in name]
            assert sorted(scripts) == sorted(f"{name}.R" for name in LESSONS)
            archive.extractall(temporary)
        project = Path(temporary) / "start-from-zero"
        assert (project / "STUDENT_README.txt").read_bytes() == (ROOT / "STUDENT_README.txt").read_bytes()
        practice = project / "data/practice_counts.csv"
        original = practice.read_bytes()
        recorded = [float(row["count_cfu_ml"]) for row in rows(practice) if row["count_cfu_ml"] not in ("", "NA")]
        expected_mean = statistics.mean(recorded)

        for name in LESSONS:
            run((project / "scripts" / f"{name}.R").read_text(), project)
        assert (project / "outputs/practice/first-run.txt").read_text().strip() == "My first successful R run."
        assert len(rows(project / "outputs/practice/known-counts.csv")) == 3
        assert rows(project / "outputs/ch03/summary.csv") == [{
            "missing_n": "1", "recorded_n": "3", "mean_recorded": str(int(expected_mean))
        }]
        error_record = (project / "outputs/ch03/runtime-error-and-repair.txt").read_text()
        assert "object 'milk_data' not found" in error_record and "Repaired recorded-count mean: 20" in error_record
        assert practice.read_bytes() == original

        log = project / "outputs/ch03/ai-use-log.txt"
        log.write_text("My independent study record.\n")
        chapter = (project / "scripts/03-working-with-ai.R").read_text()
        main_route, boundary, _ = chapter.partition("\n# %% capture-missing-object-error\n")
        assert boundary
        (project / "outputs/ch03/runtime-error-and-repair.txt").unlink()
        run(main_route, project)
        assert not (project / "outputs/ch03/runtime-error-and-repair.txt").exists()
        assert log.read_text() == "My independent study record.\n"
        assert practice.read_bytes() == original

    report = {
        "executable_R_cells": executed,
        "student_ZIP_extracted_and_executed": True,
        "summary_independently_checked": True,
        "main_route_completes_without_optional_exercises": True,
        "student_log_and_original_data_preserved": True,
        "table_rows": 4,
        "recorded_mean": expected_mean,
    }
    (ROOT / "validation").mkdir(exist_ok=True)
    (ROOT / "validation/student-check.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

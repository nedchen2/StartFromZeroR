"""Run the R examples printed in the two hands-on pages."""
from pathlib import Path
import json
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = {
    "02-copy-and-run.md": "first-chart.png",
    "03-change-and-save.md": "green-chart.png",
}


def main():
    output = ROOT / "outputs/reference"
    output.mkdir(parents=True, exist_ok=True)
    report = []
    for chapter, image in EXAMPLES.items():
        page = (ROOT / "chapters" / chapter).read_text()
        blocks = re.findall(r"^```r\n(.*?)^```$", page, re.M | re.S)
        assert len(blocks) == 1, f"Expected one complete R example in {chapter}"
        target = (output / image).as_posix()
        code = f'png({json.dumps(target)}, width=1000, height=700, res=140)\n'
        code += blocks[0]
        code += '\nstopifnot(identical(counts, c(10,20,30,40)), mean(counts) == 25)\ndev.off()\n'
        with tempfile.TemporaryDirectory(prefix="first-r-example-") as work:
            result = subprocess.run(
                ["Rscript", "--vanilla", "-e", code], cwd=work,
                text=True, capture_output=True, timeout=30,
            )
        assert result.returncode == 0, result.stdout + result.stderr
        assert "[1] 25" in result.stdout
        assert (output / image).stat().st_size > 1000
        report.append({"chapter": chapter, "mean": 25, "plot": image, "fresh_R_session": True})
        print(f"Verified {chapter}: mean 25 and chart created.")
    validation = ROOT / "validation"
    validation.mkdir(exist_ok=True)
    (validation / "examples-check.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()

"""Package the base-R project for Chapters 1–3."""
from pathlib import Path
import zipfile
from assemble_notebooks import LESSONS

ROOT = Path(__file__).resolve().parents[1]


def package():
    files = [
        ROOT / "start-from-zero.Rproj",
        ROOT / "STUDENT_README.txt",
        ROOT / "data/practice_counts.csv",
        *(ROOT / "scripts" / f"{name}.R" for name in LESSONS),
        *sorted((ROOT / "templates").glob("*.txt")),
    ]
    target = ROOT / "downloads/start-from-zero-student.zip"
    target.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, Path("start-from-zero") / path.relative_to(ROOT))
    print(f"Packaged {len(files)} files for Chapters 1–3.")


if __name__ == "__main__":
    package()

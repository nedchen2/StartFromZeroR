"""Check the public sources of the short guide."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
root_files = {
    ".gitignore", "README.md", "STUDENT_README.txt", "start-from-zero.Rproj",
    "requirements-build.txt", "myst.yml", "intro.md",
}
extensions = {
    "assets": {".svg", ".css"}, "authoring": {".md"}, "chapters": {".md", ".ipynb"},
    "scripts": {".R"}, "templates": {".txt"}, "tools": {".py"},
}
exact = {"assets/favicon.ico", "data/practice_counts.csv", ".github/workflows/deploy.yml"}
files = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
unexpected = []
for name in filter(None, files):
    path = Path(name)
    allowed = name in root_files or name in exact
    if not allowed and len(path.parts) == 2 and path.parts[0] in extensions:
        allowed = path.suffix in extensions[path.parts[0]]
    if not allowed or path.name.startswith("my-"):
        unexpected.append(name)
assert not unexpected, "Unreviewed public paths: " + ", ".join(unexpected)
print("Public source boundaries checked.")

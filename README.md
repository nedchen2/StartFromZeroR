# Start from zero with R and AI

An independent short guide for biology students in **Machine Learning for Food Safety and Toxicology**.

Read the [online guide](https://nedchen2.github.io/StartFromZeroR/) and download the student ZIP from its homepage. Students use R and RStudio. The lessons use base R and a supplied four-row invented dataset.

The guide contains a homepage and Chapters 0–3. Students install the tools, run and save an R script, handle a missing value, and check an AI reply against a hand calculation.

Congjia Chen is the course teaching assistant. The course is led by [Professor Guosheng Yin](https://saasresearch.hku.hk/~gyin/).

This edition is adapted from the Start from zero section of [MicrobialML](https://github.com/nedchen2/MicrobialML), at source commit `2e2dd18c743f9fa0b3472132110c569557f059c8`.

## Build and check

Install the pinned Python requirements in a virtual environment and provide R with IRkernel, plus Node.js 24. Students only need the downloadable R project.

```sh
python tools/check_publication.py
python tools/execute_book.py
python tools/package_student.py
python tools/verify_student.py
BASE_URL=/StartFromZeroR jupyter-book build --html --strict
python tools/verify_html.py --base-url /StartFromZeroR
```

The GitHub Actions workflow runs these checks before publishing the site. Edit prose in `authoring/*.md` and code in `scripts/*.R`. Notebook assembly keeps the web page and downloadable scripts aligned.

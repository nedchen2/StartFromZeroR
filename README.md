# Your first R code with AI

A short guide for biology students in **Machine Learning for Food Safety and Toxicology**.

[Open the guide](https://nedchen2.github.io/StartFromZeroR/)

Students install R and RStudio, ask AI for a mean and bar chart using four invented milk counts, paste and run the code, request one change, and save a single script named `my-first-r.R`.

The guide has a homepage and four short chapters. Each plotting example uses base R.

Congjia Chen is the teaching assistant. The course is led by [Professor Guosheng Yin](https://saasresearch.hku.hk/~gyin/). The [full MicrobialML textbook](https://github.com/nedchen2/MicrobialML) is maintained separately.

## Build and verify

Provide R, Node.js 24 and the pinned Python requirements.

```sh
python tools/check_publication.py
python tools/verify_examples.py
BASE_URL=/StartFromZeroR jupyter-book build --html --strict
python tools/verify_html.py --base-url /StartFromZeroR
```

The R examples in Chapters 2 and 3 are checked directly from their code fences. Verification runs them in fresh R sessions and generates the example chart images used by the pages. GitHub Actions verifies the examples and links before publishing.

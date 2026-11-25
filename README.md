# One Day in One Image — 25 November 2026

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/tpl11295/makefun-news-image-2511-01/rank.svg)](https://make.fun/c/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/tpl11295/makefun-news-image-2511-01/reward.svg)](https://make.fun/c/news-image-20261125)

An entry for the [make.fun bounty "Sum up 25 November's world news in one image"](https://make.fun/c/news-image-20261125).

## The image

One image that sums up Wednesday 25 November 2026, in three panels under a
banner naming the day:

1. **Strait of Hormuz** — two oil tankers struck by naval mines and left
   burning, the day's biggest story.
2. **Markets plunge** — Asian stocks tumble (KOSPI −6.2%, Nikkei −2.8%)
   while the Dow closes above 50,000 for the first time.
3. **Huawei convicted** — a Brooklyn jury finds Huawei guilty of
   conspiring to steal trade secrets and bank fraud.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. The file is a JPEG stored as `entry.png`, which the
bounty rules allow — the image is told apart by its first bytes. The
program runs with no network and writes the same bytes on every run.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

# Make-A-Zine
A small CLI tool to merge any A4 pdf into a foldable zine/booklet.

## Usage
Clone this repository and initialize your virtual environment with [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/bliepp/Make-A-Zine.git
uv sync
```

Make-A-Zine takes a single PDF input file and let's you specify an option output file. If the output is omitted, the resulting PDF will be called `out.pdf`.

```bash
uv run main.py myfile.pdf [output.pdf]
```

## How it works
Make-A-Zine takes any multipage A4 document and makes a foldable A7 zine/booklet for each batch of 8 pages, i.e.:
| Pages | Number of zines/booklets |
| ----- | ------------------------ |
| 1-8   | 1                        |
| 9-16  | 2                        |
| 17-24 | 3                        |
| ...   | ...                      |

Missing pages will be added as blank pages.

## How to fold it
The resulting 8-page zines/booklets can be folded according to the following instructions:
[![](https://cdn.thebigdraw.org/uploads/_article_image/381/Step-by-step-Making-a-Happiness-Zine-GRAPHIC.webp?v=1757502583)](https://www.thebigdraw.org/blog/how-to-make-a-happiness-zine)
(Image source: https://www.thebigdraw.org/blog/how-to-make-a-happiness-zine)

If you prefer a video, here's a nice and short one by VicHealth:
[![YouTube Video](https://img.youtube.com/vi/sMdus-lNqFg/maxresdefault.jpg)](https://www.youtube.com/watch?v=sMdus-lNqFg)

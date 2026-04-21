import math
import sys
from itertools import batched

import click
from pypdf import PageObject, PaperSize, PdfReader, PdfWriter, Transformation
from pypdf.errors import PdfStreamError


def zine8(pages: list[PageObject], writer: PdfWriter):
    for batch in batched(pages, n=8):
        merged_page = writer.add_blank_page(PaperSize.A4.height, PaperSize.A4.width)

        for i, page in enumerate(batch):
            page.rotation += 180 * (1 <= i <= 4)
            page.transfer_rotation_to_content()

            y = page.trimbox.height * (1 <= i <= 4)  # lower row
            x = (
                page.trimbox.width * 3 * (i == 0 or i == 1)
                + page.trimbox.width * 2 * (i == 2 or i == 7)
                + page.trimbox.width * 1 * (i == 3 or i == 6)
                + page.trimbox.width * 0 * (i == 4 or i == 5)
            )
            t = (
                Transformation()
                .translate(x, y)
                .scale(
                    1 / (2 * math.sqrt(2)),
                    1 / (2 * math.sqrt(2)),
                )
            )

            merged_page.merge_transformed_page(page, t)


@click.command(
    context_settings=dict(
        help_option_names=["-h", "--help"],
    )
)
@click.argument("input", type=click.File("rb"))
@click.argument("output", type=click.File("wb"), default="out.pdf")
def cli(input, output):
    try:
        reader = PdfReader(input)
    except PdfStreamError:
        click.echo("Invalid PDF", err=True)
        sys.exit(1)

    out = PdfWriter()
    zine8(reader.pages, out)
    out.write(output)


if __name__ == "__main__":
    cli()

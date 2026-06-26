import pymupdf4llm
from pathlib import Path


def pdf_to_markdown(pdf_file):
    markdown = pymupdf4llm.to_markdown(pdf_file)

    output = Path("extracted")
    output.mkdir(exist_ok=True)

    md_file = output / f"{Path(pdf_file).stem}.md"

    md_file.write_text(markdown, encoding="utf-8")

    return str(md_file)

import pymupdf4llm
from pathlib import Path

def pdf_to_markdown(pdf_file):
    markdown = pymupdf4llm.to_markdown(pdf_file)

    Path("extracted").mkdir(exist_ok=True)

    output_file = f"extracted/{Path(pdf_file).stem}.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)

    return output_file

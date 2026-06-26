from pathlib import Path

from extractor import pdf_to_markdown
from chunker import split_sections
from retriever import Retriever
from llm import ask_llm


PDF_PATH = "documents/Machine_Learning_Report.pdf"

md_file = pdf_to_markdown(PDF_PATH)

markdown = Path(md_file).read_text(
    encoding="utf-8"
)

sections = split_sections(markdown)

retriever = Retriever(sections)

print("Document loaded successfully!")

while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    context = "\n\n".join(
        retriever.search(question)
    )

    answer = ask_llm(
        question,
        context
    )

    print("\nAnswer:")
    print(answer)

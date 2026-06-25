import streamlit as st
from pathlib import Path

from src.extractor import pdf_to_markdown
from src.chunker import split_sections
from src.retriever import Retriever
from src.llm import ask_llm

st.title("📚 Local PDF Q&A")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file:

    Path("documents").mkdir(exist_ok=True)

    pdf_path = f"documents/{uploaded_file.name}"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    md_file = pdf_to_markdown(pdf_path)

    markdown = Path(md_file).read_text(
        encoding="utf-8"
    )

    sections = split_sections(markdown)

    retriever = Retriever(sections)

    question = st.text_input(
        "Ask a question"
    )

    if question:

        context = "\n\n".join(
            retriever.search(question)
        )

        answer = ask_llm(
            question,
            context
        )

        st.write(answer)

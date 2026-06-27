from pathlib import Path
import streamlit as st

from src.extractor import pdf_to_markdown
from src.chunker import split_sections
from src.retriever import Retriever
from src.llm import ask_llm

st.set_page_config(
    page_title="📄 Local Document Q&A",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Local Document Q&A")
st.write("Upload any PDF and ask questions.")

Path("documents").mkdir(exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf_path = f"documents/{uploaded_file.name}"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Extracting document..."):

        md_file = pdf_to_markdown(pdf_path)

        markdown = Path(md_file).read_text(
            encoding="utf-8"
        )

        sections = split_sections(markdown)

        retriever = Retriever(sections)

    st.success("PDF processed successfully!")

    question = st.text_input(
        "Ask your question"
    )

    if question:

        with st.spinner("Thinking..."):

            context = "\n\n".join(
                retriever.search(question)
            )

            answer = ask_llm(
                question,
                context
            )

        st.subheader("Answer")

        st.write(answer)

        with st.expander("Retrieved Context"):

            st.write(context)

import streamlit as st
from pathlib import Path

from src.extractor import pdf_to_markdown
from src.chunker import split_sections
from src.retriever import Retriever
from src.llm import ask_llm

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Local Document Q&A",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Local Document Q&A")
st.write("Upload a PDF and ask questions about its contents.")

# Create required folders
Path("documents").mkdir(exist_ok=True)
Path("extracted").mkdir(exist_ok=True)

# -------------------------------
# Upload PDF
# -------------------------------
uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf_path = Path("documents") / uploaded_file.name

    # Save uploaded PDF
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Uploaded: {uploaded_file.name}")

    # Process PDF only once
    if "retriever" not in st.session_state or st.session_state.get("current_pdf") != uploaded_file.name:

        with st.spinner("Extracting and indexing document..."):

            md_file = pdf_to_markdown(str(pdf_path))

            markdown = Path(md_file).read_text(
                encoding="utf-8"
            )

            sections = split_sections(markdown)

            st.session_state.retriever = Retriever(sections)
            st.session_state.current_pdf = uploaded_file.name

        st.success("Document processed successfully!")

    # -------------------------------
    # Ask Question
    # -------------------------------
    question = st.text_input(
        "Ask a question"
    )

    if question:

        retriever = st.session_state.retriever

        context = "\n\n".join(
            retriever.search(question)
        )

        with st.spinner("Generating answer..."):

            answer = ask_llm(
                question,
                context
            )

        st.subheader("Answer")
        st.write(answer)

        with st.expander("Retrieved Context"):
            st.write(context)

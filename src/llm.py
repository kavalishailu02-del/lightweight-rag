import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def ask_llm(question, context):

    prompt = f"""
You are a helpful document assistant.

Answer ONLY using the context below.

If the answer is not present in the context,
say "The answer is not available in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=512,
    )

    return response.choices[0].message.content

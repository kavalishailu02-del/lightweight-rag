from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_llm(context, question):
    prompt = f"""
You are a helpful document assistant.

Use ONLY the information below to answer.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
"I couldn't find that information in the document."
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content

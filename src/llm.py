from llama_cpp import Llama


llm = Llama(
    model_path="models/Qwen2.5-3B-Instruct-Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=8,
    verbose=False
)


def ask_llm(question, context):

    prompt = f"""
You are a document assistant.

Use ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    output = llm(
        prompt,
        max_tokens=512,
        temperature=0.1
    )

    return output["choices"][0]["text"]

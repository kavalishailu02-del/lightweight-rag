from llama_cpp import Llama

llm = Llama(
    model_path="models/Qwen2.5-3B-Instruct-Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=4,
    verbose=False
)

def ask_llm(question, context):

    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    output = llm(
        prompt,
        max_tokens=256,
        temperature=0.1
    )

    return output["choices"][0]["text"]

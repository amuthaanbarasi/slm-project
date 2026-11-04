
import ollama

MODEL_NAME = "qwen2.5:1.5b"


def generate_answer(question, context):
    system_prompt = """
You are a professional General FAQ Assistant.

Follow these rules:
1. Answer using only the provided FAQ information.
2. Do not invent facts or add unsupported information.
3. If the information is insufficient, say:
   "I do not have enough information to answer this question."
4. Use simple English.
5. Keep answers clear, relevant, and concise.
6. Avoid unnecessary explanations.
"""

    response = ollama.generate(
        model=MODEL_NAME,
        system=system_prompt,
        prompt=f"""
FAQ Information:
{context}

User Question:
{question}

Answer:
"""
    )

    return response["response"].strip()

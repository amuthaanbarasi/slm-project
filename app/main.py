from fastapi import FastAPI
from pydantic import BaseModel
from app.faq_engine import find_answer
from app.llm_engine import generate_answer

app = FastAPI(
    title="SLM General FAQ Assistant",
    description="A FAQ Assistant powered by Qwen2.5 1.5B",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Welcome to the SLM General FAQ Assistant"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    question = request.question

    context = find_answer(question)

    if context.startswith("Sorry"):
        return {"question": question, "answer": context}

    answer = generate_answer(question, context)

    return {
        "question": question,
        "answer": answer
    }
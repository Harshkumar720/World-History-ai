from fastapi import APIRouter
from ai_engine import ask_history_ai

router = APIRouter()

@router.get("/chat")

def chat(question: str):
    answer = ask_history_ai(question)
    
    return {
        "question": question,
        "answer": answer
    }
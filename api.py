from fastapi import FastAPI
from pydantic import BaseModel
from app.chat import get_answer

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    answer = get_answer(req.question)
    return ChatResponse(answer=answer)

@app.get("/health")
def health():
    return {"status": "ok"}

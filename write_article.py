from fastapi import FastAPI
from llm_service import call_gemini,close_conversation
from pydantic import BaseModel
app = FastAPI()

class UserInput(BaseModel):
    message: str
    session_id: str

@app.post("/generate_article")
async def generate_article(user_input: UserInput):
    """
    Endpoint to generate an article based on user input.
    """
    if user_input.message.lower() == "exit":
        return {"message": "Exiting the conversation."}
    if user_input.message.lower() == "reset":
        close_conversation(user_input.session_id)
        return {"message": "Conversation reset."}
    
    response = call_gemini(user_input.session_id, "generate_article", context_vars={"userInput": user_input.message})
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=4000)


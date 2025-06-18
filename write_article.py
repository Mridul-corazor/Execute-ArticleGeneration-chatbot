from fastapi import FastAPI
from llm_service import call_gemini,close_conversation
from pydantic import BaseModel
import logging
app = FastAPI()
logging.basicConfig(level=logging.INFO)
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
        logging.info(f"Resetting conversation for session {user_input.session_id}")
        close_conversation(user_input.session_id)
        return {"message": "Conversation reset."}
    logging.info(f"Received message: {user_input.message} for session {user_input.session_id}")
    response = call_gemini(user_input.session_id, "generate_article", context_vars={"userInput": user_input.message})
    logging.info(f"Response from Gemini: {response}")
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=4000)


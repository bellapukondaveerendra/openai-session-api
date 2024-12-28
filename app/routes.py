from fastapi import APIRouter,HTTPException
from uuid import uuid4
from app.db import sessions_collection
import openai
from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv()

#loads open_ai API key
openai.api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

# Pydantic model for the chat request
class ChatRequest(BaseModel):
    sessionId: str
    message: str

@router.post("/session")
def create_session():
    # Generate a unique sessionId
    session_id = str(uuid4())
    # Insert session into the database
    sessions_collection.insert_one({"sessionId": session_id, "history": []})
    return {"sessionId": session_id}


@router.post("/chat")
def send_message(request: ChatRequest):
    sessionId = request.sessionId
    message = request.message
    # Fetch session from the database
    session = sessions_collection.find_one({"sessionId": sessionId})
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Append user message to history
    history = session["history"]
    history.append({"role": "user", "content": message})

    # Create prompt for OpenAI
    messages = [{"role": h["role"], "content": h["content"]} for h in history]
    # Call OpenAI API
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Use the appropriate model
            messages=messages
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Get assistant's response
    bot_response = response.choices[0].message.content


    history.append({"role": "assistant", "content": bot_response})

    # Update session in the database
    sessions_collection.update_one(
        {"sessionId": sessionId},
        {"$set": {"history": history}}
    )

    return {"response": bot_response}

@router.get("/session/{sessionId}/history")
def get_history(sessionId: str):
    # Fetch session from the database
    session = sessions_collection.find_one({"sessionId": sessionId})
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"sessionId": sessionId, "history": session["history"]}

@router.get("/")
def read_root():
    return {"message": "Welcome to the OpenAI Session API!"}
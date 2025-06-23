from pydantic import BaseModel

class MessageRequest(BaseModel):
    chat_id: str
    message: str

class MessageResponse(BaseModel):
    response: str
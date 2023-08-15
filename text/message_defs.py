from pydantic import BaseModel
from enum import Enum



class Message(BaseModel):
    role: str
    content: str

class StoredMessage(BaseModel):
    message: Message
    message_type: str

class PromptChainMessage(StoredMessage):
    history_message: StoredMessage
    message_title: str
    message_description: str

class PersonaMessage(StoredMessage):
    prompt_chain_message: PromptChainMessage
    persona_avatar: str
    
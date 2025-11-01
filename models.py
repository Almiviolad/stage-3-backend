from pydantic import BaseModel, ConfigDict
from typing import Optional, List # <-- We need 'List'
from datetime import datetime

class NoteCreate(BaseModel):
    """data recieved to create a note and start spaced review"""
    user_id:str
    note_content:str
    
class NoteReview(BaseModel):
    """user sends this to shiw their masterybofntye note"""
    mastery_level: str

class FlashCard(BadeModel):
    """pydantic model for a flashcard"""
    question: str
    answer: str

    model_config = ConfigDict(from_attrivutes=True)

class NoteResponse(BaseModel):
    """sta sent to telex as output"""
    id: str
    content: str
    flashcards: list[dict]
    review_at: datetime

    model_config = ConfigDict(from_attribut
es=True)

# database.py
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship # <-- Import 'relationship' and 'ForeignKey'
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db") 
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class NoteDB(Base):
    """
    This is the PARENT "Note" or "Chapter" model.
    The spaced repetition logic lives here.
    """
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    title = Column(String, nullable=False) # The AI-generated title
    review_at = Column(DateTime, nullable=False, index=True)
    current_interval = Column(Float, default=1.0)
    flashcards = relationship("FlashcardDB", back_populates="note")


class FlashcardDB(Base):
    """
    This is the CHILD "Flashcard" or "Page" model.
    """
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    note_id = Column(Integer, ForeignKey("notes.id"))
    note = relationship("NoteDB", back_populates="flashcards")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db_tables():
    """This will now create BOTH tables."""
    Base.metadata.create_all(bind=engine)

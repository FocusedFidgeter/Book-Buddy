from sqlmodel import SQLModel, create_engine
from pathlib import Path
import os

# Get the absolute path to the database file
DB_DIR = Path(__file__).parent.parent.parent / "data"
DB_FILE = DB_DIR / "book_buddy.db"

# Create data directory if it doesn't exist
DB_DIR.mkdir(exist_ok=True)

# Database URL
DATABASE_URL = f"sqlite:///{DB_FILE}"

# Create engine with echo for debugging
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    """Initialize the database, creating all tables."""
    # Import all models to ensure they're registered
    from .models import (
        User,
        Book,
        ReadingProgress,
        KnowledgeNode,
        KnowledgeRelationship,
        ChatMessage,
    )
    
    # Create all tables
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    print("Creating database tables...")
    init_db()
    print(f"Database initialized at: {DB_FILE}")

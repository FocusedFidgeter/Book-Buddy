from datetime import datetime
from sqlmodel import Session, create_engine
from pathlib import Path
from .models import User, Book, ReadingProgress, KnowledgeNode, KnowledgeRelationship, ChatMessage
import bcrypt

# Get the absolute path to the database file
DB_DIR = Path(__file__).parent.parent.parent / "data"
DB_FILE = DB_DIR / "book_buddy.db"
DATABASE_URL = f"sqlite:///{DB_FILE}"

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def create_seed_data():
    """Create initial seed data for testing."""
    engine = create_engine(DATABASE_URL, echo=True)
    
    with Session(engine) as session:
        # Create test users
        users = [
            User(
                email="alice@example.com",
                hashed_password=hash_password("password123"),
                name="Alice Johnson"
            ),
            User(
                email="bob@example.com",
                hashed_password=hash_password("password456"),
                name="Bob Smith"
            )
        ]
        session.add_all(users)
        session.commit()
        
        # Create test books
        books = [
            Book(
                title="The Great Gatsby",
                author="F. Scott Fitzgerald",
                total_chapters=9,
                description="A story of decadence and excess.",
                publication_year=1925
            ),
            Book(
                title="1984",
                author="George Orwell",
                total_chapters=23,
                description="A dystopian social science fiction.",
                publication_year=1949
            )
        ]
        session.add_all(books)
        session.commit()
        
        # Create reading progress
        reading_progress = [
            ReadingProgress(
                user_id=users[0].id,
                book_id=books[0].id,
                current_chapter=3
            ),
            ReadingProgress(
                user_id=users[1].id,
                book_id=books[1].id,
                current_chapter=5
            )
        ]
        session.add_all(reading_progress)
        session.commit()
        
        # Create knowledge nodes
        nodes = [
            KnowledgeNode(
                book_id=books[0].id,
                chapter=1,
                content="Nick Carraway moves to New York and becomes Gatsby's neighbor.",
                context="Setting and initial character introduction"
            ),
            KnowledgeNode(
                book_id=books[0].id,
                chapter=2,
                content="Introduction to the Valley of Ashes and George Wilson's garage.",
                context="Setting development"
            ),
            KnowledgeNode(
                book_id=books[1].id,
                chapter=1,
                content="Winston Smith begins his diary.",
                context="Character introduction"
            )
        ]
        session.add_all(nodes)
        session.commit()
        
        # Create relationships between knowledge nodes
        relationships = [
            KnowledgeRelationship(
                source_node_id=nodes[0].id,
                target_node_id=nodes[1].id,
                relationship_type="leads_to"
            )
        ]
        session.add_all(relationships)
        session.commit()
        
        # Create some chat messages
        messages = [
            ChatMessage(
                user_id=users[0].id,
                content="What happens in chapter 1 of The Great Gatsby?",
                is_user_message=True
            ),
            ChatMessage(
                user_id=users[0].id,
                content="In Chapter 1, Nick Carraway moves to West Egg, Long Island...",
                is_user_message=False
            )
        ]
        session.add_all(messages)
        session.commit()

if __name__ == "__main__":
    create_seed_data()

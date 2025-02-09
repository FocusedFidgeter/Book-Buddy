from datetime import datetime, UTC
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    """User model for authentication and profile information."""
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    
    # Relationships
    reading_progress: List["ReadingProgress"] = Relationship(back_populates="user")
    chat_history: List["ChatMessage"] = Relationship(back_populates="user")

class Book(SQLModel, table=True):
    """Book model containing metadata and content information."""
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str
    total_chapters: int
    description: str
    publication_year: Optional[int] = None
    
    # Relationships
    reading_progress: List["ReadingProgress"] = Relationship(back_populates="book")
    knowledge_nodes: List["KnowledgeNode"] = Relationship(back_populates="book")

class ReadingProgress(SQLModel, table=True):
    """Tracks a user's reading progress for a specific book."""
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    book_id: int = Field(foreign_key="book.id")
    current_chapter: int
    last_updated: datetime = Field(default_factory=lambda: datetime.now(UTC))
    
    # Relationships
    user: User = Relationship(back_populates="reading_progress")
    book: Book = Relationship(back_populates="reading_progress")

class KnowledgeNode(SQLModel, table=True):
    """Represents a single piece of knowledge about a book."""
    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="book.id")
    chapter: int = Field(index=True)  # For efficient chapter-based queries
    content: str  # The actual knowledge/fact about the book
    context: Optional[str] = None  # Additional context or metadata
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    
    # Relationships
    book: Book = Relationship(back_populates="knowledge_nodes")
    source_relationships: List["KnowledgeRelationship"] = Relationship(
        back_populates="source_node",
        sa_relationship_kwargs={"foreign_keys": "[KnowledgeRelationship.source_node_id]"}
    )
    target_relationships: List["KnowledgeRelationship"] = Relationship(
        back_populates="target_node",
        sa_relationship_kwargs={"foreign_keys": "[KnowledgeRelationship.target_node_id]"}
    )

class KnowledgeRelationship(SQLModel, table=True):
    """Represents a relationship between two knowledge nodes."""
    id: Optional[int] = Field(default=None, primary_key=True)
    source_node_id: int = Field(foreign_key="knowledgenode.id")
    target_node_id: int = Field(foreign_key="knowledgenode.id")
    relationship_type: str  # e.g., "references", "contradicts", "builds_upon"
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    
    # Relationships
    source_node: KnowledgeNode = Relationship(
        back_populates="source_relationships",
        sa_relationship_kwargs={"foreign_keys": "[KnowledgeRelationship.source_node_id]"}
    )
    target_node: KnowledgeNode = Relationship(
        back_populates="target_relationships",
        sa_relationship_kwargs={"foreign_keys": "[KnowledgeRelationship.target_node_id]"}
    )

class ChatMessage(SQLModel, table=True):
    """Stores chat messages between users and the AI."""
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    content: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    is_user_message: bool = True  # False for bot responses
    
    # Relationships
    user: User = Relationship(back_populates="chat_history")

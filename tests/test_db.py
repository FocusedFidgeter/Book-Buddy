import pytest
from sqlmodel import Session, SQLModel, create_engine, select
from datetime import datetime, UTC
from book_buddy.db.models import User, Book, ReadingProgress, KnowledgeNode, KnowledgeRelationship, ChatMessage


@pytest.fixture
def db_session():
    """Create a new database session for testing."""
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_db_connection(db_session):
    """Test that we can connect to the database."""
    try:
        # Simple query to verify connection
        result = db_session.exec(select(User)).first()
        assert isinstance(result, User) or result is None
    except Exception as e:
        pytest.fail(f"Failed to connect to database: {str(e)}")

def test_user_operations(db_session):
    """Test basic user operations."""
    test_user = User(
        email='test@example.com',
        hashed_password='hashed_test_password',
        name='Test User'
    )
    
    try:
        # Create test user
        db_session.add(test_user)
        db_session.commit()
        db_session.refresh(test_user)
        assert test_user.id is not None, "Failed to insert test user"
        
        # Read user data
        queried_user = db_session.exec(select(User).where(User.id == test_user.id)).first()
        assert queried_user.email == test_user.email
        assert queried_user.name == test_user.name
        
        # Update user data
        queried_user.name = 'Updated Test User'
        db_session.commit()
        db_session.refresh(queried_user)
        assert queried_user.name == 'Updated Test User'
        
        # Delete test user
        db_session.delete(queried_user)
        db_session.commit()
        deleted_user = db_session.exec(select(User).where(User.id == test_user.id)).first()
        assert deleted_user is None, "Failed to delete test user"
        
    except Exception as e:
        pytest.fail(f"User operations test failed: {str(e)}")

def test_book_progress_tracking(db_session):
    """Test book progress tracking operations."""
    # Create test user and book first
    test_user = User(
        email='test@example.com',
        hashed_password='hashed_test_password',
        name='Test User'
    )
    test_book = Book(
        title='Test Book',
        author='Test Author',
        total_chapters=10,
        description='Test Description'
    )
    
    try:
        # Add user and book
        db_session.add(test_user)
        db_session.add(test_book)
        db_session.commit()
        db_session.refresh(test_user)
        db_session.refresh(test_book)
        
        # Create reading progress
        test_progress = ReadingProgress(
            user_id=test_user.id,
            book_id=test_book.id,
            current_chapter=1
        )
        
        # Insert progress
        db_session.add(test_progress)
        db_session.commit()
        db_session.refresh(test_progress)
        assert test_progress.id is not None, "Failed to insert reading progress"
        
        # Update progress
        test_progress.current_chapter = 2
        db_session.commit()
        db_session.refresh(test_progress)
        assert test_progress.current_chapter == 2
        
        # Clean up
        db_session.delete(test_progress)
        db_session.delete(test_book)
        db_session.delete(test_user)
        db_session.commit()
        
    except Exception as e:
        pytest.fail(f"Book progress tracking test failed: {str(e)}")

def test_knowledge_node_operations(db_session):
    """Test knowledge node and relationship operations."""
    # Create test book first
    test_book = Book(
        title='Test Book',
        author='Test Author',
        total_chapters=10,
        description='Test Description'
    )
    
    try:
        # Add book
        db_session.add(test_book)
        db_session.commit()
        db_session.refresh(test_book)
        
        # Create knowledge nodes
        node1 = KnowledgeNode(
            book_id=test_book.id,
            chapter=1,
            content='Test knowledge 1',
            context='Test context 1'
        )
        node2 = KnowledgeNode(
            book_id=test_book.id,
            chapter=2,
            content='Test knowledge 2',
            context='Test context 2'
        )
        
        # Add nodes
        db_session.add(node1)
        db_session.add(node2)
        db_session.commit()
        db_session.refresh(node1)
        db_session.refresh(node2)
        
        # Create relationship
        relationship = KnowledgeRelationship(
            source_node_id=node1.id,
            target_node_id=node2.id,
            relationship_type='references'
        )
        
        # Add relationship
        db_session.add(relationship)
        db_session.commit()
        db_session.refresh(relationship)
        
        # Verify relationship
        assert relationship.source_node.content == 'Test knowledge 1'
        assert relationship.target_node.content == 'Test knowledge 2'
        
        # Clean up
        db_session.delete(relationship)
        db_session.delete(node1)
        db_session.delete(node2)
        db_session.delete(test_book)
        db_session.commit()
        
    except Exception as e:
        pytest.fail(f"Knowledge node operations test failed: {str(e)}")

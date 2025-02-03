import pytest
from postgrest import AsyncPostgrestClient
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

@pytest.fixture
async def db_client() -> AsyncPostgrestClient:
    """Create a PostgREST client for testing."""
    url = os.getenv("POSTGREST_URL")
    if not url:
        pytest.skip("PostgREST URL not found in environment")
    return AsyncPostgrestClient(url)

@pytest.mark.asyncio
async def test_db_connection(db_client):
    """Test that we can connect to the database."""
    try:
        # Simple query to verify connection
        response = await db_client.from_("users").select("*").limit(1).execute()
        assert isinstance(response.data, list)
    except Exception as e:
        pytest.fail(f"Failed to connect to database: {str(e)}")

@pytest.mark.asyncio
async def test_user_operations(db_client):
    """Test basic user operations."""
    test_user = {
        'email': 'test@example.com',
        'reading_preferences': {'favorite_genre': 'fiction'}
    }
    
    try:
        # Create test user
        response = await db_client.from_("users").insert(test_user).execute()
        assert response.data, "Failed to insert test user"
        
        # Get the inserted user's ID
        user_id = response.data[0]['id']
        
        # Read user data
        response = await db_client.from_("users").select("*").eq('id', user_id).execute()
        assert response.data[0]['email'] == test_user['email']
        
        # Update user data
        updated_prefs = {'favorite_genre': 'mystery'}
        response = await db_client.from_("users")\
            .update({'reading_preferences': updated_prefs})\
            .eq('id', user_id)\
            .execute()
        assert response.data[0]['reading_preferences'] == updated_prefs
        
        # Delete test user
        response = await db_client.from_("users").delete().eq('id', user_id).execute()
        assert response.data, "Failed to delete test user"
        
    except Exception as e:
        pytest.fail(f"User operations test failed: {str(e)}")

@pytest.mark.asyncio
async def test_book_progress_tracking(db_client):
    """Test book progress tracking operations."""
    test_progress = {
        'user_id': 'test-user-id',
        'book_id': 'test-book-id',
        'current_chapter': 1,
        'last_page_read': 25,
        'completion_percentage': 10.5
    }
    
    try:
        # Insert progress
        response = await db_client.from_("reading_progress").insert(test_progress).execute()
        assert response.data, "Failed to insert reading progress"
        
        progress_id = response.data[0]['id']
        
        # Update progress
        updated_progress = {'current_chapter': 2, 'last_page_read': 50, 'completion_percentage': 21.0}
        response = await db_client.from_("reading_progress")\
            .update(updated_progress)\
            .eq('id', progress_id)\
            .execute()
        assert response.data[0]['current_chapter'] == updated_progress['current_chapter']
        
        # Clean up
        response = await db_client.from_("reading_progress").delete().eq('id', progress_id).execute()
        assert response.data, "Failed to delete test progress"
        
    except Exception as e:
        pytest.fail(f"Book progress tracking test failed: {str(e)}")

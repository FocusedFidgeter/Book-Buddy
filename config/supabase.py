import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase: Client = create_client(
    supabase_url=os.getenv("SUPABASE_URL"),
    supabase_key=os.getenv("SUPABASE_KEY")
)

def get_supabase() -> Client:
    """
    Get the Supabase client instance.
    Returns:
        Client: Supabase client instance
    """
    return supabase

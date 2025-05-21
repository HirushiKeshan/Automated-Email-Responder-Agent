# src/config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def validate_env():
    """Ensure all required environment variables are set."""
    missing = []
    if not GEMINI_API_KEY:
        missing.append("GEMINI_API_KEY")
    if not EMAIL_ID:
        missing.append("EMAIL_ID")
    if not EMAIL_PASSWORD:
        missing.append("EMAIL_PASSWORD")
    
    if missing:
        raise EnvironmentError(
            f"❌ Missing required environment variables: {', '.join(missing)}"
        )

if __name__ == "__main__":
    try:
        validate_env()
        print("✅ All required environment variables are set.")
    except EnvironmentError as e:
        print(str(e))

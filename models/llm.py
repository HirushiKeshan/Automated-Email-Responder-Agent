# models/llm.py

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the LLM once (optional optimization)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # or "gemini-1.5-pro"
    google_api_key=os.getenv("GEMINI_API_KEY")
)

def call_gemini(prompt: str) -> str:
    try:
        response = llm.invoke(prompt)
        # Handle response that could be an AIMessage or plain string
        if hasattr(response, "content"):
            return response.content.strip()
        return str(response).strip()
    except Exception as e:
        return f"❌ Error calling Gemini: {str(e)}"

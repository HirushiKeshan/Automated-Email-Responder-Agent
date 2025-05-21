from models.llm import call_gemini

def generate_reply(email_text: str, category: str) -> str:
    prompt = f"""
You are an AI assistant tasked with drafting a polite, professional, and concise email reply based on the following category: '{category}'.

Email content:
{email_text.strip()}

Please generate a suitable reply.
"""
    try:
        response = call_gemini(prompt)
        if hasattr(response, "content"):
            return response.content.strip()
        return str(response).strip()
    except Exception as e:
        return f"❌ Error generating reply: {str(e)}"

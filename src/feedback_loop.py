from models.llm import call_gemini

def refine_reply(original_reply: str, user_feedback: str) -> str:
    prompt = f"""
You are an assistant that improves email replies.

Original AI-generated email reply:
{original_reply.strip()}

User feedback:
{user_feedback.strip()}

Please refine the reply based on the feedback and make it clear, polite, and professional.
"""
    try:
        response = call_gemini(prompt)
        # If response is an object with .content, get it; otherwise, str
        if hasattr(response, "content"):
            return response.content.strip()
        return str(response).strip()
    except Exception as e:
        return f"❌ Error refining reply: {str(e)}"

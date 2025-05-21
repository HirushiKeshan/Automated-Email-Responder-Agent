# src/classifier.py
from models.llm import call_gemini

def classify_email(email_text: str) -> str:
    prompt = f"""
    Classify the following email into one of these categories:
    ['Job Inquiry', 'Meeting Request', 'Spam', 'Support Query', 'General']

    Email:
    {email_text}

    Just return the category name without any extra text.
    """
    response = call_gemini(prompt)
    # Gemini might return with newlines or quotes; clean it:
    if hasattr(response, "content"):
        category = response.content.strip()
    else:
        category = str(response).strip()

    # Normalize output - just return the category word, fix common issues:
    # For example: remove quotes or trailing punctuation
    category = category.strip(' "\'').split('\n')[0]

    # Optional: Validate category is one of the expected list
    valid_categories = ['Job Inquiry', 'Meeting Request', 'Spam', 'Support Query', 'General']
    if category not in valid_categories:
        category = "General"  # fallback category

    return category

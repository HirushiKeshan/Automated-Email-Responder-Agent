from src.email_reader import read_unread_emails
from src.classifier import classify_email
from src.responder import generate_reply
from src.feedback_loop import refine_reply
import textwrap

class EmailProcessor:
    @staticmethod
    def format_email_output(email_data):
        """Format structured email or string for display"""
        if isinstance(email_data, str):
            return f"\n📩 Raw Email Content:\n{'-'*40}\n{email_data}\n{'-'*40}"
        
        return f"""
📩 Email Received
{'-'*40}
From: {email_data.get('from', 'Unknown')}
Subject: {email_data.get('subject', 'No Subject')}
Date: {email_data.get('date', 'Unknown')}

Content Preview:
{textwrap.shorten(email_data.get('body', ''), width=100, placeholder='...')}
{'-'*40}
"""

    @staticmethod
    def format_reply_output(reply_text, is_refined=False):
        label = "✉️ Refined Reply" if is_refined else "✉️ Draft Reply"
        return f"\n{label}\n{'-'*40}\n{reply_text.strip()}\n{'-'*40}"


def main():
    print("\n" + "=" * 50)
    print("🚀 Automated Email Responder Agent - Initializing")
    print("=" * 50 + "\n")

    try:
        emails = read_unread_emails()
        if not emails:
            print("✅ No unread emails found.")
            return

        for email in emails:
            try:
                print(EmailProcessor.format_email_output(email))

                # Wrap raw string emails
                if isinstance(email, str):
                    print("⚠️ Warning: Email is raw string, wrapping for processing...")
                    email = {
                        'from': 'Unknown',
                        'subject': 'No Subject',
                        'date': 'Unknown',
                        'body': email
                    }

                body = email.get('body', '')

                # Classification
                category_result = classify_email(body)
                category = category_result.content.strip() if hasattr(category_result, "content") else str(category_result).strip()
                print(f"🧠 Classification: {category}\n")

                # Generate Reply
                draft_result = generate_reply(body, category)
                draft_reply = draft_result.content.strip() if hasattr(draft_result, "content") else str(draft_result).strip()
                print(EmailProcessor.format_reply_output(draft_reply))

                # Feedback
                feedback = input("💬 Any feedback to improve the reply? (Press enter to send as-is): ").strip()
                if feedback:
                    refined_result = refine_reply(draft_reply, feedback)
                    refined_reply = refined_result.content.strip() if hasattr(refined_result, "content") else str(refined_result).strip()
                    print(EmailProcessor.format_reply_output(refined_reply, is_refined=True))

            except Exception as e:
                print(f"⚠️ Error processing email: {str(e)}")
                continue

    except KeyboardInterrupt:
        print("\n🛑 Operation cancelled by user.")
    except Exception as e:
        print(f"\n❌ Critical error: {str(e)}")
    finally:
        print("\n" + "=" * 50)
        print("🏁 Email processing complete")
        print("=" * 50)

if __name__ == "__main__":
    main()

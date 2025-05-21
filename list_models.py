from langchain_google_genai import GoogleGenerativeAI

def main():
    # Replace with your actual API key
    api_key = "YOUR_API_KEY"

    # Create the client with any model (required by the constructor)
    client = GoogleGenerativeAI(
        model="chat-bison-001",
        google_api_key=api_key
    )

    try:
        models = client.client.list_models()
        print("Available models:")
        for model in models:
            print(model)
    except Exception as e:
        print("Error fetching models:", e)

if __name__ == "__main__":
    main()

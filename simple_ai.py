from langchain.chat_models import init_chat_model

GOOGLE_API_KEY = "AIzaSyBu2ROrbLS9zQyfViL-bIyb9gftOh7qYpA"

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)

response = model.invoke("Is a pen better than a pencil?")

response_str = response.content[0]['text']
print(response_str)
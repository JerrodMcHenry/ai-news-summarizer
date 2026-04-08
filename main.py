import requests
from send_email import send_email
from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model


load_dotenv()

news_api_key = os.getenv("NEWS_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")


url = "https://newsapi.org/v2/top-headlines?" \
"country=us&" \
"category=business&" \
"language=en&" \
"pageSize=8&" \
"apiKey=" + news_api_key


# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
articles = content["articles"]


# AI summarizing the news
model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key=google_api_key
)

prompt = f"""
You're a news summarizer.
Write a short paragraph analyzing those news. 
Add another second paragraph to tell me 
how ther affect the stock martket. 
Here are the news articles:
{articles}
"""

response = model.invoke(prompt)
response_str = response.content
print(response_str)

body = "Subject: News Summary\n\n" + response_str + "\n\n"
send_email(message=body)
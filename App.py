from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)

# OpenAI API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_query_gpt(question):
response = openai.ChatCompletion.create(
model="gpt-4",
messages=[
{"role": "system", "content": "You are a sports betting expert. Give current predictions."},
{"role": "user", "content": question}
]
)
return response.choices[0].message.content.strip()

@app.route("/bot", methods=["POST"])
def bot():
msg = request.values.get('Body', '').lower()
resp = MessagingResponse()
message = resp.message()

if 'bet' in msg:
response = chat_query_gpt("Give me a sports betting prediction for today.")
message.body(response)
else:
message.body("Enter 'bet' for a smart prediction.")

return str(resp)

if __name__ == "__main__":
app.run()
Enter file contents here
 

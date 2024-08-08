from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from slacker.config import SLACK_BOT_TOKEN, CHANNEL_ID, BOT_NAME

# Initialize a WebClient instance with your OAuth token
client = WebClient(token=SLACK_BOT_TOKEN)

def send_message(*args):
    message = " ".join(map(str, args))
    try:
        # Use the chat.postMessage method to send a message to the channel
        response = client.chat_postMessage(channel=CHANNEL_ID, text=message,username=BOT_NAME)
        print("Message sent successfully!")
    except SlackApiError as e:
        # Error handling in case the message fails to send
        print(f"Error sending message: {e}")

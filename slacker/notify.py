from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
# Initialize a WebClient instance with your OAuth token
client = WebClient(token=SLACK_BOT_TOKEN)

# The channel ID or name where you want to send the message
channel_id = "D07AWGQK821"

# The bot name 
bot_name = "notebook-notify"

# The message you want to send
message = "Hi i am Slack bot"

try:
    # Use the chat.postMessage method to send a message to the channel
    response = client.chat_postMessage(channel=channel_id, text=message,username=bot_name)
    print("Message sent successfully!")
except SlackApiError as e:
    # Error handling in case the message fails to send
    print(f"Error sending message: {e}")

slacker
=======
A notification for slackers

Usage
-----
```
slacker [OPTIONS] MESSAGE

  Slacker CLI tool to send a message using the send_message function from
  utils.

Options:
  --help  Show this message and exit.

Example:
sleep 5 && slacker "Hello World after 5 seconds!"
```
Python example:
```python
from time import sleep
from slacker.utils import send_message

a = 0
for i in range(5):
    a+=1
    sleep(1)
send_message('Done!')
send_message(f'a = {a}')
```

Use cases:
1. Install in an ipykernel and call `send_message` to notify you on status of jupyter notebook code blocks.
2. Implement into a shell function to notify you of exit status of a command that takes a long time to run.
3. Other actions involving python or shell where one might benefit from a slack messge.


Installation
------------
Clone the repo and enter the directory.  Then run:
`pip install -e .`

You will need a bot token from slack.  Go to the slack [app page](https://api.slack.com/apps)

1. Click create new app
2. Choose "from scratch"
3. Give it a name and choose workspace.
4. On the basic information page, scroll down to edit name and add custom app icon.
5. On the management sidebar of the app, click "OAuth & Permissions".
6. Scroll down to Scopes and add a bot token scope.  Choose the `chat:write` permission for the bot token scope.
7. Install app to workspace by clicking the install to workspace button.  This will provide you the "Bot User Oauth Token".
8. By having an editable install with `pip install -e .`, we then need to modify lines in `slacker/config.py` to add the oauth token as well as give the bot the name you chose.
9. In the Slack app, right click on the conversation you want the bot to post in (could be the bot's channel or your personal channel) and choose `view conversation details`
10. Note the `Channel ID` and edit `slacker/config.py` to the correct channel ID.
11. Start sending messages!

Authors
-------

`slacker` was written by `Andy Zhou <andy.zhou@czbiohub.org>`.


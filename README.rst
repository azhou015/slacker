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

```

Use cases:
1. Install in an ipykernel and call `send_message` to notify you on status of jupyter notebook code blocks.
2. Wrap into a shell function to notify you of exit status of a command that takes a long time to run.
3. Other actions involving python or shell where one might benefit from a slack messge.


Installation
------------
Clone the repo and enter the directory.  Then run:
`pip install -e .`

You will need a bot token from slack.  Go to the slack [app page](https://api.slack.com/apps)
This token will then need to be added to your environment as a variable `SLACK_BOT_TOKEN`

```
# In your .zshrc or .bashrc:
export SLACK_BOT_TOKEN="xox-**************"

```

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`slacker` was written by `Andy Zhou <andy.zhou@czbiohub.org>`_.


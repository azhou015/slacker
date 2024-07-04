import click
from slacker.utils import send_message

@click.command()
@click.argument('message')
def slacker(message):
    """
    Slacker CLI tool to send a message using the send_message function from utils.
    """
    send_message(message)
    click.echo(f"Message sent: {message}")

if __name__ == '__main__':
    slacker()

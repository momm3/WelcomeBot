#Channel lister
import os
from slackclient import SlackClient


BOT_NAME = 'welcome_bot'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


if __name__ == "__main__":
    api_call = slack_client.api_call("channels.list")
    if api_call.get('ok'):
        print (api_call)

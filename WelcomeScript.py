import os
import time
from slackclient import SlackClient


# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"
BOOT_COMMAND = "!boot"
SYSTEM_HELP = "!help"

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

#Number of Users function
def getNumUsers():
    tolnumUsers = slack_client.api_call("channels.info", channel="C3ZTYM160")
    nameList = []
    usersDataa = (tolnumUsers["channel"])
    usersData = usersDataa["members"]
    for member in usersData:
        nameList.append(member)
    numUserss = len(nameList)
    return numUserss

#Command Handler
def handle_command(command, channel):
    currentUsers = getNumUsers()
    READ_WEBSOCKET_DELAYS = 10
    #WAIT 10 SECONDS BEFORE LOOPING AGAIN
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    if command.startswith(BOOT_COMMAND):
        response = "Booted up Welcome Bot V1.0"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    if command.startswith(SYSTEM_HELP):
        response = "I can only do one thing! Please type in @welcome_bot !boot to initalize me. As long as I am online, I will welcome new users to slack!"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    while 1>0:
        if getNumUsers() > currentUsers:
            response = "Welcome to Butler Dawgs. Type /join to join a channel!"
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
            currentUsers += 1
        time.sleep(READ_WEBSOCKET_DELAYS)
    #FALSE
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
                   "* command with numbers, delimited by spaces."


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

#Determines if the running actually worked or not.
if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("WelcomeBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

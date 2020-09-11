import re
import time
from slackclient import SlackClient


# instantiate Slack client
slack_client = SlackClient('your bot token goes here')

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "Question:"
EXAMPLE_COMMAND2 = "yes"
EXAMPLE_COMMAND3 = "no"
EXAMPLE_COMMAND4 = "answer:"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"




def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def define_question(command):
    global question 
    question = command

def handle_command(command, channel):
        
    """
        Executes bot command if the command is known
    """
    if channel == "Questions channel id":
        answer = "Not sure what you mean. Try *{}*".format(EXAMPLE_COMMAND)
        if command.startswith(EXAMPLE_COMMAND):
            answer = "Sending your question to specialists!"
            define_question(command)
            slack_client.api_call(
            "chat.postMessage",
            channel="#canal0",
            text="New {} do you know how to answer it? (Say yes or no)".format(command)
            )
        if command.startswith(EXAMPLE_COMMAND2):
            answer = "Thanks for the feedback :heart:"
        if command.startswith(EXAMPLE_COMMAND3):
            answer = "Sorry for that , fell free to send me another question!"
    if channel == "channel0 id":
        answer = "Not sure what you mean. Try *{}* or *{}*.".format(EXAMPLE_COMMAND2,EXAMPLE_COMMAND3)
        if command.startswith(EXAMPLE_COMMAND2):
            answer = "Waiting for your answer (use {} to respond), Thank you!".format(EXAMPLE_COMMAND4)
        if command.startswith(EXAMPLE_COMMAND3):
            answer = "Sending question to next channel..."
            slack_client.api_call(
            "chat.postMessage",
            channel="#canal1",
            text="New {} do you know how to answer it? (Say yes or no)".format(question)
            )
            #send to next channel
        if command.startswith(EXAMPLE_COMMAND4):
            answer = "Sending your answer for the requester, Thank you! :heart: "
            slack_client.api_call(
            "chat.postMessage",
            channel="#python-bot",
            text="{} is this answer satisfactory? (say *yes* ou *no*)".format(command)
            )
    if channel == "channel1 id":
        answer = "Not sure what you mean. Try *{}* or *{}*.".format(EXAMPLE_COMMAND2,EXAMPLE_COMMAND3)
        if command.startswith(EXAMPLE_COMMAND2):
            answer = "Waiting for your answer (use {} to respond), Thank you!".format(EXAMPLE_COMMAND4)
        if command.startswith(EXAMPLE_COMMAND3):
            answer = "Sending question to next channel..."
            slack_client.api_call(
            "chat.postMessage",
            channel="#canal2",
            text="New {} do you know how to answer it? (Say yes or no)".format(question)
            )
        if command.startswith(EXAMPLE_COMMAND4):
            answer = "Sending your answer for the requester, Thank you! :heart: "
            slack_client.api_call(
            "chat.postMessage",
            channel="#python-bot",
            text="{} is this answer satisfactory? (say *yes* ou *no*)".format(command)
            )
    

    # Sends the answer back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=answer
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")

        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
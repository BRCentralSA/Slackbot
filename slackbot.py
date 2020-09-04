import re
import time
from slackclient import SlackClient


# instantiate Slack client
slack_client = SlackClient('xoxb-1333525267573-1354942281729-BByKl5BHplc1X3mtF2oINowt')

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "pergunta:"
EXAMPLE_COMMAND2 = "SIM"
EXAMPLE_COMMAND3 = "NAO"
EXAMPLE_COMMAND4 = "resposta:"
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

def definir_pergunta(command):
    global pergunta 
    pergunta = command

def handle_command(command, channel):
        
    """
        Executes bot command if the command is known
    """
    if channel == "C01AEDJQUUR":
        resposta = "Not sure what you mean. Try *{}*".format(EXAMPLE_COMMAND)
        if command.startswith(EXAMPLE_COMMAND):
            resposta = "Enviando sua pergunta para especialistas!"
            definir_pergunta(command)
            slack_client.api_call(
            "chat.postMessage",
            channel="#canal0",
            text="Chegou uma {} Sabem responder? (diga SIM ou NAO)".format(command)
            )
        if command.startswith(EXAMPLE_COMMAND2):
            resposta = "Obrigada pelo feedback :heart:"
        if command.startswith(EXAMPLE_COMMAND3):
            resposta = "Crie uma nova pergunta"
    if channel == "C01AU9N2R0Q":
        resposta = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND2)
        if command.startswith(EXAMPLE_COMMAND2):
            resposta = "Aguardo a sua resposta (use *resposta:* para responder), Obrigada!"
        if command.startswith(EXAMPLE_COMMAND3):
            resposta = "Enviando pergunta para o proximo canal..."
            slack_client.api_call(
            "chat.postMessage",
            channel="#canal1",
            text="Chegou uma {} Sabem responder? (diga SIM ou NAO)".format(pergunta)
            )
            #enviar para o proximo canal
        if command.startswith(EXAMPLE_COMMAND4):
            resposta = "Enviando sua Resposta, Obrigada! :heart: "
            slack_client.api_call(
            "chat.postMessage",
            channel="#python-bot",
            text="{} resposta satisfatoria? (diga *SIM* ou *NAO*)".format(command)
            )
    if channel == "C01AUKKK6JC":
        resposta = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND2)
        if command.startswith(EXAMPLE_COMMAND2):
            resposta = "Aguardo a sua resposta (use *resposta:* para responder), Obrigada!"
        if command.startswith(EXAMPLE_COMMAND3):
            resposta = "Enviando pergunta para o proximo canal..."
            slack_client.api_call(
            "chat.postMessage",
            channel="#canal2",
            text="Chegou uma {} Sabem responder? (diga SIM ou NAO)".format(pergunta)
            )
        if command.startswith(EXAMPLE_COMMAND4):
            resposta = "Enviando sua Resposta, Obrigada! :heart: "
            slack_client.api_call(
            "chat.postMessage",
            channel="#python-bot",
            text="{} resposta satisfatoria? (diga *SIM* ou *NAO*)".format(command)
            )
    

    # Sends the resposta back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=resposta
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

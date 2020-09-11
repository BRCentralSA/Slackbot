# Slackbot
This is a demonstration using [Amazon EC2](https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/concepts.html) and Slack API for python (slackclient) to create a slackbot that works like a proxy for questions and answers between channels in a slack workspace
## Requisites:
- Linux EC2 Instance
- Either Python 2 or 3 installed
- pip installed to manage dependencies 
- Slack client installed 
- Slack workspace and Account 

## Step-by-step
### Launch and connect to your EC2 Instance
first thing you need to do is to Launch your EC2 instance in your AWS management console or via AWS CLI (I used an t2.micro Amazon Linux 2) and then connect to it. (**IMPORTANT: Make sure your EC2 instance security group is open on port 22 (ssh) to your ip**)
- [Launch your EC2 instance](https://docs.aws.amazon.com/quickstarts/latest/vmlaunch/step-1-launch-instance.html) 
- [Connect to your EC2 instance](https://docs.aws.amazon.com/quickstarts/latest/vmlaunch/step-2-connect-to-instance.html)
### Install Python 
Some AMIs already have Python 2 installed, to check if you already have it run:
```
python --version
```
If you don´t have python installed yet run: 
```
sudo yum install python 
```
### Install pip 
```
sudo yum install pip
```
### Install Slack Client 
```
pip install slackclient
```
### Create a Slack Bot 
Inside your Slack Workspace go to **More>Apps** and search for "bots" and click on Add. You will be redirected to another page, then click on Add to Slack, give it a username, accept and configure it as you want (picture, description, etc) 
After you do that, you´ll get an **API token for your bot**, save that information! 
### Add your Bot to Slack Channels
Bots need to be added to channels to have access to it. Go to the channel you want then go to **Information>More>Add Apps** , choose the bot you´ve just crated and done! (Repeat this step in every channel you want your bot to interact with)
### Code the bot!
You can now add functions to your bot, use the [Slack Client API reference](https://pypi.org/project/slackclient/1.0.7/) to see some basic usage. I already have one bot ready for you in the code directory slackbot-en.py file in this repository! Fell free to clone this repository and use the code to test it in your Workspace. The basic function of this bot is to work as a proxy for questions and answers between channels in a slack workspace. **If you choose to use the slackbot.py file make sure to change the API token and the channels Ids inside the code** 
### Run 
To run your slackbot in your EC2 instance use:
```
python slackbot-en.py
```
If everything is working you should get this output and be able to test it in your workspace already!
```
Starter Bot connected and running!
```

## Slackbot Chat Flow

User send the question:
<br>![Imagem 1](/images/img01.PNG?raw=true "Title")
<br>Bot sends the question to channel #0 and user choose to respond or not:
<br>![Imagem 2](/images/img02.PNG?raw=true "Title")
<br>Bots sends the question to channel #1 and user respond:
<br>![Imagem 3](/images/img03.PNG?raw=true "Title")
<br>Bot sends the answer to requester:
<br>![Imagem 2](/images/img02.PNG?raw=true "Title")


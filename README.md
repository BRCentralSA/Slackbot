# Slackbot
This is a demonstration using [Amazon EC2](https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/concepts.html) and Slack API for python (slackclient) to create a slackbot that works like a proxy for questions and answers between channels in a slack workspace

## Prerequisites:
- EC2 Instance
- Either Python 2 or 3 installed
- pip installed to manage dependencies 
- Slack client installed 
- Slack workspace and Account 

## Step-by-step
### Launch and connect to your EC2 Instance
first thing you need to do is to Launch your EC2 instance in your AWS management console or via AWS CLI (I used an t2.micro Amazon Linux 2) and then connect to it. (IMPORTANT: Make sure your EC2 instance security group is open on port 22 (ssh) to your ip)
- [Launch your EC2 instance](https://docs.aws.amazon.com/quickstarts/latest/vmlaunch/step-1-launch-instance.html) 
- [Connect to your EC2 instance](https://docs.aws.amazon.com/quickstarts/latest/vmlaunch/step-2-connect-to-instance.html)
### Install Python 
Some AMIs already have Python 2 installed, to check if you already have it run:
```
python --version
```
If you don´t have it installed yet run: 
```
sudo yum install python 
```
### Install pip 
```
sudo yum install pip
```

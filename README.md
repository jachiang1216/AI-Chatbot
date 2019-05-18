# AI-Chatbot
## 1. Overview
Welcome to AI-Chatbot, an artificial intelligence chat bot designed to keep you entertained. This Conversational Chatbot is coded for Slack 
AI-Chatbot offers a helping hand through the following features:
- Greetings and Goodbyes
- Music Sharing via Youtube
- Humorous Jokes
- Cat and Dog Picture Sharing

![Alt Text](https://github.com/jachiang1216/ChatAI/blob/master/img/Demo_Chat.gif)t

## 2. Setup to Run Chatbot
### Slack API Settings
To integrate the chatbot with Slack, we will need to first create the app and modify its settings/permissions
- Go to https://api.slack.com/ and create an account
- Create or choose an existing development workspace
- In the workspace, create a Slack application. Create a bot user under the bots tab
- Go to Add Features and Functionality section and under Basic Information, turn on Bots and Permissions
- Save all changes
- Install and authorize the App in the workspace
### Ngrok
Ngrok is essential to port communications between the python program and the Slack application
- Go to https://ngrok.com/download and download Ngrok
- Navigate to ngrok.exe directory and run ./ngrok <authtoken>
- Start the public port: ./ngrok http 5004  
### Deploying AI-Chatbot to Slack
Now that we have a port running, we will deploy the chatbot. 
From Terminal:
- Train NLU Model: python nlu_model.py
- Run Action Server: python -m rasa_core_sdk.endpoint --actions actions
- Train Rasa Core Model: python dialogue_management_model.py
- In run_app.py file, Insert the Bot User OAuth Access Token when creating the SlackInput object. The token can be obtained in the OAuth and Permissions tab
- Under the Events Subscription tab, enable subscriptions and enter the Request URL: https://<your_ngrok_url>/webhooks/slack/webhook. The url is shown when the public port starts via ngrok
- Run run_app.py: python run_app.py
### Enjoy!
You should now be able to message AI-Chatbot and utilize its various amazing features for your enjoyment.
 
## 3. Credits
Cat and Dog Pictures were queried through https://shibe.online/ (Shiba Inu API). Special thanks to Jammy for the shibes and Microsoft Research Asia et al for the cats!

Jokes were queried through https://icanhazdadjoke.com/ (icanhazdadjoke API).




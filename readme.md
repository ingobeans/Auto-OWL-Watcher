#Auto OWL Watcher

Automatically watch OWL youtube streams to generate OWL Tokens in Overwatch. It checks every few minutes if OWL is streaming, if so it opens a hidden selenium browser logged in with chrome, to watch the stream. 




-------------------  Setup instructions for Auto OWL Watcher  -------------------

1. Go into main.py and change youtube_api_key to your Youtube API Key. (How to get API key:  https://blog.hubspot.com/website/how-to-get-youtube-api-key)

2. Also setup a discord webhook, and change webhook_url to your webhook url

3. optionally change logging_level.



-------------------  How it works  -------------------

Auto OWL Watcher works by checking if OWL youtube channel is streaming every few minutes, if so it opens a headless (hidden) selenium window that watches the stream. 
It uses your chrome data to connect to your youtube channel. This way you receive OWL tokens (as long as you are logged in to youtube in chrome and also has connected your youtube account to battle.net for rewards)



------------------- Troubleshooting  -------------------

"No rewards getting received"- Could be due to not being logged in to youtube in google chrome, or not connected youtube channel to battle.net (like this: https://dotesports.com/overwatch/news/how-to-earn-overwatch-league-tokens)

For errors with script crashing on start, could be due to youtube api token being incorrect

Otherwise feel free to ask for help
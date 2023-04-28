# Auto Overwatch League Watcher

Automatically watch Overwatch League youtube streams to generate Overwatch League Tokens in Overwatch. It checks every few minutes if OWL is streaming, if so it opens a hidden selenium browser logged in with chrome, to watch the stream. 




## **-------------------  Setup instructions  -------------------**

1. Go into settings.py and change youtube_api_key to your Youtube API Key. (How to get API key:  https://blog.hubspot.com/website/how-to-get-youtube-api-key)

2. You can also setup a discord webhook, and change webhook_url to your webhook url. This is if you want the script to log to your discord channel reather then the console output. I recommend turning down logging_level to 3, if you're using webhook logging (so you dont get spammed).




## **-------------------  Tips  -------------------**

Personally I enable discord_webhook_logging (and setup a discord webhook, and edit webhook_url), turn down logging_level to 3 and open the script using "launch headless.vbs". This way there is no annoying command prompt window and it still logs if it runs in to an error and when it begins watching a stream (through discord).




## **-------------------  How it works  -------------------**

Auto OWL Watcher works by checking if OWL youtube channel is streaming every few minutes, if so it opens a headless (hidden) selenium window that watches the stream. 
It uses your chrome data to connect to your youtube channel. This way you receive OWL tokens (as long as you are logged in to youtube in chrome and also has connected your youtube account to battle.net for rewards)




## **------------------- Troubleshooting  -------------------**

"No rewards getting received"- Could be due to not being logged in to youtube in google chrome, or not connected youtube channel to battle.net (like this: https://dotesports.com/overwatch/news/how-to-earn-overwatch-league-tokens)

For errors with script crashing on start, could be due to youtube api token being incorrect

Otherwise feel free to ask for help
# Auto Overwatch League Watcher

Automatically watch Overwatch League youtube streams to generate Overwatch League Tokens in Overwatch. It checks every few minutes if OWL is streaming, if so it opens a hidden selenium browser logged in with chrome, to watch the stream. 

This branch logs the status and statistics to discord.
If you instead want the newer version that hosts a localhost website with statistics, check out the main branch (https://github.com/ingobeans/Auto-OWL-Watcher)


## **-------------------  Setup instructions  -------------------**

1. Install Python.

2. Run this command in cmd: `pip install google-api-python-client, google-auth, requests, selenium`

3. Go into settings.py and change youtube_api_key to your Youtube API Key. (How to get API key:  https://blog.hubspot.com/website/how-to-get-youtube-api-key)

4. Create a discord webhook (for logging) and change webhook_url to your webhook url in settings.py. You can also set discord_webhook_logging to False, if you'd rather want logging in the console.

5. You can now run the script by running "launch headless.vbs"


## **-------------------  How it works  -------------------**

Auto OWL Watcher works by checking if OWL youtube channel is streaming every few minutes, if so it opens a headless (hidden) selenium window that watches the stream. 
It uses your chrome data to connect to your youtube channel. This way you receive OWL tokens (as long as you are logged in to youtube in chrome and also has connected your youtube account to battle.net for rewards)




## **------------------- Troubleshooting  -------------------**

"No rewards getting received" - Could be due to not being logged in to youtube in google chrome, or not connected youtube channel to battle.net (like this: https://dotesports.com/overwatch/news/how-to-earn-overwatch-league-tokens)


"Opening launch headless.vbs just shows an error popup saying that the system cannot find the file specified" - Make sure Python is installed, if it is, try restarting your PC, then making sure Python is added to path.


For errors with script crashing on start, could be due to youtube api token being incorrect

Otherwise feel free to ask for help
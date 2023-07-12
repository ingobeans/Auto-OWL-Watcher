# Auto Overwatch League Watcher

Automatically watch Overwatch League youtube streams to generate Overwatch League Tokens in Overwatch. It checks every few minutes if OWL is streaming, if so it opens a hidden selenium browser logged in via chrome, to watch the stream. 

This branch displays statistics and status at http://localhost:7676.
If you instead want it to send discord messages periodically (or whenever it starts watching stream), check out the other branch (https://github.com/ingobeans/Auto-OWL-Watcher/tree/discord-webhook-logging)


## **-------------------  Setup instructions  -------------------**

1. Install Python.

2. Run this command in cmd: `pip install google-api-python-client, google-auth, requests, selenium, flask`

3. Go into settings.py and change youtube_api_key to your Youtube API Key. (How to get API key:  https://blog.hubspot.com/website/how-to-get-youtube-api-key)

4. You can now run the script by running "launch headless.vbs"

5. While the script is running, you can goto http://localhost:7676 to see statistics, errors, etc


## **-------------------  How it works  -------------------**

Auto OWL Watcher works by checking if OWL youtube channel is streaming every few minutes, if so it opens a headless (hidden) selenium window that watches the stream. 
It uses your chrome data to connect to your youtube channel. This way you receive OWL tokens (as long as you are logged in to youtube in chrome and also has connected your youtube account to battle.net for rewards)


## **------------------- Troubleshooting  -------------------**

"No rewards getting received" - Could be due to not being logged in to youtube in google chrome, or not connected youtube channel to battle.net (like this: https://dotesports.com/overwatch/news/how-to-earn-overwatch-league-tokens)


"Opening launch headless.vbs just shows an error popup saying that the system cannot find the file specified" - Make sure Python is installed, if it is, try restarting your PC, then making sure Python is added to path.


For errors with script crashing on start, make sure that your youtube api token is correct

Otherwise feel free to ask for help
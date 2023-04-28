discord_webhook_logging = False #decides whether to log in to the console or through a discord webhook
webhook_url = "ENTER WEBHOOK URL" #only necessary if discord_webhook_logging is True
youtube_api_key = "ENTER YOUTUBE API KEY"


#-----------[LOGGING LEVELS]-----------
#4 - VERBOSE / logs everything, current status, errors (This is the default option)
#3 - DEFAULT / logs errors and whenever it starts watching a new stream (recommended if using discord webook logging)
#2 - ERRORS / logs errors
#1 - NOTHING / logs nothing 
logging_level = 4
youtube_api_key = "ENTER YOUTUBE API KEY"



#-----------[DISCORD WEBHOOK SETTINGS]-----------
discord_webhook_logging = True #decides whether to log in to the console or through a discord webhook
webhook_url = "ENTER WEBHOOK URL" #only necessary if discord_webhook_logging is True

use_predetermined_webhook_settings = True #decides if to use predetermined webhook avatar and username. If set to False, will use the webhooks avatar and username specified in discord



#-----------[LOGGING LEVELS]-----------
#4 - VERBOSE / logs everything, current status, errors (recommended if not using discord webook logging)
#3 - DEFAULT / logs errors and whenever it starts watching a new stream (recommended if using discord webook logging)
#2 - ERRORS / logs errors
#1 - NOTHING / logs nothing 
logging_level = 3
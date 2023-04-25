import google.auth
from googleapiclient.discovery import build
import time, requests, os
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#made by github.com/ingobeans



real_id = "UC5JkxQ4bNq_ewnkTgVjjtfw"

#-----------[SCRIPT SETTINGS]-----------
discord_webhook_logging = True
webhook_url = "ENTER WEBHOOK URL"
youtube_api_key = "ENTER YOUTUBE API KEY"

#use the default chrome data dir as selenium user-data-dir (this is so that you are logged in to your youtube account saved in chrome)
chrome_data_path = os.getenv('LOCALAPPDATA') + "\\Google\\Chrome\\User Data"

#-----------[LOGGING LEVELS]-----------
#4 - VERBOSE / logs everything, current status, errors
#3 - DEFAULT / logs errors and whenever it starts watching a new stream (This is the default option)
#2 - ERRORS / logs errors
#1 - NOTHING / logs nothing 
logging_level = 3

def log(msg, log_level_requirement):
    if logging_level == 1:
        return
    
    if logging_level >= log_level_requirement:
        if discord_webhook_logging:
            requests.post(url=webhook_url, json={"content":msg})
        else:
            print(msg)

def logerror(msg):
    msg = "[__**PROBLEM**__]:    "+msg
    if logging_level == 1:
        return
    
    if logging_level >= 2:
        if discord_webhook_logging:
            requests.post(url=webhook_url, json={"content":msg})
        else:
            print(msg)

def get_live_stream_url(channel_id):
    try:
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        request = youtube.search().list(
            part='id',
            channelId=channel_id,
            eventType='live',
            type='video'
        )
        response = request.execute()
        if len(response['items']) > 0:
            video_id = response['items'][0]['id']['videoId']
            return f'https://www.youtube.com/watch?v={video_id}'
        else:
            return None
    except Exception as e:
        logerror(str(e))
        quit()


has_streamed = False
previous_stream = None

log("**STARTED OWL AUTO :cowboy:**",4)

while True:
    url = get_live_stream_url(debug_id)
    if not url == None:
        if not has_streamed:
            #if this is the first time that OWL has started streaming during the current session, launch up selenium (No need to launch selenium until they start streaming to save ram)
            chrome_options = Options()
            chrome_options.add_argument("--user-data-dir="+chrome_data_path)
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options) 
        has_streamed = True
        driver.get(url)
        time.sleep(5)
        try:
            b = driver.find_element(By.CLASS_NAME, "ytp-large-play-button")
            b.click()
        except:
            pass
        
        if previous_stream == None or url != previous_stream:
            previous_stream = url
            log("started watching stream :smiling_face_with_3_hearts:. **("+url+")**", 3)

        if url != driver.current_url:
            logerror("url should be: "+url+", but is:"+driver.current_url)
        
        log("still watching stream :thumbsup:, about to reload... (next reload in **650 secs**)", 4)
        #reload because sometimes youtube flags as inactive and also as a failsafe if something in youtube stream breaks
        time.sleep(650)
    else:
        log("OWL is __not__ streaming right now :sob:, checking again in **400 secs**", 4)
        #check every 400 secs if OWL is streaming
        time.sleep(400)
        
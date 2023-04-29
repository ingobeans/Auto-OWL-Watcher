import google.auth
from googleapiclient.discovery import build
import time, requests, os, re
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from settings import *

#made by github.com/ingobeans


if not discord_webhook_logging:
    os.system("color")

owl_id = "UCiAInBL9kUzz1XRxk66v-gw"
#use the default chrome data dir as selenium user-data-dir (this is so that you are logged in to your youtube account saved in chrome)
chrome_data_path = os.getenv('LOCALAPPDATA') + "\\Google\\Chrome\\User Data"

def log(msg, log_level_requirement):
    if logging_level == 1:
        return
    
    if logging_level >= log_level_requirement:
        if discord_webhook_logging:
            requests.post(url=webhook_url, json={"content":msg,"username":"Auto OWL Status","avatar_url":"https://yt3.googleusercontent.com/ytc/AGIKgqPyXqPzHBB7rV5aoyDT6KGVYyMPx6rsMKkNh7d9=s900-c-k-c0x00ffffff-no-rj"})
        else:
            msg = re.sub(r'\*\*|__', "", msg)
            msg = re.sub(r':\w+:', '', msg)
            print("\033[96m"+msg+"\033[0m")

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
time_until_5_tokens = 6
estimated_tokens_earnt = 0
log("**STARTED OWL AUTO :cowboy:**",4)

while True:
    url = get_live_stream_url(owl_id)
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
        time_until_5_tokens -= 1
        if time_until_5_tokens == 0:
            time_until_5_tokens = 6
            estimated_tokens_earnt += 5
        
        if not estimated_tokens_earnt == 0: 
            log("still watching stream :thumbsup:, about to reload... (next reload in **10 minutes**). **Estimated tokens earnt: " + str(estimated_tokens_earnt)+"**", 4)
        else:
            log("still watching stream :thumbsup:, about to reload... (next reload in **10 minutes**).", 4)
        #reload because sometimes youtube flags as inactive and also as a failsafe if something in youtube stream breaks
        time.sleep(10*60)
    else:
        log("OWL is __not__ streaming right now :sob:, checking again in **7 minutes**", 4)
        #check every 400 secs if OWL is streaming
        time.sleep(7*60)
        
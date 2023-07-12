import google.auth
from googleapiclient.discovery import build
import time, requests, os, json, logging, datetime
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from settings import *
from threading import Thread

#made by github.com/ingobeans


def run_server():
    try:
        import server
    except Exception as e:
        with open("error server crash at " + datetime.datetime.now().strftime("%m-%d-%H-%M"), "w") as f:
            f.write(str(e))

thread = Thread(target=run_server)
thread.start()
time.sleep(1)

stats = {}

with open("stats.json","r") as f:
    stats = json.load(f)

all_time_time_spent = stats["time_watched_all_time"]

owl_id = "UCiAInBL9kUzz1XRxk66v-gw"
#owl_id = "UCSJ4gkVC6NrvII8umztf0Ow" #for testing purposes


#use the default chrome data dir as selenium user-data-dir (this is so that you are logged in to your youtube account saved in chrome)
chrome_data_path = os.getenv('LOCALAPPDATA') + "\\Google\\Chrome\\User Data"


logging.getLogger("selenium.webdriver.remote.remote_connection").disabled = True #disable selenium logging


def write_to_stats(new_stats):
    with open("stats.json","w") as f:
        json.dump(new_stats,f)


def log_error(msg):
    requests.get("http://localhost:7676/api/throw_error/",headers={"msg":msg})
        
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
        err = str(e)
        if "API key not valid. Please pass a valid API key" in err:
            err = "Invalid youtube API key. Please check your API key, and try again."
        log_error(err)
        quit()


has_streamed = False
previous_stream = None
time_watched = 0

def send_status(status):
    requests.get("http://localhost:7676/api/set_status/",headers={"status":status})

def format_time(minutes):
    if minutes < 60:
        time_watched_fancy = f"{minutes} minutes"
    elif minutes/60/24 >= 7:
        time_watched_fancy = f"{int(minutes/60/24/7)} week{'s' if int(minutes/60/24/7) > 1 else ''}"
    elif minutes/60 >= 24:
        time_watched_fancy = f"{int(minutes/60/24)} day{'s' if int(minutes/60/24) > 1 else ''}"
    elif minutes >= 60:
        time_watched_fancy = f"{int(minutes/60)} hour{'s' if int(minutes/60) > 1 else ''}"

    return time_watched_fancy

send_status(f"launching|0|0|{int(all_time_time_spent/60*5)}|{format_time(all_time_time_spent)}")

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

        if url != driver.current_url:
            log_error(f"**Url should be: {url} ,but is: {driver.current_url}**")

        time_watched_fancy = format_time(time_watched)
        
        new_stats = {"time_watched_all_time": all_time_time_spent}
        all_time_tokens_earnt = int(all_time_time_spent / 60 * 5)
        estimated_tokens_earnt = int(time_watched / 60 * 5)
        write_to_stats(new_stats)
        send_status(f"{url}|{estimated_tokens_earnt}|{time_watched_fancy}|{all_time_tokens_earnt}|{all_time_time_spent}")
        
        #reload because sometimes youtube flags as inactive and also as a failsafe if something in youtube stream breaks
        time.sleep(30*60)
        time_watched+=30
        all_time_time_spent+=30

    else:
        send_status(f"0|0|0|{int(all_time_time_spent/60*5)}|{format_time(all_time_time_spent)}")
        time_watched = 0
        #check every 15 mins if OWL is streaming
        time.sleep(15*60)


        
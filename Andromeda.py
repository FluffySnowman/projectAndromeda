from __future__ import unicode_literals
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
from requests import get
import socket
import os
import subprocess
import time
from colorama import Fore, Back, Style
import requests 
import random
import re
import twint
import sys
import youtube_dl

import youtube_dl

stdout_fileno = sys.stdout

#import TwitterSearch

#Initialising red colour
print(Fore.RED)

print("   ___              __                              __     ")
time.sleep(0.2)
print("   /   |  ____  ____/ /________  ____ ___  ___  ____/ /___ _")
time.sleep(0.2)
print("  / /| | / __ \/ __  / ___/ __ \/ __ `__ \/ _ \/ __  / __ `/")
time.sleep(0.2)
print(" / ___ |/ / / / /_/ / /  / /_/ / / / / / /  __/ /_/ / /_/ / ")
time.sleep(0.2)
print("/_/  |_/_/ /_/\__,_/_/   \____/_/ /_/ /_/\___/\__,_/\__,_/  ")
time.sleep(0.2)
print("                                                            ")
time.sleep(0.2)
print("")
print("Type help to view commands\nFind the docs at https://github.com/FluffySnowman/projectAndromeda/blob/master/docs.md\n\n")

#

while 1 < 2:


    input1 = input("Andromeda> ")


    #####################################
    ##########HELP#######################
    #####################################


    if (input1 == "help"):


        print(Fore.MAGENTA+"Find the docs at https://github.com/FluffySnowman/projectAndromeda/blob/master/docs.md\n\n"+Fore.RED+Fore.GREEN+"All Commands: wifiaudit, help, googlescrape, twitterscrape, cls, exit"+Fore.RED)


    #####################################
    ############clear####################
    #####################################


    elif (input1 =="cls"):
        print(chr(27) + "[2J")


    #####################################
    ##########hackwifi###################
    #####################################
    

    elif (input1 == "wifiaudit"):


        print("killing all network processes in 5 seconds.CNTL+C TO STOP")
        print(5)
        time.sleep(1)
        print(4)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        stream = os.popen("airmon-ng check kill")
        output = stream.read()
        print(output)
        print("now enabling monitor mode for your network card")
        input_wifi_card = input("Name of the card to put to monitor mode: ")
        temp = ("airmon-ng start " + input_wifi_card)
        stream = os.popen(temp)
        output = stream.read()
        print(output)
        input_monitor_mode_card = input("Name of the card IN monitor mode: ")
        input_start_airodumpng = input("Start airodump-ng?(y/n): ")
        if (input_start_airodumpng == "y"):
            print("starting airodump-ng")
            time.sleep(0.2)
            temp = ("airodump-ng " + input_monitor_mode_card)
            stream = os.popen(temp)
            output = stream.read()
            print(output)
        else:
            print("exiting the hackwifi process")


    ####################################
    ############google scraper##########
    ####################################

    
    elif (input1 == "googlescrape"):
        input_google_scrape = input("Scrape google for> ")

        text = input_google_scrape
        url = 'https://google.com/search?q=' + text
        A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        )
        Agent = A[random.randrange(len(A))]
        headers = {'user-agent': Agent}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        try: 
            from googlesearch import search 
        except ImportError:
            print("No module named 'google' found") 
  
        # to search 
        query = text
        i = 1
        h = 1
        print(Fore.MAGENTA+"Title scrapes:- "+Fore.RED)
        for info in soup.find_all('h3'):
            n = str(i)
            print(Fore.GREEN+str(i), ':- ',Fore.YELLOW+ info.text+Fore.RED)
            i = i + 1
        i = i - 1
        print()
        print(Fore.MAGENTA+"Link scrapes:- "+Fore.RED)
        for j in search(query, tld="co.in", num=i, stop=i, pause=2): 
            print(Fore.GREEN+str(h), ':- ',Fore.YELLOW+ str(j)+Fore.RED)
            h = h + 1


    ####################################
    ###########twitter scraper##########
    ####################################

    
    elif (input1 == "twitterscrape"):
        print(Fore.BLUE)


        while 1 < 2:
            print("\n1:- Followers")
            print("2:- Profile Information")
            print("3:- Tweets")
            print("4:- Exit\n")
            twint_search_option = input("Select a number to scrape for: ")

            if (twint_search_option == "1"):
                print("Loading up username search functions")
                break
            elif (twint_search_option == "2"):
                print()
                break
            elif (twint_search_option == "3"):
                print()
                break
            elif (twint_search_option == "4" or twint_search_option == "exit"):
                break
            else:
                print(Fore.GREEN+"enter a correct number"+Fore.RED)
        
        if (twint_search_option == "1"):
            

            twintvariable = twint.Config()
            twint_username_followers = input("Username: ")
            twintvariable.Username = (twint_username_followers)
            twint_followers_savefile = input("Path to save followers list to: ")

            print(Fore.GREEN+"\n\nFollowers will be saved to the file in plain text (this may take a while)\n\n"+Fore.BLUE)
            sys.stdout = open(twint_followers_savefile, "w")
            twint.run.Followers(twintvariable)

            sys.stdout.close()

            sys.stdout = stdout_fileno


        elif (twint_search_option == "2"):


            twintvariable = twint.Config()
            twint_username_profileinfo = input("Profile Username: ")
            twintvariable.Username = twint_username_profileinfo
            twint_profileinfo_savefile = input("Path to save profile info to: ")
            
            print(Fore.GREEN+"\n\nProfile info will be saved to the file in plain text\n\n"+Fore.BLUE)    
            sys.stdout = open(twint_profileinfo_savefile, "w")
            twint.run.Lookup(twintvariable)

            sys.stdout.close()

            sys.stdout = stdout_fileno 

        
        elif (twint_search_option == "3"):


            twintvariable = twint.Config()
            twint_username_tweets = input("Username: ")
            twintvariable.Username = twint_username_tweets
            twint_tweets_limit = input("Number of tweets to scrape: ")
            twintvariable.Limit = twint_tweets_limit
            twint_tweets_savefile = input("Path to save tweets to: ")
            
            print(Fore.GREEN+"\n\nTweets will be saved to the file in plain text\n\n"+Fore.BLUE)    
            sys.stdout = open(twint_tweets_savefile, "w")
            twint.run.Search(twintvariable)

            sys.stdout.close()

            sys.stdout = stdout_fileno 
        
        print()


        print(Fore.RED)  


    ####################################
    #########youtube downloader#########
    ####################################


    elif (input1 == "yt-download"):

        
        print(Fore.CYAN)

        video_url = input("Please enter the YouTube Video URL: ")
        # Download and convert to mp3 and store in downloads folder
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=video_url, download=False
        )
        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        # Open the file once it has been downloaded


        print(Fore.RED)




#BREAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK 


    elif (input1 == "exit"):
        break
    

    else:
        print(Fore.GREEN+"ENTER VALID COMMANDS PLEASE"+Fore.RED)


#

print("Exiting Andromeda")
exit()
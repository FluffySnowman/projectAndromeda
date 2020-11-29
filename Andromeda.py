import socket
import os
import subprocess
import time
from colorama import Fore, Back, Style
import requests 
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
from requests import get
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
print("Type help to view commands\n\n")

#

while 1 < 2:


    input1 = input("Andromeda> ")


    #####################################
    ##########HELP#######################
    #####################################


    if (input1 == "help"):


        print("\nAll Commands: hackwifi, help, googlescrape")


    #####################################
    ##########hackwifi###################
    #####################################


    elif (input1 == "hackwifi"):


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
        inputmonitormodecard = input("Name of the card to put to monitor mode: ")
        temp = ("airmon-ng start " + inputmonitormodecard)
        stream = os.popen(temp)
        output = stream.read()
        print(output)


    ####################################
    ############google scraper##########
    ####################################

    
    elif (input1 == "googlescrape"):
        input_google_scrape = input("Scrape google for> ")

        text = 'python'
        url = 'https://google.com/search?q=' + text
        A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        )
 
        Agent = A[random.randrange(len(A))]
 
        headers = {'user-agent': Agent}
        r = requests.get(url, headers=headers)
 
        soup = BeautifulSoup(r.text, 'lxml')
        for info in soup.find_all('h3'):
            print(info.text)
            print('#######')


#BREAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK 


    elif (input1 == "exit"):
        break



#

print("Exiting Andromeda in 3 seconds")
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
exit()
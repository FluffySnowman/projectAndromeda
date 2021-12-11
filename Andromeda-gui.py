from __future__ import unicode_literals
from tkinter import *
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
from requests import get
from socket import *
from colorama import Fore, Back, Style
import os
import subprocess
import time
import requests 
import random
import re
import twint
import sys
import youtube_dl
import signal
import time
import socket
#import dnspython as dns
import dns.resolver


####################################


window = Tk()

window.title("Project Andromeda")
window.geometry("400x100+10+20")
window.configure(bg='black')

label1 = Label(window, text="Enter command", bg='black', fg='green')
label1.pack(side=TOP)

inputbox1 = Entry(window, bd=5)
inputbox1.pack(side=TOP)

button1 = Button(window, text="Execute", bg='white', fg='black')
button1.pack(side=RIGHT)

window.mainloop()
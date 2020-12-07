# Project Andromeda Docs
### Introduction

Project Andromeda is a tool that can be used to collect data efficiently and easily. It has a collection of tools ranging from wifi auditing to twitter scraping. So let's get started.

### Requirements

First a shell is required to run Andromeda (on windows: cmd or powershell, on mac: terminal, on your linux distribution: use the respective terminal application)

Python version 3 or above is required (3.8 or above if possible).

For the wifi auditing tools your device must have the aircrack-ng binaries installed.

Your device must have libxml2 and libxslt installed for for the python module lxml to function properly.

Next you must install the required python modules. To do this do:-

```bash
git clone https://github.com/FluffySnowman/projectAndromeda.git

cd projectAndromeda

python3 -m pip install -r requirements.txt
```

### Executing

To execute Andromeda your shell must have superuser/admmin permissions (for commands like wifiaudit or twitterscrape where the program has to write files to the computer)

Once that is done you can simple run the program(after cloning the repository) like this:-

```bash
cd projectAndromeda

python3 Andromeda.py
```

### Basics

#### Twitter Scraping

First lets start with twitter scraping. To start the twitter scraping module do:

```bash
Andromeda> twitterscrape
```

You will be prompted with some options on what to scrape for. Enter a number(respective to the option) and press enter to continue.

Enter the prompted question's answer (username etc);
Then enter the path you want the scrape's result's to be saved to;
Press enter and watch Andromeda magically work and come up with results.

Some errors may pop up so check the fixes over [here](https://github.com/FluffySnowman/projectAndromeda/blob/master/errors.md)

#### Google Scraping

To start the google scraper use this command:

```bash
Andromeda> googlescrape
```

You will be prompted with what to scrape for. After typing in your choice press enter and wait for the results.

#### 
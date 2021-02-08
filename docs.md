# Project Andromeda Docs
### Introduction

Project Andromeda is a tool that can be used to collect data efficiently and easily. It has a collection of tools ranging from wifi auditing to twitter scraping. So let's get started.

### Requirements

First a shell is required to run Andromeda (on windows: cmd or powershell, on mac: terminal, on your linux distribution: use the respective terminal application)

Python version 3 or above is required (3.8 or above if possible) and python 2 for the wifi audit module.

Your device must have libxml2 and libxslt installed for for the python module lxml to function properly.

Next you must install the required python modules. To do this do:-

```bash
git clone https://github.com/FluffySnowman/projectAndromeda.git

cd projectAndromeda

sudo python3 -m pip install -r requirements.txt
```

### Executing

To execute Andromeda your shell must have superuser/admmin permissions (for commands like wifiaudit or twitterscrape where the program has to write files to the computer)

Once that is done you can simple run the program(after cloning the repository) like this:-

```bash
cd projectAndromeda

sudo python3 Andromeda.py
```

### Exiting

To exit Andromeda Type in exit like so:-

```bash
Andromeda> exit
Exiting Andromeda
```

<hr>

## Wifi auditing

NOTE:- MAKE SURE YOU HAVE SUPERUSER PRIVILEGES TO RUN THE WIFI AUDIT MODULE

#### Port Scanning

To scan ports with Andromeda, use these commands:-

```bash
Andromeda> wifiaudit
Andromeda:wifiaudit> portscan
```

After doing so, enter the host to be scanned (such as 192.168.1.x etc.)

Then enter(integers only) the lower range of ports to be scanned such as 80 and then the higher range such as 8080 etc.

```bash
Host to be scanned> 192.168.1.1
```

The scan may take a while so go have a coffee break and come back to it. The open ports will be displayed as the open port has been scanned. After the scan completes, the amount of time taken will be displayed too.

#### Network Scanning

To run the network scanning module you need python 2. Use this command in Andromeda to run the network scanning module:-

```bash
Andromeda> wifiaudit
Andromeda:wifiaudit> networkscan
```

Then enter the command used for python 2 and the range to scan (192.168.1.1/24 etc.) and wait for the results. 

```bash
Range to scan: 192.168.1.1/24
```

The results will be shown in a table format after scanning -> 
IP ADDRESS (space) MAC ADDRESS


## Twitter Scraping

First lets start with twitter scraping. To start the twitter scraping module do:

```bash
Andromeda> twitterscrape
```

You will be prompted with some options on what to scrape for. Enter a number(respective to the option) and press enter to continue.

Enter the prompted question's answer (username etc);
Then enter the path you want the scrape's result's to be saved to;
Press enter and watch Andromeda magically work and come up with results.

Some errors may pop up so check the fixes over [here](https://github.com/FluffySnowman/projectAndromeda/blob/master/errors.md)

## Google Scraping

To start the google scraper use this command:

```bash
Andromeda> googlescrape
```

You will be prompted with what to scrape for. After typing in your choice press enter and wait for the results.

## Youtube to mp3 downloading

To start the youtube to mp3 downloading function use this command:

```bash
Andromeda> yt-download
```

You will be asked the link for the youtube video. Enter the link and hit enter to continue. The Download process will begin. 

NOTE:- It will take a variable amount of time to download depeding on your internet speed.

The download will be saved as a '.mp3' file in the current directory/folder that you are in- that is the projectAndromeda folder that you had cloned earlier unless you have made changes to it.

## Using the shell

To start the shell use this command:

```bash
Andromeda> shell
```

Depending on your operating system's default shell, a shell will spawn (example: for windows it could be cmd.exe or for linux it could be bash or zsh or ash etc.).

You will be presented with this interface. The ":~#" after Andromeda indicating that a shell is running:-

```bash
Andromeda:~#
```

There are now infinite possibilities of what you can do with this shell. Just like a normal terminal you can navigate through the file system, have fun with files and much more!

To exit the shell type in exit like so(Pressing cntl+c will only trigger an exception and the shell will be run again like in a normal terminal):-

```bash
Andromeda:~# exit

Exiting shell

Andromeda> 
```

And there you are now back to good old Andromeda.

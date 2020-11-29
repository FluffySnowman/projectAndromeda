import socket
import os
import subprocess
import time

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
print("\n\n")

#

while 1 < 2:


    print("Type help to view commands")
    input1 = input("Andromeda> ")


    #####################################
    ##########HELP#######################
    #####################################


    if (input1 == "help"):


        print("\nAll Commands: hackwifi, help,")
    #####################################
    ##########hackwifi###################
    #####################################


    elif (input1 == "hackwifi"):


        print("killing all network processes in 5 seconds")
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
        print("now enabling monitor mode for your wireless card")
        inputmonitormodecard = input("Name of the card to put to monitor mode: ")
        temp = ("airmon-ng start " + inputmonitormodecard)
        stream = os.popen(temp)
        output = stream.read()
        print(output)
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
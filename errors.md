# Errors

### CRITICAL:root:twint.get:User:

This error is related to the twint installation/module on your device.

Fix:-

```bash
pip3 install --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

### ERROR: Unable to extract JS player URL

This error is related to the youtube downloader package.

Fix:- update youtube-dl using pip

```bash
sudo pip3 -U youtube-dl
```

### ERROR OF RUNNING NETWORKSCAN ON WINDOWS 
Traceback (most recent call last):
File "network_scan.py", line 21, in scan
   answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
 File "C:\Python27\lib\site-packages\scapy\sendrecv.py", line 553, in srp
 File "C:\Python27\lib\site-packages\scapy\arch\windows\__init__.py", line 1061, in __init__
   "Sniffing and sending packets is not available at layer 2: "
RuntimeError: Sniffing and sending packets is not available at layer 2: winpcap is not installed. You may use conf.L3socket orconf.L3socket6 to access layer 3
#### Fix^ :- Download WinPcap for windows and the command should work.

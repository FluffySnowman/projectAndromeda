import scapy as scapyarp
import scapy as scapyether
  
request = scapyarp()
  
request.pdst = 'x'
broadcast = scapyether()
  
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout = 1)[0]
for element in clients:
    print(element[1].psrc + "      " + element[1].hwsrc)
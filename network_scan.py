import os
import scapy.all as scapy
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
    options = parser.parse_args()

    if not options.target:
        parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")
    return options

def scan(ip):
    arp_req_frame = scapy.ARP(pdst = ip)

    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    result = []
    for i in range(0,len(answered_list)):
        client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
        result.append(client_dict)

    return result

def display_result(result):
    print("-----------------------------------\nIP ADDRESS\tMAC ADDRESS\n-----------------------------------")
    x = 0
    for i in result:
        x = x+1
        print("{}\t{}".format(i["ip"], i["mac"]))
    print "Total targets: ", x


options = get_args()
scanned_output = scan(options.target)
display_result(scanned_output)
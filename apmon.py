#!/usr/bin/python2.7

# Wifi AP client monitoring script

import csv
import os
import datetime
import optparse

from scapy.all import *

probe_req = []


def probesniff(fm):
   if fm.haslayer(Dot11ProbeReq):
      client_name = fm.info
      if client_name == ap_name :
         if fm.addr2 not in probe_req:
            print "New Probe Request: ", client_name
            print "Time: ", datetime.now().strftime('%H:%M')
            print "MAC ", fm.addr2
            probe_req.append(fm.addr2)

            # Below is hard coded line to play WAV on new client
            #os.system('cvlc --play-and-exit /root/bin/avon.wav >/dev/null 2>&1')

            # Check CSV client database for known wifi clients
            id = 0
            for ap in range(0, ap_lines):
               if str.upper(ap_list[ap][1]) == str.upper(fm.addr2):
                  print "IDENTIFIED!: " + ap_list[ap][0] + "\n"
                  id = 1
            if id == 0:
               print "NOT IDENTIFIED!!!!!\n"

# Get command line inputs
parser = optparse.OptionParser("\nusage ./apmon.py " + "-i <interface> -d <APs database> -e <ESSID>")
parser.add_option('-i', dest='interface', type='string', help='specify minitor interface, i.e. wlan0mon')
parser.add_option('-d', dest='apdb', type='string', help='specify APS database (CSV format)')
parser.add_option('-e', dest='ap', type='string', help='specify AP (ESSID)')

(options, args) = parser.parse_args()

if (options.interface == None) | (options.apdb == None) | (options.ap == None):
   print parser.usage
   if (options.interface != None):
      os.system("ifconfig " + options.interface + " down")
      os.system("ifconfig " + options.interface + " up")
      print "\nList of available APs:"
      list_aps = "iwlist " + options.interface + " scan | grep ESSID | sed 's/ESSID//g' | sed 's/ //g' | sed 's/\://g' | sed 's/\"//g'"
      os.system(list_aps)
      print " "
   exit(0)
else:
   interface = options.interface
   apdb = options.apdb
   ap_name = options.ap

# Load AP database
with open(apdb, 'rb') as apfile:
   reader = csv.reader(apfile)
   ap_list = list(reader)

ap_lines = sum(1 for line in ap_list)

# Wifi Sniffing
print "\n"
print "AP Monitor"
print "==========\n"
print "Monitoring AP: " + ap_name + "\n"

sniff(iface= interface,prn=probesniff,store=0)







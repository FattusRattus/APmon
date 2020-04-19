# APmon
Wifi AP clients monitor

Description
----
This is based on the script from the book: Python Penetration Testing Essentials by Packt, Chapter 4 Wireless Pentesting.

Added command line features and CSV database for printing out known wifi clients.

Also, I have added ‘store=0’ to the Scapy sniffing routine, which almost every script I have seen misses out (including this one)! Without this (or some clean up) these scripts will soon grind your system to a halt – it happens very quickly on a Raspberry Pi3.

Converted to Python 3 - 19 April 2020

Usage
----
Scan for wifi APs: ./apmon.py -i wlan0<br/>
Monitor wifi AP: ./apmon.py -i wlan0mon -d sample.csv -e WifiAP<br/>


Python3 version: <br/>
Scan for wifi APs: ./apmon3.py -i wlan0<br/>
Monitor wifi AP: ./apmon3.py -i wlan0mon -d sample.csv -e WifiAP<br/>

Requirements
----
It requires the Scapy Python module and Aircrack suite: to put wifi adapter in monitor mode and to perform channel lock or hopping if you run multiple copies of this scripts against various wifi APs, i.e.:

Put wlan0 into monitor mode: airmon-ng start wlan0

Channel hop: airodump-ng -i wlan0mon

Note: It is not necessary to put the wifi interface in monitor mode, its just that I tend to have other stuff running in parallel that does require the interface in monitor mode.

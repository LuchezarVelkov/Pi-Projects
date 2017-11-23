#!/usr/bin/python
import os
import commands

hostname = "192.168.2.1"
response = os.system("ping -c 1 " + hostname)
if response == 0:
	print "Network Active"
else:
	os.system("sudo /etc/init.d/openvpn restart")
	print "Force Reconnect to VPN"

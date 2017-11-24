from collections import defaultdict

config = defaultdict()

#Directory where git code is present
config['Luki_FingerPrint'] = "/home/pi/FingerPrint"

#FingerPrint module init

#Read name of user 0
user_0_read = open("/home/pi/FingerPrint/Users/user_0.txt", "rw+")
user_0 = user_0_read.readline()
config['user_0'] = user_0

#Read name of user 1
user_1_read = open("/home/pi/FingerPrint/Users/user_1.txt", "rw+")
user_1 = user_1_read.readline()
config['user_1'] = user_1

#Read name of user 2
user_2_read = open("/home/pi/FingerPrint/Users/user_2.txt", "rw+")
user_2 = user_2_read.readline()
config['user_2'] = user_2

#Read name of user 3
user_3_read = open("/home/pi/FingerPrint/Users/user_3.txt", "rw+")
user_3 = user_3_read.readline()
config['user_3'] = user_3

#Read name of user 4
user_4_read = open("/home/pi/FingerPrint/Users/user_4.txt", "rw+")
user_4 = user_4_read.readline()
config['user_4'] = user_4

#Read name of user 5
user_5_read = open("/home/pi/FingerPrint/Users/user_5.txt", "rw+")
user_5 = user_5_read.readline()
config['user_5'] = user_5


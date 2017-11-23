import sys
import hashlib

##########################################################
#                   |Hash Calculator|                    #
#                                                        #
#  Start date of project is                              #
#                           09.10.2017                   #
#                                      Create by Luki    #
# To use hashes calculate use this command in terminal   #
# python hashes.py finger.jpg                            #
##########################################################

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha224 =hashlib.sha224()
sha256 = hashlib.sha256()
sha384 = hashlib.sha384()
sha512 =hashlib.sha512()

with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)
        sha224.update(data)
        sha256.update(data)
        sha384.update(data)
        sha512.update(data)

print("\n MD5: {0}".format(md5.hexdigest()))
print("\n SHA1: {0}".format(sha1.hexdigest()))
print("\n SHA224: {0}".format(sha224.hexdigest()))
print("\n SHA256: {0}".format(sha256.hexdigest()))
print("\n SHA384: {0}".format(sha384.hexdigest()))
print("\n SHA512: {0}".format(sha512.hexdigest()))


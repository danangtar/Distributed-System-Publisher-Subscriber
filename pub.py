#
# Server
# Binds PUB socket to tcp://*:5556
# Kirim data
#

import zmq
import os
import time
import pickle

context = zmq.Context()
socketpub = context.socket(zmq.PUB)
socketpub.bind("tcp://*:5557")

filenya = os.listdir("../filenya/.")
listnya = filenya[:(len(filenya)/2)]

sentence = {}

for files in listnya:
    print files
    for line in open("../filenya/"+files).xreadlines():
        cek = line.split()
        cek = " ".join(cek[4:])

        if (cek in sentence):
            sentence[cek] += 1
        else:
            sentence[cek] = 0

sort = sorted(sentence.items(), key=lambda x:x[1], reverse=True)
sort = pickle.dumps(sort)

while True:
	socketpub.send(sort)
#socketpub.send("1")
time.sleep(10)    
#time.sleep(5)

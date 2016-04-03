#
# Client
# Connects SUB socket to tcp://localhost:5556
# Menerima hasil
#

import zmq
import pickle

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print "ok"

socket.connect("tcp://localhost:5556")
socket.connect("tcp://localhost:5557")

# Subscribe to zipcode, default is NYC, 10001
#zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"

# Python 2 - ascii bytes to unicode str
#if isinstance(zip_filter, bytes):
#    zip_filter = zip_filter.decode('ascii')
#socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
socket.setsockopt(zmq.SUBSCRIBE, '')


terima = socket.recv()
hasil1 = pickle.loads(terima)

terima = socket.recv()
hasil2 = pickle.loads(terima)
hasil2 = dict((x, y) for x, y in hasil2)

for freq in hasil1:
    if freq[0] in hasil2:
        hasil2[freq[0]] = hasil2[freq[0]] + freq[1]
    else:
        hasil2[freq[0]] = freq[1]

hasil2 = sorted(hasil2.items(), key=lambda x: x[1], reverse=True)

i = 0
while i < 10:
    print hasil2[i]
    i = i + 1
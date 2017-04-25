import socket
import sys
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)

print 'connecting to %s port %s' % server_address
sock.connect(server_address)
print sock.recv(100)
topic = raw_input("Masukkan topik : ")
dict_pesan = {
   "topic" : topic
}
text_json = json.dumps(dict_pesan)
sock.sendall(text_json)
while True :
    data_json = sock.recv(256)
    if data_json != " " :
        dict_hasil = json.loads(data_json)
        print dict_hasil["topik"]+" "+dict_hasil["pesan"]
print 'closing socket'
sock.close()

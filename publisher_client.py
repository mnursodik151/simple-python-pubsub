import socket
import sys
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)

print 'connecting to %s port %s' % server_address
sock.connect(server_address)
print sock.recv(100)
topic = raw_input("Masukkan topik : ")
while True :
    message = raw_input("Masukkan pesan : ")
    dict_pesan = {
       "topic" : topic,
       "pesan" : message
    }
    text_json = json.dumps(dict_pesan)
    sock.sendall(text_json)
print 'closing socket'
sock.close()

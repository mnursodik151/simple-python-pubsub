import socket
import sys
from thread import start_new_thread
import json

# Create a TCP/IP socket
sockpub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
sockpub.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sockpub.bind(server_address)
# Listen for incoming connections
sockpub.listen(10)

# Create a TCP/IP socket
socksub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
socksub.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('localhost', 10001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
socksub.bind(server_address)
# Listen for incoming connections
socksub.listen(10)

global dict_hasil
global status
dict_hasil = ""
status = False

def handle_connection_pub(conn) :
    conn.sendall("You have been conected")
    try :
        while True :
            data_json_pub = conn.recv(256)
            global dict_hasil
            global status
            if data_json_pub != " " :
                dict_hasil = json.loads(data_json_pub)
                print dict_hasil['topic']+" "+dict_hasil["pesan"]
                status = True
        conn.close()
        print "client disconnected"
    except socket.error :
        conn.close()
        print "client disconnected"

def handle_connection_sub(conn) :
    conn.sendall("You have been conected")
    try :
        data_json_sub = connection.recv(256)
        global dict_hasil
        global status
        if data_json_sub != " " :
            dict_subscriber = json.loads(data_json_sub)
            print status
            dict_hasil_temp = ""
            if status != False :
                while True :
                    if dict_subscriber['topic'] in dict_hasil['topic'] and dict_hasil != dict_hasil_temp :
                        dict_pesan = {
                            "topik" : dict_hasil["topic"],
                            "pesan" : dict_hasil["pesan"]
                        }
                        text_json = json.dumps(dict_pesan)
                        conn.sendall(text_json)
                        dict_hasil_temp = dict_hasil
        conn.close()
        print "client disconnected"
    except socket.error :
        conn.close()
        print "client disconnected"

try :
    while True :
        print "Starting server"
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sockpub.accept()
        start_new_thread(handle_connection_pub, (connection,))
        connection, client_address = socksub.accept()
        start_new_thread(handle_connection_sub, (connection,))
except KeyboardInterrupt :
    print "I have dieded"

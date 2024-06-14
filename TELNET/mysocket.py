import socket

from django.db import connections

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(( 'data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 504))

sock.listen(1)

log = open("log.txt", "w")

def handler(connection, address):
    while True:
        data = c.recv(1024)
        print(data)
        for connection in connections:
            connection.send(bytes(data + "Hello World"))
        if not data:
            connection.remove(c)
            c.close()
            break

while True:
    connection, address = sock.accept()
    cThread = threading.Thread(target=handler, args=(connection, address))
    cThread.daemon = True
    cThread.start()
    log.write(connection + "/n" + address + "/n")
    data, addr = sock.recv()
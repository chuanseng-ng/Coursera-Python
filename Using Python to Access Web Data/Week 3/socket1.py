import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                  # Standard line for socket
mysock.connect(('data.pr4e.org', 80))                                       # Port 80 connects to web server (HTTP port) to access data.pr4e.org (host)
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  # Request web page and prepare
mysock.send(cmd)                                                            # Send web page request

while True:
    data = mysock.recv(512)                                                 # Receive web page data
    if len(data) < 1:
        break
    print(data.decode(),end='')                                             # Decode received web page data

mysock.close()
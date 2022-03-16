#This file will create a server
import socket
import sys

#Passing an empty string to make all interfaces avaiable
HOST = ''
PORT = 9090

newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('Socket created successfully')

#Bindind socket to local host and port
try:
  newSocket.bind((HOST, PORT))
except socket.error as msg:
  print(f'Binding has failed. Error code: {str(msg[0])} MSG: {msg[1]}')
  sys.exit()

newSocket.listen(5)
print('Socket listening')

#Let the server talk with the client
print('Run: telnet localhost 9090 to connect to this server')

while True:
  c, address = newSocket.accept()
  data = c.recv(512)
  print('Connected with ', address)

  if data:
    file = open("store.dat", "+w")
    print(f'Connection from address : {address[0]}')
    file.write(address[0])
    file.write(" : ")
    file.write(data.decode("utf-8"))
    file.close()
    c.close()

newSocket.close()

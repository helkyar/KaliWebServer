#This file will create a server
import socket
import sys

#Passing an empty string to make all interfaces avaiable
HOST = ''
PORT = 9090

newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created successfully')

#Bindind socket to local host and port
try:
  newSocket.bind((HOST, PORT))
except socket.error as msg:
  print('Binding has failed. Error code: ' + str(msg[0]) + ' MSG: ' + msg[1])
  sys.exit()

newSocket.listen(10)
print('Socket listening')

#Let the server talk with the client
print('Run: telnet localhost 9090 to connect to this server')

while True:
  connection, address = newSocket.accept()
  print('Connected with ' + address[0] + ':' + str(address[1]))

newSocket.close()

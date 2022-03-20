#!/usr/bin/python2.7
import socket

#creating a socket object
newSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind this socket object to an IP address and port
HOST = ""
PORT = 9090
try:
  newSocket.bind((HOST, PORT))
except socket.error as msg:
  print(f'Binding has failed. Error code: {str(msg[0])} MSG: {msg[1]}')
  sys.exit()
  
#Let the server talk with the client
print('Run: telnet localhost 9090 to connect to this server')

newSock.listen(2)
(client, (ip, sock)) = newSock.accept()
print("Recieved connection from ", ip)

print ("Starting our ECHO Server object that will echo to the client")
data = "mock data"


while len(data):
  data = client.recv(2048)
  print ("Client sent this data : ", data)
  client.send(data)
print("Closing our connection after sending data to the client....")
client.close()

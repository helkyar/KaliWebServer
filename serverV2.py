import socket
import sys

try:
  newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print('Socket successfully created')

except socket.error as err:
  print('Socket creation failed with error %s' % (err))

#Default port for the socket
port = 80

try:
  host_ip = socket.gethostbyname('www.google.com')

except socket.gaierror:
  print('Couldn\'t resolve the host')
  sys.exit()

#Connecting to the server
newSocket.connect((host_ip, port))
print('Socket successfully connected on port: %s' % (host_ip))

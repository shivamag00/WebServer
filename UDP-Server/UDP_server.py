from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))			#assigning socket 12000 to server
print("The server is ready to receive")
while (1):
	message, clientAddress = serverSocket.recvfrom(2048)	#store the message and client's address
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)		#send back to the client
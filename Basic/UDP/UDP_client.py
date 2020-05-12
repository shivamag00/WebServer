from socket import *				#importing socket module
serverName = '127.0.0.1' 			#setting the ip address of the server
serverPort = 12000						#settting the server port
clientSocket = socket(AF_INET, SOCK_DGRAM)		#using IPv4 & UDP Socket
message = input('Input lowercase sentence:').encode()
clientSocket.sendto(message,(serverName, serverPort))			#attaching destination address to message and send the message
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)	#When message arrives at Client store the messsage and address of the sender
print(modifiedMessage)
clientSocket.close()
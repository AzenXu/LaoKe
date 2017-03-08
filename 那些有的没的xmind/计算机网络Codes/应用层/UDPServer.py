from socket import *
serverPort = 10008
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        print("got message ! it is: %s, clientAddress is : %s" % (message, clientAddress))
        modifiedMessage = message.upper()
        serverSocket.sendto(modifiedMessage, clientAddress)

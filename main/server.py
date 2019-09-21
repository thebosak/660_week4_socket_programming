'''
Created on September 16, 2019

@author: Brad Bosak
'''
import socket
import sys  

def createServer():
    #Create server socket
    serverSocket = socket.socket()          
    
    #Define port and bind
    port = 9500
    serverSocket.bind(('', port))
    
    serverSocket.listen(5)      
    print ("Server socket is created, binded to port {0}, and listening".format(port))
    
    while True:
        
        #Find client
        (clientSocket, address) = serverSocket.accept()
        print ("Connection found from ", address)
        dataFromClient = clientSocket.recv(1024).decode()
        
        #Logic around messages
        if dataFromClient == "Hello":
            returnMessage = "Hi"
        else:
            returnMessage = "Goodbye"
        #Print client message and send return message
        print ('Message from client is:', dataFromClient)
        clientSocket.send(returnMessage.encode())

#Call main function
createServer()
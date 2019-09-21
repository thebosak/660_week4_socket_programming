'''
Created on September 18, 2019

@author: Brad Bosak
'''
import socket
def createClient():
    #Create client socket
    clientSocket = socket.socket()
    
    #Define port
    port = 9500
    
    #Connect socket
    clientSocket.connect(('127.0.0.1', port))
    clientMessage = input("Enter your message to send to the server: ")
    #Send message to client
    clientSocket.send(clientMessage.encode())
    #Receive and print message from server
    dataFromServer = clientSocket.recv(1024).decode()
    print ("Message from server is", dataFromServer)
    
#Call main function
createClient()
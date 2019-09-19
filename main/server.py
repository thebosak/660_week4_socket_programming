'''
Created on September 16, 2019

@author: Brad Bosak
'''
import socket
import sys  
#Create main function
def main():
    # next create a socket object 
    serverSocket = socket.socket()          
    print ("Socket successfully created")
      
    # reserve a port on your computer
    port = 9500                
      
    serverSocket.bind(('', port))
    print ("Server socket binded to %s" %(port)) 
      
    serverSocket.listen(5)      
    print ("Server socket is listening")
    
    while True: 
        
        (clientSocket, address) = serverSocket.accept()
        print ("Connection found from, ", address)
        dataFromClient = clientSocket.recv(1024).decode()
        if dataFromClient == "Hello":
            returnMessage = "Hi"
        else:
            returnMessage = "Goodbye"
        print ('Message from client is:', dataFromClient)
        clientSocket.send(returnMessage.encode())
    
#        clientData = clientSocket.recv(1024)
#        print('Data sent from client: ', clientSocket.recv(1024))
#        returnMessage = "Hi"
#        clientSocket.sendall(b'Hi')
#        clientSocket.close()
    
#Call main function
main()
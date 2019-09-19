'''
Created on September 18, 2019

@author: Brad Bosak
'''
import socket
#Create main function
def main():
    # Create a socket object 
    clientSocket = socket.socket()
      
    # Define the port on which you want to connect 
    port = 9500
    
    clientSocket.connect(('127.0.0.1', port))
    clientMessage = input("Enter your message to send to the server: ")
    clientSocket.send(clientMessage.encode())
#     clientSocket.send('Hello'.encode())
    dataFromServer = clientSocket.recv(1024).decode()
    print ("Message from server is", dataFromServer)
    
    # receive data from the server 
#     print ('Data received from server: ', clientSocket.recv(1024))
    # close the connection 
#     clientSocket.close()
    
#Call main function
main()
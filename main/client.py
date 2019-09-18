'''
Created on September 18, 2019

@author: Brad Bosak
'''
import socket
#Create main function
def main():
    # Create a socket object 
    s = socket.socket()
      
    # Define the port on which you want to connect 
    port = 12345
      
    # connect to the server on local computer
    s.connect(('127.0.0.1', port))
      
    # receive data from the server 
    print ('Data received: ', s.recv(1024))
    # close the connection 
    s.close() 
    
#Call main function
main()
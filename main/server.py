'''
Created on September 16, 2019

@author: Brad Bosak
'''
import socket
import sys  
#Create main function
def main():
    # next create a socket object 
    s = socket.socket()          
    print ("Socket successfully created")
      
    # reserve a port on your computer
    port = 12345                
      
    s.bind(('', port))         
    print ("socket binded to %s" %(port)) 
      
    s.listen(5)      
    print ("socket is listening")
      
    while True: 
      
       c, addr = s.accept()      
       print ('Got connection from', addr)
       c.sendall(b'Thank you for connecting')
       c.close()
    
#Call main function
main()
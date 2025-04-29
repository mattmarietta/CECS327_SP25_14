#Client side code
import socket
#Set up a socket for the client
client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Gather the host and the port from the command line
host = input("Enter the IP to connect to: ")
port = int(input("Enter the port to connect to: "))

#Next connect to the given host and port
client_s.connect((host, port))

#While the connection is open, get the message from the user and send it to the server
#Then wait for a response from the server and print it
#If they say exit, break out of loop
while True:
    message = input("Enter a message to send to the server: ")
    client_s.send(bytearray(str(message), encoding='utf-8'))
    if message == "exit":
        break
    server_message = client_s.recv(40000)
    print("Server:", server_message.decode('utf-8'))

#Close the client socket that was opened
client_s.close()
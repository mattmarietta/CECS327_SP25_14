import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Enter the IP to connect to: ")
port_num = int(input("Enter the port to connect to: "))

#Bind the sockets to the host and port number and then listen for incoming connections
#Set the socket and address to accept the incoming connection that was tehre
server_socket.bind((host, port_num))
server_socket.listen(5)
incomingSocket, incomingAdress = server_socket.accept()

#Need to handle data while this is still open, use while loop to keep the connection open
while True:
    #Get the message and decode, if it is exit then we will stop
    message = incomingSocket.recv(1024).decode()
    print("Client:", message)
    if message == "exit":
        break
    #Return the message with the uppercase version and send it back to the client
    message = message.upper()
    incomingSocket.send(message.encode())

#Close all the sockets we opened
server_socket.close()
incomingSocket.close()
#Client side code
import socket
#Set up a socket for the client
client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Gather the host and the port from the command line
host = input("Enter the IP to connect to: ")
port = int(input("Enter the port to connect to: "))

#Next connect to the given host and port
client_s.connect((host, port))

valid_queries = {
    "1": "What is the average moisture inside my kitchen fridge in the past three hours?",
    "2": "What is the average water consumption per cycle in my smart dishwasher?",
    "3": "Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?"
}

print("Choose a query:")
for key, query in valid_queries.items():
    print(f"{key}: {query}")

#Get the users choice from teh query and then we will use it if the query is valid
choice = input("Enter the number of your choice: ")
query = valid_queries.get(choice)

#If the query is valid, then we can send it to the server and wait for a response
if query:
    #Changed from message to query from o.g. code
    #Send to the server and then wait for a response
    client_socket.send(query.encode())
    response = client_socket.recv(1024).decode()
    print("Server response:", response)
else:
    #If it it is not valid, then print error message and give user the option again
    print("Sorry, this query or choice is not valid.")
    print("Please try one of the following:")
    for query in valid_queries.values():
        print(f"- {query}")

#Close the client socket that was opened
client_s.close()
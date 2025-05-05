#Client side code
import socket
#Set up a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Gather the host and the port from the command line
host = input("Enter the IP to connect to: ")
port = int(input("Enter the port to connect to: "))

#Next connect to the given host and port
client_socket.connect((host, port))

poss_queries = {
    "1": "What is the average moisture inside my kitchen fridge in the past three hours?",
    "2": "What is the average water consumption per cycle in my smart dishwasher?",
    "3": "Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?"
}
while True:
    #Print the queries to the user so they can choose one
    print("\nChoose a query:")
    for key, query in poss_queries.items():
        print(f"{key}: {query}")

    #Get the users choice from the query and then we will use it if the query is valid
    choice = input("Enter the number of your choice (or 'exit' to quit):")
    if choice == "exit":
        break
    query = poss_queries.get(choice)

    #If the query is valid, then we can send it to the server and wait for a response
    if query:
        #Changed from message to query from o.g. code
        #Send to the server and then wait for a response
        client_socket.send(choice.encode())
        response = client_socket.recv(1024).decode()
        print("Server response:", response)
    else:
        #If it is not valid, then print error message and give user the option again
        print("Sorry, the one you entered is not valid.")
        print("Please try again and choose from the following:")
        for query in poss_queries.values():
            print(f"- {query}")

#Close the client socket that was opened
client_socket.close()

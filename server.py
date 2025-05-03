import socket
import psycopg2
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = psycopg2.connect("postgresql://neondb_owner:npg_E6AQYSafVP2x@ep-round-flower-a5hd2927-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require")
cursor = conn.cursor()

host = input("Enter the IP to connect to: ")
port_num = int(input("Enter the port to connect to: "))

server_socket.bind((host, port_num))
server_socket.listen(5)
incomingSocket, incomingAdress = server_socket.accept()

while True:
    message = incomingSocket.recv(1024).decode()

    if message == "exit":
        break

    if message == '1':
        cursor.execute("SELECT AVG((payload::json ->> 'Moisture Meter - Moisture Meter')::float) AS moisture FROM public.\"Group 14_virtual\" WHERE (payload::json ->> 'Moisture Meter - Moisture Meter')::float is not null AND time >= NOW() - INTERVAL '3 HOURS' ")
        result = cursor.fetchone()
        result = str(result[0])
    message = message.upper()
    incomingSocket.send(result.encode())

server_socket.close()
incomingSocket.close()
cursor.close()
conn.close()
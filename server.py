import socket
import psycopg2
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = psycopg2.connect("postgresql://neondb_owner:npg_E6AQYSafVP2x@ep-round-flower-a5hd2927-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require")
cursor = conn.cursor()

host = input("Enter the IP to connect to: ")
port_num = int(input("Enter the port to connect to: "))

server_socket.bind((host, port_num))
server_socket.listen(5)
incomingSocket, incomingAddress = server_socket.accept()

while True:
    message = incomingSocket.recv(1024).decode()

    if message == "exit":
        break

    if message == '1':
        # SELECT AVG((payload::json ->> 'Moisture Meter - Moisture Meter')::float) AS moisture
        # FROM public.\"Group 14_virtual\"
        # WHERE (payload::json ->> 'Moisture Meter - Moisture Meter')::float is not null AND time >= NOW() - INTERVAL '3 HOURS'
        cursor.execute("SELECT AVG((payload::json ->> 'Moisture Meter - Moisture Meter')::float) AS moisture FROM public.\"Group 14_virtual\" WHERE (payload::json ->> 'Moisture Meter - Moisture Meter')::float is not null AND time >= NOW() - INTERVAL '3 HOURS' ")
        result = cursor.fetchone()
        result = f'Average fridge moisture in the past three hours: {result[0]:.2f}% RH'

    elif message == '2':
        # SELECT AVG((payload::json ->> 'YF-S201 - WaterFlow')::float)*0.264172 AS water_flow
        # FROM public.\"Group 14_virtual\"
        # WHERE(payload::json ->> 'YF-S201 - WaterFlow')::float is not null
        cursor.execute("SELECT AVG((payload::json ->> 'YF-S201 - WaterFlow')::float)*0.264172 AS water_flow FROM public.\"Group 14_virtual\" WHERE(payload::json ->> 'YF-S201 - WaterFlow')::float is not null")
        result = cursor.fetchone()
        result = f'Average water consumption: {result[0]:.2f} gallons'

    elif message == '3':
        # WITH Devices as (SELECT CASE
        #     WHEN (payload::json ->> 'board_name') = 'Arduino Uno'
        #     THEN 'Refrigerator 1'
        #     WHEN(payload::json ->> 'board_name') = 'Arduino Uno 2'
        #     THEN 'Refrigerator 2'
        #     WHEN(payload::json ->> 'board_name') = 'Arduino Uno 3'
        #     THEN 'Dishwasher'
        #     ELSE null
        #     END as device, CASE
        #     WHEN(payload::json ->> 'ACS712 - Ammeter')::float is not null
        #     THEN(payload::json ->> 'ACS712 - Ammeter')::float
        #     WHEN(payload::json ->> 'ACS712 - Ammeter 2')::float is not null
        #     THEN(payload::json ->> 'ACS712 - Ammeter 2')::float
        #     WHEN(payload::json ->> 'Ammeter 3')::float is not null
        #     THEN(payload::json ->> 'Ammeter 3')::float
        #     ELSE null
        #     END as ammeter
        #     FROM public.\"Group 14_virtual\"
        #     WHERE payload::json ->> 'board_name' IN('Arduino Uno', 'Arduino Uno 2', 'Arduino Uno 3'))
        #
        # SELECT device, AVG(ammeter) AS avg_energy_kWh
        # FROM Devices
        # GROUP BY device
        # ORDER BY avg_energy_kWh desc
        # LIMIT 1
        cursor.execute("WITH Devices as (SELECT CASE WHEN (payload::json ->> 'board_name') = 'Arduino Uno' THEN 'Refrigerator 1' WHEN(payload::json ->> 'board_name') = 'Arduino Uno 2' THEN 'Refrigerator 2' WHEN(payload::json ->> 'board_name') = 'Arduino Uno 3' THEN 'Dishwasher' ELSE null END as device, CASE WHEN(payload::json ->> 'ACS712 - Ammeter')::float is not null THEN(payload::json ->> 'ACS712 - Ammeter')::float WHEN(payload::json ->> 'ACS712 - Ammeter 2')::float is not null THEN(payload::json ->> 'ACS712 - Ammeter 2')::float WHEN(payload::json ->> 'Ammeter 3')::float is not null THEN(payload::json ->> 'Ammeter 3')::float ELSE null END as ammeter FROM public.\"Group 14_virtual\" WHERE payload::json ->> 'board_name' IN('Arduino Uno', 'Arduino Uno 2', 'Arduino Uno 3')) SELECT device, AVG(ammeter) AS avg_energy_kWh FROM Devices GROUP BY device ORDER BY avg_energy_kWh desc LIMIT 1")
        result = cursor.fetchall()[0]
        device = result[0]
        result = f'{device} consumed the most energy: {result[1]:.2f} kWh'

    else:
        result = 'Sorry, this query cannot be processed.'
    incomingSocket.send(result.encode())

server_socket.close()
incomingSocket.close()
cursor.close()
conn.close()

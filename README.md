
# IoT_M2

This project simulates IoT device integration, data visualization, and communication using cloud-based infrastructure and virtual hardware components.

---

## Setup Instructions

### Database Configuration

1. **Visit** [Dataniz](https://dataniz.com)
2. Click on the **gear icon**.
3. Create a:
   - **Source**
   - **Destination**
4. **Visit** [Neon](https://neon.tech) and:
   - Create a new **project**.
   - Copy the **PostgreSQL connection string**.
5. Return to **Dataviz** and:
   - Paste the connection string when prompted during **destination** setup.
6. Create a **Connection**.

---

### Virtual Hardware Setup

1. Navigate to the **Virtual Hardware** section.
2. Create the following **Devices**:
   - Refrigerator 1
   - Refrigerator 2
   - Dishwasher
3. For each device, create a dedicated **Arduino Board**:
   - Arduino 1 → Refrigerator 1
   - Arduino 2 → Refrigerator 2
   - Arduino 3 → Dishwasher
4. Add **Sensors**:
   - **ACS-712** (Current sensor) for all devices
   - **Moisture Meter** and **AMG8833 (Thermal Camera)** for both refrigerators
   - **YF-S201 (Water Flow Sensor)** for the dishwasher
5. Go to the **Metadata** section:
   - Create metadata entries for each device.
6. Go to the **Data Visualization** panel:
   - Turn on **every sensor** for each device.

---

## Running Queries via GCP VM

### Server & Client Setup

1. **Start your GCP VM instances** (one for the client, one for the server).
2. **Download** `client.py` and `server.py` files to your local machine.
3. **Upload** each script to its respective VM:
   - `server.py` → Server VM
   - `client.py` → Client VM
4. On each VM:
   - Open the **command line terminal**
   - `cd` into the directory containing the Python script

### Start the Server

1. On the **server VM**, run:
   ```bash
   python server.py
   ```
2. When prompted:
   - Enter your **host IP address** (use `ipconfig` or `ifconfig` to find this)
   - Enter a **port number** (e.g., `8080`)

### Start the Client

1. On the **client VM**, run:
   ```bash
   python client.py
   ```
2. When prompted:
   - Enter the **public IP** of the server VM (visible on GCP)
   - Use the **same port number** you used on the server

---

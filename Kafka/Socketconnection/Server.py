import socket
import errno
import json
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("Port"))
SERVER = socket.gethostbyname(socket.gethostname()) #get Ip addr
print(SERVER)
ADDR = ("", PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

# bind this socket to the address we configured earlier
server.bind(ADDR)    
server.listen(2)
print(f"[LISTENING] Server is listening on {SERVER}")
conn, addr = server.accept()
print(f'CONNECTION FROM {addr} HAS BEEN ESTABLISHED')
connected = True
while connected:
        try:
            for i in range(0,5):
                route = ['Newyork,USA','Chennai, India','Bengaluru, India','London,UK']
                routefrom = random.choice(route)
                routeto = random.choice(route)
                if (routefrom!=routeto):
                    data = {
                        "Battery_Level":round(random.uniform(2.00,5.00),2),
                        "Device_ID": random.randint(1150,1158),
                        "First_Sensor_temperature":round(random.uniform(10,40.0),1),
                        "Route_From":routefrom,
                        "Route_To":routeto
                        }
                     # Convert dictionary to JSON format and encode it
                    userdata = (json.dumps(data, indent=1)).encode(FORMAT)  # Convert dictionary to JSON format and encode it
                    conn.send(userdata)
                    # print(userdata)
                    time.sleep(10)
                else:
                    continue

           
                       
                                
        except IOError as e:
            if e.errno == errno.EPIPE:
                pass

conn.close()    #close the connection
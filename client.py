import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddress = input("Enter the IP Address: ")
port = int(input("Enter the port: "))
# Connect to the server (replace 'localhost' with the server's IP address if needed)
client_socket.connect((ipaddress, port))

name = input("Enter your name: ")
client_socket.send(name.encode())

while True:
    # Receive and print server's message (options or game message)
    message = client_socket.recv(1024).decode()
    print(message)
    
    if "Choose difficulty" in message:
        difficulty = input().lower()
        client_socket.send(difficulty.encode())
        if difficulty == "exit":
            break
    elif "Do you want to play again?" in message:
        play_again = input().lower()
        client_socket.send(play_again.encode())
        if play_again != "yes":
            leaderboard = client_socket.recv(1024).decode()
            print(leaderboard)
            break
    else:
        # User input
        user_input = input()
        # Send user input to the server
        client_socket.send(user_input.encode())
    
# Receive and print the leaderboard
leaderboard = client_socket.recv(1024).decode()
print(leaderboard)

# Close the client socket
client_socket.close()

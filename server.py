import socket
import random
import json

# Load leaderboard data from file
def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save leaderboard data to file
def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file)

# Generate a random number based on difficulty
def generate_number(difficulty):
    if difficulty == "easy":
        return random.randint(1, 50)
    elif difficulty == "medium":
        return random.randint(1, 100)
    elif difficulty == "hard":
        return random.randint(1, 500)
    else:
        return random.randint(1, 50)  # Default to easy

# Update leaderboard with user's score
def update_leaderboard(leaderboard, name, score):
    leaderboard.append({"name": name, "score": score})
    leaderboard.sort(key=lambda x: x["score"])
    save_leaderboard(leaderboard)

# Print leaderboard
def print_leaderboard(leaderboard):
    leaderboard_string = "\nLeaderboard:\n"
    for idx, entry in enumerate(leaderboard):
        leaderboard_string += f"{idx+1}. {entry['name']}: {entry['score']} tries\n"
    print(leaderboard_string)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('192.168.1.124', 12345))

# Listen for incoming connections (maximum 5 queued connections)
server_socket.listen(5)
print('Server listening on port 12345...')

leaderboard = load_leaderboard()

while True:
    # Accept incoming client connections
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))
    
    # Receive name from the client
    name = client_socket.recv(1024).decode()
    
    while True:
        # Send difficulty options to the client
        client_socket.send("Choose difficulty: easy, medium, hard, exit".encode())
        # Receive difficulty choice from the client
        difficulty = client_socket.recv(1024).decode()
        
        if difficulty.lower() == "exit":
            break
        
        # Generate the number based on difficulty
        number_to_guess = generate_number(difficulty)
        
        # Send a message to the client to start the game
        start_message = f"Welcome {name}! Guess the number!."
        client_socket.send(start_message.encode())
        
        # Play the game
        tries = 0
        while True:
            guess = int(client_socket.recv(1024).decode())
            tries += 1
            if guess == number_to_guess:
                client_socket.send("Correct!".encode())
                update_leaderboard(leaderboard, name, tries)
                break
            elif guess < number_to_guess:
                client_socket.send("Too low! Try again.".encode())
            else:
                client_socket.send("Too high! Try again.".encode())
        
        # Ask if the user wants to play again
        client_socket.send("Do you want to play again? (yes/no)".encode())
        play_again = client_socket.recv(1024).decode()
        if play_again.lower() != "yes":
            break
    
    # Print leaderboard and close the client socket
    print_leaderboard(leaderboard)
    client_socket.send(print_leaderboard(leaderboard).encode())
    client_socket.close()

# Close the server socket
server_socket.close()

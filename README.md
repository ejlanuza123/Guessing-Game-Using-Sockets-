# Guessing-Game-Using-Sockets-
# Client-Server Number Guessing Game

This repository contains a simple client-server number guessing game implemented in Python.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/client-server-number-guessing-game.git
    ```

2. Navigate to the server directory:

    ```
    cd client-server-number-guessing-game/server
    ```

3. Run the server:

    ```
    python server.py
    ```

4. Open another terminal window and navigate to the client directory:

    ```
    cd client-server-number-guessing-game/client
    ```

5. Run the client:

    ```
    python client.py
    ```

## How to Play

1. Run the server and client as instructed above.
2. Enter your name when prompted.
3. Choose the difficulty level (easy, medium, or hard).
4. Guess the number until you get it right.
5. You can play again if you wish.

## Features

- User/client can repeat the game without disconnecting.
- User can choose difficulty (easy, medium, or hard).
- Scoring mechanism based on the number of tries.
- Leaderboard displaying the name of the user and their score.
- Persistence - server saves user's name, score, and the last chosen difficulty.


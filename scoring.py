import os

from funcs import *  # Imports the dice rolling function and my custom line replacing function


def scoring(roll1, roll2, playerScore):
    playerScore = roll1 + roll2 + playerScore  # Adds the roll score to current score

    even = (roll1 + roll2) % 2  # Checks if the roll score is even
    if even == 0:
        playerScore = playerScore + 10  # Adds 10 if even
    else:
        playerScore = playerScore - 5  # Subtracts 5 if not

    if roll1 == roll2: print("You rolled doubles"); roll = rollDice(); playerScore = playerScore + roll
    # Adds the double rolling mechanic

    if playerScore < 0: playerScore = 0  # Ensures score is not below zero

    return playerScore


def saveScore(score0, user0):
    try:
        f = open("scores.csv", "r+")  # Opens the score file in read mode
    except FileNotFoundError:
        f = open("scores.csv", "a+")  # Creates a file if not existent
    fileSize = os.path.getsize("scores.csv")  # Calculates the size of the file
    x = -1
    userScore = "{}, {}".format(user0, score0)  # Format the user's score and Username
    if fileSize == 0:  # Checks if the file is empty
        f.write("{}\n".format(userScore))  # If so the score is written on the first line
        return  # Ends the function
    for line in f.readlines():  # Counts every line in the file (Should be five)
        x = x + 1
        if line == "":  # Checks if the line is empty
            f.seek(x)
            f.write("{}\n".format(userScore))  # Writes score at the particular line
            break
        score1 = int(line.split(",")[1])  # Separates the score and the username
        if score0 > score1:  # Sees if current score is higher than the saved score
            insertLine(x, "scores.csv", userScore)  # If so insert the line with the user and score
            break


def scoreboard():
    try:
        f = open("scores.csv", "r+")  # Opens the score file in read mode
    except FileNotFoundError:
        f = open("scores.csv", "a+")  # Creates a file if not existent
    fileSize = os.path.getsize("scores.csv")
    if fileSize != 0:
        formatPrint(f.read())
    else:
        print("No one has played the game")
    pause()
    return ()


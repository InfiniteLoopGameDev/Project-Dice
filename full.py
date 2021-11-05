import sys
import os
from tkinter import *
from tkinter import ttk

def formatPrint(text):
    for i in range(50):
        print("\n")
    print("Project Dice")
    print("------------------------")
    print(text)


def rollDice():
    import random
    input("Press [Enter] to roll")
    num = random.randint(1, 6)
    print("You rolled a {}".format(num))
    return num


def isEven(x):
    mod = x % 2
    if mod == 0:
        return True
    else:
        return False


def insertLine(lineNum, file, newLine):
    f = open(file, "r+")  # Opens file in read mode
    newLine = "{}\n".format(newLine)  # Formats the newline
    data = f.readlines()  # Stores contents of files as a list
    data.insert(lineNum, newLine)  # Inserts line in the list
    try:
        data.pop(5)  # Removes the 6th score
    except IndexError:
        pass
    f.close()
    f = open(file, "w+")  # Purges the file by opening in write mode
    f.writelines(data)  # Writes list on the file
    f.close()


def pause():
    input("Press [Enter] to continue")


def menu_gui():
    root = Tk()
    root.title("Project Dice")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    var = IntVar()
    title = ttk.Label(mainframe, text="Project Dice").grid(column=2, row=1)
    login = ttk.Button(mainframe, text="Login", command=lambda: menu(2)).grid(column=2, row=2)
    sign_up = ttk.Button(mainframe, text="Sign Up", command=lambda: [menu(3), root.destroy()]).grid(column=2, row=3)
    scoreboard = ttk.Button(mainframe, text="Scoreboard", command=lambda: [menu(1), root.destroy()]).grid(column=2, row=4)
    close = ttk.Button(mainframe, text="Close", command=lambda: root.destroy()).grid(column=2, row=5)
    spacer1 = ttk.Frame(mainframe, width=40, height=40).grid(column=1, row=1)
    spacer2 = ttk.Frame(mainframe, width=40, height=40).grid(column=3, row=1)
    spacer3 = ttk.Frame(mainframe, width=40, height=20).grid(column=2, row=6)

    for n in sorted(root.children):
        root.children[n].pack()

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=10)

    root.mainloop()

    
def menu(input0):
    while True:
        if input0 == 1:
            scoreboard()
        elif input0 == 2:
            user1, user2 = login()
            if user1 == "" and user2 == "":
                pass
            else:
                game(user1, user2)
        elif input0 == 3:
            sign_up()
            formatPrint("Sign Up Successful! \nPlease Proceed to Login or Sign Up another user")
            pause()


def game(user0, user1):  # Asks the two users from the main program
    currentUser = lambda x: x[0]  # Lambda functions to get the User from the tuple
    userScore = lambda x: x[1]  # Lambda functions to get the Score from the tuple
    users = [(user0, 0), (user1, 0)]  # List of user score and user name
    playerCounter = 1  # Player counter to determine who's turn it is
    numberRounds = 0
    while numberRounds < 1: formatPrint("Enter the desiered number of rounds "); numberRounds = int(
        input())  # Asks for the number of rounds
    for x in range(numberRounds * 2):  # Initiates loop
        if isEven(playerCounter):
            player = 1  # Determines who is the current user
        else:
            player = 0
        formatPrint("{}'s turn".format(currentUser(users[player])))
        roll1 = rollDice()  # Rolls the dies
        roll2 = rollDice()
        score = scoring(roll1, roll2, userScore(users[player]))  # Calculates score according to both rolls
        users[player] = (currentUser(users[player]), score)  # Assigns the score to the player in the list
        print("{user}'s score is now {score}".format(user=currentUser(users[player]), score=score))  # Displays score
        pause()
        playerCounter = playerCounter + 1

    if userScore(users[1]) > userScore(users[0]):  # Determines who is the winner
        winner = users[1]
        formatPrint("{user} won with {score} points".format(user=currentUser(winner),
                                                            score=userScore(winner)))  # Displays winner
    if userScore(users[0]) > userScore(users[1]):
        winner = users[1]
        formatPrint("{user} won with {score} points".format(user=currentUser(winner),
                                                            score=userScore(winner)))  # Displays winner
    if userScore(users[0]) == userScore(users[1]):
        winner = []
        formatPrint("It's a tie! Both players ended up with {score} points".format(score=userScore(users[0])))
    saveScore(userScore(users[1]), currentUser(users[1]))  # Saves user1 score
    saveScore(userScore(users[0]), currentUser(users[0]))  # Saves user1 score
    pause()


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

def login():
    try:
        f = open("auth.csv", "r+")  # Open the CSV storing the usernames and passwords in read-only mode
    except FileNotFoundError:
        print("Please sign up first!")
        pause()
        return("", "")
    found1 = False
    found2 = False

    while not found1:  # Checks if the user is successfully logged in
        user1 = str(input("Enter Player 1 username: "))
        pass1 = str(input("Enter Player 1 password: "))
        userpass1 = user1 + ", " + pass1 + "\n"
        for line in f.readlines():  # Moves the read-head down a line
            if(line == userpass1):  # Checks if current line is the same as the username and password
                print("\nWelcome, " + user1 + "\n")
                found1 = True  # Declares the user as logged in
                break  # Stops the program for searching further down the list
        if not found1 :
            print("\nPlease try again\n")
            f.seek(0)  # Sets the read-head to the start of the file

    while not found2:  # Repeates process for the second user
        f.seek(0)  # Sets the read-head to the start of the file
        user2 = input("Enter Player 2 username: ")
        pass2 = input("Enter Player 2 password: ")
        userpass2 = user2 + ", " + pass2 + "\n"
        for line in f.readlines():
            if(line == userpass2) and (userpass2 != userpass1):
                print("\nWelcome, " + user2 + "\n")
                found2 = True
                break
        if not found2 and (userpass2 == userpass1):  # Checks if the second user is the same as the first
            print("Player 2 cannot be the same as Player 1")
            f.seek(0)
        elif not found2 :
            print("\nPlease try again\n")
            f.seek(0)

    return(user1, user2)  # Sends the name of both users to the main program


def sign_up():
    f = open("auth.csv", "a+")  # Open the CSV storing the usernames and passwords in read mode to verify the username hasn't already been used
    Valid = False
    Valid2 = True

    while not Valid:
        user = str(input("Enter Desired Username: "))
        passw = str(input("Enter Desired Password: "))
        userpass = user + ", " + passw + "\n"
        for line in f.readlines():  # Moves the read-head down a line
            temp = line.split(",")  # Splits the username-password combination
            userline = temp[0]  # Removes the password
            if(userline == user):  # Compares the chosen username with the existing one
                print("Desired Username is already user")
                Valid = False
                Valid2 = False
                f.seek(0)
                break
            else:
                Valid2 = True
        if Valid2:
            f.close()
            f = open("auth.csv", "a")  # Switches to file append mode
            f.write(userpass)  # Appends chosem username-password combination
            Valid = True

menu_gui()


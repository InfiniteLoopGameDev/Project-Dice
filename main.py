from auth import *  # Importing all functions from the auth.py file
from funcs import *  # Importing all of my basic functions from the funcs.py file
from scoring import *  # Importing all of functions from the scoring.py file
import sys


def game(user0, user1):  # Asks the two users from the main program
    currentUser = lambda x: x[0]  # Lambda functions to get the User from the tuple
    userScore = lambda x: x[1]  # Lambda functions to get the Score from the tuple
    users = [(user0, 0), (user1, 0)]  # List of user score and user name
    playerCounter = 1  # Player counter to determine who's turn it is
    numberRounds = 0
    while numberRounds < 1: formatPrint("Enter the desiered number of rounds "); numberRounds = int(
        input())  # Asks for the number of rounds
    for x in range(numberRounds * 2):  # Intiates loop
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


def menu():  # menu function is here in case needed for another time
    inputValid = False
    formatPrint("""1.See Scoreboard\n2.Login\n3.Sign Up""")  # Printing the options
    while not inputValid:  # Verifies if the input has been validated
        input0 = input("Enter Option: ")
        try:
            if int(input0) != 1 and int(input0) != 2 and int(input0) != 3:
                print("Sorry, please try a valid number")
            else:  # Verifies if the input is one of the valid numbers
                inputValid = True  # Sets the input as valid
        except ValueError:
            if input0 == "":
                sys.exit()
            else:
                print("Sorry, please try a valid number")
    return int(input0)


while True:
    input0 = menu()
    if input0 == 1:
        scoreboard()
    elif input0 == 2:
        user1, user2 = login()
        if user1 == "" and user2 == "":
            pass
        else:
            game(user1, user2)
    elif input0 == 3:
        signUp()
        formatPrint("Sign Up Successful! \nPlease Proceed to Login or Sign Up another user")
        pause()

# Namkhey_Yoesel_Tshering_02240085_A1_PB.py


# Random Guessing Game
import random

def random_guessing_game():

    lowest_number = 1
    highest_number = 100

    number = random.randint(lowest_number, highest_number)
    guess = int(input("Guess a number between 1 and 100: "))

    while guess != number:
        if guess < number:
            print("Too low! Try again!")
        elif guess > number:
            print("Too high! Try again!")

        guess = int(input("Guess again: "))

    print(f"CORRECT! The answer was {number}")



# Rock paper scissors

import random

def rock_paper_scissors_game():
    player_1 = str(input("Rock, Paper or Scissors?")).lower()
    player_2 = random.randint(1, 3)

    if player_2 == 1:
        player_2 = "Rock"
    elif player_2 == 2:
        player_2 = "Paper"
    elif player_2 == 3:
        player_2 = "Scissors"

    print("computer: ", player_2)

    if player_1 == player_2:
        print("It's a tie!")
    elif (player_1 == "Rock" and player_2 == "Scissors") or (player_1 == "Paper" and player_2 == "Rock") or (player_1 == "Scissors" and player_2 == "Paper"):
        print("You win!")

    else:
        print("You lose")


def menu():

    while True: 
        print("\nSelect a Game (1-3): ")
        print("1. Random Guessing Game")
        print("2. Rock Paper Scissors Game")
        print("3. Exit Program")

        option = input("Enter your choice: ")

        if option == "1":
            random_guessing_game()
        elif option == "2":
            rock_paper_scissors_game()
        elif option == "3":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3")
    
if __name__ == "__main__":
    menu()
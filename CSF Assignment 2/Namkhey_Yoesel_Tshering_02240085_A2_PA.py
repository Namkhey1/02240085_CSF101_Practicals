# Namkhey_Yoesel_Tshering_02240085_A2_PA

import random 
from Namkhey_Yoesel_Tshering_02240085_A2_PB import rungame

class RandomGuessingGame:

    def __init__(self):

        self.lowest_number = 1

        self.highest_number = 100


    def user_guess(self):
       
        while True:

            try:
                guess = int(input(f"Guess a number between {self.lowest_number} and {self.highest_number}: "))

                if 1 <= guess <= 100:
                    return guess
                
                else:
                    print("Out of bound! Please guess a number between 1 and 100.")

            except: 
                print("Invalid input! Please enter a number")

            

    def play(self):
     
        while True:
          
            number = random.randint(self.lowest_number, self.highest_number)

            guess = self.user_guess()

            guesses = 1


            while guess != number:

                if guess < number:
                    print("Your guess was too low! Try again!")

                elif guess > number:
                    print("Your guess was too high! Try again!")

                
                guess = self.user_guess()
                guesses += 1

            print(f"CORRECT! The number was {number}")

            print(f"Your total guesses was {guesses}\n")

        

            play_again = input("Do you want to play again? (yes/no): ").lower()
            
            if play_again != "yes":
                print("Thanks for playing! Goodbye!")
                break



class RockPaperScissorsGame:

    def __init__(self):
        
        self.choices = ["rock", "paper", "scissors"]

    def user_choice(self):
        
        while True:

            player_choice = input("Rock, Paper, or Scissors? ").lower()

            if player_choice in self.choices:
                return player_choice
            
            print("Invalid choice. Please select Rock, Paper, or Scissors.")


    def computer_choice(self):

        computer_choice = random.choice(self.choices)
        return computer_choice


    def winner(self, player_choice, computer_choice):
        
        if player_choice == computer_choice:
            return "It's a tie!"
        
        elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        
        else:
            return "You lose!"

    def play(self):

        while True:
        
            player_choice = self.user_choice()

            computer_choice = self.computer_choice()
            
            print(f"\nYou chose: {player_choice}")

            print(f"Computer chose: {computer_choice}")

        
            result = self.winner(player_choice, computer_choice)
            print(result)

            play_again = input("\nDo you want to play again? (yes/no):").lower()
            if play_again != "yes":
                print("Thank you for playing! Goodbye!")
                break


class Question:
    def __init__(self, question, options, answer):

        self.question = question

        self.options = options

        self.answer = answer

    def ask(self):

        print(self.question)

        for option in self.options:
            print(option)

        answer = input("Your answer (A/B/C/D): ").upper()
        return answer == self.answer

class TriviaGame:
    def __init__(self):
        
        self.subjects = ["Math", "Science", "History", "Geography"]

        self.questions = {
            "Math": [
                Question("What is the derivative of x² with respect to x?",
                ["A) 2x", "B) x", "C) x²", "D) 1"], "A"),

                Question("What is the value of 2 to the power of 5?",
                ["A) 10", "B) 16", "C) 32", "D) 64"], "C"),

                Question("What is the sum of the interior angles of a hexagon?",
                ["A) 540°", "B) 720°", "C) 900°", "D) 1080°"], "B")
            ],
            "Science": [
                Question("What is the hardest natural substance on Earth?",
                ["A) Diamond", "B) Quartz", "C) Graphite", "D) Gold"], "A"),

                Question("What was the name of the first man-made satellite launched by the Soviet Union in 1957?",
                ["A) Vostok 1", "B) Sputnik 1", "C) Luna 2", "D) Soyuz 1"], "B"),

                Question("Which is the only metal that is a liquid at room temperature?",
                ["A) Lead", "B) Gold", "C) Silver", "D) Mercury"], "D")
            ],
            "History": [
                Question("Who is the first hereditary monarch of Bhutan?",
                ["A) Jigme Namgyal", "B) Ugyen Wangchuck", "C) Jigme Wangchuck", "D) Gongsar Ugyen Wangchuck"], "D"),

                Question("Who is the father of modern Bhutan?",
                ["A) Jigme Namgyal", "B) Ugyen Wangchuck", "C) Jigme Dorji Wangchuck", "D) Jigme Namgyal Wangchuck"], "C"),

                Question("Who was the grandfather of Gongsar Ugyen Wangchuk?",
                ["A) Sharp Panchung", "B) Tshewang Namgyal", "C) Pala", "D) Pila"], "C")
            ],
            "Geography": [
                Question("What is the chief mountain range to be found in Bhutan?",
                ["A) Himalayas", "B) Andes", "C) Alps", "D) Appalachians"], "A"),

                Question("What is the predominantly practised religion of Bhutan?",
                ["A) Hinduism", "B) Islam", "C) Buddhism", "D) Christianity"], "C"),

                Question("What is the highest peak in Bhutan?",
                ["A) Jomolharo", "B) Kula Kangri", "C) Tongshanjiabu", "D) Gangkhar Puensum"], "D")
            ]
        }

    def play(self):

        total_score = 0
        print("Welcome to the Trivia Game!")

        while True:
            print("\nCATEGORIES")
            
            subject = list(self.subjects)

            for i in range(len(subject)):
                print(f"{i + 1}. {subject[i]}")
            print("5. Exit")

            
            choice = input("Pick a number (1–5): ")

            if choice == "5":

                print(f"Your final score is {total_score}")

                print("Thank you for playing!")
                break

            if choice in ["1", "2", "3", "4"]:

                subject_input = subject[int(choice) - 1]

                print(f"\nYou chose {subject_input}")
                
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
                continue

            score = 0
                
            questions = self.questions[subject_input]

            for question in questions:

                if question.ask():
                    print("Correct!")
                    score += 1

                else:
                    print(f"Wrong! The correct answer was {question.answer}")
                        
            total_score += score
            print(f"You scored {score} out of {len(questions)} in {subject_input}")



def main_menu():
    while True:
        print("\nMAIN MENU")
        print("1. Random Guessing Game")
        print("2. Rock Paper Scissors")
        print("3. Trivia Game")
        print("4. Pokemon blinder")
        print("5. Exit")

        choice = input("Choose a game (1-4): ")

        if choice == "1":
            game = RandomGuessingGame()
            game.play()

        elif choice == "2":
            game = RockPaperScissorsGame()
            game.play()

        elif choice == "3":
            game = TriviaGame()
            game.play()

        elif choice == "4":
            rungame()

        elif choice == "5":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")


if __name__ == "__main__":
    main_menu()

#  Namkhey_Yoesel_Tshering_02240085_A2_PB
class PokemonBinder:

    def __init__(self):
      
        self.MAX_POKEDEX = 1025              

        self.CARDS_PER_PAGE = 64             
        
        self.GRID_SIZE = 8                    

        self.binder = {}

    # This block of codes calculate the page number and position on the page for a given Pokedex number
    # It is a simple algorithm where, the algorithm divides the pokedex number by 64 and adds 1 to figure out which page it should go in.
    # For example, if you want to put a pokedex #345 then divide it by 64 which gives 5.339. Since // sign is there we round it down, which give 5 and then add 1, which gives 6.
    # So the pokedex #345 should go in page 6.

    def get_card_position(self, pokedex_number):

        index = pokedex_number - 1               
        
        page = index // 64 + 1  
        
        position = index % 64 
          
        row = position // 8 + 1     
       
        column = position % 8 + 1      
    
        return page, row, column

   
    def add_card(self):

        while True:
            
            try:
                number = int(input("Enter Pokedex number (1-1025): "))

                if 1 <= number <= self.MAX_POKEDEX:

                    if number in self.binder:

                        page, row, column = self.binder[number]

                        print("Status: This card already exists.")

                        print(f"Page: {page}")
                        print(f"Position: {row},{column}")

                    else:

                        page, row, column = self.get_card_position(number)

                        self.binder[number] = (page, row, column)

                        print("Status: Your card has been added.")

                        print(f"Page: {page}")
                        print(f"Position: ({row},{column})")
                        
                        if len(self.binder) == 1025:
                            print("You have caught them all!")

                    break
                else:
                    print("Invalid Pokedex number! Please enter a number between 1 and 1025.")
            except ValueError:
                print("Invalid input! Please enter a number.")



    # The block of code below reset the binder session with confirmation and clears lears all stored data in memory.

    def reset_binder(self):


        reset = input("Type 'confirm' to reset or 'exit' to return: ") 

        if reset == "confirm":
            self.binder.clear()               
            print("Your binder has been reset.")

        elif reset == "exit":             
            print("Returning to the main menu.")

        else:
            print("Invalid input. No action taken.")



    def show_summary(self):

        print("\nView current placement")

        if not self.binder:                                      
            print("There is no cards in the binder.")   
            return

        for number in sorted(self.binder):                       
            page, row, column = self.binder[number] 
            print(f"Page number: {page}")               
            print(f"Position : ({row},{column})")

        total = len(self.binder)                                
        percentage = (total / self.MAX_POKEDEX) * 100
        print(f"Total cards: {total}")
        print(f"Completion: {percentage:.2f}%")
    

    def exit_program(self):
        print("\nThe session have ended.")
        print(f"You have collected {len(self.binder)} cards")
        print("Goodbye!")

    def run(self):
        while True:
            print("\nPokemon Binder Menu")
            print("1. Add a card")
            print("2. Reset binder")
            print("3. View current placement")
            print("4. Exit")

            choice = input("Select a mode (1-4): ")

            if choice == "1":
                self.add_card()
            elif choice == "2":
                self.reset_binder()
            elif choice == "3":
                self.show_summary()
            elif choice == "4":
                self.exit_program()
                break
            else:
                print("Invalid choice. Please select between 1-4.")


def rungame():
    pokegame = PokemonBinder()
    pokegame.run()

if __name__ == "__main__":
    rungame()



# Data structure
# Dictionary is primarily used in this Pokemon binder because it has fast access, duplicate is not allowed which helps in preventing adding of the same card twice and it is easy to store data because it is store in key-value pairs
# Also tuple is used in self.binder[num] = (page, row, column). It is used to store card location.

# Deletion process:
# Its a simple process,
# 1) Where first the self.bonder store all the cards using dictionary.
# 2) Then, the user input a pokedex number which maps a key to a location tuple(value).
# For example: The binder dictionary might look like this:
''' { 
    25 : (1, 4, 1),
    150: (3, 3, 6),
    7: (1, 1, 7)
} '''
# 3) Then in the reset section, its uses .clear() to clear all the data in the dictionart
# 4) After that the self.binder becomes an empty dictionary.
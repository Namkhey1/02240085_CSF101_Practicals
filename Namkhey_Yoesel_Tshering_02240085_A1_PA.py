# Namkhey_Yoesel_Tshering_02240085_A1_PA.py

#  1. Prime number
def prime_sum_calculator():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    sum = 0
    for i in range(start, end + 1):
        prime_number = True
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    prime_number = False
                    break
            if prime_number:
                sum += i
    print(f"Sum of prime number between {start} and {end}: {sum}")


#2. Length unit conversion

#1 meter = 3.28084 feet
#1 foot = 0.3048 meters

def length_converter():
    Length = float(input("Enter a length: "))
    unit = input("Meters or Feet? (M or F): ").upper()

    if unit == "M":
        Length = Length * 3.28084
        unit = "feet"

    elif unit == "F":
        Length = Length / 0.3048
        unit = "meters"

    else:
        print(f"{unit} was not valid")
        return
    print(f"Length is: {round(Length, 2)} {unit}")


# 3. Consonant Counter

def count_consonants(a):
    count = 0

    for character in a:
        if (character in "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWyYzZ"):
            count += 1
    return count

def consonant_counter():
    a = input("Enter a string: ")
    count = count_consonants(a)
    print("Count: ", count)

#4. Min-Max Number Finder

def min_max_finder():
    try:
        count = int(input("How many numbers do you want to enter? "))
        if count <= 0:
            print("Please enter a positive number.")
            return
        
        numbers = []
        for i in range(count):
            while True:
                try:
                    num = int(input(f"Enter number {i+1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer.")
        
        print(f"Smallest: {min(numbers)}, Largest: {max(numbers)}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


    min_max_finder()


# 5. Palindrome Checker

def palindrome_checker():
    a = input("Enter a value: ")

    new = ''.join(a.lower().split())
    reverse = new[::-1]

    if new == reverse:
        print("True! It is a palindrome")

    else:
        print("False! It is not a palindrome")


#6. Word counter

def word_counter():
    words_to_count = ["the", "was", "and"]

    with open("story.txt", "r") as file:    
        content = file.read().lower()

    import string
    translator = str.maketrans("","", string.punctuation)
    new_content = content.translate(translator)

    for word in words_to_count:
        count = new_content.split().count(word)
        print(f"{word}: {count}")


def menu():

    while True: 
        print("\nSelect a function (1-7): ")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find the min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("7. Exit Program")

        option = input("Enter your choice: ")

        if option == "1":
            prime_sum_calculator()
        elif option == "2":
            length_converter()
        elif option == "3":
            consonant_counter()
        elif option == "4":
            min_max_finder()
        elif option == "5":
            palindrome_checker()
        elif option == "6":
            word_counter()
        elif option == "7":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7")
    
if __name__ == "__main__":
    menu()
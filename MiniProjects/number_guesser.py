import random
import re


def top_range():
    top_of_range = input("Type a number (larger than 0): ")
    
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        
        while top_of_range <= 0:
            return top_range()
        else:
            while not top_of_range:
                return top_range()
    elif top_of_range is not int:
        while top_of_range is not int:
            return top_range()


    random_number = random.randint(0, top_of_range) 
    print(random_number)

    def make_guess():
        user_guess = input("Make a guess: ")
        guesses = 0

        while True:
            guesses+=1
            if int(random_number) > int(user_guess):
                user_guess = input("Higher! ")
            elif int(random_number) < int(user_guess):
                user_guess = input("Lower! ")
            elif user_guess.isdigit():
                user_guess = int(user_guess)
            elif user_guess > random_number:
                user_guess = input("Higher! ")
            elif user_guess < random_number:
                user_guess = input("Lower! ")

            if user_guess == random_number:
                print("You got it! You got it in", guesses,"guesses")
                answer = input("Play again? ")
                if answer.lower() == "yes":
                    return top_range()
                if answer.lower() == "no":
                    quit()
                elif not answer:
                    quit()
                else:
                    quit()
                
    make_guess()


top_range()
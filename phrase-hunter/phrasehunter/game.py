# Import libraries
import random
import sys


# Import Phrase class
from phrasehunter.phrase import Phrase


# Create your Game class logic in here.
class Game:
    def __init__(self, **kwargs):
        self.phrases = [
            Phrase("You had me at hello"),
            Phrase("You got a friend in me"),
            Phrase("May the force be with you"),
            Phrase("Just keep swimming"),
            Phrase("This is a tasty burger")
        ]
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def start(self):
        self.welcome()
        self.guesses = []
        self.missed = 0
        self.active_phrase = self.get_random_phrase()
        # self.phrase = Phrase(self.active_phrase)
        
        # print(f"{self.active_phrase}\n")
        
        self.active_phrase.display(self.guesses)
        print("\n")
        
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print("Missed Guesses:")
            print(f"{self.missed}\n")
            print("\n")
            user_guess = self.get_guess()
            if len(user_guess) > 1:
                print("Whoops! Only one letter at a time please...")
                user_guess
            elif not user_guess.isalpha():
                print("Whoops! Only alphabetical letters please...")
                user_guess
            else:
                user_guess = user_guess.lower()
                if not self.active_phrase.check_guess(user_guess):
                    self.missed += 1
            self.guesses.append(user_guess)
            self.active_phrase.display(self.guesses)
            print("\n")
        
        self.game_over()
    
    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print("="*20)
        print("PHRASE HUNTER")
        print("="*20)
        print("\nThere are 5 quotes from 5 different movies.")
        print("One of these quotes has been chosen at random.")
        print("Try to guess the quote letter by letter...\n")
    
    def get_guess(self):
        guess = input("Guess a letter... ")
        
        return guess
    
    def game_over(self):
        if self.missed == 5:
            print("Ouch... That's the max number of missed guesses...")
            print("Try again next time!")
            again = input("Would you like to play again? (Y/N) ")
            again = again.lower()
            if again == "y":
                self.start()
            elif again == "n":
                print("Thank you for playing!")
                print("Goodbye! :)\n")
                sys.exit()
            else:
                print("Please enter either Y or N...\n")
                self.game_over()
        else:
            print("Congratulations! You won!")
            again = input("Would you like to play again? (Y/N) ")
            again = again.lower()
            if again == "y":
                self.start()
            elif again == "n":
                print("Thank you for playing!")
                print("Goodbye! :)\n")
                sys.exit()
            else:
                print("Please enter either Y or N...\n")
                self.game_over()
                

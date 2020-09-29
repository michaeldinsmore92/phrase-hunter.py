# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase, **kwargs):
        self.phrase = phrase.lower()
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            elif letter == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
                
    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False
            
    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter == " ":
                continue
            if letter not in guesses:
                return False
            
        return True

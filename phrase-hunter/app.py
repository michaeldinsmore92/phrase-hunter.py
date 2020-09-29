# Import Game class
from phrasehunter.game import Game

# Import Game class
from phrasehunter.game import Game


# Proper use of dunder __main__ ? :)
if __name__ == '__main__':
    # Create an instance of your Game class
    game = Game()
    
    player = input("Hello! \nWhat's your name? ")
    player = player.title()
    print(f"\nHello, {player}!")
    # Start your game by calling the instance method that starts the game loop
    game.start()

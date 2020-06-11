#   Imports random module and all if methods.
from random import * 

#   Sets up the user and cpu score variables. 
player_score = 0
cpu_score = 0

#   The dictionary scores house the player and cpu scores.
scores = {"player_score" : 0, "cpu_score" : 0}

#   The dictionary message contains majority of the messages that will repeatedly be used over the
#   duration of the application runtime. The format specifier(%s) is used to later import variables 
#   into the string and in doing so these variables gets converted to a sting.
messages = {
    "cpu" : "\n[*] You weren't lucky this time around. One score for the computer!", 
    "player" : "\n[^] You stand firmly smiling at the computers loss. One score for the player!", 
    "neither" : "'\n[-] This must be a mistake' you utter. Both you and the computer are at a tie.",
    "result" : "\nYou rolled an %s the cpu rolled a %s",
    "ask_player" : "\nWould you like to play a game of throw the die? ",
    "play_again" : "\nWould you like to play another game of throw the die? ",
    "error" : "\n\n[!!]Sorry your input was not understood please review and follow the rules provided.\n\n"
}

class PyDice():
    #   This function is the initialize method and its purpose is to display the welcoming
    #   message when its parent class, PyDice() is called.
    def __init__(self):
        print(f'''
                          Welcome to PyDice!
     ==============================================================
       Comepete against your own computer to see who the luckiest

        Rules:
                1. To play either enter 'y' or 'n' when input is 
                    required.
                2. To stop playing simply enter 'n' the next time
                   your input is required.
                3. Your goal is to beat the cpu, you can view
                   your scores after you end the game.
                    ''') 

    #   The request() methods' purpose is to prompt the user for input to verify
    #   whether or not the user wishes to play or not. This method takes the user
    #   input and coverts it to a lowercase string it then takes the first character
    #   of the string and returns the value.
    def request(self):
        if scores["player_score"] == 0:
            ask_user = str(input(messages["ask_player"])).lower()[0]
            return ask_user
        else:
            ask_user = str(input(messages["play_again"])).lower()[0]
            return ask_user

    #   The start() method is used to start the game and keep track of the score of
    #   both the player and cpu. I made use of the random module to generate random
    #   variables between 1 and 6 to simulate the possible result we would expect from
    #   rolling a die. The function also relies on the messages and score dictionaries
    #   to make the user aware of the situation. messages["results"] lets the player
    #   know what he/she rolled and the cpu.
    def start(self):
        player_roll = randint(1, 6)
        cpu_roll = randint(1, 6)

        #   If the players value is less than the cpu, the cpu get a point extra. 
        #   The format specifier is being used in line 69 and 74 (% (player_roll, cpu_roll))
        #   the purpose of this is to call the selected variables into the string.
        if player_roll < cpu_roll:
            print(f'{messages["result"] % (player_roll, cpu_roll)}  {messages["cpu"]}')
            scores["cpu_score"] += 1

        #   If the cpu's value is less than the player, the player get a point extra.
        elif player_roll > cpu_roll:
            print(f'{messages["result"] % (player_roll, cpu_roll)}  {messages["player"]}')
            scores["player_score"] += 1

        #   If both of them are equal nobody gets a point.
        else:
            print(messages["neither"])

    #   The stop() method is called to display the score of both the user and the cpu. 
    def stop(self):
        print(f'''
                    Score Board
                    ===========
                    Player : {scores["player_score"]}
                    CPU    : {scores["cpu_score"]}

                    Take care and have a great Day!
                ''')

#   The main() method is used to call the class PyGame().
def main():
    game = PyDice()

    #   The while loop is used to keep the game from stopping to prevent the
    #   scores from being reset. The loop will keep running as long as active
    #   is not equal to True.
    while True:
        #   The var answer is calling the request() method within the PyDice() class.
        answer = game.request()
        
        if answer == "y":
            #   The var start is calling the start() method within the PyDice() class.
            start = game.start()
        elif answer == 'n':
            #   Over here I called the stop() method within the PyDice() class. The break
            #   statement is to stop the while loop so that our game ends.
            game.stop()
            break

        #   This brings up an error message when the user enters something other than 'y' or 'n'.
        else:
            print(messages["error"])

#   This will verify if this python file is being ran locally and not being imported.
#   if it's locally name will equal to main and the main() method will run.
if __name__ == "__main__":
    main()

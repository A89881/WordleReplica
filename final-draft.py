# Importing The Necessary Dependencies And Libraries For The Project
# Import For Randomization
import random
# Import For Colour Manipulation, i.e., to color the words
from termcolor import colored
# Import For Tracking Player Time
import time
# Import For Terminal Manipulation, i.e., to clear the terminal for an "aesthetic" look
import os

# Initializing Variables/Data Structures
# Dictionary That Is The Scoreboard
scoreboard_dict = {}
# List That Tracks The Current Name, i.e., inputted username by the player
name_list = []

# Links To The Files:
# - scoreboard-file = file that stores the Scoreboard
# - secret-word-file = file that has the collections of words to guess
# - guess-file = file of words to guess from
scoreboard_file = "scoreboard.txt"
secret_word_file = "word-file.txt"
guess_file = "guess-file.txt"

#Main Class In Which Everything Occurs
class Wordle:
    #Initializing Attributes Of The Class:
    # - secret_word: initially set to None, will hold the chosen word for the game
    # - max_attempts: the maximum number of attempts allowed in the game (default: 6)
    # - board_list: an empty list to store the guessed words and their status
    def __init__(self):
        self.secret_word = None
        self.max_attempts = 6
        self.board_list = []

   # Code that selects a random word from the file as the secret word the player is after
    def get_word(self):
        # Opens the text file in reading mode
        with open(secret_word_file, 'r') as file:
            contents = file.read()
            # Remove double quotes and split the contents into words
            words = [word.strip().strip('"') for word in contents.split(',')]
            # Randomly selects a word from the file and sets it to uppercase for style purposes
            self.secret_word = random.choice(words).upper()

    # Code that checks if a word exists in the file and returns True if it does
    def check_word(self, word):
        # Sets the file accesing to "reading" mode
        with open(guess_file, "r") as file:
            # Iterates through ever line in the file
            for line in file:
                # If the word is in the file it returns true
                if word in line:
                    return True
        # Otherwise flags false
        return False

    # Code that checks if a name exists in the file and returns True if it does
    def check_name(self, name):
        # Sets the file accesing to "reading" mode
        with open(scoreboard_file, 'r') as file:
            # Iterates through every line in the files
            for line in file:
                # String Manipulation
                line = line.strip()
                # Checks if a line in the file starts, with the inputed name + ","
                if line.startswith(name + ','):
                    # If it is true that it does, start with the inputed name + "," that means it exist so it flags True
                    return True
        # Otherwise Flags False that it doesn't Exist
        return False
    
    # Code to access the data in the scoreboard_file and then adds it to the scoreboard dictionary
    def get_scoreboard_dict(self):
        # Read the scoreboard file and populate the scoreboard_dict dictionary with the existing files data
        with open(scoreboard_file, "r") as file:
          # Iterates through every line in the file
          for line in file:
              # String Manipulation
              parts = line.strip().split(",")
              # Identifies the Username
              name = parts[0]
              # And their respective record/score
              attempts = int(parts[1])
              time = float(parts[2])
              # Sets the key (name) as the key and values (record) into the scoreboard dictionary
              scoreboard_dict[name] = [attempts, time]

    # Code that creates the board, i.e., prints out the board
    def board(self):
          # Iterates through the list, and subseqeuntly prints out each element
          for i in range(len(self.board_list)):
              # Print Statement to Visualise the Board
              print(f"| {self.board_list[i]} |")
            
    #Code that removes spaces from a string, and returns edited string
    def remove_spaces(self, string):
        return "".join(string.split())
    
     # Code that checks if a input has spaces
    def has_space(self, string):
        # If statement to check if the string has a space
        if ' ' in string:
            return True
        else:
            return False
    
    # Information about how enter values into the username, for the User (UI - Component) 
    def username_info(self):
        print("If you want to save your score, Enter a Username below. Enter 'C' to continue without saving.")
        print("However, if you have played before, you can re-enter your username to automatically update, but will only update if the new score is better.")
    
    # Information about how the Scoreboard is Sorted, for the User (UI - Component) 
    def scoreboard_info(self):
        print(" ")
        print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
        print("Name: Attempt(s): Time") 
        print(" ")

    # Information about how to play the game, for the User (UI - Component) 
    def start_info(self):
        print(" ")
        print("When you play, the game you get feedback based on the accurcy of your guess, in which 'Green' = Right place and letter, 'Yellow' = Right letter, 'Grey' = Just Wrong ")
        print(f"The Premise of the Game is to Guess the Hidden Word. You have {self.max_attempts} to Guess and the words are 5 letters long ")
    
  
   # Code that asks the user if they wish to save their score into the scoreboard
    def user(self):
        # While loop, so that it can "infinitely" loop again, and again in situations of inproper inputs or mistakes
        while True:
          # Access data from the scoreboard file and updates the dictionary
          self.get_scoreboard_dict()
          print(" ")
          # Shows the Scoreboard for the user, intent was so the user knows what names exist
          self.Scoreboard(record=None)
          print(" ")  
          # Gives info about the username
          self.username_info()
          # Prompt the user to enter a username
          username = str(input("Enter Username? (No Spaces): "))
          # Checks if the user's input is not nothing or has a space 
          # (Reason is due, printing issues if it has spaces, that when one prints after, it does not show print)
          if 0 < len(username) == True and self.has_space(string=username) != True:
              # If the user doesn't want to save their score
              if self.remove_spaces(username.lower()) == "c":
                  os.system("cls")
                  # If the user enters 'C', call the start() function to Continue Further to the "Start"/Main Menu without saving the score
                  start()
                  break
              # If the username exist
              elif self.check_name(name=username):
                  # Access the record of that specific username
                  value = scoreboard_dict[username]
                  # Checks first amount of attempts are fewer than before 
                  if value[0] > self.player_record[0]:
                        os.system("cls")
                        print("Your score has been updated")
                        # Append the username to the name_list
                        name_list.append(username)
                        os.system("cls")
                        # Update the scoreboard using the player_record
                        self.Scoreboard(record=self.player_record)
                        # Call the start() function to Continue Further to the "Start"/Main Menu
                        start()
                        break
                  # However if the amount of attempts are the same then ... 
                  elif value[0] == self.player_record[0]:
                          # Checks if the new time is less than before
                          if value[1] > self.player_record[1]:
                                os.system("cls")
                                print("Your score has been updated")
                                # Append the username to the name_list
                                name_list.append(username)
                                # Update the scoreboard using the player_record
                                self.Scoreboard(record=self.player_record)
                                # Call the start() function to Continue Further to the "Start"/Main Menu
                                start()
                                break
                          else:
                            # If not then, we tell the user ... 
                            os.system("cls")
                            print(f"Sorry, not better this time. Last score: {value}, this score: {self.player_record}")
                  else:
                    # If not then, we tell the user ... 
                    os.system("cls")
                    print(f"Sorry, not better this time. Last score: {value}, this score: {self.player_record}")
                       
              # Then an else statement, that accepts the username the user entered
              else:
                  os.system("cls")
                  name_list.append(username)
                  # Update the scoreboard using the player_record
                  self.Scoreboard(record=self.player_record)
                  # Call the start() function to Continue Further to the "Start"/Main Menu
                  start()
                  break
          # If Invalid then just passes to loop back to the prompt        
          else:
              os.system("cls")
              print("Not Permitted Input")
              pass
          
    #Code for the Scoreboard: storing the data into a file and priniting it out   
    def Scoreboard(self, record):
        # Make the Global Variables accessable in this Method in the Class
        global scoreboard_dict
        global name_list

        # Access the data from the scoreboard_file
        self.get_scoreboard_dict()

        #Checks if the record is not a none value and an actual value
        if record != None:
            name = name_list[-1]   
            scoreboard_dict[name] = record
            self.scoreboard_info()
            # Write the updated scoreboard to the scoreboard file
            with open(scoreboard_file, "w") as file:
                for key, value in scoreboard_dict.items():
                    file.write(f"{key},{value[0]},{value[1]}\n")  
            # Sort the scoreboard dictionary by attempts and then time
            sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))
            # Print the sorted scoreboard
            for i, (key, value) in enumerate(sorted_scores):
                print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")    
        else:
            # Print the introduction for the scoreboard
            self.scoreboard_info()
            # Sort the scoreboard dictionary by attempts and then time
            sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))
            # Print the sorted scoreboard
            for i, (key, value) in enumerate(sorted_scores):
                # Print each player's name, number of attempts, and time taken
                print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")
    
    def play_game(self):
        # Print a blank line for visual separation
        print(" ")
        # Set the main loop flag to True
        main_loop = True
        # Set the counter for amount attempts to 1
        self.counter = 1
        # Get the start time of the game
        start_time = time.time()
        # Initialize the player's record list
        self.player_record = []
        # Main game loop
        while main_loop:
            # Check if the counter is within the max attempts limit
            if self.counter < self.max_attempts + 1:
                # Print the current attempt number out of total attempts
                print(f"This is Attempt Number {self.counter} out of {self.max_attempts}")
                # Display the game board
                self.board()
                # Get the inputted word from the user
                inputed_word = str(input("Enter Guess?: ")).upper()
                # Clear the terminal screen
                os.system("cls")
                # Remove spaces from the inputted word
                inputed_word = self.remove_spaces(string=inputed_word)
                check = [str(i) for i in inputed_word]
                # Check if the inputed word has the correct length
                if len(inputed_word) == 5:
                    # Check if the inputed word is a valid word
                    if self.check_word(word=f'"{inputed_word.lower()}"'):
                        # Check if the inputed word matches the secret word
                        if inputed_word == self.secret_word:
                            # Mark the correctly guessed letters in green
                            for i in range(len(inputed_word)):
                                if check[i] == self.secret_word[i]:
                                  check[i] = colored(check[i], "green")
                                    
                            inputed_word = "".join(map(str, check))
                            # Calculate the end time and total time taken
                            end_time = time.time()
                            total_time = round(end_time - start_time, 3)
                            # Print the winning message and game statistics
                            print("You Won!")
                            self.board_list.append(inputed_word)
                            self.board()
                            print(f"The Word was {inputed_word}")
                            print(f"It took you {self.counter} attempt(s)")
                            print(f"It took you in total {total_time} seconds")

                            # Update the player's record with the attempt count and total time
                            self.player_record.append(self.counter)
                            self.player_record.append(total_time)

                            # Prompt the user to enter their username or continue without saving the score
                            self.user()
                            break
                        else:
                            correct = 0
                            letterCount = {}

                            # Count the occurrence of each letter in the secret word
                            for letter in self.secret_word:
                                if letter in letterCount:
                                    letterCount[letter] += 1
                                else:
                                    letterCount[letter] = 1

                            # First iteration, check all the correct letters in the correct positions
                            for value, letter in enumerate(inputed_word):
                                # Is the letter in the correct position?
                                if value < len(self.secret_word) and letter == self.secret_word[value]:
                                    # Check if the letter is still available in the word
                                    if letterCount[letter] > 0:
                                        letterCount[letter] -= 1
                                        # Mark the letter in green
                                        check[value] = colored(check[value], "green")
                                    correct += 1
                                    if correct == len(self.secret_word):
                                        break

                        # Second iteration, mark letters that are present but in the wrong positions
                        for value, letter in enumerate(inputed_word):
                            # Skip the letter if it has been marked correct
                            if check[value] != colored(check[value], "green"):
                                # Check if the letter is in the word and still available
                                if letter in self.secret_word and letterCount[letter] > 0:
                                    letterCount[letter] -= 1
                                    # Mark the letter in yellow
                                    check[value] = colored(check[value], "yellow")
                                else:
                                    # Mark the letter in grey as it's not in the word or already used
                                    check[value] = colored(check[value], "grey")
                               
                        inputed_word = "".join(map(str, check))
                        # Add the inputed word to the board list and increment the counter
                        self.board_list.append(inputed_word)
                        # Increase the Counter by one
                        self.counter += 1
                    else:
                        print(f"{inputed_word} is invalid; Word Doesn't exist in the Dictionary")
                else:
                    print("Word entered is not 5 letters long")
            else:
                self.board_list.append(inputed_word)
                self.board()
                print("You have no more Attempts; You have lost the game")
                print(f"The Word was {self.secret_word}")
                start()
                break

# The Main Function in Which the Game Will Be Initiated                                               
def main():
    # Create a Wordle Instance
    wordle = Wordle()
    # Get A Random Word
    wordle.get_word()
    # Play the Game
    wordle.play_game()

# The Start Function, in Which the Start Menu or Continue-Play Menu is Shown
def start():
    # Create a Wordle Instance
    wordle = Wordle()
    # A While Loop running, in which the play can in essence indefinitely choose what they want to do
    while True:
        # Wordle Game Info
        wordle.start_info()
        # Ask for player input, if they wish to play, see the scoreboard or exit the application
        play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()
        # Striping away spaces from their input, in case of user error
        play = wordle.remove_spaces(string=play)
      
        if play == "p":
            # Start the game
            main()
            # Exits this Loop
            break
        elif play == "s":
            os.system("cls")
            # Show the scoreboard
            # Record is set to None since the player hasn't played so there is no record value to exist in essence
            wordle.Scoreboard(record=None)
        elif play == "e":
            break
        else:
            # Clear the terminal
            os.system("cls")
            # Invalid Input since the input, wasn't a permitted input, i.e., not "p" or "s" or "e"
            print("Invalid Input")


# The Game Begins Here ....

# Clear the console screen
os.system("cls")
# Print a welcome message
print("Hello and welcome to Wordle!")
# Start the game
start()
# Importing The Necessary Dependencies And Libraries For The Project
# Import For Dictionary Manipulation
from collections import defaultdict
# Import For Randomization
import random
# Import For Colour Manipulation, i.e., to color the words
from termcolor import colored
# Import For Tracking Player Time
import time
# Import For Terminal Manipulation, i.e., to clear the terminal for an "aesthetic" look
import os
# Import to Strip Color
import re
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
    # - word_length: the length of the words to be guessed in the game (default: 5)
    # - board_list: an empty list to store the guessed words and their status
    def __init__(self):
        self.secret_word = None
        self.max_attempts = 6
        self.word_length = 5
        self.board_list = []

   # Code that selects a "pseudo" random word from the file as the secret word the player is after
    def get_word(self):
        # Opens the text file in reading mode
        with open(secret_word_file, 'r') as file:
            contents = file.read()
            # Remove double quotes and split the contents into words
            words = [word.strip().strip('"') for word in contents.split(',')]
            # Randomly selects a word from the file and sets it to uppercase for style purposes
            self.secret_word = random.choice(words).upper()
            # Slices the word into individual letters and converts them into a list (for better personal comprehension)
            # self.secret_word = "APPLE"
            self.secret_word = [str(i) for i in self.secret_word]

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

    # Code that checks if a name exists in the file and returns False if it does
    def check_name_in_file(self, name):
        # Sets the file accesing to "reading" mode
        with open(scoreboard_file, 'r') as file:
            # Iterates through every line in the files
            for line in file:
                # String Manipulation
                line = line.strip()
                # Checks if a line in the file starts, with the inputed name + ","
                if line.startswith(name + ','):
                    # If it is true that it does, start with the inputed name + "," that means it exist so it flags false
                    return False
        # Otherwise Flags True that it doesn't Exist
        return True

    # Code that creates the board, i.e., prints out the board
    def board(self):
        # Iterates through the list, and subseqeuntly prints out each element
        for i in range(0, len(self.board_list)):
            # To Format the Element, which is currently a list in the board_list to a string --> [] (list) to "" (str) 
            self.board_list[i] = "".join(map(str, self.board_list[i]))
            # Print Statement to Visualise the Board
            print(f"| {self.board_list[i]} |")

    # Code that sorts out duplicates from the name_list
    def sort_name_list(self, input):
        # An Empty list
        list1 = []
        # Only Adds elements from the inputed list (input) into the empty list if element does not exist in the empty list 
        [list1.append(x) for x in input if x not in list1]
        # Then returns the "empty" list so inputed list automatically has the same content of the "empty" list
        return list1


    # Code that checks if a input has spaces
    def has_space(self, string):
        # If statement to check if the string has a space
        if ' ' in string:
            return False
        else:
            return True
        
    #Code that removes spaces from a string, and returns edited string
    def remove_spaces(self, string):
        return "".join(string.split())

    # Code that asks the user if they wish to save their score into the scoreboard
    def user(self):
        # Print instructions for entering a username or continuing without saving
        print(" ")
        print("If you want to save your score, or Enter a Username below. Enter 'C' to continue without saving.")
        print("If you have played before, you can reenter your username to automatically update it if the new score is better.")
        
        # Prompt the user to enter a username
        username = str(input("Enter Username? (No Spaces): "))
        
        # Convert the entered username to lowercase characters and store in the 'check' list
        check = [str(x).lower() for x in username]
        
        # List containing the letter 'c'
        c = ["c"]

        # While loop, so that it can "infinitely" loop again, and again in situations of inproper inputs or mistakes
        while True:
            # Checks if the user's input is proper and legitimate, i.e., no spaces or empty input
            if 0 < len(check) and self.has_space(string=check):
                if check == c:
                    # If the user enters 'C', call the start() function to Continue Further to the "Start"/Main Menu without saving the score
                    start()
                    break
                else:
                    # Append the username to the name_list
                    name_list.append(username)
                    # Update the scoreboard using the player_record
                    self.Scoreboard(record=self.player_record)
                    # Call the start() function to Continue Further to the "Start"/Main Menu
                    start()
                    break
            else:
                # Clear the terminal screen
                os.system("cls")
                # Print error message for an invalid username
                print(" ")
                print("Invalid Username")
                print("If you want to save your score, or Enter a Username below. Enter 'C' to continue without saving.")
                print("If you have played before, you can reenter your username to automatically update it if the new score is better.")
                username = str(input("Enter Username? (No Spaces): "))
                check = [str(x).lower() for x in username]

   #Code for the Scoreboard; accessing the file, storing the data into a file, priniting it out   
    def Scoreboard(self, record):
        # Make the Global Variables accessable in this Method in the Class
        global scoreboard_dict
        global name_list
        
        # Read the scoreboard file and populate the scoreboard_dict dictionary with the existing file
        if os.path.exists(scoreboard_file):
            with open(scoreboard_file, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    name = parts[0]
                    attempts = int(parts[1])
                    time = float(parts[2])
                    scoreboard_dict[name] = [attempts, time]

        # Sort the name_list, by removing duplicates
        name_list = self.sort_name_list(input=name_list)

        # If Statement utilized in the beginning of the game, to check if the record given is not an None Value and if the Length of the List is Not O
        if (record != None and len(name_list) != 0):
          # Get the last name from the name_list
          name = name_list[-1]

          # Check if the name already exists in the scoreboard dictionary
          if name in scoreboard_dict:
              while True:
                  # Prompt the user for an action: continue without saving the score, confirm the update, or enter a new name
                  choice = input("Name already exists. Enter 'C' to continue without saving the score, 'Y' to confirm the update, or enter a new name: ")
                  if choice.lower() == 'c':
                      # If the user chooses to continue without saving, set the record to None
                      record = None
                      break
                  if choice.lower() == "y":
                      # If the user chooses to confirm the update
                      value = scoreboard_dict[choice]
                      if value > record:
                          # If the new score is better than the existing score, update the scoreboard dictionary
                          print("Your score has been updated")
                          scoreboard_dict[name] = record
                          break
                      else:
                          # If the new score is not better, inform the user
                          print(f"Sorry, not better this time. Last score: {value}, this score: {record}")
                  elif self.check_name_in_file(name=choice) and self.has_space(string=choice):
                      # If the user enters a new name that is valid, update the name and append it to the name_list
                      name = choice
                      name_list.append(name)
                      break
                  else:
                      # Invalid name entered, prompt for a different name
                      print("Invalid name. Please enter a different name.")
          else:
              # If the name doesn't exist in the scoreboard dictionary, append it to the list
              name_list.append(name)

          # If statement to check if the name and corresponding record have been updated
          if record != None and len(name_list) != 0:
              # If there is a valid record and a non-empty name_list, update the scoreboard dictionary with the new record
              scoreboard_dict[name] = record
              os.system("cls")
              print("The scoreboard ranks the players based on the number of attempts required to win and the time taken to win")
              print("Name: Attempts: Time")
              print(" ")

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
            # Clear the terminal
            os.system("cls")
            # Print the introduction for the scoreboard
            print("The Scoreboard ranks the players based on the number of attempts required to win and the amount of time it took to win")
            print("Name: Attempt(s): Time") 
            print(" ")

             # Write the current scoreboard to the scoreboard file
            with open(scoreboard_file, "w") as file:
                for key, value in scoreboard_dict.items():
                    file.write(f"{key},{value[0]},{value[1]}\n")

            # Sort the scoreboard dictionary by attempts and then time
            sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))
            
            # Print the sorted scoreboard
            for i, (key, value) in enumerate(sorted_scores):
                print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")
            
        else:
            # Clear the terminal
            os.system("cls")
            # Print the introduction for the scoreboard
            print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
            print("Name: Attempt(s): Time") 
            print(" ")

            with open(scoreboard_file, "w") as file:
                for key, value in scoreboard_dict.items():
                    file.write(f"{key},{value[0]},{value[1]}\n")

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
        counter = 1
        # Get the start time of the game
        start_time = time.time()
        # Initialize the player's record list
        self.player_record = []

        # Main game loop
        while main_loop:
            # Check if the counter is within the max attempts limit
            if counter < self.max_attempts + 1:
                # Print the secret word (for testing purposes)
                print(self.secret_word)
                # Print the current attempt number out of total attempts
                print(f"This is Attempt Number {counter} out of {self.max_attempts}")
                # Display the game board
                self.board()
                # Get the inputted word from the user
                inputed_word = str(input("Enter Guess?: ")).upper()
                # Clear the terminal screen
                os.system("cls")

                # Remove spaces from the inputted word
                inputed_word = self.remove_spaces(string=inputed_word)
                # Convert the inputed word into a list of individual characters
                inputed_word = [str(i) for i in inputed_word]
                # Get the length of the inputed word
                inputed_word_length = len(inputed_word)

                # Check if the inputed word has the correct length
                if inputed_word_length == self.word_length:
                    # Check if the inputed word is a valid word
                    if self.check_word(word=f'"{"".join(map(str, inputed_word)).lower()}"'):
                        # Check if the inputed word matches the secret word
                        if inputed_word == self.secret_word:
                            # Mark the correctly guessed letters in green
                            for i in range(0, inputed_word_length):
                                if inputed_word[i] == self.secret_word[i]:
                                    inputed_word[i] = colored(inputed_word[i], "green")   

                            # Calculate the end time and total time taken
                            end_time = time.time()
                            total_time = round(end_time - start_time, 3)
                            # Print the winning message and game statistics
                            print("You Won!")
                            inputed_word = "".join(map(str, inputed_word))
                            self.board_list.append(inputed_word)
                            self.board()
                            print(f"The Word was {inputed_word}")
                            print(f"It took you {counter} attempt(s)")
                            print(f"It took you in total {total_time} seconds")
                            
                            # Update the player's record with the attempt count and total time
                            self.player_record.append(counter)
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
                                        inputed_word[value] = colored(inputed_word[value], "green")
                                    correct += 1
                                    if correct == len(self.secret_word):
                                        break

                        # Second iteration, mark letters that are present but in the wrong positions
                        for value, letter in enumerate(inputed_word):
                            # Skip the letter if it has been marked correct
                            if inputed_word[value] != colored(inputed_word[value], "green"):
                                # Check if the letter is in the word and still available
                                if letter in self.secret_word and letterCount[letter] > 0:
                                    letterCount[letter] -= 1
                                    # Mark the letter in yellow
                                    inputed_word[value] = colored(inputed_word[value], "yellow")
                                else:
                                    # Mark the letter in grey as it's not in the word or already used
                                    inputed_word[value] = colored(inputed_word[value], "grey")

                        # Add the inputed word to the board list and increment the counter
                        self.board_list.append(inputed_word)
                        # Increase the Counter by one
                        counter += 1
                    else:
                        word = "".join(map(str, inputed_word))
                        print(f"{word} is invalid; Word Doesn't exist in the Dictionary")
                else:
                    print(f"Word entered is not {self.word_length} letters long")
            else:
                self.secret_word = "".join(map(str, self.secret_word))
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
    # Start Menu Info
    print(" ")
    print("When you play, the game you get feedback based on the accurcy of your guess, in which 'Green' = Right place and letter, 'Yellow' = Right letter, 'Grey' = Just Wrong ")
    print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long ")
    # Ask for player input, if they wish to play, see the scoreboard or exit the application
    play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()
    # Striping away spaces from their input, in case of user error
    play = wordle.remove_spaces(string=play)

    # A While Loop running, in which the play can in essence indefinitely choose what they want to do
    while True:
        if play == "p":
            # Start the game
            main()
            # Exits this Loop
            break
        elif play == "s":
            # Show the scoreboard
            # Record is set to None since the player hasn't played so there is no record value to exist in essence
            wordle.Scoreboard(record=None)
            # Aesthetic purpose, terminal seperation
            print(" ")
            # Start Menu Info
            print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long")
            print("When you play, the game you get feedback based on the accurcy of your guess, in which 'Green' = Right place and letter, 'Yellow' = Right letter, 'Grey' = Just Wrong ")
            # Ask for play input, if they wish to play, see the scoreboard or exit the application
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()
            # Striping away spaces from their input, in case of user error
            play = wordle.remove_spaces(string=play)
        elif play == "e":
            break
        else:
            # Clear the terminal
            os.system("cls")
            # Invalid Input since the input, wasn't a permitted input, i.e., not "p" or "s"
            print("Invalid Input")
            # Start Menu Info
            print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long")
            print("When you play, the game you get feedback based on the accurcy of your guess, in which 'Green' = Right place and letter, 'Yellow' = Right letter, 'Grey' = Just Wrong ")
            # Ask for player input, if they wish to play, see the scoreboard or exit the application
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()
            # Striping away spaces from their input, in case of user error
            play = wordle.remove_spaces(string=play)

#  Ensures that the code within it is only executed when the module is run directly and not imported as a module by another program.
if __name__ == "__main__":
    # Clear the console screen
    os.system("cls")
    # Print a welcome message
    print("Hello and welcome to Wordle!")
    # Start the game
    start()


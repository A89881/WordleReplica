#Importing The Neccesary Dependencies And Libraries For The Project

#Import For Dictionary Manipulation
from collections import defaultdict
#Import For Randomisation
import random
#Import For Colour Manipulation i.e to colour the words
from termcolor import colored
#Import For Tracking Player Time
import time
#Import For Terminal Manipulation i.e to clear the terminal for "aesthetic" look
import os
#Import to Strip Color
import re

#Initializing Variables/Data Structures

#Dictionary That Is The Scoreboard 
scoreboard_dict = {}
#List That Tracks The Current Name i.e inputed username by the player
name_list = []

#Links To The Files, 

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

    #Code that selects "psudeo" randomly a word from the file, as the secret-word the player is after
    def get_word(self):
        #Opens the text file, in reading mode
        with open(secret_word_file, 'r') as file:
            contents = file.read()
            # Remove double quotes and split the contents into words
            words = [word.strip().strip('"') for word in contents.split(',')]
            #Randomly selects a word from the files, and sets the word to uppercase for style purposes
            self.secret_word = random.choice(words).upper()
            #String slices the word, by using list comprehensions, i.e, makes every letter into an element in a list (done for my own comprehension)
            self.secret_word = [str(i) for i in self.secret_word]
    
    #Code that checks if a word exist in the file and returns true if it does
    def check_word(self, word):
        with open(guess_file, "r") as file:
            for line in file:
                if word in line:
                    return True
        return False
    
    #Code that checks if a name exist in the file and returns false if it does
    def check_name_in_file(self, name):
        with open(scoreboard_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith(name + ','):
                    return False
        return True

    #Code that creates the board i.e. prints out the board
    def board(self):
        for i in range(0, len(self.board_list)):
            self.board_list[i] = "".join(map(str, self.board_list[i]))
            print(f"| {self.board_list[i]} |")
    
    
    def sort_name_list(self, input):
        list1 = []
        [list1.append(x) for x in input if x not in list1]
        return list1


    #Code that checks if a input has spaces
    def has_space(self, string):
        if ' ' in string:
            return False
        else:
            return True
        

    #Code that removes spaces from a string
    def remove_spaces(self, string):
        return "".join(string.split())

    
    # Code that asks the user if they wish to save their score into the scoreboard
    def user(self):
        print(" ")
        print("If you want to save your score Enter Username Below, or Enter 'C' to continue (Be Warned Score Will not be Saved)")
        print("However if you have played before, you can reenter Your Username, then it will automatically update, however will only update if the new one is better then the previous one")
        username = str(input("Enter Username? (No Spaces): "))
        check = [str(x).lower() for x in username]
        c = ["c"]

        # Checks if the value inputted by the user is proper and legitimate i.e., no spaces or empty anything
        while True:
            if 0 < len(check) and self.has_space(string=check):
                if check == c:
                    # If the user enters 'C', call start() to continue the game without saving the score
                    start()
                    break
                else:
                    # Append the username to name_list
                    name_list.append(username)
                    # Update the scoreboard using the player_record
                    self.Scoreboard(record=self.player_record)
                    # Call start() to continue the game
                    start()
                    break
            else:
                os.system("cls")
                print(" ")
                print("Invalid Username")
                print("If you want to save your score Enter Username Below, or Enter 'C' to continue (Be Warned Score Will not be Saved)")
                print("However if you have played before, you can reenter Your Username, then it will automatically update, however will only update if the new one is better then the previous one")
                username = str(input("Enter Username? (No Spaces): "))
                check = [str(x).lower() for x in username]


   #Code that     
    def Scoreboard(self, record):
        global scoreboard_dict
        global name_list
        if os.path.exists(scoreboard_file):
            with open(scoreboard_file, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    name = parts[0]
                    attempts = int(parts[1])
                    time = float(parts[2])
                    scoreboard_dict[name] = [attempts, time]

        name_list = self.sort_name_list(input=name_list)

        if (record != None and len(name_list) != 0) == True:
            name = name_list[-1]
            if name in scoreboard_dict:
                while True:
                    choice = input("Name already exists. Enter 'C' to continue (Be Warned Score Will not be Saved), or Enter 'Y' to Confirm Update or enter a new name: ")
                    if choice.lower() == 'c':
                        record = None 
                        break
                    if choice.lower() == "y":
                            value = scoreboard_dict[name]
                            if value > record:
                                print("Your Score has been update")
                                scoreboard_dict[name] = record
                                break
                            else:
                                print(f"Sorry, bud not better this time, last time {value}, this time {record}")
                    elif self.check_name_in_file(name=choice) and self.has_space(string=choice):
                        name = choice
                        name_list.append(name)
                        break
                    else:
                        print("Invalid Name. Please enter a different name.")
            else:
                name_list.append(name)

            if record != None and len(name_list) != 0:
                # Fix the code here with the overriding issue
                scoreboard_dict[name] = record
                os.system("cls")
                print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
                print("Name: Attempt(s): Time")
                print(" ") 
              
                # sort the scoreboard dictionary by attempts and then time
                sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

                # print the sorted scoreboard
                for i, (key, value) in enumerate(sorted_scores):
                    print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")
                
                with open(scoreboard_file, "w") as file:
                    for key, value in scoreboard_dict.items():
                        file.write(f"{key},{value[0]},{value[1]}\n")

            else:
                os.system("cls")
                print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
                print("Name: Attempt(s): Time")
                print(" ") 
                

                # sort the scoreboard dictionary by attempts and then time
                sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))
                # print the sorted scoreboard
                for i, (key, value) in enumerate(sorted_scores):
                    print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")
                
                with open(scoreboard_file, "w") as file:
                    for key, value in scoreboard_dict.items():
                        file.write(f"{key},{value[0]},{value[1]}\n")
                
        else:
            os.system("cls")
            print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
            print("Name: Attempt(s): Time") 
            print(" ")

            # sort the scoreboard dictionary by attempts and then time
            sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

            # print the sorted scoreboard
            for i, (key, value) in enumerate(sorted_scores):
                print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")
    
               


    def play_game(self):
        print(" ")
        main_loop = True
        counter = 1
        start_time = time.time()
        self.player_record = []

        while main_loop:
          if counter < self.max_attempts + 1:
            print(self.secret_word)
            print(f"This is Attempt Number {counter} out of {self.max_attempts}")
            self.board()
            inputed_word = str(input("Enter Guess?: ")).upper()
            os.system("cls")

            inputed_word = self.remove_spaces(string=inputed_word)
            inputed_word = [str(i) for i in inputed_word]
            inputed_word_length = len(inputed_word)
      
            if inputed_word_length == self.word_length:
                if self.check_word(word=f'"{"".join(map(str, inputed_word)).lower()}"'):
                        if inputed_word == self.secret_word:
                            for i in range(0, inputed_word_length):
                                if inputed_word[i] == self.secret_word[i]:
                                    inputed_word[i] = colored(inputed_word[i], "green")   

                            
                            end_time = time.time()
                            total_time = round(end_time - start_time, 3) 
                            print("You Won!")
                            inputed_word = "".join(map(str, inputed_word))
                            self.board_list.append(inputed_word)
                            self.board()
                            print(f"The Word was {inputed_word}")
                            print(f"It took you {counter} attempt(s)")
                            print(f"It took you in total {total_time} seconds")
                            
                            self.player_record.append(counter)
                            self.player_record.append(total_time)

                            self.user()
                            break
                         
                        else:
                            correct = 0
                            letterCount = {}

                            for letter in self.secret_word:
                                if letter in letterCount:
                                    letterCount[letter] += 1
                                else:
                                    letterCount[letter] = 1


                            # First iteration, check all the correct ones first
                            for value, letter in enumerate(inputed_word):
                                # Is it in the correct position?
                                if value < len(self.secret_word) and letter == self.secret_word[value]:
                                    if letterCount[letter] > 0:
                                        letterCount[letter] -= 1
                                        inputed_word[value] = colored(inputed_word[value], "green")
                                    correct += 1
                                    if correct == len(self.secret_word):
                                        break

                            # Go again and mark which ones are present but in the wrong position
                            for value, letter in enumerate(inputed_word):
                                # Skip the letter if it has been marked correct
                                if inputed_word[value] != colored(inputed_word[value], "green"):
                                    # Is it in the word? // Make sure we don't double count
                                    if letter in self.secret_word and letterCount[letter] > 0:
                                        letterCount[letter] -= 1
                                        inputed_word[value] = colored(inputed_word[value], "yellow")
                                    else:  # Not in the word or (was in word but letters all used up to avoid overcount)
                                        inputed_word[value] = colored(inputed_word[value], "grey")

                            self.board_list.append(inputed_word)

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
            
def main():
    wordle = Wordle()
    wordle.get_word()
    wordle.play_game()

def start():
    wordle = Wordle()
    print(" ")
    print("When you play, the game you get feedback based on the accurcy of your guess, in which 'Green' = Right place and letter, 'Yellow' = Right letter, 'Grey' = Just Wrong ")
    print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long ")
    play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()

    while True:
        if play == "p":
            main()
            break
        elif play == "s":
            wordle.Scoreboard(record=None)
            print(" ")
            print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long")
            print("When you play, the game you get feedback based on the accurcy of your guess, in which 'Green' = Right place and letter, 'Yellow' = Right letter, 'Grey' = Just Wrong ")
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()
        elif play == "e":
            break
        else:
            os.system("cls")
            print("Invalid Input")
            print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long")
            print("When you play, the game you get feedback based on the accurcy of your guess, in which 'Green' = Right place and letter, 'Yellow' = Right letter, 'Grey' = Just Wrong ")
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()

if __name__ == "__main__":
    os.system("cls")
    print("Hello And Welcome to Wordle!")
    start()


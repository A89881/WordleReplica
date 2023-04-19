import random
import re
import requests
from termcolor import colored
import time
import os

scoreboard_dict = {}
name_list = []


class Wordle:
    def __init__(self):
        self.word_list = []
        self.secret_word = None
        self.max_attempts = 6
        self.word_length = 5
        self.board_list = []


    def find_words(self):
        word_link = requests.get("https://meaningpedia.com/5-letter-words?show=all")
        pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
        self.word_list = pattern.findall(word_link.text)

    def choose_word(self):
        self.secret_word = random.choice(self.word_list).upper()
        self.secret_word = [str(i) for i in self.secret_word]
    
    def board(self):      
        for i in range(0, len(self.board_list)):
            self.board_list[i] = "".join(map(str, self.board_list[i]))
            print(f"| {self.board_list[i]} |")

    
    def sort_name_list(self, input):
        list1 = []
        [list1.append(x) for x in input if x not in list1]
        return list1

    
    def user(self):
        print(" ")
        print("If you want to save your score Enter Username Below, else Enter 'C' to continue (Be Warned Score Will not be Saved) ")
        username = str(input("Enter Username? (Max 5 Characters): "))
        check = [str(x).lower() for x in username]
        c = ["c"]

        while True:
            if 0 < len(check) <= 5:
                if check == c:
          
                    continue_start()
                    break
                else:
                    name_list.append(username)
         
                    self.Scoreboard(record=self.player_record)
                    continue_start()
                    break
            else: 
                print("Invalid Username")
                print("If you want to save your score Enter Username Below, else Enter 'C' to continue ")
                username = str(input("Enter Username? (Max 5 Character): ")).lower()
                check = [str(x) for x in username]

        
    def Scoreboard(self, record):
        global scoreboard_dict
        global name_list

        name_list = self.sort_name_list(input=name_list)

        if (record != None and len(name_list) != 0) == True:
            name = name_list[-1]
            if name in scoreboard_dict:
                while True:
                    choice = input("Name already exists. Enter 'C' to continue without updating, or enter a new name: ")
                    if choice.lower() == 'c':
                        record = None 
                        break
                    elif choice not in name_list:
                        name = choice
                        name_list.append(name)
                        break
                    else:
                        print("Name already exists. Please enter a different name.")
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
            # print(self.secret_word)
            print(f"This is Attempt Number {counter} out of {self.max_attempts}")
            self.board()
            inputed_word = str(input("Enter Guess?: ")).upper()
            os.system("cls")

            inputed_word = [str(i) for i in inputed_word]
            inputed_word_length = len(inputed_word)

            if inputed_word_length == self.word_length:
                if "".join(map(str, inputed_word)).lower() in self.word_list:
                
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
                         
                        if inputed_word != self.secret_word:
                            for i in range(0, inputed_word_length):

                                if inputed_word[i] == self.secret_word[i]: 
                                    inputed_word[i] = colored(inputed_word[i], "green")  
                                elif inputed_word[i] in self.secret_word:
                                    inputed_word[i] = colored(inputed_word[i], "yellow")
                                else:
                                    inputed_word[i] = colored(inputed_word[i], "grey")
                            
                            self.board_list.append(inputed_word)
                            counter += 1                 
                else:
                   print("Word is not valid; word doesn't exist")          
            else:
                print(f"Word entered is not {self.word_length} letters long")
          else:
            self.secret_word = "".join(map(str, self.secret_word))
            self.board()
            print("You have no more Attempts; You have lost the game")
            print(f"The Word was {self.secret_word}")
            continue_start()
            break
            
        

def main():
    wordle = Wordle()
    wordle.find_words()
    wordle.choose_word()
    wordle.play_game()

def start():
    wordle = Wordle()
    print("Hello and Welcome to Wordle")
    print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long")
    play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()

    while True:
        if play == "p":
            main()
            break
        elif play == "s":
            wordle.Scoreboard(record=None)
            print(" ")
            print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long")
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()
        elif play == "e":
            break
        else:
            os.system("cls")
            print("Invalid Input")
            print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long")
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()

def continue_start():
    wordle = Wordle()
    print(" ")
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
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()
        elif play == "e":
            break
        else:
            os.system("cls")
            print("Invalid Input")
            print(f"The Premise of the Game is to Guess the Hidden Word. You have {wordle.max_attempts} to Guess and the words are {wordle.word_length} letters long")
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()



if __name__ == "__main__":
    start()

import random
import re
import requests
from termcolor import colored
import time
import os

class Wordle:
    def __init__(self):
        self.word_list = []
        self.secret_word = None
        self.max_attempts = 6
        self.word_length = 5
        self.board_list = []
        self.dict1 = {}




    def find_words(self):
        word_link = requests.get("https://meaningpedia.com/5-letter-words?show=all")
        pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
        self.word_list = pattern.findall(word_link.text)

    def choose_word(self):
        self.secret_word = random.choice(self.word_list).upper()
        self.secret_word = [str(i) for i in self.secret_word]
    
    def user(self):
        print("If you want to save ")
        username = str(input("Enter Username?: "))

        pass

    def printScoreboard(self):
        pass
    

    def board(self):      
        for i in range(0, len(self.board_list)):
            self.board_list[i] = "".join(map(str, self.board_list[i]))
            print(self.board_list[i])


    def play_game(self):
        main_loop = True
        counter = 1
        #  start_time = time.time()

        while main_loop:
          if counter < self.max_attempts + 1:
            print(self.secret_word)
            print(f"This is Attempt Number {counter}")
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
          
                         
                            print("You Won!")
                            inputed_word = "".join(map(str, inputed_word))
                            self.board_list.append(inputed_word)
                            self.board()
                            print(f"The Word is {inputed_word}")
                            print(f"It took you {counter} attempt(s)")
                            # end_time = time.time()
                            # print(f"It took you in total {total_time} seconds")
                            continue_start()
                            break
                            
                
                        if inputed_word != self.secret_word:
                            for i in range(0, inputed_word_length):
                                if inputed_word[i] == self.secret_word[i]: 
                                    inputed_word[i] = colored(inputed_word[i], "green")  
                           
                                elif inputed_word[i] in self.secret_word:
                                    inputed_word[i] = colored(inputed_word[i], "yellow")
                                
                                else:
                                    pass
                            
        
                            self.board_list.append(inputed_word)
                            counter += 1                 
                else:
                   print("Word is not valid; word doesn't exist")          
            else:
                print(f"Word entered is not {self.word_length} letters long")
          else:
            print("You have no more Attempts; You have lost the game")
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
    play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()

    while True:
        if play == "p":
            main()
            break
        elif play == "s":
            wordle.printScoreboard()
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()
        elif play == "e":
            break
        else:
            os.system("cls")
            print("Invalid Answer")
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()

def continue_start():
    wordle = Wordle()
    play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()

    while True:
        if play == "p":
            main()
            break
        elif play == "s":
            wordle.printScoreboard()
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()
        elif play == "e":
            break
        else:
            os.system("cls")
            print("Invalid Answer")
            play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter 'E' to Exit?: ")).lower()


      
if __name__ == "__main__":
    start()

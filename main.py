import random
import re
import requests
import sys
from termcolor import colored
import time

class Wordle:
    def __init__(self):
        self.word_list = []
        self.secret_word = None
        self.max_attempts = 6
        self.word_length = 5
        self.username = None




    def find_words(self):
        word_link = requests.get("https://meaningpedia.com/5-letter-words?show=all")
        pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
        self.word_list = pattern.findall(word_link.text)

    def choose_word(self):
        self.secret_word = random.choice(self.word_list).upper()
        self.secret_word = [str(i) for i in self.secret_word]
        print(self.secret_word)
    
    def user(self):
        pass


    def play_game(self):
        main_loop = True
        counter = 1

        while main_loop:
          start_time = time.time()
          if counter < self.max_attempts + 1:
            print(f"This is Attempt Number {counter}")
            inputed_word = str(input("Enter Guess?: ")).upper()
            

            inputed_word = [str(i) for i in inputed_word]
            inputed_word_length = len(inputed_word)

            if inputed_word_length == self.word_length:
                
                if "".join(map(str, inputed_word)).lower() in self.word_list:
                    
               

                        if inputed_word == self.secret_word:
                            for i in range(0, inputed_word_length):
                                if inputed_word[i] == self.secret_word[i]:   
                                    print(colored(inputed_word[i], "green"), end="")

                            print("      ")
                            print("You Won!")
                            inputed_word = "".join(map(str, inputed_word))

                            print(f"The Word is {inputed_word}")
                            print(f"It took you {counter} attempt(s)")
                            end_time = time.time()
                            total_time = round(end_time - start_time)
                            print(f"It took you in total {total_time} seconds")


                            

                            continue_play = str(input("Enter 'P' to Continue Playing, Enter 'S' to access Scoreboard or Enter Any other Key to Exit Game: ").lower())
                            if continue_play == "p":
                                main()
                            if continue_play == "s":
                                break
                            else:
                                break
                            
                            

                        if inputed_word != self.secret_word:

                            for i in range(0, inputed_word_length):
                                if inputed_word[i] == self.secret_word[i]:   
                                    print(colored(inputed_word[i], "green"), end="")
                                elif inputed_word[i] in self.secret_word:
                                    print(colored(inputed_word[i], "yellow"), end="")
                                else:
                                    print(inputed_word[i], end="")
                                
                          
                            counter += 1
                            print("      ")   
                else:
                   print("Word is not valid; word doesn't exist")
                  
            else:
                print(f"Word entered is not {self.word_length} letters long")

          else:
            print("You have no more Attempts; You have lost the game")
            break
        


def start():
    print("Hello and Welcome to Wordle")
    play = str(input("Enter 'P' if you wish to Play, Enter 'S' to access Scoreboard or Enter Any other Key to Exit game?: ")).lower()

    if play == "p":
        main()
    elif play == "s":
        pass
    else:
        pass 


def main():
    wordle = Wordle()
    wordle.find_words()
    wordle.choose_word()
    wordle.play_game()


if __name__ == "__main__":
    start()

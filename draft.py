import random
import re
import requests



letters = ["abcdefghijklmnopqrstuvrst"]
list1 = []
 
main_loop = True
counter = 1

class main:
  def __init__(self, name):
    self.player_dict = {}
    self.name = name
    pass
  
  def Intro(self):
    print("Welcome to the game!")
    self.name = str(input(print("Enter Username?: ")))
    self.player_dict[self.name] = 0

  def word_generation(self):
    print("Finding Word")
    word_link = requests.get(
        "https://meaningpedia.com/5-letter-words?show=all")

    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    word_list = pattern.findall(word_link.text)


    game_word = random.choice(word_list)
    game_word = [str(i) for i in game_word] 
    print(game_word)

    




while main_loop == True:
    
    word = str(input("Enter Guess?: ")).lower()
    print("-----------------------------------------")
    word = [str(i) for i in word ]
    word_length = len(word)

    if "".join(map(str, word)) in word_list: 
      if word_length == 5:
        if counter < 6:
          if game_word == word:
            print("You Won") 
            word = "".join(map(str, word))
            print(f"the word is {word.capitalize()}")
            print(f"It took you {counter} attempt(s)")
            break

          if game_word != word:

            for i in game_word:
              for j in word:
                  if i == j:
                    list1.append(j)
                    # list1 = list(set(list1))

            if len(list1) == 0:
              counter += 1
              print(f"This is your {counter} attempt")

            else:  
              print(f"the letter(s) {list1} are in the word")
              counter += 1
              print(f"This is your {counter} attempt")
            
        else:
          print("You have the lost the game")
          break
      else:
        print("Word entered is not 5 letters long")
    else:
      print("Word is not valid; word doesn't exist")





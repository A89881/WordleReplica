# import random

# def generate_word():
#     # create a list of possible words
#     words = ['apple', 'banana', 'cherry', 'orange', 'pear']
#     # select a random word from the list
#     return random.choice(words)

# def compare_words(word, guess):
#     correct_letters = 0
#     correct_positions = 0
#     for i in range(len(word)):
#         if word[i] == guess[i]:
#             correct_positions += 1
#         elif guess[i] in word:
#             correct_letters += 1
#     return correct_letters, correct_positions

# def main():
#     # generate the random word
#     word = generate_word()
#     guesses = 0
#     max_guesses = 6
#     while guesses < max_guesses:
#         # get the player's guess
#         guess = input('Enter your guess: ')
#         # compare the guess to the random word
#         correct_letters, correct_positions = compare_words(word, guess)
#         # display the results of the guess
#         print(f'Correct letters: {correct_letters}, Correct positions: {correct_positions}')
#         guesses += 1
#         if guess == word:
#             # player has won
#             print('Congratulations! You have won!')
#             return
#     # player has lost
#     print(f'Sorry, you have run out of guesses. The word was {word}.')

# if __name__ == '__main__':
#     main()

import random
import re
import requests

print("Finding Word")

word_link = requests.get(
    "https://meaningpedia.com/5-letter-words?show=all")

pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
word_list = pattern.findall(word_link.text)


item = random.choice(word_list)
item = [str(i) for i in item]
print(item)

letters = ["abcdefghijklmnopqrstuvrst"]
list1 = []
 
main_loop = True
counter = 1

while main_loop == True:
    
    word = str(input("Enter Guess?: ")).lower()
    print("-----------------------------------------")
    word = [str(i) for i in word ]
    word_length = len(word)

    if "".join(map(str, word)) in word_list: 
      if word_length == 5:
        if counter < 6:
          if item == word:
            print("You Won") 
            word = "".join(map(str, word))
            print(f"the word is {word.capitalize()}")
            print(f"It took you {counter} attempt(s)")
            break

          if item != word:

            for i in item:
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





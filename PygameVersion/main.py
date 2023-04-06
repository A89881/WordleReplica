# import random
# import re
# import requests

# import pygame
# from .settings import *
# from .sprites import *


# class Wordle:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption(title=title)
#         self.img = pygame.image.load("Assets/Icon.png")
#         pygame.display.set_icon(self.img)

#         self.clock = pygame.time.Clock()
#         self.word_list = []
#         self.secret_word = None
    
#     def events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT():
#               pygame.quit()
#               quit(0)

#     def find_words(self):
#         word_link = requests.get("https://meaningpedia.com/5-letter-words?show=all")
#         pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
#         self.word_list = pattern.findall(word_link.text)

#     def choose_word(self):
#         self.secret_word = random.choice(self.word_list)
#         self.secret_word = [str(i) for i in self.secret_word]
#         print(self.secret_word)

#     def play_game(self):
#         letters = ["abcdefghijklmnopqrstuvrst"]
#         char_list = []
#         main_loop = True
#         counter = 1

#         while main_loop:
#             word = str(input("Enter Guess?: ")).lower()
#             print("-----------------------------------------")
#             word = [str(i) for i in word]
#             word_length = len(word)

#             if "".join(map(str, word)) in self.word_list:
#                 if word_length == 5:
#                     if counter < 6:
#                         if self.secret_word == word:
#                             print("You Won")
#                             word = "".join(map(str, word))
#                             print(f"the word is {word.capitalize()}")
#                             print(f"It took you {counter} attempt(s)")
#                             break

#                         if self.secret_word != word:
#                             for i in self.secret_word:
#                                 for j in word:
#                                     if i == j:
#                                         char_list.append(j)
                          

#                             for i in range(len(char_list)):
#                                 j = i + 1
#                                 while j < len(char_list):
#                                     if char_list[i] == char_list[j]:
#                                         char_list.pop(j)
#                                     else:
#                                         j += 1

#                             if len(char_list) == 0:
#                                 counter += 1
#                                 print(f"This is your {counter} attempt")

#                             else:
#                                 print(f"the letter(s) {char_list} are in the word")
#                                 counter += 1
#                                 print(f"This is your {counter} attempt")

#                     else:
#                         print("You have lost the game")
#                         break
#                 else:
#                     print("Word entered is not 5 letters long")
#             else:
#                 print("Word is not valid; word doesn't exist")


# def main():
#     wordle = Wordle()
#     wordle.find_words()
#     wordle.choose_word()
#     wordle.play_game()


# if __name__ == "__main__":
#     main()

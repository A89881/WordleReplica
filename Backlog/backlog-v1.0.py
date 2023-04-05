import random
import re
import requests


class WordGame:
    def __init__(self):
        self.word_list = []
        self.item = None

    def find_words(self):
        word_link = requests.get("https://meaningpedia.com/5-letter-words?show=all")
        pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
        self.word_list = pattern.findall(word_link.text)

    def choose_word(self):
        self.item = random.choice(self.word_list)
        self.item = [str(i) for i in self.item]
        print(self.item)

    def play_game(self):
        letters = ["abcdefghijklmnopqrstuvrst"]
        char_list = []
        main_loop = True
        counter = 1

        while main_loop:
            word = str(input("Enter Guess?: ")).lower()
            print("-----------------------------------------")
            word = [str(i) for i in word]
            word_length = len(word)

            if "".join(map(str, word)) in self.word_list:
                if word_length == 5:
                    if counter < 6:
                        if self.item == word:
                            print("You Won")
                            word = "".join(map(str, word))
                            print(f"the word is {word.capitalize()}")
                            print(f"It took you {counter} attempt(s)")
                            break

                        if self.item != word:
                            for i in self.item:
                                for j in word:
                                    if i == j:
                                        char_list.append(j)
                          

                            for i in range(len(char_list)):
                                j = i + 1
                                while j < len(char_list):
                                    if char_list[i] == char_list[j]:
                                        char_list.pop(j)
                                    else:
                                        j += 1

                            if len(char_list) == 0:
                                counter += 1
                                print(f"This is your {counter} attempt")

                            else:
                                print(f"the letter(s) {char_list} are in the word")
                                counter += 1
                                print(f"This is your {counter} attempt")

                    else:
                        print("You have lost the game")
                        break
                else:
                    print("Word entered is not 5 letters long")
            else:
                print("Word is not valid; word doesn't exist")


def main():
    word_game = WordGame()
    word_game.find_words()
    word_game.choose_word()
    word_game.play_game()


if __name__ == "__main__":
    main()

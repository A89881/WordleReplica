import random
import re
import requests


class Wordle:

    def __init__(self):
        self.word_list = []
        self.secret_word = None

    def find_words(self):
        word_link = requests.get("https://meaningpedia.com/5-letter-words?show=all")
        pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
        self.word_list = pattern.findall(word_link.text)

    def choose_word(self):
        self.secret_word = random.choice(self.word_list)
        self.secret_word = [str(i) for i in self.secret_word]
        print(self.secret_word)

    def play_game(self):
        letters = ["abcdefghijklmnopqrstuvrst"]
        char_list = []
        main_loop = True
        counter = 1
        max_attempts = 6
        word_length = 5

        while main_loop:
            inputed_word = str(input("Enter Guess?: ")).lower()
            print("-----------------------------------------")
            inputed_word = [str(i) for i in inputed_word]
            inputed_word_length = len(inputed_word)

            if "".join(map(str, inputed_word)) in self.word_list:
                if inputed_word_length == word_length:
                    if counter < max_attempts:
                        if self.secret_word == inputed_word:
                            print("You Won")
                            inputed_word = "".join(map(str, inputed_word))
                            print(f"the inputed_word is {inputed_word.capitalize()}")
                            print(f"It took you {counter} attempt(s)")
                            break

                        if self.secret_word != inputed_word:
                            for i in self.secret_word:
                                for j in inputed_word:
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
                                print(f"the letter(s) {char_list} are in the inputed_word")
                                counter += 1
                                print(f"This is your {counter} attempt")

                    else:
                        print("You have lost the game")
                        break
                else:
                    print("Word entered is not 5 letters long")
            else:
                print("Word is not valid; inputed_word doesn't exist")


def main():
    wordle = Wordle()
    wordle.find_words()
    wordle.choose_word()
    wordle.play_game()


if __name__ == "__main__":
    main()

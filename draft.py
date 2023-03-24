import random

word_list = ["broke","steak","drake","sharp","space", "U gay boy"]
item = random.choice(word_list)
item = [str(i) for i in item]

letters = ["abcde"]
list1 = []
print(item)
main_loop = True
counter = 1

while main_loop == True:
    
    word = str(input("Enter Guess?: ")).lower()
    word = [str(i) for i in word ]

    if counter < 6:

      if item == word:
        word = "".join(map(str, word))
        print(f"the word is {word.capitalize()}")
        print(f"It took you {counter} attempt(s)")
        print("You Won")
        break

      if item != word:
        for i in item:
          for j in word:
              if i == j:
                list1.append(j)
                list1 = list(set(list1))
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
    






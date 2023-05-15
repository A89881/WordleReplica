"""
Shit
"""
# class Test: 
#     def __init__(self):
#       self.max_attempts = 6
#       self.word_length = 5
#       self.table_list = []
#       self.column_list = []


#     # def printTable(self):
#     #         for row in range (0, self.max_attempts+1):
#     #             for column in range(0, self.word_length):
#     #                 print("! - !", end="")
#     # self.table_list.append("| - | ")
  
#   # for i in self.table_list:
#   #     print(i, end="")

#     def board(self):
#         for column in range(0, self.word_length):
#             self.column_list.append("-")
       
#         for row in range(0, self.max_attempts):
#             self.table_list.append(self.column_list)
        
#         for element in range(0, len(self.table_list)): 
#           print(self.table_list[element])


#         print("pause")
#         print(self.table_list)
      


# test = Test()                  
# test.board()

# class Test:
#     def __init__(self):
#         self.dict1 = {}
#         pass
    
# test = Test()
# print(test.dict1)

# my_dictionary = {}
# my_list = [["three", 3], ["four", 4]]
# print("Before:", my_dictionary)
# for key,value in my_list:
#     my_dictionary[key] = value
# print("After:", my_dictionary)

# list1 = ["1", "2"]

# # Using update() method
# my_dict = {}
# my_dict.update({"my_list": list1})
# print(my_dict)  # Output: {'my_list': ['1', '2']}

# # Using square bracket notation
# my_dict = {}
# my_dict["my_list"] = list1
# print(my_dict)  # Output: {'my_list': ['1', '2']}

# my_list = ['apple', 'banana', 'orange']
# my_dict = {item: None for item in my_list}
# print(my_dict)

# my_list.append("berry")
# print(my_list)
# print(my_dict)

"""
Code that takes in the values and prints them properly
"""

  # def Scoreboard(self, record):
    #     global scoreboard_dict
    #     global name_list

    #     if record != None:
    #         username = name_list[-1]
    #         if username in scoreboard_dict:
    #             scoreboard_dict[username].append(record)
    #         else:
    #             scoreboard_dict[username] = [record]

    #         os.system("cls")
    #         print("The Scoreboard ranks the players based on the number of guesses required for them to win and the amount of time it took to win")
    #         print("Name: Attempts: Time")
    #         for key, value in scoreboard_dict.items():
    #             print(key, value)
    #     else:
    #         for key, value in scoreboard_dict.items():
    #             print(key, value)

"""
Similar Code that takes in values and prints them properly but sorts them also
"""
    # def Scoreboard(self, record):
    #     if record != None:
    #         global scoreboard_dict
    #         global name_list
    #         scoreboard_dict[name_list[-1]] = record
    #         os.system("cls")
    #         print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
    #         print("Name: Attempt(s): Time")
    #         print(" ") 

    #         # sort the scoreboard dictionary by attempts and then time
    #         sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

    #         # print the sorted scoreboard
    #         for i, (key, value) in enumerate(sorted_scores):
    #             print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")

    #     else:
    #         os.system("cls")
    #         print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
    #         print("Name: Attempts: Time") 
    #         print(" ")

    #         # sort the scoreboard dictionary by attempts and then time
    #         sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

    #         # print the sorted scoreboard
    #         for i, (key, value) in enumerate(sorted_scores):
    #             print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")

"""
Code that takes in values, prints them properly sorts them but if duplicate name is found it removes the recent one: punishes you for entering in the same name
"""
# def Scoreboard(self, record):
#         if record != None:
#             global scoreboard_dict
#             global name_list
#             name = name_list[-1]
#             if name in scoreboard_dict:
#                 print(f"The name '{name}' already exists in the scoreboard. You cannot replace it.")
#                 return
#             scoreboard_dict[name] = record
#             os.system("cls")
#             print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
#             print("Name: Attempt(s): Time")
#             print(" ") 

#             # sort the scoreboard dictionary by attempts and then time
#             sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

#             # print the sorted scoreboard
#             for i, (key, value) in enumerate(sorted_scores):
#                 print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")

#         else:
#             os.system("cls")
#             print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
#             print("Name: Attempts: Time") 
#             print(" ")

#             # sort the scoreboard dictionary by attempts and then time
#             sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

#             # print the sorted scoreboard
#             for i, (key, value) in enumerate(sorted_scores):
#                 print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")


"""
Code that returns that invalid input 
"""

 # def Scoreboard(self, record):
    #     if record != None:
    #         global scoreboard_dict
    #         global name_list
    #         scoreboard_dict[name_list[-1]] = record
    #         os.system("cls")
    #         print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
    #         print("Name: Attempt(s): Time")
    #         print(" ") 

    #         # sort the scoreboard dictionary by attempts and then time
    #         sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

    #         # print the sorted scoreboard
    #         for i, (key, value) in enumerate(sorted_scores):
    #             print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")

    #     else:
    #         os.system("cls")
    #         print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
    #         print("Name: Attempts: Time") 
    #         print(" ")

    #         # sort the scoreboard dictionary by attempts and then time
    #         sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

    #         # print the sorted scoreboard
    #         for i, (key, value) in enumerate(sorted_scores):
    #             print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")

# def my_function():
#     # some code here
#     return False

# if my_function() == False:
#     # do something here if the function returns False
#     print("works")

# if bool(my_function()) == False:
#     print("works too")

# my_function()

"""
Scoreboard Overide stuff
"""

  # if name_list[-1] != name and len(name_list) >= 0:
            #     scoreboard_dict[name] = record
            #     os.system("cls")
            #     print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
            #     print("Name: Attempt(s): Time")
            #     print(" ") 

            #     # sort the scoreboard dictionary by attempts and then time
            #     sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

            #     # print the sorted scoreboard
            #     for i, (key, value) in enumerate(sorted_scores):
            #         print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")
            

            # else:
            #     scoreboard_dict[name] = record
            #     os.system("cls")
            #     print("The Scoreboard ranks the players based on amount of guesses required for them to win and the amount of time it took to win")
            #     print("Name: Attempt(s): Time")
            #     print(" ") 

            #     # sort the scoreboard dictionary by attempts and then time
            #     sorted_scores = sorted(scoreboard_dict.items(), key=lambda x: (x[1][0], x[1][1]))

            #     # print the sorted scoreboard
            #     for i, (key, value) in enumerate(sorted_scores):
            #         print(f"{i+1}. {key}: {value[0]} attempt(s), {value[1]} seconds")

# import random

# list1 = [] 
# for a in range(1, 5):
#     for i in range(1, 14):
#         list1.append(i)


# print(list1)


# a = random.sample(list1, 2)

# alphabet = ["abcdefghijklmnopqrstuvwyz"]
# alphabet = [str(x) for x in alphabet]

# def has_space(string):
#     if ' ' in string:
#         return True
#     else:
#         return False

# # Example usage:
# # user_input = input("Enter a string: ")
# while True:
#   user_input = input("Enter a string: ")
#   if has_space(user_input):
#       print("String contains a space.")
#   else:
#       print("String does not contain a space.")


# for a in range(0, inputed_word_length):
#     letter = self.secret_word[a]
#     if letters_check[letter]:
#         letters_check[letter] += 1
#     else:
#         letters_check[letter] = 1

# correct_letters = 0
# correct_positions = []
# for i in range(0, inputed_word_length):
#     if inputed_word[i] == self.secret_word[i]:
#         inputed_word[i] = colored(inputed_word[i], "green")
#         correct_letters += 1
#         correct_positions.append(i)
#     elif inputed_word[i] in self.secret_word:
#         inputed_word[i] = colored(inputed_word[i], "yellow")
# for i in range(0, inputed_word_length):
#     if i not in correct_positions:
#         inputed_word[i] = colored(inputed_word[i], "grey")

# self.board_list.append(inputed_word)
# counter += 1


# list1 = [5, 20.13]
# list2 = [2, 40.13]

# if list1 < list2:
#     print("list1 is smaller than list2")
# elif list1 > list2:
#     print("list1 is greater than list2")
# else:
#     print("list1 and list2 are equal")


def remove_spaces(string):
    return "".join(string.split())

# Example usage
input_string = "This is an example string"
output_string = remove_spaces(input_string)
print(output_string)

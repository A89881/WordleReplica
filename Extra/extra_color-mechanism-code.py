# print(self.secret_word)
# dictionary = {}


# for a in range(0, inputed_word_length):
#     letter = self.secret_word[a]
#     if letter in dictionary:
#         dictionary[letter] += 1
#     else:
#         dictionary[letter] = 1

# print(dictionary)


"""
Chat Gpt Version One - My goofing with enumerate
"""

# for value, i in enumerate(inputed_word):
#     if i in self.secret_word:
#         if value == self.secret_word.index(i):  
#             if dictionary[i] > 0:
#                 dictionary[i] -= 1
#                 inputed_word[value] = colored(inputed_word[value], "green")                                   
#         else:
#             if inputed_word[value] != colored(inputed_word[value], "green"):                                   
#                 if 0 < dictionary[i] <= self.secret_word.count(i):
#                     dictionary[i] -= 1
#                     inputed_word[value] = colored(inputed_word[value], "yellow")                 
#                 else:
#                     inputed_word[value] = colored(inputed_word[value], "grey")
#     else:
#         inputed_word[value] = colored(inputed_word[value], "grey")


# self.board_list.append(inputed_word)

"""
My Slightly better version
"""

# for i in inputed_word:
#     if i in self.secret_word:
#         value = inputed_word.index(i)
#         if inputed_word.index(i) == self.secret_word.index(i):  
#             dictionary[inputed_word[value]] -= 1          
#             inputed_word[value] = colored(inputed_word[value], "green")                                   
#         else: 
#             if inputed_word[value] != colored(inputed_word[value], "green"):                                   
#                 if 0 < dictionary[i] <= self.secret_word.count(i):
#                     dictionary[i] -= 1
#                     inputed_word[value] = colored(inputed_word[value], "yellow")                 
#                 else:
#                     inputed_word[value] = colored(inputed_word[value], "grey")
#             else:
#                 if 0 < dictionary[i] <= self.secret_word.count(i):
#                     dictionary[i] -= 1
#                     inputed_word[value] = colored(inputed_word[value], "yellow")       
#     else:
#         value = inputed_word.index(i)
#         inputed_word[value] = colored(inputed_word[value], "grey")
    

# self.board_list.append(inputed_word)


"""
My Original Version
"""

# letters_check = {}   
                            
# for a in range(0, inputed_word_length):
#     letter = self.secret_word[a]
#     if letter in letters_check:
#         letters_check[letter] += 1
#     else:
#         letters_check[letter] = 1

# for i in reversed(range(0, inputed_word_length)):
#     letter = inputed_word[i]
#     if inputed_word[i] == self.secret_word[i]:
#         inputed_word[i] = colored(inputed_word[i], "green")
#         letters_check[letter] -= 1
#     else:
#         if inputed_word[i] != colored(inputed_word[i], "green"):             
#             if inputed_word[i] in self.secret_word and letters_check[letter] > 0:
#                     inputed_word[i] = colored(inputed_word[i], "yellow")  
#                     letters_check[letter] -= 1
#             else:
#                 inputed_word[i] = colored(inputed_word[i], "grey")                                                
# self.board_list.append(inputed_word)
# counter += 1

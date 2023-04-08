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

my_list = ['apple', 'banana', 'orange']
my_dict = {item: None for item in my_list}
print(my_dict)

my_list.append("berry")
print(my_list)
print(my_dict)


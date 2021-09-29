"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# assign a variable to each item in the list
input_string = 'pow 3 5'
token = input_string.split(' ')
func_name = token[0]
param_a = token[1]
param_b = token[2]

# pseudo-code
# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens
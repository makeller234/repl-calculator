"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# assign a variable to each item in the list


#print(func_name, param_a, param_b)

while True:
    user_input= input("Enter math function and two numbers")
    token = user_input.split(' ')
    func_name = token[0]
    
    if len(token)>=2:
        param_a= float(token[1])
    if len(token)>=3:
        param_b= float(token[2])

        
    if func_name == "q":
        break

    elif func_name == "+":
        print(add(param_a, param_b))

    elif func_name == "-":
        print(subtract(param_a, param_b))
    elif func_name == "*":
        print(multiply(param_a, param_b))
    elif func_name == "/":
        print(divide(param_a, param_b))
    elif func_name == "square":
        print(square(param_a))
    elif func_name == "cube":
        print(cube(param_a))
    elif func_name == "power":
        print(power(param_a, param_b))
    elif func_name == "mod":
        print(mod(param_a, param_b))

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

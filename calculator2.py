from arithmetic2 import (add, subtract)

while True:
    user_input= input("Enter math function and numbers")
    token = user_input.split(' ')
    func_name = token[0]

    user_numbers = []
    for i in token[1::]:
        user_numbers.append(int(i))

    if func_name == "q":
        break

    elif func_name == "+":
        print(add(user_numbers))

    elif func_name == "-":
        print(subtract(user_numbers))



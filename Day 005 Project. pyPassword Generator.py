import random

print("Welcome to the PyPython Generator")
pass_length = int(input("How many letters would you like in your password: \n"))
symbols_in_pass = int(input("How many symbols would you like to include: \n"))
numbers_in_pass = int(input("How many numbers would you like to include: \n"))
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
common_symb = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

password = []
for i in range(symbols_in_pass):
    random_symb = random.choice(common_symb)
    password.append(random_symb)
for i in range(numbers_in_pass):
    random_num = random.choice(num)
    password.append(numbers_in_pass)
for i in range (pass_length):
    random_alpha = random.choice(alpha)
    password.append(random_alpha)

random.shuffle(password)
final_password = ""
for i in range(len(password)):
    final_password += str(password[i])

print(final_password)

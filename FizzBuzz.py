"""
Rules of FizzBuzz game:

if a number divisible by  3 you have to say Fizz
if a number divisible by 5 you have to say Buzz
if a number divisible by both 3 & 5 you have to say FizzBuzz instead of number

"""

target = int(input("Enter a number to print FizzBuzz: "))
for i in range(1, target):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



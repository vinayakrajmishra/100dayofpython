import random

# ASCII Arts for rock, paper, and scissors by Veronica Karlsson
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
lst = [rock, paper, scissors]

user_choice_abbreviation = input("Enter R for Rock, P for Paper & S for Scissor:\n").upper()
if user_choice_abbreviation == "R":
    user_choice = "Rock"
    user_choice_symbol = lst[0]
elif user_choice_abbreviation == "P":
    user_choice = "Paper"
    user_choice_symbol = lst[1]
elif user_choice_abbreviation == "S":
    user_choice = "Scissor"
    user_choice_symbol = lst[2]
else:
    print(f"You entered wrong choice. {exit()}")
computer_choice = random.randint(0, 2)
computer_choice_symbol = lst[computer_choice]

print(f"You got {user_choice_symbol}\nAnd computer got {computer_choice_symbol}")

if user_choice.lower() == "rock":
    if computer_choice == 0:
        print("Since both are same, No one won")
    elif computer_choice == 1:
        print(f"Paper beats rock by covering it, Computer Won")
    elif computer_choice == 2:
        print("Rock beats scissors by breaking it, You won")
elif user_choice.lower() == "paper":
    if computer_choice == 0:
        print(f"Paper beats rock by covering it, Computer Won")
    elif computer_choice == 1:
        print("Since both are same, No one won")
    elif computer_choice == 2:
        print("Scissors beats paper by cutting it, Computer won")
elif user_choice.lower() == "scissor":
    if computer_choice == 0:
        print("Rock beats scissors by breaking it, Computer Won")
    elif computer_choice == 1:
        print("Scissors beats paper by cutting it, You won")
    elif computer_choice == 2:
        print("Since both are same, No one won")



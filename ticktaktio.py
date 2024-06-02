import random

line0 = [0, "a", "b", "c"]
line1 = [1, "☐", "☐", "☐"]
line2 = [2, "☐", "☐", "☐"]
line3 = [3, "☐", "☐", "☐"]

print("Welcome to ticktactio\n-----------------------------------")
print("Choose whether you wanna go with O or X")

# Deciding X & O
user_key = input().upper()
if user_key == "O":
    computerkey = "X"
elif user_key == "X":
    computerkey = "O"
else:
    print(f"You entered wrong key, restart the program{exit()}")

# Printing blank
print(f"{line0}\n{line1}\n{line2}\n{line3}")

# Creating function for putting X and cross


def positioning(p):
    if int(position[1]) == 1:
        if (position[0]).lower() == "a":
            line1[1] = user_key
        elif (position[0]).lower() == "b":
            line1[2] = user_key
        elif (position[0]).lower() == "c":
            line1[3] = user_key
        else:
            print(f"You entered wrong position. Restart the program{exit()}")
    elif int(position[1]) == 2:
        if (position[0]).lower() == "a":
            line2[1] = user_key
        elif (position[0]).lower() == "b":
            line2[2] = user_key
        elif (position[0]).lower() == "c":
            line2[3] = user_key
        else:
            print(f"You entered wrong position. Restart the program{exit()}")
    elif int(position[1]) == 3:
        if (position[0]).lower() == "a":
            line3[1] = user_key
        elif (position[0]).lower() == "b":
            line3[2] = user_key
        elif (position[0]).lower() == "c":
            line3[3] = user_key
        else:
            print(f"You entered wrong position. Restart the program{exit()}")
    else:
        print(f"You entered wrong position. Restart the program{exit()}")


flag = 0
while flag == 0:
    position = input("Enter a position you wanna start with: ").upper()
    positioning(position)
    print(f"{line0}\n{line1}\n{line2}\n{line3}\n")
    i = position[0]
    j = random.randint(1, 3)
    computer_position = i + j.__str__()
  #  if != "☐"
  #  positioning(computer_position)

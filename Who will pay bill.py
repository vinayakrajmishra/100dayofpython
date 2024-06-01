import random

try:
    no_of_people = int(input("How many people are there: \n "))
except ValueError:
    print("You entered a wrong argument. Please restart the program")
    exit()
if no_of_people > 1:
    name = input(f"Please enter all {no_of_people} names separated by comma: \n").split(sep=",", maxsplit=no_of_people)
    len_name = len(name)
elif no_of_people == 1:
    print("No need to use this app.")
    exit()
else:
    print("You entered a wrong argument. Please restart the program")
    exit()


def print_bill_person():
    try:
        bill_person = name[random.randint(0, no_of_people-1)]
        print(f"Today's bill is on {bill_person}")
    except IndexError:
        bill_person = name[random.randint(0, len_name-1)]
        print(f"Though you have not entered all {no_of_people} entries but out of the {len_name} name you entered, "
              f"Today's bill is on {bill_person}")


if len_name == no_of_people:
    print_bill_person()
elif len_name > no_of_people:
    print(f"Number of people were only {no_of_people} but you entered more names. So we are taking only"
          f"first {no_of_people} names for randomization.")
    name = name[:no_of_people]  # Truncate the list to the first no_of_people names
    print_bill_person()


print(len_name)
#Write a function that prompts the user for an integer and handles the ValueError if they type text instead.
def get_number():
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
    except ValueError:
        print("Invalid input! Please enter an integer.")

get_number()

ANS:
Enter an integer:  str
Invalid input! Please enter an integer.

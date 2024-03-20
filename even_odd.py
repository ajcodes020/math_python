print("This program will check if a given integer number is even or odd.")


def is_even(n):
    """ Returns True if given integer number is even, else False """
    return n % 2 == 0


number = int(input("Enter an integer number: "))
print(f"{number} is an even number.") if is_even(number) else print(f"{number} is an odd number.")

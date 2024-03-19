print("This program will check if a given integer number is a prime number.")


def is_prime(n):
    """ Returns True if given integer number is a prime number, else False """
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


number = int(input("Enter an integer number: "))
print(f"{number} is a prime number.") if is_prime(number) else print(f"{number} is not a prime number.")

print("This program will check if a given integer number is a perfect number.")


def is_perfect_number(n):
    """ Return True if given integer number is a perfect number, else False """
    divisors_sum = sum([x for x in range(1, n) if n % x == 0])
    return divisors_sum == n


number = int(input("Enter an integer number: "))
print(f"{number} is a perfect number.") if is_perfect_number(number) else print(f"{number} is not a perfect number.")

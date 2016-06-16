# Write a factorial function that takes a positive integer,  N as a
# parameter and prints the result of  N! (N factorial).


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(factorial(int(input())))

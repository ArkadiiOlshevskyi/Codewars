# lest make a list with 1 000 000 numbers and iterate trough it

num = list(range(2, 100000))
divisor = 3

for n in num:
    if n % divisor == 0:
        print(f"{n} is divisible by {divisor}")


# second example

num2 = list(range(2, 1000000))

for n in num2:
    result = n // 3
    print(f"The floor division of {n} by 3 is: {result}")

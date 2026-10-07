def FizzBuzz(n):
    for item in range(1, n+1):
        if item % 3 == 0:
            print("Fizz")
        elif item % 5 == 0:
            print("Buzz")
        elif item % 15 == 0:
            print("FizzBuzz")
        else:
            print(item)

FizzBuzz(15)


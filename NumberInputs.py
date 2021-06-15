import statistics


def AskNum():
    num1 = input("What is the first number?")
    num2 = input("What is the second number?")
    num3 = input("What is the third number?")
    num4 = input("What is the fourth number?")
    num5 = input("What is the fifth number?")
    numbers = [num1, num2, num3, num4, num5]
    return numbers


things = AskNum()
stuff = list(map(int, things))
max = max(stuff)
min = min(stuff)
average = statistics.mean(stuff)
mode = statistics.mode(stuff)

print(f'The max is {max}')
print(f'The min is {min}')
print(f'The mean is {average}')
print(f'The mode is {mode}')

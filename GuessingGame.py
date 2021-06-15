import random

randomNum = random.randint(1, 10)
userNum = input(
    "Imagine going from professional programming to having to read this lol,\
what's your guess (between 1 and 10)?")
userNum = int(userNum)


if randomNum == userNum:
    print(f"Correct! The number was {randomNum}, you guessed {userNum}")
elif (abs(userNum-randomNum)) == 1:
    print(f"Wrongo, Bucko. The number was {randomNum},\
you were off by {abs(userNum-randomNum)}. So close!")
elif (abs(userNum-randomNum)) >= 2 and (abs(userNum-randomNum)) < 5:
    print(f"Little further off mark there bud. The number was {randomNum},\
you were off by {abs(userNum-randomNum)}. Keep trying!")
elif (abs(userNum-randomNum)) >= 5:
    print(f"Uninstall the game, you're bad. The number was {randomNum},\
you were off by {abs(userNum-randomNum)}. Maybe stick to Fortnite?")

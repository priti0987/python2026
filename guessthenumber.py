import random

n = random.randint(1,10)
print(n)
while True:
    num = int(input("Guess the number between 1 to 10 = "))

    if num == n:
        print("You win ..!")
        break
    else:
        print("Try again...")
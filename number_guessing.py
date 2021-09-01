import random

num1 = random.randint(0, 100)
num2 = eval(input("Guess the number")) 

if num1 == num2:
    print("Yes the number is", num1)
elif  num1 > num2:
    print("Your guess is low")
    while num1 != num2:
        num2 = eval(input("Guess the number"))
        if num1 == num2:
            print("Yes the number is", num1)
        elif(num1 > num2):
            print("Your guess is low")
        else:
            print("Your guess is high")
else:
    print("Your guess is high")
    while num1 != num2:
        num2 = eval(input("Guess the number"))
        if num1 == num2:
            print("Yes the number is", num1)
        elif(num1 > num2):
            print("Your guess is low")
        else:
            print("Your guess is high")



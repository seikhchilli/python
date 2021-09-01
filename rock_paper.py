import random

num1 = random.randint(0,2)


if num1 == 0:
    cmo = "rock"
elif num1 == 1:
    cmo = "paper"
else:
    cmo = "scissors"

num2 = eval(input("Choose rock(0), paper(1), or scissors(2)"))

print("Computer chose " + cmo)

if num1 == num2:
    print("Tie")
elif num1 == 0:
    if num2 == 1:
        print("You won")
    else:
        print("You lost")
elif num1 == 1:
    if num2 == 0:
        print("You lost")
    else:
        print("You won")
else:
    if num2 == 0:
        print("You won")
    else:
        print("You lost")





import random

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

sum_input = eval(input(str(number1) + "+"+ str(number2)+ " = "))

print(number1, "+", number2, " = ", sum_input, "is", number2+number1 == sum_input)
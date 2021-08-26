day = 0;

question1 = "Is your birthday in Set 1? \n"+\
    " 1  3  5  7\n" + \
    " 9 11 13 15\n" + \
    "17 19 21 23\n" + \
    "25 27 29 31\n" + \
    "\nEnter \'y' for Yes or \'n' for No: "
    
question2 = "Is your birthday in Set 2? \n"+\
    " 2  3  6  7\n" + \
    "10 11 14 15\n" + \
    "18 19 22 23\n" + \
    "26 27 30 31\n" + \
    "\nEnter \'y' for Yes or \'n' for No: "

question3 = "Is your birthday in Set 3? \n"+\
    " 4  5  6  7\n" + \
    "12 13 14 15\n" + \
    "20 21 22 23\n" + \
    "28 29 30 31\n" + \
    "\nEnter \'y' for Yes or \'n' for No: "

question4 = "Is your birthday in Set 4? \n"+\
    " 8  9 10 11\n" + \
    "12 13 14 15\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31\n" + \
    "\nEnter \'y' for Yes or \'n' for No: "

question5 = "Is your birthday in Set 5? \n"+\
    "16 17 18 19\n" + \
    "20 21 22 23\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31\n" + \
    "\nEnter \'y' for Yes or \'n' for No: "

answer = input(question1)
if answer == 'y':
    day += 1

answer = input(question2)
if answer == 'y':
    day += 2

answer = input(question3)
if answer == 'y':
    day += 4

answer = input(question4)
if answer == 'y':
    day += 8

answer = input(question5)
if answer == 'y':
    day += 16

print("Your birthday is: ", day)



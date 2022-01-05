from tkinter import *

class BirthdayGuessing:
    def __init__(self):
        window = Tk()
        window.title("Birthday Guessing")

        self.day = 0

        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text = "Is your birthday in following set?", font=("Arial", 20))

        self.question1 = "\n"+\
        " 1   3   5   7\n" + \
        " 9  11  13  15\n" + \
        "17  19  21  23\n" + \
        "25  27  29  31\n"
        
        self.question2 = "\n"+\
        " 2   3   6   7\n" + \
        "10  11  14  15\n" + \
        "18  19  22  23\n" + \
        "26  27  30  31\n"

        self.question3 = "\n"+\
        " 4   5   6   7\n" + \
        "12  13  14  15\n" + \
        "20  21  22  23\n" + \
        "28  29  30  31\n"

        self.question4 = "\n"+\
        " 8   9  10  11\n" + \
        "12  13  14  15\n" + \
        "24  25  26  27\n" + \
        "28  29  30  31\n"

        self.question5 = "\n"+\
        "16  17  18  19\n" + \
        "20  21  22  23\n" + \
        "24  25  26  27\n" + \
        "28  29  30  31\n"

        frame2 = Frame(window)
        frame2.pack()
        self.lbl2 = Label(frame2, bg = "yellow", font=("Arial", 15), text = self.question1)

        frame3 = Frame(window, padx= 10, pady = 10)
        frame3.pack()


        rbYes = Button(frame3, text= "Yes", padx = 10, command= self.dayincre)
        rbNo = Button(frame3, text = "No", padx = 10, command= self.lblchange)


        self.lbl.pack(pady = 10, padx = 10)
        self.lbl2.grid(row = 0, columnspan= 3, column= 0)
        rbYes.grid(row = 0, column= 2)
        rbNo.grid(row = 0, column= 4)

        window.mainloop()

    def lblchange(self):
        if self.lbl2["text"] == self.question1:
            self.lbl2["text"] = self.question2
            return
        
        if self.lbl2["text"] == self.question2:
            self.lbl2["text"] = self.question3
            return
        
        if self.lbl2["text"] == self.question3:
            self.lbl2["text"] = self.question4
            return
        
        if self.lbl2["text"] == self.question4:
            self.lbl2["text"] = self.question5
            return
        
        if self.lbl2["text"] == self.question5:

            self.lbl2["text"] = ""
            self.lbl["text"] = "Your birthday is on " + str(self.day)
            return
    
    
    def dayincre(self):
        if self.lbl2["text"] == self.question1:
            self.lbl2["text"] = self.question2
            self.day += 1
            return
        
        if self.lbl2["text"] == self.question2:
            self.lbl2["text"] = self.question3
            self.day += 2
            return
        
        if self.lbl2["text"] == self.question3:
            self.lbl2["text"] = self.question4
            self.day += 4
            return
        
        if self.lbl2["text"] == self.question4:
            self.lbl2["text"] = self.question5
            self.day += 8
            return
        
        if self.lbl2["text"] == self.question5:
            self.day += 16

            self.lbl2["text"] = ""
            self.lbl["text"] = "Your birthday is on " + str(self.day)

            return
    


BirthdayGuessing()

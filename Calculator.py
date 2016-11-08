#Chiedu Nduka-Eze 11/8/16
#This program creates a claculator

import tkinter
root = tkinter.Tk()
root.title("Chiedu's masterpiece")

textbox = tkinter.StringVar()
textbox.set("")

#all these functions put a number at the end of the string and replaces it


def clickNine():
    """This functions puts 9 at the end of the string and replaces the string"""
    pie = textbox.get()
    pie += "9"
    textbox.set(pie)


def clickEight():
    pie = textbox.get()
    pie += "8"
    textbox.set(pie)


def clickSeven():
    pie = textbox.get()
    pie += "7"
    textbox.set(pie)


def clickSix():
    pie = textbox.get()
    pie += "6"
    textbox.set(pie)


def clickFive():
    pie = textbox.get()
    pie += "5"
    textbox.set(pie)


def clickFour():
    pie = textbox.get()
    pie += "4"
    textbox.set(pie)


def clickThree():
    pie = textbox.get()
    pie += "3"
    textbox.set(pie)


def clickTwo():
    pie = textbox.get()
    pie += "2"
    textbox.set(pie)


def clickOne():
    pie = textbox.get()
    pie += "1"
    textbox.set(pie)


def clickZero():
    pie = textbox.get()
    pie += "0"
    textbox.set(pie)


def clickMultiply():
    pie = textbox.get()
    pie += "*"
    textbox.set(pie)


def clickAdd():
    pie = textbox.get()
    pie += "+"
    textbox.set(pie)


def clickSubtract():
    pie = textbox.get()
    pie += "-"
    textbox.set(pie)


def clickDivide():
    pie = textbox.get()
    pie += "/"
    textbox.set(pie)


def clickDecimal():
    pie = textbox.get()
    pie += "."
    textbox.set(pie)


def clickNegative():
    pie = textbox.get()
    piee = eval(pie) * -1
    textbox.set(piee)



def Evaluate():
    pie = textbox.get()
    piee = eval(pie)
    textbox.set(piee)


def Clear():
    textbox.set("")




#These all put a button at a specific point in the calculator
numberNine = tkinter.Button(root, text="9", command=clickNine)
numberNine.grid(column=3, row=2)


numberOne= tkinter.Button(root, text = "1", command= clickOne)
numberOne.grid(column=1, row=4)

numberTwo= tkinter.Button(root, text = "2", command= clickTwo)
numberTwo.grid(column=2, row=4)

numberThree= tkinter.Button(root, text = "3", command= clickThree)
numberThree.grid(column=3, row=4)

numberFour= tkinter.Button(root, text = "4", command= clickFour)
numberFour.grid(column=1, row=3)

numberFive= tkinter.Button(root, text = "5", command= clickFive)
numberFive.grid(column=2, row=3)

numberSix= tkinter.Button(root, text = "6", command= clickSix)
numberSix.grid(column=3, row=3)

numberSeven= tkinter.Button(root, text = "7", command= clickSeven)
numberSeven.grid(column=1, row=2)

numberEight= tkinter.Button(root, text = "8", command= clickEight)
numberEight.grid(column=2, row=2)

numberMultiply= tkinter.Button(root, text = "*", command= clickMultiply)
numberMultiply.grid(column=4, row=4)

numberAdd= tkinter.Button(root, text = "+", command= clickAdd)
numberAdd.grid(column=4, row=2)

numberSubtract= tkinter.Button(root, text = "-", command= clickSubtract)
numberSubtract.grid(column=4, row=3)

numberDivide= tkinter.Button(root, text = "/", command= clickDivide)
numberDivide.grid(column=3, row=5)

numberDecimal= tkinter.Button(root, text = ".", command= clickDecimal)
numberDecimal.grid(column=2, row=5)

numberNegative= tkinter.Button(root, text = "-/+", command= clickNegative)
numberNegative.grid(column=1, row=5)

numberEqual= tkinter.Button(root, text = "Enter", command= Evaluate)
numberEqual.grid(column=4, row=5)

numberClear= tkinter.Button(root, text = "C", command= Clear)
numberClear.grid(column=4, row=1)

calcBox = tkinter.Entry(root,textvariable= textbox)
calcBox.grid(row=1, column=1, columnspan=3)

root.mainloop()
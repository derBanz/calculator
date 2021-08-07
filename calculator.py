"""
Set task: Build a calculator to handle the most simple mathematical operations.
Method:
* On __init__() the GUI is built consisting of textLabel at top where the expression (String) is displayed at all times as well as buttons below it for the different operations.
* The top row of buttons includes the resetButton to reset both expression with __reset__() and save (String), saveButton to equal save to expression with __save__() and the
recallButton to add save to expression with __saveRecall__().
* The equalButton triggers __evaluate__(), which uses the inbuilt eval() function to evaluate expression and updates the textLabel.
* All other buttons adds the respective number or operator to expression with __input__() and updates the textLabel.
"""

import tkinter as tk
from tkinter.font import Font

class Calculator:
    
    def __init__(self):
        self.expression = ""
        self.save = ""
        
        self.root = tk.Tk()
        self.root.resizable(False,False)
        self.root.title("Calculator")
        #self.root.pack(padx=250,pady=1)

        buttonFont = Font(family="Verdana",size=12)
        self.textLabel = tk.Label(self.root,text="",font="Verdana 12",background="white",foreground="black",width=24, height=2)
        self.textLabel.grid(row=0,column=0,columnspan=4)

        self.resetButton = tk.Button(self.root,text="Reset",font=buttonFont,command=self.__reset__,height=3,width=6)
        self.resetButton.grid(row=1,column=0)
        self.saveButton = tk.Button(self.root,text="M+",font=buttonFont,command=self.__save__,height=3,width=6)
        self.saveButton.grid(row=1,column=1)
        self.recallButton = tk.Button(self.root,text="M",font=buttonFont,command=self.__saveRecall__,height=3,width=6)
        self.recallButton.grid(row=1,column=2)
        self.divButton = tk.Button(self.root,text="÷",font=buttonFont,command=lambda: self.__input__("/"),height=3,width=6)
        self.divButton.grid(row=1,column=3)

        self.sevenButton = tk.Button(self.root,text="7",font=buttonFont,command=lambda: self.__input__("7"),height=3,width=6)
        self.sevenButton.grid(row=2,column=0)
        self.eightButton = tk.Button(self.root,text="8",font=buttonFont,command=lambda: self.__input__("8"),height=3,width=6)
        self.eightButton.grid(row=2,column=1)
        self.nineButton = tk.Button(self.root,text="9",font=buttonFont,command=lambda: self.__input__("9"),height=3,width=6)
        self.nineButton.grid(row=2,column=2)
        self.multButton = tk.Button(self.root,text="*",font=buttonFont,command=lambda: self.__input__("*"),height=3,width=6)
        self.multButton.grid(row=2,column=3)

        self.fourButton = tk.Button(self.root,text="4",font=buttonFont,command=lambda: self.__input__("4"),height=3,width=6)
        self.fourButton.grid(row=3,column=0)
        self.fiveButton = tk.Button(self.root,text="5",font=buttonFont,command=lambda: self.__input__("5"),height=3,width=6)
        self.fiveButton.grid(row=3,column=1)
        self.sixButton = tk.Button(self.root,text="6",font=buttonFont,command=lambda: self.__input__("6"),height=3,width=6)
        self.sixButton.grid(row=3,column=2)
        self.minusButton = tk.Button(self.root,text="-",font=buttonFont,command=lambda: self.__input__("-"),height=3,width=6)
        self.minusButton.grid(row=3,column=3)

        self.oneButton = tk.Button(self.root,text="1",font=buttonFont,command=lambda: self.__input__("1"),height=3,width=6)
        self.oneButton.grid(row=4,column=0)
        self.twoButton = tk.Button(self.root,text="2",font=buttonFont,command=lambda: self.__input__("2"),height=3,width=6)
        self.twoButton.grid(row=4,column=1)
        self.threeButton = tk.Button(self.root,text="3",font=buttonFont,command=lambda: self.__input__("3"),height=3,width=6)
        self.threeButton.grid(row=4,column=2)
        self.plusButton = tk.Button(self.root,text="+",font=buttonFont,command=lambda: self.__input__("+"),height=3,width=6)
        self.plusButton.grid(row=4,column=3)

        self.zeroButton = tk.Button(self.root,text="0",font=buttonFont,command=lambda: self.__input__("0"),height=3,width=6)
        self.zeroButton.grid(row=5,column=0)
        self.decButton = tk.Button(self.root,text=".",font=buttonFont,command=lambda: self.__input__("."),height=3,width=6)
        self.decButton.grid(row=5,column=1)
        self.equalButton = tk.Button(self.root,text="=",font=buttonFont,command=lambda: self.__evaluate__(),height=3,width=12)
        self.equalButton.grid(row=5,column=2,columnspan=2)

        self.root.mainloop()

    def __evaluate__(self):
        self.expression = str(eval(self.expression))
        self.textLabel.configure(text=self.expression)

    def __input__(self,val):
        self.expression += val
        self.textLabel.configure(text=self.expression)

    def __save__(self):
        self.save = self.expression
    
    def __saveRecall__(self):
        self.expression += self.save
        self.textLabel.configure(text=self.expression)
    
    def __reset__(self):
        self.expression = ""
        self.save = ""
        self.textLabel.configure(text=self.expression)

C = Calculator()
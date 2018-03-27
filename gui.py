# gui example
# create simple calculator

from tkinter import *


class SimpleCalculator(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.btn0 = Button(self, text="+")
        self.btn1 = Button(self, text="-")
        self.btn2 = Button(self, text="*")
        self.btn3 = Button(self, text="/")
        self.btn4 = Button(self, text="=", command=self.on_button)
        self.btn5 = Button(self, text="C")
        self.field = Entry(self)
        self.string_var = StringVar()
        self.status_bar = Label(self, textvariable=self.string_var)
        self.string_var.set("The result of the operation will appear here")

        self.field.pack(side=TOP)
        self.status_bar.pack(side=BOTTOM)
        self.btn0.pack(side=LEFT)
        self.btn1.pack(side=LEFT)
        self.btn2.pack(side=LEFT)
        self.btn3.pack(side=LEFT)
        self.btn4.pack(side=LEFT)
        self.btn5.pack(side=LEFT)

        self.resizable(width=False, height=False)
        self.title("Calculator")

    def on_button(self):
        self.string_var.set("You typed: " + self.field.get())


calculatorApp = SimpleCalculator()
calculatorApp.mainloop()


# main_window.resizable(width=False, height=False)

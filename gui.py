# gui example
# create simple calculator

from tkinter import *


class SimpleCalculator(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.input_field = Entry(self)
        # self.btn0 = Button(self, text="0")
        # self.btn1 = Button(self, text="1")
        # self.btn2 = Button(self, text="2")
        # self.btn3 = Button(self, text="3")
        # self.btn4 = Button(self, text="4")
        # self.btn5 = Button(self, text="5")
        # self.btn6 = Button(self, text="6")
        # self.btn7 = Button(self, text="7")
        # self.btn8 = Button(self, text="8")
        # self.btn9 = Button(self, text="9")



        # self.string_var = StringVar()
        # self.status_bar = Label(self, textvariable=self.string_var)
        # self.string_var.set("The result of the operation will appear here")

        self.input_field.grid(row=0, column=0, columnspan=3)
        # self.status_bar.pack(side=BOTTOM)
        # self.btn0.grid(side=LEFT)
        # self.btn1.pack(side=LEFT)
        # self.btn2.pack(side=LEFT)
        # self.btn3.pack(side=LEFT)
        # self.btn4.pack(side=LEFT)
        # self.btn5.pack(side=LEFT)
        #
        # self.resizable(width=False, height=False)
        # self.title("Simple calculator")

    def on_button(self):
        self.string_var.set("You typed: " + self.field.get())


calculatorApp = SimpleCalculator()
calculatorApp.mainloop()


# main_window.resizable(width=False, height=False)

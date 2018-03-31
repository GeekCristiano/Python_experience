# gui example
# create simple calculator

from tkinter import *


class SimpleCalculator(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.input_field = Entry(self, )
        self.btn0 = Button(self, text="0")
        self.btn1 = Button(self, text="1")
        self.btn2 = Button(self, text="2")
        self.btn3 = Button(self, text="3")
        self.btn4 = Button(self, text="4")
        self.btn5 = Button(self, text="5")
        self.btn6 = Button(self, text="6")
        self.btn7 = Button(self, text="7")
        self.btn8 = Button(self, text="8")
        self.btn9 = Button(self, text="9")
        self.btn_clean = Button(self, text="C")
        self.btn_equal = Button(self, text="=", command=self.get_input_text)
        self.btn_pl = Button(self, text="+")
        self.btn_ms = Button(self, text="-")
        self.btn_mul = Button(self, text="*")
        self.btn_div = Button(self, text="/")
        self.string_var = StringVar()
        self.status_bar = Label(self, textvariable=self.string_var)
        self.string_var.set("Result:")

        self.input_field.grid(row=0, columnspan=4)

        self.btn0.grid(row=1, column=0)
        self.btn1.grid(row=1, column=1)
        self.btn2.grid(row=1, column=2)
        self.btn3.grid(row=1, column=3)
        self.btn4.grid(row=2, column=0)
        self.btn5.grid(row=2, column=1)
        self.btn6.grid(row=2, column=2)
        self.btn7.grid(row=2, column=3)
        self.btn8.grid(row=3, column=0)
        self.btn9.grid(row=3, column=1)
        self.btn_clean.grid(row=3, column=2)
        self.btn_equal.grid(row=3, column=3)
        self.btn_pl.grid(row=4, column=0)
        self.btn_ms.grid(row=4, column=1)
        self.btn_mul.grid(row=4, column=2)
        self.btn_div.grid(row=4, column=3)

        self.status_bar.grid(row=5, columnspan=4)

        self.title("Simple calculator")
        self.resizable(width=False, height=False)
        self.grid_rowconfigure(0, pad=5)
        self.grid_rowconfigure(1, pad=5)
        self.grid_rowconfigure(2, pad=5)
        self.grid_rowconfigure(3, pad=5)

    def get_input_text(self):
        print("Input text is:" + self.input_field.get())


def main():
    calculatorApp = SimpleCalculator()
    calculatorApp.mainloop()


if __name__ == "__main__":
    main()

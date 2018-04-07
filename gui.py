# gui example
# create simple calculator

from tkinter import *


class SimpleCalculator(Tk):
    def __init__(self):
        Tk.__init__(self)

        vcmd = self.register(self.onValidate)
        self.input_field = Entry(self, validate="key", validatecommand=(vcmd, '%S'))

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
        self.btn_equal = Button(self, text="=", command=self.get_result)
        self.btn_pl = Button(self, text="+")
        self.btn_ms = Button(self, text="-")
        self.btn_mul = Button(self, text="*")
        self.btn_div = Button(self, text="/")
        self.string_var = StringVar()
        self.status_bar = Label(self, textvariable=self.string_var)
        self.string_var.set("Result:")

        self.btn_pl.bind("<Button-1>", self.update_input_field)
        self.btn_ms.bind("<Button-1>", self.update_input_field)
        self.btn_mul.bind("<Button-1>", self.update_input_field)
        self.btn_div.bind("<Button-1>", self.update_input_field)

        self.btn0.bind("<Button-1>", self.update_input_field)
        self.btn1.bind("<Button-1>", self.update_input_field)
        self.btn2.bind("<Button-1>", self.update_input_field)
        self.btn3.bind("<Button-1>", self.update_input_field)
        self.btn4.bind("<Button-1>", self.update_input_field)
        self.btn5.bind("<Button-1>", self.update_input_field)
        self.btn6.bind("<Button-1>", self.update_input_field)
        self.btn7.bind("<Button-1>", self.update_input_field)
        self.btn8.bind("<Button-1>", self.update_input_field)
        self.btn9.bind("<Button-1>", self.update_input_field)
        self.btn_clean.bind("<Button-1>", self.delete_last_symbol)

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

    def get_result(self):
        current_value = self.input_field.get()

        if "+" in current_value:
            right_operand, left_operand = current_value.split(sep="+")
            result = "{:.2f}".format(float(right_operand) + float(left_operand))
        elif "-" in current_value:
            right_operand, left_operand = current_value.split(sep="-")
            result = "{:.2f}".format(float(right_operand) - float(left_operand))
        elif "*" in current_value:
            right_operand, left_operand = current_value.split(sep="*")
            result = "{:.2f}".format(float(right_operand) * float(left_operand))
        elif "/" in current_value:
            right_operand, left_operand = current_value.split(sep="/")
            result = "{:.2f}".format(float(right_operand) / float(left_operand))
        self.input_field.delete(0, END)
        self.input_field.insert(0, result)

    def delete_last_symbol(self, event):
        current_value = self.input_field.get()
        self.input_field.delete(0, END)
        self.input_field.insert(0, current_value[:-1])

    def update_input_field(self, event):
        current_value = self.input_field.get()
        control_element_text = event.widget["text"]
        if control_element_text == current_value[-1:] and control_element_text in "+-/*":
            self.bell()
            return
        self.input_field.delete(0, END)
        self.input_field.insert(0, current_value + control_element_text)

    def onValidate(self, S):
        correct_char_num = 0
        for char in S:
            if char in "0123456789.*/+-":
                correct_char_num += 1

        if correct_char_num == len(S):
            return True
        else:
            self.bell()
            return False


def main():
    calculatorApp = SimpleCalculator()
    calculatorApp.mainloop()


if __name__ == "__main__":
    main()

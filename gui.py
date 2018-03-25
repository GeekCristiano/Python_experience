# gui example
# create simple calculator

from tkinter import *


def main():
    main_window = Tk()
    btn0 = Button(main_window, text=0)
    btn1 = Button(main_window, text=1)
    btn2 = Button(main_window, text=2)
    btn3 = Button(main_window, text=3)
    btn4 = Button(main_window, text=4)
    btn5 = Button(main_window, text=5)
    btn6 = Button(main_window, text=6)
    btn7 = Button(main_window, text=7)
    btn8 = Button(main_window, text=8)
    btn9 = Button(main_window, text=9)
    btn_del = Button(main_window, text="c")
    btn_point = Button(main_window, text=" ,")

    btn0.grid(row=0, column=0, ipadx=10, ipady=10)
    btn1.grid(row=0, column=1, ipadx=10, ipady=10)
    btn2.grid(row=0, column=2, ipadx=10, ipady=10)
    btn3.grid(row=1, column=0, ipadx=10, ipady=10)
    btn4.grid(row=1, column=1, ipadx=10, ipady=10)
    btn5.grid(row=1, column=2, ipadx=10, ipady=10)
    btn6.grid(row=2, column=0, ipadx=10, ipady=10)
    btn7.grid(row=2, column=1, ipadx=10, ipady=10)
    btn8.grid(row=2, column=2, ipadx=10, ipady=10)
    btn9.grid(row=3, column=0, ipadx=10, ipady=10)
    btn_del.grid(row=3, column=1, ipadx=10, ipady=10)
    btn_point.grid(row=3, column=2, ipadx=10, ipady=10)
    # main_window.resizable(width=False, height=False)
    main_window.mainloop()


if __name__ == "__main__":
    main()

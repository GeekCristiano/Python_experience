# gui example
# create simple calculator

from tkinter import *


def main():
    main_window = Tk()
    btn0 = Button(main_window, text="+")
    btn1 = Button(main_window, text="-")
    btn2 = Button(main_window, text="*")
    btn3 = Button(main_window, text="/")
    btn4 = Button(main_window, text="=")
    btn5 = Button(main_window, text="C")
    field = Entry(main_window)
    string_var = StringVar()
    status_bar = Label(main_window, textvariable=string_var)
    string_var.set("The result of the operation will appear here")

    field.pack(side=TOP)
    status_bar.pack(side=BOTTOM)
    btn0.pack(side=LEFT)
    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT)
    btn4.pack(side=LEFT)
    btn5.pack(side=LEFT)

    # main_window.resizable(width=False, height=False)
    main_window.mainloop()


if __name__ == "__main__":
    main()

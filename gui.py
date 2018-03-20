# gui example

from tkinter import *


def main():
    main_window = Tk()
    text = StringVar()
    label = Label(main_window, textvariable=text)
    text.set("Hello, world!")
    label.pack()
    main_window.resizable(width=False, height=False)
    main_window.mainloop()


if __name__ == "__main__":
    main()

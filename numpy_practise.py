import matplotlib.pyplot as plt
import numpy as np


def square(x):
    return x * x


def main():
    x = np.linspace(0, 11, 100)
    y = square(x)
    plt.plot(x, y, "r")
    plt.plot(-x, y, 'b')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Square of a number")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()

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
    plt.title("$f(x)=x^2$")
    plt.grid()
    plt.xlim(-11, 11)
    plt.ylim(0, 121)
    plt.show()


if __name__ == "__main__":
    main()

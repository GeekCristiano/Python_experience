import matplotlib.pyplot as plt
import numpy as np


def square(x):
    return x * x


def d2plot():
    x = np.linspace(0, 11, 100)
    y = square(x)
    print("numpy.size", x.size)
    print("numpy.shape", x.shape)
    print("numpy.itemsize", x.itemsize)
    print("numpy.ndim", x.ndim)
    plt.plot(x, y, "r")
    plt.plot(-x, y, 'b')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("$f(x)=x^2$")
    plt.grid()
    plt.xlim(-11, 11)
    plt.ylim(0, 121)
    plt.show()


def main():
    d2plot()


if __name__ == "__main__":
    main()

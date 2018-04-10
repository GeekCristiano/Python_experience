import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def square(x):
    return x * x


def d3plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    phi = np.arange(0, 2 * np.pi, np.pi/1000)
    th = np.arange(0, np.pi, np.pi/1000)
    r = 3

    phiGrid, thGrid = np.meshgrid(phi, th)

    x = r * np.sin(thGrid) * np.cos(phiGrid)
    y = r * np.sin(thGrid) * np.sin(phiGrid)
    z = r * np.cos(thGrid)

    ax.plot_surface(x, y, z,cmap="inferno")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.set_title("It's sphere")
    plt.show()


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
    # d2plot()
    d3plot()


if __name__ == "__main__":
    main()

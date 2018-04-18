import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import matplotlib.animation as animation


def square(x):
    return x * x


def plot_sphere():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    phi = np.arange(0, 2 * np.pi, np.pi / 1000)
    th = np.arange(0, np.pi, np.pi / 1000)
    r = 3

    phiGrid, thGrid = np.meshgrid(phi, th)

    x = r * np.sin(thGrid) * np.cos(phiGrid)
    y = r * np.sin(thGrid) * np.sin(phiGrid)
    z = r * np.cos(thGrid)

    ax.plot_surface(x, y, z, cmap="inferno")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.set_title("It's sphere")

    m = cm.ScalarMappable(cmap=cm.jet)
    m.set_array(z)
    plt.colorbar(m)

    plt.show()


def plot_parabola():
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


def plot_many_lines():
    x = np.arange(-2 * np.pi, 2 * np.pi, np.pi / 10)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.figure(1)
    plt.subplot(211)
    line = plt.plot(x, y1)
    plt.setp(line, color='r', linewidth=2.0, marker=".", ms='8')
    plt.title("$sin(x)$")
    l2= plt.subplot(212)
    # add title for second subplot
    l2.set_title("$cos(x)$")
    # set style with third argument of plot function or using setp method
    plt.plot(x, y2, "--b+")
    plt.show()


def animated_line():
    fig, ax = plt.subplots()

    x = np.arange(0, 2 * np.pi, 0.01)
    line = ax.plot(x, np.sin(x))

    ani = animation.FuncAnimation(fig, lambda i: line.set_ydata(np.sin(x + i / 10.0)), np.arange(1, 200),
                                  interval=25, blit=True)

    plt.title("animation line")
    plt.show()


def main():
    plot_many_lines()
    # plot_parabola()
    # plot_sphere()
    # animated_line()


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt

def plot(x, y, title):
    plt.plot(x, y)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title(title)

    plt.show()
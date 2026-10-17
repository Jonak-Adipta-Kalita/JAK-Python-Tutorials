import numpy as np


def save():
    data = np.random.choice([10, 20, 30, 40, 50, 60], size=(4, 5, 6))
    print("With Random Values of Choice:\n", data, end="\n\n")

    np.save("random_array.npy", data)


def load():
    arr = np.load("random_array.npy")
    print(arr)


if int(input("Save (0) or Load (1) >> ")) == 0:
    save()
else:
    load()

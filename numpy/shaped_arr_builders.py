import numpy as np

shape = [int(i) for i in input(
    "Enter Shape (write the numbers with no space & no bracket group): ").strip().split()]
print()

a = np.full(shape, 9)
print("Full:\n", a, end="\n\n")

b = np.zeros(shape)
print("Zeros:\n", b, end="\n\n")

c = np.ones(shape)
print("Ones:\n", c, end="\n\n")

d = np.empty(shape)  # Allocates Space
print("Empty (Allocates Space):\n", d, end="\n\n")

with_random = np.random.randint(0, 100, size=shape)
print("With Random Values:\n", with_random, end="\n\n")

with_random_choice = np.random.choice([10, 20, 30, 40, 50, 60], size=shape)
print("With Random Values of Choice:\n", with_random_choice, end="\n\n")

# And... a lot of the other random_module functions

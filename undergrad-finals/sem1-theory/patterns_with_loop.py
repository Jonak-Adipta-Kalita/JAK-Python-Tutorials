n = int(input())

# Pattern 1
for i in range(1, n+1):
    for j in range(i):
        print(i ** 2, end=" ")
    print()

print()

# Pattern 2
counter = 1
for i in range(1, n+1):
    for _ in range(i):
        print(counter, end=" ")
        counter += 1
    print()

print()

# Pattern 3
for i in range(1, n+1):
    spaces = n - i
    print(" " * spaces + (str(i) + " ") * i + " " * (spaces - 1))

print()

# Pattern 4
for i in range(0, n):
    nums = list(range(1, n+1))
    shifted = [str(nums[(i + j) % len(nums)]) for j in range(len(nums))]
    print(" ".join(shifted))

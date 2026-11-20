# Q1 - Smallest Missing Positive Number
n = int(input())
numbers = [int(i) for i in input().strip().split(" ")]

for i in range(1, n+1):
    if i not in numbers:
        print(i)
        break
else:
    print(i + 1)

# Q2 - Plant IDs Sorted by Height
n = int(input())
valid = True
ids = []
pairs = []

for i in range(n):
    id_ = int(input())
    if id_ in ids:
        print("Invalid input")
        valid = False
        break

    ids.append(id_)

    height = int(input())
    pair = (height, id_)

    pairs.append(pair)

if valid:
    pairs.sort()
    sorted_ids = [p[1] for p in pairs]
    print(sorted_ids)

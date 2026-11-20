# Q1 - Flattening a 2D Array
import numpy as np

rows = int(input())
cols = int(input())

array = []

for i in range(rows):
    array.append([int(i) for i in input().strip().split(" ")])

array = np.array(array)

print(f"Array:\n{array}")
print(f"Shape: {array.shape}")
print(f"Flatten (row-major): {array.flatten()}")
print(f"Ravel: {array.ravel()}")
print(f"Flatten (column-major): {array.flatten('F')}")
print(f"Flattened Size: {array.flatten().size}")

# Q2 - Railway Seat Booking
n = int(input())
seats = {seat: "Available" for seat in input().split()}

for i in range(int(input())):
    action, seat = input().split()

    if action == "BOOK" and seats[seat] == "Available":
        seats[seat] = "Booked"
    elif action == "CANCEL" and seats[seat] == "Booked":
        seats[seat] = "Available"

for seat in sorted(seats):
    print(f"{seat}: {seats[seat]}")

booked = list(seats.values()).count("Booked")

print(f"Total Booked: {booked}")
print(f"Total Available: {len(seats) - booked}")

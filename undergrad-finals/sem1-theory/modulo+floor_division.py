# Convert 100000 seconds to days, hours, minutes and seconds.
hours_mins_and_sec = 100000

hours = hours_mins_and_sec // 3600
mins_and_sec = hours_mins_and_sec % 3600

mins = mins_and_sec // 60
secs = mins_and_sec % 60

print(f"Hours: {hours}, Minutes: {mins}, Seconds: {secs}")

# Given ₹2750, find the minimum number of ₹500, ₹100, ₹50, ₹10 notes
amount = 2750

n500 = amount // 500
amount = amount % 500

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n10 = amount // 10
amount = amount % 10

print("500:", n500, "100:", n100, "50:", n50, "10:", n10, "left:", amount)

# Read a n-digit number and print the sum of its digits
number = 1012335
digits = []

while number > 0:
    digit = number % 10
    digits.append(digit)
    number //= 10

print(sum(digits))

# Today is Tuesday (day 2, with Sunday = 0). What day is it after 100 days?
days = 100 + 2

weeks = days // 7
remaining_days = days % 7

print(remaining_days)

# Cyclic Shifting
seq = [10, 20, 30, 40, 50, 60]
n = len(seq)
k = 2

shifted = [seq[(i + k) % n] for i in range(n)]
print(shifted)

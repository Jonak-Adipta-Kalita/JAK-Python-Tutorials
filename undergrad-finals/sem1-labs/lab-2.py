# Q1 - Order of Evaluation
a, b, c = [int(i) for i in input().split()]

with_order = (a * b) + (c // (a + b)) - (a % c)
without_order = a * b + c // a + b - a % c

print(f"With order of evaluation: {with_order}")
print(f"Without order of evaluation: {without_order}")

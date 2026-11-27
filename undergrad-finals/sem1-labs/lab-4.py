# Q1 - Factorial Calculator
n = int(input())
i = 1
f = 1

while i < n:
    i += 1
    f *= i

print(f"The factorial of {n} is: {f}")

# Q2 - Factorial Digit Sum
print(f)  # Calculated Earlier
print(sum([int(i) for i in list(str(f))]))

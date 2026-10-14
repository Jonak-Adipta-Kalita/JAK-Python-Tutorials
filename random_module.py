import random
random.seed(70)

print(random.random())  # Returns a Float 0 <= N < 1
print(5 + random.random() * (8 - 5))  # Returns a Float 5 <= N < 8

print(random.randint(69, 420))  # Returns 69 <= N <= 420

# Returns 69 <= N <= 420 but, consecutive possible selections will differ by 2
print(random.randrange(69, 420, 2))

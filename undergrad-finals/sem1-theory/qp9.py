def factorial(n: int) -> int:
    if n == 0:
        return 1

    return n * factorial(n - 1)


n = int(input())
r = int(input())

facto_ = factorial(n)
permutations = facto_ / factorial(n - r)

print(facto_)
print(permutations)

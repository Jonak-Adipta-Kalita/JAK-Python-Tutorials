# Q1 - Score Analyzer
scores = [int(i) for i in input().split()]
threshold = int(input())

percentages = [s * 100 / 50 for s in scores]
passing = [p for p in percentages if p >= threshold]

print("Original Scores:", *scores)
print("Percentage Scores:", *[f"{p:.2f}" for p in percentages])
print("Passing Scores:", *[f"{p:.2f}" for p in passing])

# Q2 - Print Until a Digit
s = input()
result = ""

for c in s:
    if c.isdigit():
        break
    result += c

print(result)

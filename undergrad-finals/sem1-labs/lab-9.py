# Q1 - Word Count Using a File
sentence = input()

with open("sentence_file.txt", "w") as file:
    file.write(sentence)

with open("sentence_file.txt", "r") as file:
    saved = file.read()

print(len(saved.split()))

# Q2 - Palindrome Check Using a File
word = input()

with open("word_file.txt", "w") as file:
    file.write(word)

with open("word_file.txt", "r") as file:
    saved = file.read().strip().lower()

if saved == saved[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")

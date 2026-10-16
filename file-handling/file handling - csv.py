import csv

l = []
with open("pre-boards 1/musicians.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")

    for i in reader:
        if i != []:
            l.append(i)

print(l)

with open("pre-boards 1/musicians.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")

    writer.writerows(l)

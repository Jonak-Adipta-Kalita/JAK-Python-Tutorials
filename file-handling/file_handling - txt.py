# READing from File
def q7p24_COUNTAE():
    with open("WRITER.TXT", "r") as f:
        for i in f.readlines():
            i = str(i).upper()
            if i[0] in ["A", "E"]:
                print(i.rstrip("\n"))


def q1p24():
    counter = 0

    with open("WRITER.TXT", "r") as f:
        for i in f.read():
            if i.lower() == "a":
                counter += 1

    print(counter)


def q2p24():
    with open("WRITER.TXT", "r") as f:
        print(f.read().replace("E", "I"))


def q6p24():
    inclusion = ["IS", "UP", "TO"]
    counter = 0
    with open("WRITER.TXT", "r") as f:
        for i in f.read().split():
            if i in inclusion:
                counter += 1

    print(counter)


q1p24()
print()
q2p24()
print()
q6p24()
print()
q7p24_COUNTAE()

# WRITEing in File
with open("WRITER.TXT", "a") as f:
    f.write("blah blah - appended")

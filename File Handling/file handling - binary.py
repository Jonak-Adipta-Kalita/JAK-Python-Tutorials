import pickle

# with open("pre-boards 1/fuck you.dat", "wb") as f:
#     dat = {"bro": "idk", "meow": "meow", 123: 3235, "hellow": "world?"}
#     pickle.dump(dat, f)

# with open("pre-boards 1/fuck you.dat", "rb") as f:
#     print(pickle.load(f))


class FileHandlingBinary:
    def __init__(self):
        self.file_name = "pre-boards 1/employee.dat"

    def add_record(self, name: str, id: str):
        with open(self.file_name, "ab") as f:
            employee = {"name": name, "id": id}
            pickle.dump(employee, f)

    def add_employees(self):
        while True:
            y = str(input("Continue? (y/n)"))

            if y.lower() != "y":
                break

            self.add_record(str(input("Enter Name: ")), str(input("Enter ID: ")))

    def get_employees(self, i: int):
        try:
            l = 0
            with open(self.file_name, "rb") as f:
                for _ in range(i):
                    l += 1
                    print(pickle.load(f))
        except EOFError:
            print(f"Items found: {l-1}")

    def search_employee_id(self, id_: int):
        with open(self.file_name, "rb") as f:
            try:
                while True:
                    record = pickle.load(f)
                    if record["id"] == str(id_):
                        return True
            except EOFError:
                return False

    def update_employee_id(self, old: int, new: int):
        if len(str(old)) != len(str(new)):
            raise Exception("Different Sizes")

        with open(self.file_name, "rb+") as f:
            try:
                while True:
                    pos = f.tell()
                    data = pickle.load(f)

                    if data["id"] == str(old):
                        f.seek(pos)
                        data["id"] = str(new)
                        pickle.dump(data, f)

                        return True
            except EOFError:
                return False


f = FileHandlingBinary()
# f.add_employees()
f.get_employees(5)
# print("Found" if f.search_employee_id(12312) else "Nop")
print("Updated!" if f.update_employee_id(12312, 97879) else "Nop Not Found")
f.get_employees(5)

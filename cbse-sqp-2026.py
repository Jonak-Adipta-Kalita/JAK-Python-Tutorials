# q23
import mysql.connector as mys
import csv
import pickle


def remove_first_last(str):
    if len(str) < 2:
        return str
    new_str = str[1:-2]
    return new_str


result = remove_first_last("Hello")
print("Resulting string:", result)


# q24
review = "good day sir, how are you?"
index = review.find("good")

list_ = []
reversed(list_.sort())
list_.sort(reverse=True)

# or
("Learn Python", "with", "fun and practice")
3


# q25
def remove_element(L: list, n: int):
    try:
        L.remove(n)
    except ValueError:
        print("Element not found")


# or
def add_contacts(phone_book, name, number):
    if phone_book.get(name) is not None:
        return print("Contact already exists")

    phone_book[name] = number


# q26
["Arv", "Ria"]


# q29
def q29():
    with open("Prog.txt", "r") as f:
        content = f.read()

        content.count("Python")


def q29_or():
    with open("STORIES.txt", "r") as f:
        content = f.readlines()

        for i in content:
            if i.lower()[0] in ("aeiou"):
                print(i)


# q30
L = [("Laptop", 90000), ("Mobile", 30000), ("Pen", 50), ("Headphones", 1500)]

Product = []
top = 0


def Push_element(name, price):
    global top

    if (price <= 50):
        return

    Product.append((name, price))
    top += 1


for i in L:
    Push_element(i[0], i[1])

print(Product)


def Pop_element():
    if len(Product) > 0:
        return Product.pop()

    return "Stack Empty"


print(Pop_element())
print(Pop_element())
print(Pop_element())
print(Pop_element())


# q33
def Accept(id_, name, q_sold, unit_price):
    with open("Sales.csv", "a") as f:
        writer = csv.writer(f, delimiter=", ")
        writer.writerow([id_, name, q_sold, unit_price])


def CalculateTotalSales():
    total_sales = 0
    with open("Sales.csv", "r") as f:
        reader = csv.reader(f, delimiter=", ")
        for i in reader:
            total_sales += int(i[2]) * float(i[3])

    return total_sales


# q35
conn = mys.connect(host="localhost", username="admin_user",
                   password="warehouse2024", database="WarehouseDB")
cursor = conn.cursor()

cursor.execute(
    "UPDATE product_inventory SET Quantity = 91 WHERE Item_code = 208;")
conn.commit()

cursor.close()
conn.close()


# q36
def Add_Data(Employee_ID, Employee_Name, Department, Salary):
    with open("employee.dat", "ab") as f:
        data = {"Employee_ID": Employee_ID, "Employee_Name": Employee_Name,
                "Department": Department, "Salary": Salary}
        pickle.dump(data, f)


def Updating_Data():
    data = []

    with open("employee.dat", "rb") as f:
        try:
            while True:
                curr_data = pickle.load(f)
                data.append(curr_data)
        except EOFError:
            pass

    processed_data = []
    for i in data:
        if i[2] == "IT":
            i[3] = 200000
        processed_data.append(i)

    with open("employee.dat", "wb") as f:
        for i in processed_data:
            pickle.dump(i, f)

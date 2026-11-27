family_tree = [{
    "name": "Anil",
    "relationship": "father",
    "dob": "1980-05-15",
    "children": [
        {
            "name": "Arjun",
            "relationship": "Son",
            "dob": "2008-12-10",
            "children": []
        },
        {
            "name": "Ananya",
            "relationship": "Daughter",
            "dob": "2012-03-20",
            "children": []
        }
    ]
}]


def count_attendees(family_tree: list[dict]) -> int:
    count = 0

    for i in family_tree:
        count += 1
        count += count_attendees(i["children"])

    return count


def calculate_age(dob: str) -> int:
    year = int(dob.split("-")[0])
    month = int(dob.split("-")[1])
    day = int(dob.split("-")[2])

    current_year = 2026
    current_month = 11
    current_day = 26

    age = current_year - year
    if month > current_month or (month == current_month and day > current_day):
        age -= 1

    return age


def book_logistics(guests: int) -> int:
    tables = guests // 6

    if guests % 6 > 0:
        tables += 1

    return tables

# Leaving the printing ;-;

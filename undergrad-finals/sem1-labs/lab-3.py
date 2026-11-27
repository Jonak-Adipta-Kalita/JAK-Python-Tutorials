# Q1 - Smart Home Commands
allowed = ["LightsOn", "LightsOff", "FanOn", "FanOff", "Status"]

for n in range(int(input())):
    if (i := input()) in allowed:
        print(i)
    else:
        print("Invalid Command")


# Q2 - Seasonal Vacation Packages
for i in range(int(input())):
    n = int(input())

    if 1 <= n <= 3:
        print("Winter Getaways")
    elif 4 <= n <= 6:
        print("Spring Holidays")
    elif 7 <= n <= 9:
        print("Summer Escapes")
    elif 10 <= n <= 12:
        print("Holiday Adventures")

T = int(input())

readings = 0
r = []
sensors = set()

with open("readings.txt", "r") as f:
    for i in f.readlines():
        readings += 1
        if float(i.split(",")[1]) > T:
            r.append(i)
            sensors.add(i.split(",")[0])

print(f"Total readings={readings}")

if len(r) == 0:
    print("No alerts")
else:
    print(f"Alerts={len(r)}")

with open("alerts.txt", "w") as f:
    f.writelines(r)

print(f"Sensors={list(sensors)}")

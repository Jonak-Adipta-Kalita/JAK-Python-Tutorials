# Question Paper's 4's b

d = float(input("Enter distance in km: "))

if d > 15:
    fare = 120 + (d - 15) * 6
elif d > 5:
    fare = 40 + (d - 5) * 8
else:
    fare = 40

print(f"Fare = ₹{fare:.2f}")

your_pin=int(input("Enter your pin:"))
print("Pin registered!")

pin=int(input("Enter the pin to access:"))
while pin!=your_pin:
    print("Access Denied!")
    break
if pin==your_pin:
    print("You are in !")
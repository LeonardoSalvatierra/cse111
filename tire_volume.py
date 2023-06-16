
import math
import time
from datetime import datetime

width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi*(width**2)*ratio*((width * ratio)+(2540 * diameter)))/(10000000000)

print(f"The approximate volume is {round(volume,2)} liters")

want_buy = input("do you want to buy tires with the dimensions you entered? (yes/no): ")

current_date = datetime.now()

if want_buy == "yes":
    phone_number = input("What's your phone number?: ")
    with open("volumes.txt", "at") as volumes_text:
        print(f"{current_date:%Y-%m-%d}, {phone_number}, {width}, {ratio}, {diameter}, {round(volume,2)}", file=volumes_text)
else:
    with open("volumes.txt", "at") as volumes_text:
        print(f"{current_date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {round(volume,2)}", file=volumes_text)
time.sleep(8)
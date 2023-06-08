
import math
import time

items = int(input("Enter the number of items:"))
items_box = int(input("Enter the number of items per box:"))

num_box= math.ceil(items/items_box)

print(f"For {items} items, packing {items_box} items in each box, you will need {num_box} boxes.")

time.sleep(8)
order = [
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]
 # NEW CODE HERE

item =input("What is the item that you want to purchase? ")

# 3. Check if the customer typed a number
# NEW CODE HERE
if item.isdigit():
    number = int(item)
    print(f"Input '{number}' is a number!")
else:
    print(f"{item} is not a number.")


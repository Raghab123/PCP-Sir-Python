"""
Build a dictionary where the keys are product names and the values are their prices. Implement options to:
a. Add a new product
b. Update price of an existing product
c. Find products within a given price range
"""


products = {}

while True:
    print("\n1) Add  2) Update  3) Range  4) Show  5) Exit")
    ch = input("Choice: ")

    if ch == "1":                       # add
        name  = input("Product name: ")
        price = float(input("Price: "))     # straight cast
        products[name] = price
        print("Added.")

    elif ch == "2":                     # update
        name = input("Product to update: ")
        if name in products:
            products[name] = float(input("New price: "))
            print("Updated.")
        else:
            print("Not found.")

    elif ch == "3":                     # range
        low  = float(input("Min price: "))
        high = float(input("Max price: "))
        for n, p in products.items():
            if low <= p <= high:
                print(n, p)

    elif ch == "4":                     # show all
        for n, p in products.items():
            print(n, p)

    elif ch == "5":                     # exit
        break

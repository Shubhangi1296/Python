inventory = {}

def add_product(name, quantity):
    inventory[name] = quantity
    print(name, "added.")

def update_product(name, quantity):
    if name in inventory:
        inventory[name] = quantity
        print(name, "updated.")
    else:
        print("Product not found.")

def remove_product(name):
    if name in inventory and inventory[name] == 0:
        del inventory[name]
        print(name, "removed.")
    else:
        print("Product cannot be removed.")

def highest_stock():
    if inventory:
        product = max(inventory, key=inventory.get)
        print("Highest stock:", product, inventory[product])
    else:
        print("Inventory is empty.")

add_product("Pen", 50)
add_product("Book", 30)
add_product("Bag", 10)

update_product("Book", 60)

highest_stock()

inventory["Bag"] = 0
remove_product("Bag")

print("Inventory:", inventory)
print("Total unique products:", len(inventory))
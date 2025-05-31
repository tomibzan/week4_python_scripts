
# Welcome message
print("Tom's Coffee Shop Drinks")
print("------------------------")

# Drink selection
i = 1
for d in drinks:
    print(i, d)
    i += 1
drink_choice = input("Choose your drink: ")

print("\nTom's Coffee Shop Flavors")
print("------------------------")

# Flavor selection
i = 1
for f in flavors:
    print(i, f)
    i += 1
flavor_choice = input("Choose your flavor: ")

print("\nTom's Coffee Shop Toppings")
print("--------------------------")

# Topping selection
i = 1
for t in toppings:
    print(i, t)
    i += 1
topping_choice = input("Choose your topping: ")

# Confirm order
print("\nHere is your order:")
print("Main product:", drinks[int(drink_choice) - 1])
print("Flavor:", flavors[int(flavor_choice) - 1])
print("Topping:", toppings[int(topping_choice) - 1])
print("Thanks for your order!")
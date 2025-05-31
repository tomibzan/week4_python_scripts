drinks = ["chocolate", "coffee", "decaf"]
flavors = ["caramel", "vanilla", "peppermint", "raspberry", "plain"]
toppings = ["chocolate", "cinnamon", "caramel"]
print("Tom's Coffee Shop Drinks")
print("------------------------")
i = 1
for d in drinks:
    print(i, d)
    i = i + 1
drink = input("Choose your drink: ")
print("Tom's Coffee Shop Flavors")
print("------------------------")

i = 1 
for f in flavors:
    print(i, f)
    i = i + 1
flavor = input("Choose your flavor: ")
print("Tom's Coffee Shop Toppings")
print("--------------------------")
i = 1 
for t in toppings:
    print(i, t)
    i = i + 1
toppings = input("Choose your toppings: ")
print("Here is your order: ")
print("Main product: ", drinks [drink])
print("Flavor: ", flavors[flavor])
print("Toppings: ", toppings[topping])
print("Thanks for your order")
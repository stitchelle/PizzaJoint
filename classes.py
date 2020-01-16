# 1. Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

# 2. Add a method for interacting with a pizza's toppings, called add_topping.

# 3. Add a method for outputting a description of the pizza (sample output below).

# 4. Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

class Pizza:
    def __init__(self):
        # Establish the properties of each book
        # with a default value
        self.size = ""
        self.style = ""
        self.topping = []
        self.sauce = ""

    def add_topping(self, topping):
        self.topping.append(topping)
        print(f'{self.topping}')
    
meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
# meat_lovers.print_order()

for n in meat_lovers.topping:
    print(n)
  
s = " and "
  
s = s.join(meat_lovers.topping) 
  
print(s) 

print(f'I would like a {meat_lovers.size} inch, {meat_lovers.style} pizza with {s}.')

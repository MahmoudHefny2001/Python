class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def descripe_restaurant(self):
        print(f"Restaurant name is: {self.name}")
        print(f"Cuisine type is: {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant is open")


restaurant = Restaurant("Hamza", "Chickens")
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.descripe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("Burger King", "Burger")
restaurant3 = Restaurant("Pizza Royal", "Pizzas") 

restaurant2.descripe_restaurant()
restaurant3.descripe_restaurant()


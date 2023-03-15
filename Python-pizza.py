# Pizza Top Class:
class pizza:
    def __init__(self, description,prices):
        self.description = description
        self.prices = prices
    
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.prices
     


# Pizza Subclasses:
class Classic_pizza(pizza):
    def __init__(self):
        description = f"Klasik Pizza"
        prices = 120.00
        super().__init__(description,prices)


class margherita_pizza(pizza):
    def __init__(self):
        description = f"Margherita Pizza"
        prices = 130.00
        super().__init__(description,prices)


class turk_Pizza(pizza):
    def __init__(self):
        description = f"Türk pizza"
        prices = 187.00
        super().__init__(description,prices)

class sade_pizza(pizza):
    def __init__(self):
        description = f"Sade pizza"
        prices = 250.00
        super().__init__(description,prices)


#Size Top Class:
class decorator_size(pizza):
    def __init__(self, pizza, size_ratio):
        self.pizza = pizza
        self.size_ratio = size_ratio
        self.prices = self.pizza.get_cost() * self.size_ratio

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.prices
     

#Size Subclasses:
class size_one(decorator_size):
    def __init__(self, pizza):
        super().__init__(pizza,0.5)
        self.description = "Small Size"

    def get_description(self):
        return self.description


class size_two(decorator_size):
    def __init__(self, pizza):
        super().__init__(pizza,1)
        self.price_multiplier = 1
        self.description = "Medium Size"

    def get_description(self):
        return self.description


class size_three(decorator_size):
    def __init__(self, pizza):
        super().__init__(pizza,1.5)
        self.description = "Large Size"

    def get_description(self):
        return self.description
 

#Sauce Top Classes:
class decorator_sauce(pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()
     

# Sauce Subclasses:
class olive_sauce(decorator_sauce):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 14.00
        self.description = " Zeytin Sosu"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class mushroom_sauce(decorator_sauce):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 12.00
        self.description = " Mantar Sosu "

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class goat_sauce(decorator_sauce):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 18.00
        self.description = " Keçi Peyniri Sosu"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class meat_sauce(decorator_sauce):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 20.00
        self.description = "Et Sosu"


    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price
    

class onion_sauce(decorator_sauce):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 8.00
        self.description = "Soğan Sosu"
        

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class corn_sauce(decorator_sauce):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 10.00
        self.description = "Mısır Sosu"
        

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price





# Printing our order to the database
import csv
import os
from datetime import datetime

def add_order_to_database(name, id_no, card_no, description, card_cvv, total_cost):

    now = datetime.now()
    order_time = now.strftime("%Y-%m-%d %H:%M:%S")


    new_order = [name, id_no, card_no, description, order_time, card_cvv, total_cost]

    file_exists = os.path.isfile("Orders_Database.csv")


    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if file_exists:
            writer.writerow(new_order)
        else:
            header = (["Name", "Id", "Card Number", "Order Description", "Order Time", "Card Password", "Total Price"])
            writer.writerow(header)
            writer.writerow(new_order)
     


def main():
  
    with open('Menu.txt', 'r') as f:
       menu_items = f.readlines()
    for item in menu_items:
       print(item.strip())
    
    

    pizza_choice = input("Please select to pizza (1-4): ")
    while pizza_choice not in ["1", "2", "3", "4"]:
        pizza_choice = input("Wrong Number! Please enter a valid number (1-4): ")

    if pizza_choice == "1":
        pizza = Classic_pizza()
    elif pizza_choice == "2":
        pizza = margherita_pizza()
    elif  pizza_choice == "3":
        pizza = turk_Pizza()
    else :
        pizza = sade_pizza()

   
    size_choice = input("Please select to size of pizza (5-7): ")
    while size_choice not in ["5", "6", "7"]:
        size_choice = input("Wrong Number! Please enter a valid number (5-7): ")


    if size_choice == "5":
        size = size_one(pizza)
    elif size_choice == "6":
        size = size_two(pizza)
    else:
        size =size_three(pizza)


    sauce_choice = input("Please select to sauce (8-13): ")
    while sauce_choice not in ["8", "9", "10", "11"]:
        sauce_choice = input("Wrong Number! Please enter a invalid number (8-13): ")

    if sauce_choice == "8":
        sauce = olive_sauce(pizza)
    elif sauce_choice == "9":
        sauce = mushroom_sauce(pizza)
    elif sauce_choice == "10":
        sauce = goat_sauce(pizza)
    elif sauce_choice == "11":
        sauce = meat_sauce (pizza)
    elif sauce_choice == "12":
        sauce = onion_sauce(pizza)
    else:
        sauce = corn_sauce(pizza)
    

  

    name = input("Name: ")
    id_no = input("Identity Number: ")
    card_no = input("Credit Card Number: ")
    card_cvv = input("Credit Card Password: ")


    order_description = size.get_description() + " " + pizza.get_description() + " with" + sauce.get_description()

    total_cost = size.get_cost() + sauce.get_cost()

    add_order_to_database(name, id_no, card_no, order_description, card_cvv,total_cost)

    print("Order Details:")

    print("Name: ", name)
    print("Identity Number: ", id_no)
    print("Credit Card Number: ", card_no)
    print("Order Explanation: ", order_description)
    print("Total Cost: ", total_cost)
    print("Order Time: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print("\n Your order has been received. Thank you!")
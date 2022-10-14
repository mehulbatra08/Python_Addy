class Item:
    def __init__(self,name,price,quantity):
        print(f"An instance created : {name}")
        self.name = name
    def calculate_total_price(self,x,y):
        return x*y
item1 = Item("Phone")
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price,item1.quantity))

item2 = Item("Laptop",100,5)
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 6
print(item2.calculate_total_price(item2.price,item2.quantity))

print(item1.name)
print(item2.name)
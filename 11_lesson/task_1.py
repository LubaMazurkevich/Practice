

class Shop:
    def __init__(self, objarea, objquantity, objcolor):
        self.area=objarea
        self.quantity=objquantity
        self.color=objcolor

    def open(self):
        print("we are open!")

    def close(self):
        print("we are close!")

    def sell_products(self):
        print("we are sell products!")

    def __str__(self):
        return f"Площадь магазина:{self.area}\nКоличество товара в магазине:{self.quantity} \
        \nЦвет магазина:{self.color}"


Shop_1= Shop (24, 500, "white")
print(Shop_1)
Shop_1.open()
Shop_1.close()
Shop_1.sell_products()


class Product():
    def __init__(self, objcolor, objform, objsize):
        self.color=objcolor
        self.form=objform
        self.size=objsize

    def sell(self):
        return "Товар продается"

    def edible(self):
        print("Товар съедобный")

    def tasty(self):
        print("Товар вкусный")

    def expensive(self):
        print("Товар дорогой")

    def __str__(self):
        return f"Цвет продукта:{self.color}\nФорма продукта:{self.form}\nРазмер продукта:{self.size} ,{Product_1.sell()}"


Product_1=Product("red", "circle" ,"2cm")
Product_2=Product("while", "circle", "4cm")
print(Product_1)
Product_1.edible()
Product_1.tasty()
Product_2.expensive()


class Apartment_House:
    def __init__(self, objcolor, objnumber_of_entrances, objform):
        self.color=objcolor
        self.number_of_entrances=objnumber_of_entrances
        self.form=objform

    def presentable(self):
        print("Дом презентабельный")

    def under_construction(self):
        print("Дом строится")

    def sell(self):
        print("Дом продается")

    def break_down(self):
        print("Дом ломается")

    def __str__(self):
        return f"Цвет дома:{self.color}\nКоличество подъездов:{self.number_of_entrances}\nФорма дома:{self.form}"


House_1= Apartment_House("red", 10, "usual")
print(House_1)
House_1.presentable()
House_1.under_construction()
House_1.sell()
House_1.break_down()









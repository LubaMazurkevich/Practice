

class Animals:
    def __init__(self,objquantity, objcolor,objtype):
        self.quantity=objquantity
        self.color=objcolor
        self.kind=objtype
        print("animal")

    def make_sounds(self):
        print("kra-kra")

    def eat(self):
        print("we are eat")

    def sleep(self):
        print("we are sleep")

    def __str__(self):
        return f"Количество живытных: {self.quantity}\nЦвет: {self.color}\nТип животных: {self.kind}\n"


Cat=Animals(40,"grey","cats")
print(Cat)

class Dog(Animals):
    def __init__(self, objquantity, objclr, objtp):
        super().__init__(objquantity, objclr, objtp)
        print("dog")

dg = Dog(40, "blue", "baskervili")
print(dg)

class Kangaroo(Animals):
    def __init__(self,objquant,objclr,objtp):
        super().__init__(objquant,objclr,objtp)
kangaroo_1=Kangaroo(50, "white", "kangaroo")
print(kangaroo_1)

class Canary(Animals):
    def __init__(self,quant,color,type):
        super().__init__(quant,color,type)
canary_1=Canary(20, "yellow", "canary")
print(canary_1)

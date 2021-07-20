

def function(s):

    return f"**** **** **** {s[-4:]}"

print(function("2255 6785 5678 9900"))


def polundrom(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


t = True
while t:
    s = input("Введите слово для проверки без пробелов или exit чтобы выйти: ")
    if s == "exit":
        t = False
    elif s == " ":
        print("Слово не ввведено!")
    else:
        print(polundrom(s))




class Tomato:
    states={1:"зелено-зрелые томаты",
            2:"бланжевые томаты",
            3:"полностью спелые томаты"}

    def __init__(self,_index):
        self._index=_index
        self.current_key=1
        self.state=Tomato.states[self.current_key]


    def grow(self):
        if self.current_key>=len(Tomato.states):
            print("Следующей стадии созревания не существует ")
        else:
            self.current_key += 1
            self.state = Tomato.states[self.current_key]



    def is_ripe(self):
        if self.state==Tomato.states[3]:
            return True
        else:
            return False

class TomatoBush:
    def __init__(self,quantity):
        self.quantity=quantity
        objects=[]
        for i in range(0,quantity):
            objects.append(Tomato(i))
        self.tomatoes=objects


    def grow_all(self):
        for i in self.tomatoes:
            i.grow()


    def all_are_ripe(self):
        for i in self.tomatoes:
            if i.is_ripe() is False:
                return False
        return True

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:

    def __init__(self,name,Tomatoobject):
        self.name=name
        self.__plant=Tomatoobject

    def work(self):
        self.__plant.grow_all()

    def harvest(self):
        if self.__plant.all_are_ripe() is True:
            self.__plant.give_away_all()
        else:
            print("Предупреждение!Плоды не созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству")


Tomato_1=Tomato(1)
Tomato_1.grow()
print(Tomato_1.is_ripe())


print("///")

TomatoBush_1=TomatoBush(5)
print(TomatoBush_1.all_are_ripe())
print(TomatoBush_1.give_away_all())

print("///")

Gardener_1=Gardener("Luba")
print(Gardener_1.harvest())
Gardener_1.knowledge_base()


class Flyer:

    def __init__(self):
        pass

    def fly(self):
        print("Лечу")


class Plane(Flyer):

    def __init__(self, objcolor, objfirm):
        super().__init__()
        self.color=objcolor
        self.firm=objfirm

    def go(self):
        print("Самолет едет")

    def increase_speed(self):
        print("Самолет увеличивает скорость")

    def stop(self):
        print("Самолет останавливается")

    def __str__(self):
        return f"Цвет самолета: {self.color}\nФирма самолета: {self.firm}\n"


Plane_1=Plane("while" , "Boeing")
print(Plane_1)
Plane_1.fly()
Plane_1.go()
Plane_1.increase_speed()
Plane_1.stop()
print("///")


class Gull(Flyer):

    def __init__(self,eye_color,objsize):
        super().__init__()
        self.color=eye_color
        self.size=objsize

    def eat(self):
        print("Чайка ест,хрум-хрум")

    def drink(self):
        print("глыдь-глыдь")

    def sleep(self):
        print("Хррррр")

    def fly(self):
        print("Чайка не летит")

    def __str__(self):
        return f"Цвет глаз чайки: {self.color}\nРазмер чайки: {self.size}"


Gull_1=Gull("while", "not big")
print(Gull_1)
Gull_1.fly()
Gull_1.drink()
Gull_1.sleep()






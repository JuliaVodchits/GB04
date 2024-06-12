# Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)
# Объекты в программе должны быть заменяемыми на экземпляры подтипов без влияния на правильность программы.
# Это значит, что объекты производного класса должны иметь возможность заменить объекты базового класса без изменения работы программы.

# 1. Код не использующий этот принцип
# class Bird():
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print("I am flying")
#
# class Ping(Bird):
#     pass
#
# p = Ping("Сара")
# p.fly() # но пингвин не летает!

#2. Исправленный код
# Если подставлять вместо родительского класса Bird любой дочерний, программа не испортится - все методы,
# которые были в родительском классе, реализованы в дочерних
class Bird():
    def cry(self):
        print("Птица кричит")

class FlyingBird(Bird):
    def fly(self):
        print("Эта птица летает")

    def cry(self):
        print("Птица кричит с высоты")

class Duck(FlyingBird):
    def fly(self):
        print("Эта утка летает быстро")

    def cry(self):
        print("Утка кричит с высоты")

class Penguin(Bird):
    def cry(self):
        print("Пингвин кричит")

def fly_in_the_sky(animal):
    animal.fly()

def crying_animal(animal):
    animal.cry()


fb = FlyingBird()
d = Duck()
b = Bird()
p = Penguin()
fly_in_the_sky(fb)
fly_in_the_sky(d)
crying_animal(fb)
crying_animal(d)
crying_animal(b)
crying_animal(p)
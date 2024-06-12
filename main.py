from abc import ABC, abstractmethod
import math

class Fighter():
    def __init__(self, nickname, offence, weapon=None):
        self.nickname = nickname
        self.offence = offence
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon


# Monsters
class Monster():
    def __init__(self, moniker, hit_points=100):
        self.moniker = moniker  # кличка
        self.__hit_points = hit_points            # оставшиеся ОЖ
        self.__is_bleading = False               # кровотечение
        self.__bleading_speed = 0                # скорость кровотечения
        self._type = ''

    def current_hit_points(self):
        current_hit_points = self.__hit_points
        if self.__is_bleading:
            current_hit_points -= self.__bleading_speed
        return current_hit_points

    def set_hit_points(self, new_hit_points):
        self.__hit_points = new_hit_points

    def set_bleading_speed(self, new_bleading_speed):
        self.__is_bleading = 1
        if self.__bleading_speed < new_bleading_speed:
            self.__bleading_speed = new_bleading_speed

    def get_name(self):
        return f"{self._type} {self.moniker}"

    def view_info(self):
        print(f"{self.get_name()} имеет {self.__hit_points} ОЖ")

class Golem(Monster):
    def __init__(self, moniker, hit_points=40):
        super().__init__(moniker, hit_points)
        self._type = 'Голем'


class Ogre(Monster):
    def __init__(self, moniker, hit_points=30):
        super().__init__(moniker, hit_points)
        self._type = 'Огр'

class Ghost(Monster):
    def __init__(self, moniker, hit_points=18):
        super().__init__(moniker, hit_points)
        self._type = 'Привидение'


# Weapons
class Weapon(ABC):
    def __init__(self, weapon_power):
        self.weapon_power = weapon_power
        self.type = ''

    @abstractmethod
    def attack(self, fighter, monster):
        pass

class Sword(Weapon):
    def __init__(self, weapon_power=5):
        super().__init__(weapon_power)
        self.type = 'Меч'

    def attack(self, fighter: Fighter, monster: Monster):
        damage = self.weapon_power + fighter.offence
        remaining_hit_points = monster.current_hit_points()
        if damage >= remaining_hit_points:
            remaining_hit_points = 0
        else:
            remaining_hit_points = remaining_hit_points - damage
            monster.set_bleading_speed(1)
        return remaining_hit_points

class Bow(Weapon):
    def __init__(self, weapon_power=4):
        super().__init__(weapon_power)
        self.type = 'Лук'

    def attack(self, fighter: Fighter, monster: Monster):
        damage = math.floor((self.weapon_power + fighter.offence) / 2)
        remaining_hit_points = monster.current_hit_points()
        if damage >= remaining_hit_points:
            remaining_hit_points = 0
        else:
            remaining_hit_points = remaining_hit_points - damage
            monster.set_bleading_speed(2)
        return remaining_hit_points

class Axe(Weapon):
    def __init__(self, weapon_power=10):
        super().__init__(weapon_power)
        self.type = 'Топор'

    def attack(self, fighter: Fighter, monster: Monster):
        damage = self.weapon_power + fighter.offence
        remaining_hit_points = monster.current_hit_points()
        if damage >= remaining_hit_points:
            remaining_hit_points = 0
        else:
            remaining_hit_points = remaining_hit_points - damage
        return remaining_hit_points


def fighting_round(fighter: Fighter, monster: Monster):
    if fighter.weapon is None:
        print(f"Не выбрано оружие")
        return 0
    remaining_hit_points = fighter.weapon.attack(fighter, monster)
    monster.set_hit_points(remaining_hit_points)
    if remaining_hit_points > 0:
        print(f"Воин {fighter.nickname} атаковал монстра {monster.get_name()} оружием {fighter.weapon.type}. "
              f"У монстра осталось {remaining_hit_points} ОЖ")
        return 1
    print(f"Воин {fighter.nickname} атаковал монстра {monster.get_name()} оружием {fighter.weapon.type} и победил!")
    return 0

fighter = Fighter("Юлия", 6)
ogre1 = Ogre("Петя")
golem1 = Golem("Вася")
ghost1 = Ghost("Зина")
sword1 = Sword()
axe1 = Axe()
bow1 = Bow()

ogre1.view_info()

result = 1
while result == 1:
    result = fighting_round(fighter, ogre1)

fighter.change_weapon(sword1)
result = 1
while result == 1:
    result = fighting_round(fighter, ogre1)

golem1.view_info()
fighter.change_weapon(axe1)
result = 1
while result == 1:
    result = fighting_round(fighter, golem1)


ghost1.view_info()
fighter.change_weapon(bow1)
result = 1
while result == 1:
    result = fighting_round(fighter, golem1)

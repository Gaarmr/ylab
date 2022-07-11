from abc import ABC, abstractmethod
from mixins import AttackWithGun, AttackWithLasers
from places import Place


class SuperHero(ABC):
    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    def find(self, place: Place):
        place.get_antagonist()

    @abstractmethod
    def attack(self):
        pass

    def ultimate(self):
        pass


class ChuckNorris(SuperHero, AttackWithGun):
    def __init__(self):
        super().__init__('Chuck Norris', False)

    def attack(self):
        self.fire_a_gun()


class Superman(SuperHero, AttackWithLasers):
    def __init__(self):
        super().__init__('Clark Kent', True)

    def attack(self):
        print('Kick')

    def ultimate(self):
        self.incinerate_with_lasers()

from abc import ABC, abstractmethod
from places import Place
from heroes import SuperHero


class MassMedia(ABC):
    @abstractmethod
    def create_news(self, place: Place, hero: SuperHero):
        pass


class NewsPaper(MassMedia):
    def create_news(self, place: Place, hero: SuperHero):
        print(
            f'{hero.name} saved the {place.get_name()}!',
            'Это напечатали в газете!'
        )


class TV(MassMedia):
    def create_news(self, place: Place, hero: SuperHero):
        print(
            f'{hero.name} saved the {place.get_name()}!',
            'Об этом сообщили по телевизору!'
        )

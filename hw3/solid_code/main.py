from massmedia import MassMedia, NewsPaper, TV
from heroes import ChuckNorris, Superman, SuperHero
from places import Kostroma, Place, Tokyo


def save_the_place(
        hero: SuperHero,
        place: Place,
        media: MassMedia
):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    media.create_news(place, hero)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), NewsPaper())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), TV())

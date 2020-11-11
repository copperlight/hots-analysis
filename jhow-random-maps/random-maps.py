import random
from typing import List

CUSTOM_GAME_MAPS = {
    'Alterac Pass': {
        'lanes': 3,
        'storm_league_rotation': True,
        'sandbox_available': False,
        'retired': False
    },
    'Battlefield of Eternity': {
        'lanes': 2,
        'storm_league_rotation': True,
        'sandbox_available': False,
        'retired': False
    },
    "Blackheart's Bay": {
        'lanes': 3,
        'storm_league_rotation': False,
        'sandbox_available': False,
        'retired': False
    },
    'Braxis Holdout': {
        'lanes': 2,
        'storm_league_rotation': True,
        'sandbox_available': False,
        'retired': False
    },
    'Cursed Hollow': {
        'lanes': 3,
        'storm_league_rotation': True,
        'sandbox_available': True,
        'retired': False
    },
    'Dragon Shire': {
        'lanes': 3,
        'storm_league_rotation': True,
        'sandbox_available': False,
        'retired': False
    },
    'Garden of Terror': {
        'lanes': 3,
        'storm_league_rotation': False,
        'sandbox_available': False,
        'retired': False
    },
    'Hanamura Temple': {
        'lanes': 2,
        'storm_league_rotation': True,
        'sandbox_available': False,
        'retired': False
    },
    'Haunted Mines': {
        'lanes': 2,
        'storm_league_rotation': False,
        'sandbox_available': False,
        'retired': True
    },
    'Infernal Shrines': {
        'lanes': 3,
        'storm_league_rotation': True,
        'sandbox_available': False,
        'retired': False
    },
    'Lost Cavern': {
        'lanes': 1,
        'storm_league_rotation': False,
        'sandbox_available': False,
        'retired': False
    },
    'Sky Temple': {
        'lanes': 3,
        'storm_league_rotation': True,
        'sandbox_available': False,
        'retired': False
    },
    'Tomb of the Spider Queen': {
        'lanes': 3,
        'storm_league_rotation': True,
        'sandbox_available': False,
        'retired': False
    },
    'Towers of Doom': {
        'lanes': 3,
        'storm_league_rotation': True,
        'sandbox_available': False,
        'retired': False
    },
    'Volskaya Foundry': {
        'lanes': 3,
        'storm_league_rotation': True,
        'sandbox_avaialble': True,
        'retired': False
    },
    'Warhead Junction': {
        'lanes': 3,
        'storm_league_rotation': False,
        'sandbox_available': False,
        'retired': False
    },
}


def random_map(count: int = 1) -> List[str]:
    maps = [m for m in CUSTOM_GAME_MAPS if CUSTOM_GAME_MAPS[m]['lanes'] >= 2]
    random.shuffle(maps)
    return maps[:count]


def main():
    print(random_map(5))


if __name__ == '__main__':
    main()

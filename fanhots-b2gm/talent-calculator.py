
def twitch_video(video_id: str, timestamp: str) -> str:
    """Example: https://twitch.tv/videos/783015871?t=4h58m18s"""
    pass


def psionic_storm_talent_calculator(hero: str, talents: str) -> str:
    """Example: https://psionic-storm.com/en/talent-calculator/artanis/#talents=2-3-2-1-4-2-1"""
    return f'https://psionic-storm.com/en/talent-calculator/{hero.lower()}/#talents={talents}'


def hots_build(hero: str, talents: str) -> str:
    """Example: [T2321421,Artanis]"""
    return f'[T{talents.replace("-", "")},{hero}]'

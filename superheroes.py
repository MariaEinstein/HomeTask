import requests

TOKEN = "2619421814940190"

urls = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
]

# Функция, принимающая список адресов

def requests_get(url_all):
    r = (requests.get(url) for url in url_all)
    return r

# Функция, собирающая информацию об интеллектах супергероев

def parser():
    super_man = []
    for item in requests_get(urls):
        intelligence = item.json()
        for power_stats in intelligence['results']:
            super_man.append({
                'name': power_stats['name'],
                'intelligence': power_stats['powerstats']['intelligence'],
            })

# Сравним интеллекты героев

    intelligence_hero = 0
    for intel_hero in super_man:
        if intelligence_hero < int(intel_hero['intelligence']):
            intelligence_hero = int(intel_hero['intelligence'])
            name = intel_hero['name']

    print(f"Самый интеллектуальный {name}, интеллект: {intelligence_hero}")

parser()
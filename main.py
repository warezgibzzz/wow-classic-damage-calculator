from player import Player
from monster import Monster
from pprint import pprint
from flask import Flask
app = Flask(__name__)

hit = int(input('Input hit: '))
crit = int(input('Input crit: '))
spd = int(input('Input spell damage: '))
dmg_min = int(input('Input spell min damage: '))
dmg_max = int(input('Input spell max damage: '))

player = Player(hit, [dmg_min, dmg_max], crit, spd)
monster = Monster(83)

results = []
total = 0
misses = 0
throws = 0
while throws < 100:
    dmg = player.damage(monster)
    try:
        dmg = int(dmg)
        results.append(dmg)
        total += dmg
    except ValueError:
        misses += 1
        results.append(dmg)

    throws += 1

result = {
    "total damage": total,
    "misses": misses,
    "throws": throws,
    "boss resist": monster.resist,
    "log": results
}

pprint(result)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'

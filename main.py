from player import Player
from monster import Monster
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        hit = int(request.form['hit'])
        crit = int(request.form['crit'])
        spd = int(request.form['spd'])
        dmg_min = int(request.form['min'])
        dmg_max = int(request.form['max'])

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

        return render_template(
            "result.html",
            total=total,
            misses=misses,
            throws=throws,
            resist=monster.resist,
            log=results,
            hit=hit,
            crit=crit,
            spd=spd,
            dmg_min=dmg_min,
            dmg_max=dmg_max
        )
    else:
        return render_template("index.html")

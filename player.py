import random

class Player:
  def __init__(self, hit, minmax, crit, spd):
    self.minmax = minmax
    self.hit = hit
    self.crit = crit
    self.spd = spd
  
  def is_hit(self, monster):
    return random.randint(0, 100) >= (monster.resist + self.hit)
    
  def is_crit(self):
    return random.randint(0, 100) <= self.crit

  def damage(self, monster):
    dice = random.randint(0, 100)
    if self.is_hit(monster):
      return "miss"

    avg = random.randint(self.minmax[0], self.minmax[1])
    dmg = (avg + (self.spd * 0.814))

    if self.is_crit():
      return dmg * 2

    return dmg
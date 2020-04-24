import random


# class Enemy:
#     atkl = 60
#     atkh = 80

#     def getAtk(self):
#         print(self.atkl)

# enemy1 = Enemy()
# enemy1.getAtk()

# enemy2 = Enemy()
# enemy2.getAtk()


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("atk is", self.atkl)

    def getHp(self):
        print("hp is", self.hp)

enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()


"""
playerhp = 260
enemyatkl = 60
enemyatkh = 80


while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp == 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp > 30:
        continue

    print("You have low health. You have been transported to the nearest in.")
    break

"""

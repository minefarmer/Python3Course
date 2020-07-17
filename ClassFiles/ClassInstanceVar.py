import random
# 
# 
# 
# 
# 
# 
# 
# 
# 
class Enemy:
    hp = 200
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh
        
    
    
    def getAtk(self):
        print('atk is', self.atkl)  # atk is 40
                          # atk is 75
    
    def getHp(self):
        print('Hp is', self.hp)  # Hp is 200
                                # Hp is 200

enemy1 = Enemy(40, 49)
enemy1.getAtk()  # atk is 40
enemy1.getHp()  # Hp is 200

enemy2 = Enemy(75, 90)
enemy2.getAtk()  # atk is 75
enemy2.getHp()  # Hp is 200

'''

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg
    
    if playerhp <= 30:
        playerhp = 30
        
    print('Enemy strikes for', dmg, 'points of damage. Current HP is', playerhp)  # Enemy strikes for 67 points of damage. Current HP is 193
    
    if playerhp == 30:
        pass  # use to create an empty block of code
        
    print('You have low health. You have been teleported to the nearest inn.')  # You have low health. You have been teleported to the nearest inn.
    break
'''
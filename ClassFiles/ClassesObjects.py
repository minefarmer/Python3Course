import random


class Enemy:
    atkl = 60
    atkh = 80
    
    def getAtk(self):
        print(self.atkl)  # 60
                          # 60

enemy1 = Enemy()
enemy1.getAtk()  # creates first printout

enemy2 = Enemy()
enemy1.getAtk()  # creates second printout


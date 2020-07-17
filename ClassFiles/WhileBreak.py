import random
# Step 1 died  11
# Step 2 injured  32
# 
step 3   55
# 
# 
# 
# 
# 

# playerhp = 260
# enemyatkl = 60
# enemyatkh = 80

# while playerhp > 0:
#     dmg = random.randrange(enemyatkl, enemyatkh)
#     playerhp = playerhp - dmg
    
#     if playerhp <= 0:
#         playerhp = 0
    
#     print('Enemy strikes for', dmg, 'points of damage. Current HP is', playerhp)  # Enemy strikes for 66 points of damage. Current HP is 194
#                                                                                     # Enemy strikes for 73 points of damage. Current HP is 121
#                                                                                     # Enemy strikes for 78 points of damage. Current HP is 43 
#                                                                                     # Enemy strikes for 61 points of damage. Current HP is 0

#     if playerhp == 0:
#         print('You have died. You cannot respond, as you qre dead.')  # You have died. You cannot respond, as you qre dead. 



#  Step 2 ***********************************************************************************
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg
    
    if playerhp <= 30:
        playerhp = 30
        
    print('Enemy strikes for', dmg, 'points of damage. Current HP is', playerhp)  # Enemy strikes for 64 points of damage. Current HP is 196
                                                                                    # Enemy strikes for 77 points of damage. Current HP is 119
                                                                                    # Enemy strikes for 77 points of damage. Current HP is 42 
                                                                                    # Enemy strikes for 75 points of damage. Current HP is 30
    
    if playerhp == 30:
        print('You have low health. You have been teleported to the nearest inn.')  # You have low health. You have been teleported to the nearest inn.
        break
    
    
    
#  Step 3 ***********************************************************************************
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
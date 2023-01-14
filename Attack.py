from System.Collections.Generic import List
from System import Byte
scanrange = 5 #Range to attack initially
keeprange = 2 #range to keep attacking same mobile
primaryweaponid = [0x143E,0x26C2,0x14F0] #weapon ids to do primary with. add yours in if not in there.
secondaryweaponid = [0x2D28,0x0F52, 0x27A5] #weapon ids to do secondary with. add yours in if not in there.
shields = [0x0A22, 0x0A25, 0x2B01] #shield ids to ignore. add yours in if not in there.
stamcheck = 250 # how much stam to cast divine fury if under for healing/swing speed. this may vary player to player.
castconsecrate = True #True does Consecrate Weapon False does not.
castdivine = True  #True does Divine Fury False does not.

def consecrateweapon():
    if not Player.BuffsExist('Consecrate Weapon'):
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(350)
        
def divinefury():
    if not Player.BuffsExist('Divine Fury'):
        Spells.CastChivalry('Divine Fury')
        Misc.Pause(150)

def PrimaryOrSecondary():
    weapon = Player.GetItemOnLayer('LeftHand')
    weapon2 = Player.GetItemOnLayer('RightHand')
    if weapon != None and weapon.ItemID not in shields:
        if weapon.ItemID in primaryweaponid:
            if not Player.HasPrimarySpecial:
                Player.WeaponPrimarySA()
        elif weapon.ItemID in secondaryweaponid:
            if not Player.HasSecondarySpecial:
                Player.WeaponSecondarySA()
    elif weapon2 != None and weapon2.ItemID not in shields:
        if weapon2.ItemID in primaryweaponid:
            if not Player.HasPrimarySpecial:
                Player.WeaponPrimarySA()
        elif weapon2.ItemID in secondaryweaponid:
            if not Player.HasSecondarySpecial :
                Player.WeaponSecondarySA()
    else:
        if not Player.HasPrimarySpecial:
            Player.WeaponPrimarySA()
    return
    
def searchArea(): #search filter function
    atk = Mobiles.Filter()#set filter variable
    atk.Enabled = True #is filter on?
    atk.RangeMax = scanrange #range to add to filter
    atk.Notorieties = List[Byte](bytes([3,4,5,6])) #mobile notorieties
    enemies = Mobiles.ApplyFilter(atk) # apply filter to list
    return enemies #return variable

def goattackenemy(enemy): #attack function
    monster = Mobiles.FindBySerial(enemy.Serial) #set mobile to variable
    if monster: #does monster exist?
        if castconsecrate:
            consecrateweapon()
        if castdivine:
            divinefury()
        PrimaryOrSecondary() #turn on special
        Misc.Pause(50) # pause
        Player.Attack(enemy) #attack target
        Misc.Pause(150) # pause
        if Player.Stam < stamcheck and castdivine:
            Spells.CastChivalry('Divine Fury')
            Misc.Pause(150)
        if monster and Player.InRangeMobile(monster,keeprange): #if monster still exists and in range do not move on to a new monster
            goattackenemy(monster)# call to attack function

def main():  #main function
    enemies = searchArea() #call function to add to list
    Mobiles.Select(enemies,'Nearest') # set order by nearest first
    for enemy in enemies: #go through each mobile in list
        monster = Mobiles.FindBySerial(enemy.Serial)  #set mobile to variable
        if monster: #does monster exist?
            goattackenemy(monster) #call function to attack
            Misc.Pause(350)#pause
        Misc.Pause(350) #pause
  
while True: #while program is running. You need to turn script off using this function if u get disconnected before trying to log back in.
  main()  #call main function

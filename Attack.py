from System.Collections.Generic import List
from System import Byte
scanrange = 5 #Range to attack initially
keeprange = 2 #range to keep attacking same mobile
primaryweaponid = [0x143E,0x26C2,0x14F0, 0x0F4B] #weapon ids to do primary with. add yours in if not in there.
secondaryweaponid = [0x2D28,0x0F52, 0x27A5] #weapon ids to do secondary with. add yours in if not in there.
shields = [0x0A22, 0x0A25, 0x2B01] #shield ids to ignore. add yours in if not in there.
stamcheck = 250 # how much stam to cast divine fury if under for healing/swing speed. this may vary player to player.
castconsecrate = True #True does Consecrate Weapon False does not.
castdivine = True  #True does Divine Fury False does not.

def consecrateweapon(): #cast Consecrate Weapon method
    if not Player.BuffsExist('Consecrate Weapon'): #if consecrate is not in buff bar
        Spells.CastChivalry('Consecrate Weapon') # cast consecrate weapon.
        Misc.Pause(350) # pause
        
def divinefury(): # cast divine fury method
    if not Player.BuffsExist('Divine Fury'): #if divine fury is not in buff bar
        Spells.CastChivalry('Divine Fury') # cast divine fury
        Misc.Pause(150) # pause

def PrimaryOrSecondary(): # use primary or secondary method
    weapon = Player.GetItemOnLayer('LeftHand') # set weapon in left hand
    weapon2 = Player.GetItemOnLayer('RightHand') # set weapon in right hand
    if weapon != None and weapon.ItemID not in shields: # if item present in left hand and not a shield.
        if weapon.ItemID in primaryweaponid: # if weapon itemid is in primary ids
            if not Player.HasPrimarySpecial: # if primary is not on
                Player.WeaponPrimarySA() #use primary
        elif weapon.ItemID in secondaryweaponid: # if weapon itemid is in secondary ids
            if not Player.HasSecondarySpecial: # if secondary is not on
                Player.WeaponSecondarySA() #use secondary
    elif weapon2 != None and weapon2.ItemID not in shields: # if item present in right hand and not a shield.
        if weapon2.ItemID in primaryweaponid: # if weapon itemid is in primary ids
            if not Player.HasPrimarySpecial: # if primary is not on
                Player.WeaponPrimarySA() #use primary
        elif weapon2.ItemID in secondaryweaponid: # if weapon itemid is in secondary ids
            if not Player.HasSecondarySpecial: # if secondary is not on
                Player.WeaponSecondarySA() #use secondary
    else:
        if not Player.HasPrimarySpecial: # if primary is not on
            Player.WeaponPrimarySA() #use primary
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
        if castconsecrate: # If castconsecrate setting is set to True at top.
            consecrateweapon() # call cast consecrate weapon function
        if castdivine: # If castdivine setting is set to True at top.
            divinefury() # call cast divine fury function
        PrimaryOrSecondary() #turn on special
        Misc.Pause(50) # pause
        Player.Attack(enemy) #attack target
        Misc.Pause(150) # pause
        if Player.Stam < stamcheck and castdivine: # if stam is under set stam check up top and castdivine setting is set to True at top. 
            Spells.CastChivalry('Divine Fury') #Cast Divine Fury
            Misc.Pause(150) # pause
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

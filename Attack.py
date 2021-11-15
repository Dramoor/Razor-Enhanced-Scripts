from System.Collections.Generic import List
from System import Byte
scanrange = 5 #Range to attack initially
keeprange = 2 #range to keep attacking same mobile

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
        Player.Attack(enemy) #attack target
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
  
while True: #while logged in after hitting play(when using this you should not need to use loop)
  main()  #call main function

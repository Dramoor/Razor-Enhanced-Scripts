from System.Collections.Generic import List
#
setX = 25 #x location of gump on screen (if gump up have to click button to move)
setY = 50 # y location of gump on screen (same)

def sendgump(): #Method to call to send gump. 
    gd = Gumps.CreateGump(movable=False) #making the gump movable=False (gump not movable) closeable=False(right click does not close gump with button zero)
    Gumps.AddPage(gd, 0); #add page to the gump.
    Gumps.AddBackground(gd, 0, 0, 450, 142, 30546) #Add Background (gump, x, y, length, height, gumpid)
    Gumps.AddAlphaRegion(gd,0,0,450,142) #Add See Thru Region (gump, x, y, length, height)
    Gumps.AddButton(gd, 5, 5, 2241, 2241, 1, 1, 0)#Add Button (gump, x, y, unpressedid, pressedid, buttonnumber, buttoncalltype, param)
    Gumps.AddTooltip(gd, r"Create Food") #Add Tool Tip for hovering over the button above.
    Gumps.AddButton(gd, 49, 5, 2254, 2254, 2, 1, 0)
    Gumps.AddTooltip(gd, r"Protection")
    Gumps.AddButton(gd, 93, 5, 2261, 2261, 3, 1, 0)
    Gumps.AddTooltip(gd, r"Teleport")
    Gumps.AddButton(gd, 137, 5, 2269, 2269, 4, 1, 0)
    Gumps.AddTooltip(gd, r"Lightning")
    Gumps.AddButton(gd, 181, 5, 2271, 2271, 5, 1, 0)
    Gumps.AddTooltip(gd, r"Recall")
    Gumps.AddButton(gd, 225, 5, 2281, 2281, 6, 1, 0)
    Gumps.AddTooltip(gd, r"Energy Bolt")
    Gumps.AddButton(gd, 269, 5, 2283, 2283, 7, 1, 0)
    Gumps.AddTooltip(gd, r"Invisibility")
    Gumps.AddButton(gd, 313, 5, 2284, 2284, 8, 1, 0)
    Gumps.AddTooltip(gd, r"Mark")
    Gumps.AddButton(gd, 357, 5, 2287, 2287, 9, 1, 0)
    Gumps.AddTooltip(gd, r"Reveal")
    Gumps.AddButton(gd, 401, 5, 2291, 2291, 10, 1, 0)
    Gumps.AddTooltip(gd, r"Gate Travel")
    #row 2
    Gumps.AddButton(gd, 5, 49, 2295, 2295, 11, 1, 0)
    Gumps.AddTooltip(gd, r"Polymorph")
    Gumps.AddButton(gd, 49, 49, 20492, 20492, 12, 1, 0)
    Gumps.AddTooltip(gd, r"Vampiric Embrace")
    Gumps.AddButton(gd, 93, 49, 20494, 20494, 13, 1, 0)
    Gumps.AddTooltip(gd, r"Wither")
    Gumps.AddButton(gd, 137, 49, 20495, 20495, 14, 1, 0)
    Gumps.AddTooltip(gd, r"Wraith Form")
    Gumps.AddButton(gd, 181, 49, 20738, 20738, 15, 1, 0)
    Gumps.AddTooltip(gd, r"Consecrate Weapon")
    Gumps.AddButton(gd, 225, 49, 20740, 20740, 16, 1, 0)
    Gumps.AddTooltip(gd, r"Divine Fury")
    Gumps.AddButton(gd, 269, 49, 20741, 20741, 17, 1, 0)
    Gumps.AddTooltip(gd, r"Enemy of One")
    Gumps.AddButton(gd, 313, 49, 20745, 20745, 18, 1, 0)
    Gumps.AddTooltip(gd, r"Sacred Journey")
    Gumps.AddButton(gd, 357, 49, 21282, 21282, 19, 1, 0)
    Gumps.AddTooltip(gd, r"Animal Form")
    Gumps.AddButton(gd, 401, 49, 21287, 21287, 20, 1, 0)
    Gumps.AddTooltip(gd, r"Mirror Image")
    
    #row 3
    Gumps.AddButton(gd, 5, 93, 21282, 21282, 21, 1, 0)
    Gumps.AddTooltip(gd, r"Animal Form")
    Gumps.AddButton(gd, 49, 93, 24000, 24000, 22, 1, 0)
    Gumps.AddTooltip(gd, r"Nether Bolt")
    Gumps.AddButton(gd, 93, 93, 21538, 21538, 23, 1, 0)
    Gumps.AddTooltip(gd, r"Evasion")
    
    Gumps.SendGump(987654, Player.Serial, setX, setY, gd.gumpDefinition, gd.gumpStrings) #sends gump (gumpid use high to not interfere with in gamegumps and make sure every gump has different id, player serial to get gump, x y location of gump, definition gump information, gumpStrings ) )
    buttoncheck() #once send gump go to check for button presses.

def buttoncheck(): #method called to check for a button push.
    Gumps.WaitForGump(987654, 60000) # waiting for gump (gumpid, ms to wait)
    Gumps.CloseGump(987654) #close gump (gumpid)
    gd = Gumps.GetGumpData(987654) #get data from gump (gumpid)
    if gd.buttonid == 1: #if button pressed is buttonid 1.
        Spells.CastMagery('Create Food') #cast spell create food since ubtton 1 was called.
    elif gd.buttonid == 2:
        Spells.CastMagery('Protection')
    elif gd.buttonid == 3:
        Spells.CastMagery('Teleport') 
    elif gd.buttonid == 4:
        Spells.CastMagery('Lightning')
    elif gd.buttonid == 5:
        Spells.CastMagery('Recall')
    elif gd.buttonid == 6:
        Spells.CastMagery('Energy Bolt')
    elif gd.buttonid == 7:
        Spells.CastMagery('Invisibility')
    elif gd.buttonid == 8:
        Spells.CastMagery('Mark') 
    elif gd.buttonid == 9:
        Spells.CastMagery('Reveal') 
    elif gd.buttonid == 10:
        Spells.CastMagery('Gate Travel') 
    elif gd.buttonid == 11:
        Spells.CastMagery('Polymorph') 
    elif gd.buttonid == 12:
        Spells.CastNecro('Vampiric Embrace')
    elif gd.buttonid == 13:
        Spells.CastNecro('Wither')
    elif gd.buttonid == 14:
        Spells.CastNecro('Wraith Form')  
    elif gd.buttonid == 15:
        Spells.CastChivalry('Consecrate Weapon')    
    elif gd.buttonid == 16:
        Spells.CastChivalry('Divine Fury') 
    elif gd.buttonid == 17:
        Spells.CastChivalry('Enemy of One') 
    elif gd.buttonid == 18:
        Spells.CastChivalry('Sacred Journey') 
    elif gd.buttonid == 19:
        Spells.CastNinjitsu('Animal Form')
    elif gd.buttonid == 20:
        Spells.CastNinjitsu('Mirror Image') 
    elif gd.buttonid == 21:
        Spells.CastNinjitsu('Animal Form')
    elif gd.buttonid == 22:
        Spells.CastMysticism('Nether Bolt')
    elif gd.buttonid == 23:
        Spells.CastBushido('Evasion') 

while True: # if program running. Replaces having to loop it and keeps from returning to top if variables that change are set.
    sendgump()#go to start sendgump method.
    Misc.Pause(750) #pause for 750ms

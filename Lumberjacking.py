import sys
toolid = 0x0F43 #set chopping tool graphic id defaulted as hatchet
maxweight = 1000

target = Target.PromptGroundTarget('Select tree to chop') #open a target for player to target tile to mine.
Journal.Clear() #Make sure journal is not reading ahead of when this started.
while Journal.Search("There's not enough wood here to harvest.") == False: #do under until this message happens.
    Journal.Clear() #clear message as to not get confused.
    hatchet = Items.FindByID(toolid, -1, Player.Backpack.Serial) #find hatchet in pack.
    if hatchet: #if hatchet exists
        Items.UseItem(hatchet) #use hatchet
        Target.WaitForTarget(2500,False) #wait for the target to appear on screen.
        tiles = Statics.GetStaticsTileInfo(target.X, target.Y, Player.Map) #read map files to find target as static
        if len(tiles) != 0 and tiles[0].StaticID != 0: #if tile is not id 0
            Target.TargetExecute(target.X, target.Y, tiles[0].StaticZ, tiles[0].StaticID) #target tile
            Misc.Pause(650)#pause
            if Journal.Search("That is too far away.") == True: #if string is read in journal
                Player.ChatSay(67, "Too Far Away") #player says this aloud
                sys.exit(99) #turns script off
            if Player.Weight >= maxweight: 
                Player.ChatSay(67, "Overweight!") #player says this aloud
                sys.exit(99) #turns script off
            Misc.Pause(750) #pause
        else: #if tile does not exist
            Target.Cancel() #cancel target
            sys.exit(99) #turns script off
    else: #if hatchet does not exist
        Player.ChatSay(67, "No Hatchet") #player says this aloud
        sys.exit(99) #turns script off
else: #if journal returns nothing to mine
    Player.ChatSay(67, "Tree is Done")#player says this aloud
    sys.exit(99) #turns script off

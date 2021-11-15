import sys
toolid = 0x0F39 #set digging tool graphic id defaulted as shovel
maxweight = 400 #set max weight before it stops if ore is going to pack.

target = Target.PromptGroundTarget('Select location to mine') #open a target for player to target tile to mine.
Journal.Clear() #Make sure journal is not reading ahead of when this started.
while Journal.Search("There is no metal here to mine.") == False: #do under until this message happens.
    Journal.Clear() #clear message as to not get confused.
    shovel = Items.FindByID(toolid, -1, Player.Backpack.Serial) #find shovel in pack.
    if shovel: #if shovel exists
        Items.UseItem(shovel) #use shovel
        Target.WaitForTarget(2500,False) #wait for the target to appear on screen.
        tiles = Statics.GetStaticsTileInfo(target.X, target.Y, Player.Map) #read map files to find target as static
        if len(tiles) != 0 and tiles[0].StaticID != 0: #if tile is not id 0
            Target.TargetExecute(target.X, target.Y, tiles[0].StaticZ, tiles[0].StaticID) #target tile
            Misc.Pause(650)#pause
            if Journal.Search("That is too far away.") == True: #if string is read in journal
                Player.ChatSay(67, "Too Far Away") #player says this aloud
                sys.exit(99) #turns script off
            if Player.Weight >= maxweight: #if players weight hits max weight indicated above.
                Player.ChatSay(67, "Overweight!") #player says this aloud
                sys.exit(99) #turns script off
            Misc.Pause(750) #pause
        else: #if tile does not exist
            Target.Cancel() #cancel target
            sys.exit(99) #turns script off
    else: #if shovel does not exist
        Player.ChatSay(67, "No Shovel") #player says this aloud
        sys.exit(99) #turns script off
else: #if journal returns nothing to mine
    Player.ChatSay(67, "Location is Done")#player says this aloud
    sys.exit(99) #turns script off

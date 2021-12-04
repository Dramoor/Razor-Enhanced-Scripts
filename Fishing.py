import sys

target = Target.PromptGroundTarget('Select location to fish') # Set Target of place to fish.

Journal.Clear() # Clear journal in scan as to not detect a previous end.

def DoFishing(): # create method.
    while Journal.Search("seem to be biting here.") == False: # Do everything inside here until this message comes up in journal.
        pole = Player.GetItemOnLayer('RightHand') # find any item in right hand.
        if pole and pole.ItemID == 0x0DC0: # check if item in right hand exists and itemid is a fishing pole. 
            Items.UseItem(pole) # Use Fishing Pole. 
            Target.WaitForTarget(1500) # Wait 1.5 seconds for a target. 
        else: # If item in right hand does not exists or itemid is not a fishing pole. 
            pole = Items.FindByID(0x0DC0, -1, Player.Backpack.Serial) # Check in backpack by itemid for fishing pole. 
            if pole: # If pole now exists. 
                Items.UseItem(pole) # Use Fishing Pole
                Target.WaitForTarget(1500) # Wait up to 1.5 seconds for a target. 
            else: # if pole does not exist.
                Misc.SendMessage('no fishing pole') # Send system message to player.
                sys.exit(99) # stop script. 
        if Target.HasTarget: # if player has a target receptical up.
            tiles = Statics.GetStaticsTileInfo(target.X, target.Y, Player.Map) # Make list of any static tiles at target.
            if len(tiles) != 0 and tiles[0].StaticID != 0: # If static tile exists.
                Target.TargetExecute(target.X, target.Y, tiles[0].StaticZ, tiles[0].StaticID)  # Target static tile.
                Misc.Pause(8500) # pause 8.5 seconds.
            else: # If static tile does not exist.
                Target.TargetExecute( target.X, target.Y, -5, 0x0000 ) # Target the location targeted with a z of -5.
                Misc.Pause(8500) # pause 8.5 seconds.
                #sys.exit(99)
        else:  # If player has no target up.
            if pole: # if pole exists.
                Items.UseItem(pole) # Use Fishing Pole
                Target.WaitForTarget(1500) # Wait up to 1.5 seconds for a target. 
                if Target.HasTarget: # if player has a target receptical up.
                    tiles = Statics.GetStaticsTileInfo(target.X, target.Y, Player.Map) # Make list of any static tiles at target.
                    if len(tiles) != 0 and tiles[0].StaticID != 0: # If static tile exists.
                        Target.TargetExecute(target.X, target.Y, tiles[0].StaticZ, tiles[0].StaticID)  # Target static tile.
                        Misc.Pause(8500) # pause 8.5 seconds.
                    else: # If static tile does not exist.
                        Target.TargetExecute( target.X, target.Y, -5, 0x0000 )# Target the location targeted with a z of -5.
                        Misc.Pause(8500) # pause 8.5 seconds.
            else: # if pole does not exist.
                Misc.SendMessage('no fishing pole') # Send system message to player.
                sys.exit(99) # stop script. 
    Misc.SendMessage('Location Empty.') # Send system message to player.
    sys.exit(99) # stop script. 

while True: # while online. 
    DoFishing() # run method above.

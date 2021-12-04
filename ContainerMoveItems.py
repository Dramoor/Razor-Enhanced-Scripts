pausetime = 650 # Scripts universal pause time
source = Target.PromptTarget('Select Source Container')# Target Item to get.
sourcecont = Items.FindBySerial(source)# Set item to variable by serial
target = Target.PromptTarget('Select Target Container')# Target Item to get.
targetcont = Items.FindBySerial(target)# Set item to variable by serial

def DoMove():
    Items.UseItem(sourcecont)# Open container to be sure to get the items to move.
    Misc.Pause(pausetime)# Pause
    Items.WaitForContents(sourcecont,2500)# Wait to get all items inside container. Timeout at delay in milliseconds.
    for i in sourcecont.Contains: # Do inside for every item in container. 
        Items.Move(i,targetcont,-1)# Move item to target container. -1 means any amount.
        Misc.Pause(pausetime)# Pause
    Misc.SendMessage('DONE', 32)# Send in game message telling you done.

DoMove() # Do the Move.

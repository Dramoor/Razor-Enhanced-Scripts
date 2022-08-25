import sys #for stop script after skill set

corpses = Target.PromptTarget('Select Corpse') # target the corpse to use skill on
corpse = Items.FindBySerial(corpses) #setting corpse after targeted

while corpse: #if corpse exists
    Player.UseSkill('forensics',corpse, 2500) #use forensics, target corpse, timeout 
    Misc.Pause(1000) #pause 1 second
    if Player.GetSkillValue('forensics') >= 120: # if skill 120 or higher
        Player.ChatSay(32, "done!") #say message
        sys.exit(90) #stop script

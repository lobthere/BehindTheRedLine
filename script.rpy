define player = Character("[playerName]")
default playerName = "None"

label start:
    $ playerName = renpy.input("What is your name ?")
    $ playerName = playerName.strip()

    if not playerName:
        $povname = "None"

    player "my name is [playerName]"
    return

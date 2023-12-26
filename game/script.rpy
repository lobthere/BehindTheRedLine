label splashscreen:
    scene black
    with Pause(1)

    show text "EclipsedHeart Studios" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    play sound "audio/warnings-music.wav"
    show image "images/warningsplashscreen.png" with dissolve
    with Pause(13)

    hide image warningsplashscreen with dissolve
    with Pause(15)
    stop sound

    play sound "audio/vhs-sound.wav"
    with Pause(3)
    stop sound

    return
    with fade

define c = Character("Charlotte", color = "#ffffff")
define p = Character("[povname]", color = "#ffffff")
define u = Character("...", color = "#ffffff")
define po = Character("Police officer", color = "#ffffff")
define idk = Character("???", color = "#ffffff")
define config.custom_text_tags("[glitch]")

label start:

    stop music

    show text "{glitch 5.0}{color=#0aad07}4 months earlier...{/glitch}{/color}"
    with Pause(4)
    show text "{glitch 5.0}{color=#0aad07}{b}? ?????? ??????????{/b}{/glitch}"
    show text "{glitch 5.0}{color=#940303}{b}? ?????? ??????????{/b}{/glitch}"

    u "uh..."

    play music "audio/traffic-police-sound.wav"

    scene black
    with dissolve

    "I'm so tired... it's already dark outside"
    "I hope there are still buses at this hour."
    " "
    #regarde son téléphone
    #cadre horraire qui s'affiche en haut en vert, il est 22h

    scene bg test
    with dissolve

    u "Woah my god its really cold ooof..."
    u "I should hurry up"
    #changer de scène, uni extérieur
    u "hm"
    "There's a lot of agitation in this area"
    "Yet i don't see anyone around"
    #moving camera, vue sur la scène de crime
    " "
    "cops."
    "Could it be murder again ...?"
    "All i can see from here are the police cars."
    "There's no one watching over the place."
    "...Strange"
    "..."
    " "
    menu:
        " ... Should i get closer?"
        "Yes.":
            jump yes
        "That's none of my business":
            jump no

label yes:
    u "I hope i won't get myself in trouble for this."
    #scène de crime rapprochée
    #Enlever la box de texte pour voir la scène
    u "Ugh... the smell"
    #vue sur le corps sous la bache
    "..."
    "Hm, 4 murders in one month, that's a lot for a quiet town like this"
    "Guess i'm still not used to it."
    #s'accroupit, vue sur le corps recouvers de prés
    menu:
        "Maybe i could take a look..."
        "Just a little peek":
            jump ok
        "*Step back*":
            jump nuh

    label ok:
        "..."
        #main qui se pose sur la bache
        "i placed my shaking hand on the cover and lifted."

        scene uh
        with dissolve

        #illu corps de la petite fille
        "i stumbled backwards, falling to the floor."

        scene black

        u "God..."
        u "I-..."
        "My body couldn't stop shaking."
        idk "HEY YOU !!" #shaking screen
        #le joueur se relève brusquement, on voit un policier en face, visiblement en colère
        "I scrambled to my feet quickly."
        po "Who are you !? What are you doing here ??"
        u "Uh- ...me?"
        po "Yes YOU ! What's your name ?"
        "I..."

        $ povname = renpy.input("What's your name?", length=32)
        $ povname = povname.strip()

        if not povname:
            $povname = "Maia"

        po "[povname] What are you doing here, can't you see this is a closed search area ?"
        po "You want your figerprints on the crime scene or what??"
        p "I'm... sor-" #le policier lui coupe la parole
        po "Go home, you shouldn't be here"
        p "Uh yes... sorry"
        po "And..."
        po "Be careful on your way home. I think you've seen what's been going on the last few weeks."
        p "..."
        p "...yeah"
        #pars et se rends vers l'arrêt de bus
        " "
        #illu bus, vidéo paysage qui défile, il fait nuit et il neige beaucoup
        "This winter is going to be even colder than last year..."
        #image noire, iel s'endors dans le bus
        idk "Excuse me... this is the last stop."
        "so tired i completly forgot i was there."
        p "...ah thank you for wake me up"
        "Thanks god my stop is the last one"
        #the player get off the bus and makes his way home
        "  "
        " "
        "...finally home."

        menu:
            "lets sleep a little now":
                jump charlotte

    label nuh:
        "Yeah... no...maybe i shouldn't do that."
        idk "HEY YOU !!" #shaking screen
        #le joueur se relève brusquement, on voit un policier en face, visiblement en colère
        "I scrambled to my feet quickly."
        po "Who are you !? What are you doing here ??"
        u "Uh- ...me?"
        "Police officer" "Yes YOU ! What's your name ?"
        "I..."

        $ povname = renpy.input("What's your name?", length=32)
        $ povname = povname.strip()

        if not povname:
            $povname = "Maia"

        po "[povname] What are you doing here, can't you see this is a closed search area ?"
        po "You want your figerprints on the crime scene or what??"
        P "I-... sor-" #le policier lui coupe la parole
        po "Go home, you shouldn't be here"
        p "Uh yes... sorry"
        po "And..."
        po "Be careful on your way home. I think you've seen what's been going on the last few weeks."
        p "..."
        p "...yeah"
        #pars et se rends vers l'arrêt de bus
        " "
        #illu bus, vidéo paysage qui défile, il fait nuit et il neige beaucoup
        "This winter is going to be even colder than last year..."
        #image noire, iel s'endors dans le bus
        idk "Excuse me... this is the last stop."
        "so tired i completly forgot i was there."
        p "...ah thank you for wake me up"
        "Thanks god my stop is the last one"
        #the player get off the bus and makes his way home
        " "
        " "
        "...finally home."
        menu:
            "lets sleep a little now":
                jump charlotte

label no:
    "Ugh...it's been a long day, i'm sleepy."
    # se rends vers l'arrêt de bus
    " "
    #illu bus, vidéo paysage qui défile, il fait nuit et il neige beaucoup
    "This winter is going to be even colder than last year..."
    #image noire, iel s'endors dans le bus
    idk "Excuse me... this is the last stop."
    "so tired i completly forgot i was there."
    u "...ah thank you for wake me up"
    "Thanks god my stop is the last one"
    #the player get off the bus and makes his way home
    idk "HEY ! you dropped your bus card."
    u " ah... shit thanks again."
    "I'm really not in my right mind tonight."
    "I look down at my bus card"
    "it's so worn that my name has been erased from it"
    u "...let's fix that."

    $ povname = renpy.input("my name...", length=32)
    $ povname = povname.strip()

    if not povname:
        $povname = "Maia"

    "[povname]"
    " ugh its late, my bed miss me so much, let's hurry up"
    #the player makes his way home
    " "
    " "
    "...finally home."
    menu:
        "lets sleep a little now":
            jump charlotte

label charlotte:
    "    "
    p "ugh... my head hurts."
    "I woke up slowly, my body aching."

    play music "audio/Charlotte-Theme.wav"

    "The memory of the night before came flooding back
    to me with a wave of panic."

    scene black
    with dissolve

    "I looked down at the ground"
    "I just remembered that i fell asleep here..."
    "..."
    "I wonder how long i slept"
    c "It's about time."

    show sprite1_charlotte

    "Charlotte..."
    "She was still there, staring at me from a distance without saying a word."
    c "You've been asleep for quite a while now."
    "It's like she can read minds"

    hide sprite1_charlotte

    menu:
        p " ... I need to see what time it is, it must be late, i shouldn't stay here too long."
        "*Search my phone*":
            jump phone
        "*Look at the time on my watch*":
            jump watch
        "*Ask Charlotte for the time*":
            jump charlotteuh

label phone:
    "It's probably in my bag"
    "..."
    p "ooh...Found it!"
    "...no battery uhh"
    " Guess the timing is just right."
    "And i guess there's nowhere i can plug it in around here..."
    return

label watch:
    "Wait it's...broken?"
    p "Shit..."
    "It must have happened when i fell down the stairs... I didn't even think to check..."
    return

label charlotteuh:
    p "Do you know what time it is by any chance ?"
    show sprite1_charlotte
    c "Seriously?"
    p "ah...my bad, that was a stupid question."

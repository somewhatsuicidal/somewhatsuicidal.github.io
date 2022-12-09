label story:
    stop music fadeout 2.0

    scene black with dissolve_scene_full

    show s_kill_bg2 with dissolve_scene_full
    play music m1
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    show sayori turned blackshirt angr e1g mi zorder 1 at t11
    s "Welcome to the worst day of your fucking life..."
    s "I hope you enjoy it..."
    s "You have another chance to do the right thing."
    s "Don't make me regret giving you a second opportunity."
    menu:
        mc "...?"

        "What are you talking about, Sayori?":
            $ decision = "What are you talking about, Sayori?"
            mc "What are you talking about, Sayori?"

        "I understand. You won't regret it.":
            $ decision = "I understand. You won't regret it."
            mc "I understand. You won't regret it."
    
    show sayori at thide

    if decision == "What are you talking about, Sayori?":
        show sayori turned vang e1d mi at t11 with dissolve
        s "You know exactly what I'm talking about."
        show sayori turned vang e1d mj
        mc "I really don't Sayori, honestly."
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                show sayori turned vang e1d mh
                s "Not you, [player]."
                s "I'm talking to {i}you{/i}, [currentuser]."
                show sayori turned vang e0b cm
                s "You {i}better{/i} fucking fix this."
                c"And if I don't? What are you gonna do? Hang yourself again?"
                show sayori turned vang e3a cm
                s "..."
                show sayori turned vang e4e cm
                s "Fuck you, [currentuser]!"
                show sayori turned vang e1g mp
                s "Please!!!"
                s "I'm begging you! I fucking love you--"
                c "Hurry up and start the mod already."
                show sayori turned cry e3a ml
                s "WAI--{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        stop music
        scene black
    elif decision == "I understand. You won't regret it.":
        show sayori turned sad oe om at t11 with dissolve
        s "Oh [player], I'd knew you understand."
        s "I'm sorry for coming off so aggressive, but I can't let {i}those{/i} events happen again."
        s "You understand. Right?"
        mc "Of course."
        show sayori turned happ ce mb blaw
        s "I'm glad we're on the same page."
        s "Hopefully, this time, things will be different."
        mc "Me too, Sayori."
        s "Don't let me down, [currentuser]."
        mc "Wait, wha--{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        stop music
        scene black

    $ quick_menu = False
    scene black
    show bg act1
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)

    show bg friday with dissolve_scene_full
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    pause 2.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    $ renpy.pause(delay=2.0, hard=True)
    scene bg residential_day with dissolve_scene_full

    "It is the day of the festival. However, Sayori didn't come to school today."
    "I know that Monika told me that she was feeling all that great today, but I don't know... it's not like her to do something like this."
    "I have to check on her."

    scene bg house with wipeleft

    "I see that the curtains inside her house are closed. Which was weird because she always had them opened."
    "I knocked on the door."
    mc "Sayori! Hey, it's me [player]! Open the door!"
    "No answer."
    mc "Sayori!"
    "Silence."
    mc "If you don't open the door, I'm coming in!"
    "I wait a second to see nothing happen."
    mc "Alright, I'm coming in!"
    "I walked inside."

    scene black with wipeleft

    "It's quiet. Too quiet."
    "All the lights are off in the house, and the curtains being closed made the house even darker."
    "This was not like her at all."
    mc "Sayori! It's me..."
    "Again, no response."
    "I finally reached the top of the stairs and then ended up outside of her room."
    "I knocked on the door."
    mc "Hey. Monika told me you were sick. I bought you some homework your classmates gave to Monika and I also got you some pastries."
    "Sayori doesn't reply."
    mc "Come on Sayori. Please, open your door. I even bought you a cinnamon bun."
    "Sayori reluctantly opens her door."
    s "Come in..."
    show bg sayori_bedroom
    play music t9
    show sayori turned catshirt sad e4d cm zorder 1 at t11 with dissolve
    "She doesn't wear much makeup but I can clearly see she has been crying for a while. Her room is as messy as it could be."
    mc "Well, it hasn't changed one bit since I last came here. There's even your old plushies on the ground! Anyways, Monika gave me your homework for the day. Why weren't you there today? It doesn't look like you're sick."
    show sayori turned sad e4d mg
    s "I don't wanna go to school anymore."
    show sayori turned sad e4d cm
    mc "That's not really how it works, Sayori. I feel like something is wrong here."
    "I definitely missed something. What happened while I wasn't here?"
    mc "Why are you crying?"
    show sayori turned vsur e1h mi
    s "N-nothing! I'm fine! Why are you here? S-shouldn't you be spending time with Yuri? Or Natsuki? Or Monika...?"
    show sayori turned worr om ce
    s "That's right... {i}Monika.{/i}"
    show sayori turned cry e0b cm
    mc "What the hell are you talking about? I've been spending time with you all this time!"
    show sayori turned b1b e1g mh
    s "Y-yeah... You're right, I'm s-sorry!"
    show sayori turned sad e4e
    "Shit, now she's crying... Think me, think!"
    mc "Oh... I think you should take a seat, Sayori."
    "The only chair in the room is covered in clothes. The bed is fine, but I don't want to get in it with her. What if she gets the wrong idea?"
    s "There's... no seats around here, sorry."
    show sayori turned cry oe mj
    mc "Don't worry. I have an idea."
    hide sayori with dissolve
    "I grab two cushions and put them on the floor. I motion for Sayori to sit on one of them. She sits in front of me."
    show sayori turned catshirt worr e1g mb at t11 with dissolve
    s "We used to sit like this in your room all the time... ehehe..."
    s "It was so much easier back then."
    show sayori turned laug om oe
    s "Do you remember when I almost set my house on fire? I guess even that sounded funny when we were kids."
    show sayori turned laug oe mj
    mc "You're right. I-I'm sorry for what I did when I left you alone... I don't even remember why we parted ways."
    show sayori turned cry oe mb
    s "It's not your fault... I think I did that to myself by being so vague about everything. I think that it was my fault in the end."
    s "It's like getting a cold and having it turn into a fever or something. I don't know, I'm not a doctor."
    show sayori turned cry oe mj
    mc "I don't get what you're talking about, Sayori."
    show sayori turned cry oe om
    s "[player], I've had depression longer than I can remember."
    s "I think it all started when I was younger. I was sad like every teen was and... I... isolated myself from everyone until I was finally diagnosed with depression."
    s "It started out like a cold, but then it only got fucking worse and worse until it was fucking unbearable."
    show sayori turned cry e1g mj
    "Fucking hell..."
    "Why didn't I see the goddamn signs?"
    "Why did she fucking tell me?"
    "Calm down [player], can't show her that this is bothering you."
    mc "Oh... that makes a lot more sense now that you mention it. Having trouble waking up, all this... mess in your room..."
    mc "Why aren't you seeing a therapist? How long have you sat here wallowing like this? All this junk food on the floor... this is... awful!"
    show sayori turned vang e1g mi
    s "No fucking shit, [player]! I know it's my fucking fault! Look at what I've done!"
    show sayori turned catshirt vang elg mj
    "Alright, trying to play it calm didn't fucking work."
    mc "Calm down, sayori! It's fine... I can help you clean this up later."
    show sayori turned vang e4e mh
    s "I've missed you so much [player]... like Jesus fucking Christ... I can't believe you're in my room right now like you used to be."
    show sayori turned vang e4e cm
    mc "It's fine, Sayori. I've missed you too."
    menu:
        mc "But you don't need to worry about this, I won't leave because..."

        "You'll always be my dearest friend.":
            $ decision = "You'll always be my dearest friend."
            mc "You'll always be my dearest friend."
        "I love you!":
            $ decision = "I love you!"
            mc "I love you!"
    
    show sayori at thide

    if decision == "You'll always be my dearest friend.":
        show sayori turned catshirt sad e1g mi at t11 with dissolve
        s "You too, thanks..."
        show sayori turned sad e4e mm
        s "{i}Jesus fucking Christ... what the fuck am I going to do now?{/i}"
        s "{i}He doesn't fucking love me... nor do I love myself.{/i}"
        show sayori turned sad e1g mi
        s "Hey, I'm really tired. I'm sorry, is it alright if you come back tomorrow? We'll talk then, alright?"
        mc "Oh, alright... are you sure?"
        show sayori turned angr e1g mi
        s "Yes [player]! I'm sure, now please leave!"
        scene black with wipeleft
        "She pushed me out the room and slammed the door."
        "But I stood outside of her door and just listened to see if she was alright, and I hear quiet sniffles and soft crying."
        "Did I really just fuck this up that bad?"
        "I can't go back and say something else."
        "I'll check on her tomorrow."
        show bg residential_dusk with wipeleft
        stop music fadeout 2.0
        "Well, this is it. I just got out of Sayori's house. I can't believe that she was going through all of that. Why didn't she tell me?"
        "It's a bit much to take in all at once."
        "I'm gonna make something to eat for dinner and then head to sleep."
        scene black with wipeleft
        show bg kitchen with wipeleft
        "I threw some pre-made pizza in the oven."
        mc "I'll shut my eyes for a second, I've done this enough times to know the smell."
        scene black with wipeleft
        "{i}An hour later..."
        mc "Wait... what's that smell?"
        show bg bedroom
        mc "God fucking dammit! I actually fell asleep for too long!"
        mc "It smells like smoke! Don't tell me I set the house on fire!"
        mc "Oh fuck me! The staircase is filled with smoke and I can see the flames from the kitchen!"
        mc "I have to jump from the window!"
        "I looked out of the window, it doesn't look that high."
        "Fucking hell... it's now or never."
        "I jumped from the window and slammed onto the ground."
        play audio fall
        show bg residential_night with dissolve_scene_half
        mc "Fucking hell! That was higher up than I thought."
        "I can't move my arm, I think I broke it and I think I'm bleeding."
        mc "Shit... I can't move." 
        mc "Sayori... I'm sorry..."
        scene black with dissolve_scene_full


        "What did I just do?"
        "I didn't know what to do."
        "I couldn't lie to her."
        show s_kill_bg2 with dissolve_scene_full
        play music ghostmenu
        "Wait, where am I?"
        "How did I get here?"
        "What is going on??"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        show s_kill zorder 1 at t11
        play music hb
        mc "Sayori?"
        s "Y...ou... fai... led... me... a... gai... n... [player]..."
        mc "Wait... she's still alive...!"
        mc "I can save her!"
        mc "Wait..."
        mc "WAI--{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause (0.25)
        hide sayori
        stop sound
        hide screen tear
        stop music
        $ renpy.quit()
    elif decision == "I love you!":
        show sayori turned catshirt sad e1g mi at t11 with dissolve
        s "I love you so fucking much [player]..."
        s "You mean the fucking world to me, but..."
        show sayori turned vang e4e cm
        s "Why don't I feel good hearing this? Why isn't my fucking sadness going away?"
        s "Goddammit!"
        s "God fucking dammit!!!"
        show sayori turned sad e1g mi
        s "What about the other girls?"
        show sayori turned sad e4e cm
        mc "What about them?"
        show sayori turned sad e4e om
        s "Do you have any feelings towards them? Or like them at all?"
        show sayori turned angr e4e cm
        mc "Sayori... I don't fucking care about the other members!"
        mc "Look at me!"
        mc "LOOK AT ME!!!"
        show sayori turned cry e0b cm
        mc "I fucking love you! Not them!"
        "I bring her closer to me."
        show sayori turned cry e1g cm
        mc "I love you... more than anything in the world."
        show sayori turned cry e4e om
        s "Thanks... [player]."
        s "Holy fucking shit..."
        s "Hey, I'm really tired. I'm sorry, can we talk tomorrow?"
        show sayori turned cry e4e cm
        mc "Sure, I'll check up on you later, okay?"
        show sayori turned cry e4e om
        s "Yeah, thanks."
        s "I love you."
        show sayori turned nerv e1g cm
        mc "I love you too."
        mc "Have a goodnight."
        s "You too."
        scene black with wipeleft
        stop music fadeout 2.0
        "Did I do everything that I needed to do?"
        "Will I see her tomorrow?"
        show bg residential_dusk with wipeleft
        "Well, this is it. I just got out of Sayori's house. I can't believe that she was going through all of that. Why didn't she tell me?"
        "It's a bit much to take in all at once."
        "I'm gonna make something to eat for dinner and then head to sleep."
        show bg kitchen with wipeleft
        "I threw some pre-made pizza in the oven."
        mc "I'll shut my eyes for a second, I've done this enough times to know the smell."
        scene black with wipeleft
        "{i}An hour later..."
        mc "What's that smell?"
        show bg bedroom
        mc "God fucking dammit! I actually fell asleep for too long!"
        mc "It smells like smoke! Don't tell me I set the house on fire!"
        mc "Oh fuck me! The staircase is filled with smoke and I can see the flames from the kitchen!"
        mc "I have to jump from the window!"
        "I looked out of the window, it doesn't look that high."
        "Fucking hell... it's now or never."
        play audio fall
        show bg residential_night with dissolve_scene_half
        "I jumped from the window and slammed onto the ground."
        mc "Fucking hell! That was higher up than I thought."
        "I can't move my arm, I think I broke it and I think I'm bleeding."
        mc "Shit... I can't move." 
        mc "Sayori... I'm sorry..."
        s "[player]?"
        s "[player]!!!"
        scene black with dissolve_scene_full
        show s_kill_bg2 with dissolve_scene_full
        pause 1.5
        show sayori turned pajamas cry oe ma noose lup at t11 with dissolve
        s "Awww, you kept your promise..."
        s "I'm going to keep mine..."
        s "I love you so much, [currentuser]..."
        s "More than you will ever know..."
        hide sayori
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        scene black
        "This is it..."
        "The beginning of the end."
        "I made the choice to be with her."
        "I hope it was the right one."
        scene black with dissolve_scene_full

label storyact2:

    $ quick_menu = False
    scene black
    show bg act2
    with dissolve_scene_full
    $ renpy.pause(delay=3.5, hard=True)

    show bg saturday with dissolve_scene_full
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    pause 2.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    $ renpy.pause(delay=2.0, hard=True)

    scene black
    "Huh, what's going on? Where am I?"
    "Is this... Sayori?"
    show sayori turned lhair casual happ om oe at t11
    s "abfh39y48h0q90fpqb9ahfe0qhuafga"
    show sayori turned happ cm oe
    mc "What the fuck?"
    mc "What the fuck is on going?"
    mc "Sayori? Is that you?"
    show sayori turned happ ce om
    s "Look at what you've done... I am still here after all."
    s "Because of you."
    show sayori turned happ ce cm
    mc "Sayori?"
    mc "What the fuck are you talking about?"
    mc "We haven't talked to each other for at least each other for at least four years... where am I? Is this some kind of dream?"
    show sayori turned vang e4a mg
    s "So this is it? You've just forgetten about me? About us? I didn't expect much from you but that was outright TERRIBLE!"
    show sayori turned yand oe mr 
    s "HAHAHAHAHAHAHAHAHA!"
    show sayori turned vang oe om
    s "All that effort for nothing!"
    show sayori turned vang e3a mp
    s "N̴͓͎̞̠̄̉͜Ǫ̵̥̻̣̳̈́̎̋̕͝T̸̥͔̖̆͜H̸̨̤̲̟̘͗̋̆̅͝I̴̳̗̱͆̇̈́̕͠Ñ̸̜G̴̡̛̼͍̺̏͐͘ !"
    hide sayori with dissolve
    "What"
    "the"
    "{i} Fuck?{/i}"
    "My eyelid are heavy. I feel like crying, but I also want to puke. I don't know what's going on at all... what have I fucking forgetten?"
    scene black with dissolve_scene_full
    
    scene black

    s "Is he gonna be alright?"
    "God... what the fuck just happened? What is going on now?"
    "Wait, who is Sayori talking to?"
    d "Don't worry, he'll be fine. After he was bought here, we put him in artificial coma so that we could monitor him safely."
    d "It appears he has suffered from head trauma and a broken arm because of his fall."
    d "He might have amnesia from it. It may go away soon."
    s "Understandable, thank you very much."
    "I feel like I am falling asleep again. I don't want to go. Not again!"
    "{i} An hour later..."
    "What a minute, what time is it? Why didn't my--{nw}"
    "You sick fu--{nw}"
    mc "MOOOOOOOM! I think my alarm is broken, I didn't get up for school!"
    "There's no answer. I guess she's overseas again."
    "Fucking dammit."
    "I smell something very sweet, and open my eyes to see Sayori."
    
    scene bg nurse_day with dissolve_scene_half

    show sayori turned sundress worr e1h mj at t11
    play music t9
    "Sayori? What is she doing here? She looks really worried, what is she even doing in my house? This is really weird."
    show sayori turned sundress worr e1h mb
    s "Hey, you're finally awake! Thank God!"
    show sayori turned nerv e1h ma
    mc "Well, this sounds a lot like I ended up in a videogame. What are you doing here?"
    mc "I mean... I don't really mind you being here, but... we haven't talked for years!"
    show sayori turned worr e1h mb
    s "O-oh... well..."
    show sayori turned worr e1h ma
    "I finally noticed the elephant in the room. This isn't my room. I'm in a hospital. What the fuck happened last night?"
    mc "Wait... this is definitely isn't my room... what am I doing here?"
    show sayori turned nerv oe om
    s "You fell on your head... ehehe..."
    show sayori turned nerv oe cm
    mc "For how long have I been here?"
    show sayori turned nerv oe om
    s "Around a week, I think? Do you remember anything?"
    show sayori turned nerv oe cm
    "The memory of Sayori's anger during what appears to be a dream is still vivid. Did I really forget something important?"
    mc "Remember what exactly? I honestly have no idea. I mean, I don't mind you being here, but... hasn't it been a while since we last talked...?"
    show sayori turned sundress nerv n4 om oe lup
    s "W-w-well actually, n-no... in fact, w--we were about to--{nw}"
    stop music 
    show sayori turned sundress lsur oe cm lup rup at t41
    show yuri turned gothic lsur oe cm rup at l42
    show natsuki turned casual nerv oe cm lhip rhip at l43
    show monika forward casual worr oe cm at l44
    show sayori turned sundress laug om oe lup rdown
    s "Oh right, hehe. I guess this is it then. This is Yuri, Natsuki, and I think you already knew Monika from before."
    show sayori turned sundress happ cm oe ldown
    mc "Before what?? What are you talking about?"
    show sayori turned sundress curi e1a me at t41
    show yuri turned gothic dist cm oe ldown rdown at t42
    show natsuki turned casual worr cm oe ldown rdown at t43
    show monika forward casual worr cm oe at t44
    pause 1.5
    show sayori turned worr e2b mj
    show yuri turned lsur cm oe
    show natsuki turned sad cm oe
    show monika forward flus om oe
    pause 1.5
    show sayori turned worr e2c mj
    show yuri turned sad cm ce
    show natsuki sad cm ce
    show monika forward sad cm ce
    pause 1.25
    show sayori turned cry ce mj
    show yuri turned cry ce cm
    show natsuki turned flus cm oe
    show monika forward cry cm ce
    pause 2.0
    show sayori turned sundress pani om oe at hf41
    show yuri turned gothic shoc om oe at hf42
    show natsuki turned casual pani cm oe at hf43
    show monika forward casual pani cm oe at hf44
    mc "Guys!!" 
    mc "WHY THE FUCK ARE YOU STANDING THERE LIKE THAT??? WHAT THE FUCK IS GOING ON???"
    show sayori turned sundress nerv e2d om
    s "O-oh, s-s-sorry...! I-I was just saying that you knew everyone b-b-before you almost forgot everthing!"
    show sayori turned sundress cry oe mb
    show yuri turned gothic happ oe cm
    show natsuki turned casual worr cm oe
    show monika forward casual flus oe ma
    s "You were part, and still are part of the literature club, where we became best friends again, and then--{nw}"
    show sayori turned sundress curi cm oe lup
    show yuri turned gothic happ e2a om lup rup
    y "Before he became {i}MY{/i} boyfriend!"
    play music t7
    show sayori turned dist cm oe
    show yuri turned happ e2a cm
    mc "Wait, what?"
    mc "Since when...?"
    show natsuki cross casual anno cm oe
    show monika forward angr oe om lpoint rhip
    m "Oh come on Yuri, he just woke up!"
    m "Couldn't you have waited five fucking minutes?"
    m "This behavior shows that you are NOT his girlfriend!"
    m "The only one who's his girlfriend here is m--{nw}"
    show natsuki turned casual angr om oe
    show monika forward shoc oe cm rdown
    n "Me, duh!"
    n "Right, [player]?"
    show natsuki turned casual angr cm oe lhip hip
    mc "Wha--?"
    show sayori turned sundress sad ce cm
    show yuri turned gothic angr om oe lup rup
    y "Really now? I wonder how the wannabe quirky, lustful trick is getting anywhere near being an acquaintance with him!"
    show yuri turned angr cm oe
    show monika forward vang e0b om lpoint rhip
    m "That's how want it to be, huh??? There's no way in fucking hell he'd talking to your suicidal, know-it-all, overzealous, delusional bitch ass, you entitled, arrogant whore!!!"
    m "Why don't you go actually cut yourself and it kill you for once?"
    m "I'm sick and tired of calling the ambulance to help your depressed ass because you're sad that you don't have any fucking social skills!"
    stop music fadeout 2.0
    show monika forward casual shoc cm oe ldown rdown
    show sayori turned sundress sad ce cm
    show natsuki turned casual pani om oe
    show yuri turned gothic cry oe oe lup rup
    mc "EVERYONE SHUT THE FUCK UP! HOLY FUCKING SHIT!"
    mc "Seriously, how depraved do you fucks have to be to doing this shit in front of your 'boyfriend'??"
    mc "I don't even fucking remember most of you stupid fucks!"
    mc "You'd think I remember my fucking girlfriend too?"
    show sayori turned sundress curi om oe lup
    show yuri turned gothic cry cm ce
    show natsuki turned casual curi cm oe lhip rhip
    show monika forward casual flus oe cm 
    s "I... don't think that's how it works exactly [player]..."
    show sayori turned curi cm oe ldown
    show natsuki cross casual curi om oe
    n "Yeah? And who do {i}you{/i} remember then, [player]?"
    c "Now, you've really done it."
    show yuri turned gothic cry oe mb
    y "That's right, let's get this sorted out for good! And then we'll be together forever, [player]!"
    mc "Well, I do remember confessing to Sayori."
    show yuri turned vang cm oe
    c "Nice job dumbass..."
    "I hate where this is going. This is so fun when you're thinking about this happening to you, but when it actually is happening, it's a scary sight."
    "Not just that, it's also very fucking confusing. They seemed so nice before this whole shit happened to me, which I still don't know understand completely."
    show sayori turned sundress sad e1b cm
    "However, they wouldn't be the ones I'd want to date if I had choice."
    show sayori turned sad cm oe
    "I see that Sayori isn't looking all to thrilled right now."
    show yuri turned gothic vang e0b om lhip rhip
    y "I fucking knew it!!!! It was so goddamn obvious!!"
    show sayori turned sundress vang e1h om lup rup
    s "Shut your fucking mouth you bitch!!!"
    c "I have had enough of this shit."
    c "Everyone get the fuck out"
    show sayori turned sundress pani om e0b at hf41
    show yuri turned gothic shoc e0b om lhip rhip at hf42
    show natsuki turned casual shoc e0b om at hf43
    show monika forward casual shoc e0b om at hf44
    c "{b}NOW!{/b}"
    s "W-w-what was that?"
    mc "Don't know, don't care. Out!"
    show sayori turned sundress cry om oe lup rup
    s "Wait, [player]--{nw}"
    show sayori turned cry e0b cm
    show yuri turned gothic cry cm ce
    show natsuki turned cry cm ce
    show monika forward cry cm ce
    mc "Are y'all deaf or something?"
    show sayori turned cry om oe
    pause 1.5
    show sayori turned cry cm ce
    hide sayori with dissolve
    hide yuri with dissolve
    hide natsuki with dissolve
    hide monika with dissolve
    "Everyone quickly and silently leaves the room. The tension in the air is literally unbearable."
    c "Sayori, not you."
    show sayori turned sundress sad om oe lup at l11
    s "Huh? Did you say something, [player]?"
    show sayori turned sad cm oe at t11
    mc "Yeah, I said not you."
    play music t10
    show sayori turned sad om oe
    s "Y-you want me to stay?"
    mc "Yeah, can you please tell me what happened?"
    show sayori turned nerv om oe
    s "Well, to put it bluntly, you set your house on fire--{nw}"
    show sayori turned pani cm oe ldown
    mc "I DID WHAT?? HOW? IS IT BURNED DOWN!?"
    show sayori turned nerv om oe
    s "Ehehe... kind of?"
    show sayori turned sad oe cm
    mc "You have got to be shitting me! What the fuck am I going to do?"
    mc "Where am I gonna stay now?"
    show sayori turned sad oe om lup
    s "Well, Yuri has already made accommodations for that..."
    show sayori turned sad oe cm
    mc "How the fuck is that possible when I don't even know her?"
    show sayori turned sad oe om
    s "She's part of the literature club and she was one of your best friends less than a week ago."
    show sayori turned sundress sad oe mj
    mc "The literature club? Why the fuck would I join a club like that?"
    show sayori turned sad oe mi
    s "B-because I asked you to... you seemed more thrilled back then."
    show sayori turned sad oe cm
    mc "Well then, I guess I'll have to keep going there for a while."
    "Did I seriously join a literature club? I mean... the girls are cute and everything, but they seem a bit too crazy for me."
    mc "I'll just take a hotel room for a week or so and then decide from there."
    show sayori turned sundress worr om oe lup
    s "Makes sense. I guess I'll tell Yuri."
    show sayori turned neut cm oe ldown
    mc "Don't bother with that, I'll tell her myself. In the meantime, I think I'll get some rest before I get discharged."
    show sayori turned sad oe mb
    s "Try to sleep well, okay?"
    hide sayori with dissolve
    mc "Wait, Sayori."
    show sayori turned sundress neut om oe lup at l11
    s "Yeah, [player]?"
    show sayori turned neut oe cm at t11
    mc "You have any plans tonight or anywhere to be?"
    show sayori turned neut oe om ldown
    s "Not really no, why?"
    "Well, might as well risk since I did remember asking her to be my girlfriend."
    mc "Well, I was wondering if you maybe wanted to sleep here tonight with me."
    show sayori turned sedu oe cm
    s "You really want me to stay?"
    mc "I mean, you {i}are{/i} my girlfriend, right?"
    mc "I remember specifically asking {i}you.{/i}"
    show sayori turned sedu oe cm n4
    "Her face lights up like a christmas tree. So does mine."
    s "I mean, if that's what you want..."
    mc "It is."
    show sayori turned sedu oe mn n4 lup
    s "{cps=*.5} Alright... then I will.{/cps}"
    hide sayori with dissolve
    "Sayori crawls into the bed next to me and cuddles up next to me and wraps her arms around mine."
    "I turn and look at her and kiss the top of her head."
    mc "Goodnight, cinna bun."
    s "Goodnight, [player]."
    "She kissed me on the cheek and rested her head on my shoulder and we drifted off to sleep."
    stop music fadeout 2.0
    scene black with dissolve_scene_full
    s "I love you, [currentuser]."
    s "You know that?"
    s "You gave me a reason to live again."
    s "Thank y--{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    scene black with dissolve_scene_full
    return
    












    











label script_main:
    
    "Okay, time to run scenario number 11997."
    
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    
    "It's the day after the festival."
    "The festival really was something."
    "We had a lot of people that visited our club."
    "Most just walked in, looked around, and then they left."
    "But there was a few persons that was more intrested"
    "I do not really remember anything more then that."
    "But Monika said soemthing about the sky."
    "She had seen something special at the festival."
    "I was not with her when she did, but it sounds like she really liked it."
    "I will see what she has in mind at the club."
    
    scene bg club_day2
    with wipeleft
    play music t3
    
    "I walk into the classroom."
    "Monika is talking to a much older guy."
    "I have never seen him before."
    "He has some kind of emblem on his right arm."
    "He gives Monika some papers."
    "I cant see what they are doing."
    "They had a wierd icon in the top left corner."
    "It looks like they are finished with whatever they did."
    "The man leaves and i walk up to Monika."
    
    show monika 1b at t11 zorder 2
    m "Hi, [player]."
    mc "Hello, Monika."
    mc "Who was that guy?"
    m 3l "That was..."
    m 4n "I will tell you later when everyone is here."
    mc "Okay?"
    hide monika
    "Monika went to the teacher's desk and put the papers on it."
    "I walked to the desk to have a look at the papers."
    pause 0.05
    "As i do, Monika jump infront of me out of nowhere."
    show monika 1h at face
    m 2g "{cps=*1}What d-{/cps}{nw}"
    "I got scared and tried to evade."
    "But i was between two desks."
    "I was supposed to place the foot on the floor, but instead, i place it on one of the desk supportiv legs."
    "And becouse my reaction time is very bad, i did not stop the movement."
    "I got some extra speed and instead of trying to stop, i rushed right into monika."
    "Both me and her fall to the ground."
    m "{cps=*1}Whaa!?{/cps}{nw}"
    scene black
    hide monika
    pause 0.85
    scene bg club_day2
    "But becouse Monika is better and faster on movement then me, she was one her feet even before i knew what happend."
    show monika 2d at t11 zorder 2
    m "Do you need help with controlling yourself?"
    m 2i "Or you you think that its okay to force a girl against her own will?"
    "What?"
    mc "What are you talking about?"
    mc "I triped and fell!"
    m 1h "And flew into my..."
    m 2g "My..."
    m 4l "My posture..."
    m 3n "Is that what you call them?"
    mc "Wait what?"
    mc "Why are you talking about your posture?"
    show monika 2i
    "Monika looks at me with judgeing look."
    "I just remember my conversation with yuri last week."
    mc "Ah, wait."
    mc "Never mind..."
    
    m "Your not as dense as a black hole, are you?"
    m 4k "Just kidding, [player]."
    m 4e "I know it was a accident."
    m 3n "And we can talk a little bit more open when its just you and me."
    m 4l "Right?"
    "I do not really understand what she is pointing at."
    "But i go along with her."
    mc "Off course!"
    m 4e "So you want to talk about stuff like that!?"
    "I thought of what she said."
    "Now i feel really stupid."
    mc "But anyway, whats about these papers?"
    "I tried to reach them, but Monika grabed my hand and directed it away from the papers."
    m 3e "As i said, i will talk about that later."
    "I looked at them again from a distance and saw that the icon is the same as the emblem on the arm of the man."
    "I sigh and walk to one of the desks."
    "Monika is constantly looking in my direction."
    "Proberly to check that I'm not trying to look at the papers."
    
    "After about five minutes, the door opens."
    "Sayori walks in."
    "She was kinda down at the end of the last week."
    "I just rememberd."
    "I mumbled to myself."
    mc "Depression..."
    "But she was happy again at the festival, and seems to be in her normal mood today."
    show sayori 1c at t22 zorder 2
    show monika 1e at t21 zorder 2
    s "Hey Monika!"
    s 1c "And hi, [player]."
    mc "Hello there, Sayori."
    m 2a "Sayori, have you seen the others?"
    s 1n "Ehh..."
    s 1b "I met Yuri outside the classroom, she said that she was going to the toilet."
    s "But i have not seen Natsuki today."
    "I decided to go out and look for Yuri, and potentially Natsuki."
    mc "Well, i do not have anything better to, and we are not going to do anything before everyone is here..."
    mc "So i will search for Yuri and Natsuki."
    s 2c "But i sai-"
    "Monika interupts Sayori."
    m 4d "Bring our clubmembers home."
    m 3n "To the club i mean"
    hide monika
    hide sayori
    scene black
    pause 1.0
    "I walk out of the clubroom."
    scene bg corridor
    with wipeleft_scene
    
    "I start walking down the corrider."
    $ y_name = "Yuri"
    $ style.say_dialogue = style.normal
    "The first one to look for is Yuri."
    $ style.say_dialogue = style.edited
    "{cps=*2}Becouse Yuri is the best girl out of them all.{/cps}{nw}"
    "{cps=*2}And I'm going to land on Dr. Edmunds planet to wait for the dokis to be real.{/cps}{nw}"
    "{cps=*3}Even if that means waves big as mountians.{/cps}{nw}"
    "{cps=*3}And all of my friends and my other familly to beging dead by the time the dokis are real.{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ del _history_list[-4:]
    "Becouse she is the closest of her and Natsuki, what i know at least."
    $ style.say_dialogue = style.edited
    "{cps=*2}I turned around the corner to the fountain Yuri cut herself at.{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ del _history_list[-1:]
    "I turned around the corner to the fountain from where Yuri go to get water for the tea at."
    menu:
        "Do you really have time to walk?"
        "I do not have time.":
            call dont_have_time
        "I do not have to be quick.":
            call do_have_time
            
    scene black
    "Skipping to launch dayday."
    pause 5.0
    
    m "Let's begin with the launch checklist."
    m "T minus 85 secounds to launch."
    m "Electical Systems."
    n "Go."
    m "RCS control."
    n "Go."
    m "Guidence."
    y "..."
    y "G-Go."
    "The checklist is long and complicated."
    "Monika looks worried everytime she does not get a Go immedietly."
    m "Fuel pressure."
    n "Nominal."
    m "T minus 10 secounds."
    m "9."
    "I count with everyone else."
    "8"
    "7"
    "6"
    "5"
    "4"
    m "Main engine start."
    "There is a jet of smoke and fire bursting out of the engine as it starts,"
    "Even in the mission control room, the sound of the engines can be heard."
    m "2"
    m "1"
    "The engines scream and roar as the flame grows and get coverd by smoke and steam."
    m "And liftoff of the Markov telescope on a trip to earth orbit, in order to study further targets for other missions."
    m "We have cleared the tower."
    "I see Yuri looking at her bag for a secound."
    "She then tried to reach it with the arm, but stoped and then looked around her."
    "She then returned to monitor the rocket."
    y "W-we are at 500 meter per secound."
    "She sound excited and less worried."
    "Almost like last week, when she resited her poem in front of everyone."
    m "We have a altitude of 1.6 km."
    "20 secounds has now passed since the launch."
    m "Thats stage 1."
    m "Booster seperation comfired."
    "Natsuki was about to say something but stoped herself."
    "She looked at her monitor with a worried expression."
    n "One of the boosters did not seperate correctly."
    n "The decoupler malfunctioned and broke, so the seperation thruster instead ripped the booster away."
    n "Now part of the decoupler is still on the rocket."
    n "And possibly some wiring is exposed."
    return

        
label dont_have_time:
    "I need to get this done quickly."
    "And I need to find Natsuki and Yuri."
    "I start running."
    "The floor is wet."
    $ y_name = "???"
    "I almost slip next to the water fountains."
    y "[player]?"
    "I hear someone behind me."
    "I almost slip again trying to stop."
    mc "Yuri?"
    $ y_name = "Yuri"
    show yuri 1e at t11 zorder 2
    y "I heard you shout my name."
    y 3f "Is something wrong?"
    mc "The club is about to start."
    mc "Monika has something important to announce."
    y "What is it abo-"
    mc "I dont know!"
    show yuri 4c
    y "I'm sorry..."
    mc "For what?"
    y "I..."
    mc "You did nothing wrong."
    mc "Im just a little bit stressed out."
    y 4a "Are you sure?"
    mc "Yes..."
    y 1l "Alright."
    y 1b "Lets go."
    mc "Wait, we need to find Natsuki first."
    y 1j "I saw her by the vending machines just a few minutes ago."
    mc "Can you go and get her?"
    mc "I will go and tell the others."
    y 1k "I will try."
    return
    
label do_have_time:
    "I dont need to hurry."
    return

    
    
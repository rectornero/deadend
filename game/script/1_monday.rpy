# CHAPTER 1: QUIETUS #

label monday:

    label lunedi_casa:
        scene appartamento pomeriggio with fade
        play music audio.light_serenita
        pause 1.0
        "Aaah!{w=0.5} Back to my everday life again!"
        "I really need to get out and in touch with reality. I also feel that I'm getting back part of my memories."
        "This morning, for instance, I just have remembered how I loved going out with Ed and Bianca."
        "It always feels refreshing and intriguing at the same time. This is the reason why we get along so well."
        "If we're lucky, we're gonna find also Norman, there. He should be on shift."
        "We use to call him \"Newsman\", or \"Newz\", for short, as he seems to know pretty much everything about anything new around our place."
        "He's a [nome_scuola] student too."
        "..."
        "It's 15:30, and there's still no trace of Edward."
        "Bianca always has her share of reason, no matter what."
        "..."
        "Maybe I should call him..."

        play sound audio.umani_passi fadein 2.0
        pause 2.0
        show edward shocked_1 with dissolve
        stop sound

        e wink_1 "Hey, man! Here I am!"
        m "Oh, here you are! We're late, y'know! Bianca's gonna lecture us again..."
        e smile_4 "Oh, she's gonna lecture us anyways on something, so I thought being late could be the nicer one!"
        e "Don't worry that much, bro! Aren't you used to this?"
        m "Oh, well... y-yeah, think so..."
        "I don't remember I ever got used to it, but, anyways..."
        e urgh_1 "Oh... sorry. You must being still struggling with getting back your memories..."
        m "No, don't worry. I feel it's getting better and better."
        e shocked_1 "Really?"
        e smile_1 "Really?{fast} I'm glad about that."
        m "Yeah, so, are you ready to go?"
        e smile_3 "But of course! Let's get going!"

    label lunedi:
        scene sottopassaggio giorno with fade
        play music audio.mezzi_macchina_interno_ovattato
        m "So, how far are we from Cafè Memoria, exactly?"
        e "It's about 20 minutes. We'll make it, don't worry! I was joking about arriving late, before."
        m "Nice!"

        scene cafe strada pomeriggio with fade
        e "Here we are!"
        stop music
        play sound audio.umani_passi
        pause 0.5
        stop sound
        m "Are we meeting inside?"
        e "We usually meet outside, I think we'll find Bianca there."

        scene cafe nordf pomeriggio with fade
        show bianca default_1 at cright with dissolve
        play music audio.light_amici
        pause 1.0
        show edward default_1 at cleft with dissolve

        b smile_1 "You're on time, I'm impressed!"
        show edward at front
        show bianca at rear
        e smile_3 "See? This time I did my best to bring you [nome_protagonista] as soon as I could!"
        show bianca at front
        show edward at rear
        b smile_3 "Nice to see. I hope it can become an habit from now on!"
        b default_1 "How do you feel today, [nome_protagonista]?"
        m "Fine, thanks. I'm glad to see you here, I really miss this place."
        b "So, I can assume you're getting some of your memory back. That's good news."
        show edward at front
        show bianca at rear
        e smile_1 "Are we waiting for someone else?"
        show bianca at front
        show edward at rear
        b "No, but we have Newz- I mean, Norman inside. He's waiting for us."
        m "Feel free to use our nicks'n'stuff, Bianca. I do remember Norman's nick, and it can help me gathering back something else."
        b shock_3 "Oh. By all means, then!"
        b default_1 "Very nice, let's get in!"




        scene cafe interno nordf pomeriggio with fade
        play sound audio.porta_campanelle
        show bianca default_1
        pause 0.5
        stop sound
        show edward smile_1 at right
        e "Hey, Newz! Come and see who've brought back!"
        show norman default_1 at left with easeinleft
        n "Hey. So you've made it."
        m "Y-yes, as you can see!"
        show bianca at front
        b angry_4 "Norman! Can you say such things after what have happened to [nome_protagonista]?"
        show norman at front
        show bianca at rear
        n "I can, as he's made it. Cannot talk to dead guys, so..."
        show bianca at front
        show norman at rear
        b angry_8 "Norman, stop it!"
        m "Easy, Bianca, I'm used to Newz's ways. I think they're awkwardly comfy."
        show norman at front
        show bianca at rear
        n smile_2 "Yeah, tell her. I'm fuckin' comfy."
        show edward smile_6 at right
        show bianca at front
        show norman at rear
        b embarassed_1 "O-okay, now please stop, both of you! And, Newz, you're not comfy at all!"
        show edward at front
        show bianca at rear
        e smile_5 "I know how this is going..."
        stop music fadeout 3.0
        play music audio.light_situazione_buffa fadein 5.0
        show edward at rear
        show norman at front
        n surprised_1 "You say this as I'm something - I mean, someone you laid on! Y'know, it's not something I'd speak that loud."
        show bianca at front
        show norman at rear
        b shock_2 "W-WHAT?! Norman, quit this, already!!"
        show edward at front
        show bianca at rear
        e smile_4 "Here he goes!"
        show bianca at front
        show edward at rear
        b embarassed_4 "[nome_protagonista], please, help me stop them..."

        menu:
            "Yeah Newz, please stop. *laughs*":
                b embarassed_5 "I hate you, all of you..."
            "Easy, Newz, you know that she's not talking with us for a while, if we keep this for too long.":
                b pissed_3 "You bet it."
            "Yeah, stop Newz, y'know I'm jealous.":
                b shock_2 "Wait, what...? You are joking, right?"
                show norman at front
                show bianca at rear
                n wink_1 "Cool, man! The lady's all yours!"
                show edward at front
                show norman at rear
                e surprised_1 "...and I never realised that! Am I sleeping, or what?"
                show bianca at front
                show edward at rear
                b embarassed_5 "Please, stop now, really..."

        stop music fadeout 0.5
        play music audio.light_amici fadein 2.0
        show bianca at front
        b lookaway_2 "Now that we've lost all this useful time, what do you think about sitting down and drinking some tea?"
        show norman at front
        show bianca at rear
        n frown_1 "'bout that, guys."
        show edward at front
        show norman at rear
        e surprised_1 "Hm?"
        show norman at front
        show edward at rear
        n frown_1 "Got some news."
        show bianca at front
        show norman at rear
        b unimpressed_1 "No news, here."
        show norman at front
        show bianca at rear
        n frown_1 "Hot news. I'm serious."
        show bianca at front
        show norman at rear
        b talk_1 "Oh. Well, let's sit, then."
        scene cafe interno sudest pomeriggio with fade
        stop music fadeout 0.5
        play music audio.myst_indagini fadein 2.0
        show norman default_1
        show bianca default_1 at left
        show edward default_1 at right
        n default_1 "Listen up. Yesterday, 't was evening, was my free day."
        n "Was spendin' it 'round here. Seems there's nothing to do: no girls around, few old people chatting. Boring situation. So, I went out walkin'."
        scene cafe ovest sera bn with fade
        n default_1 "That's when I saw a guy with phones talking with a little flower."
        show elise shadowed_1 at ccleft
        show gain shadowed_1 at ccright
        with dissolve
        b angry_1 "If you made up all this because you want to talk about another lady, Norman, I..."
        e glare_1 "Wait, Bianca. I'm sure there's more."
        "So do I... I just feel the vibes."
        n default_1 "So, that lil' flower, let's call her Lily, and Phony are talking. Then Phony just grab her and hides in the back alley."
        hide elise
        hide gain
        with moveoutright
        e glare_1 "Things are getting hot."
        m "Yeah, you can bet."
        b lookaway_3 "..."
        n frown_1 "That's when I decided to follow them."
        m "If I may, News, why have you felt this compelled...?"
        n frown_1 "Somehing fryin'."
        b lookaway_2 "Yeah, the curiosity of a perv."
        e glare_1 "Sssh! Go on!"
        scene cafe retro sera bn with fade
        n "Got there, and... well, Lily was just gone. Disappeared."
        e glare_1 "And Phony?"
        show gain shadowed_1_sit at rearcenter with dissolve
        n "Phony was still there. Lookin' straight to his feet."
        b default_1 "On his feet? What do you mean?"
        b "He seemed like... looking for something."
        b "Did you manage to discover what it was, exactly?"
        n frown_1 "No, but luck was by my side. Somethin' told me that people just don't disappear, and came back to the entrance."
        scene cafe ovest sera bn with fade
        n "There, I found Lily. She was alone, absent-minded."
        show elise shadowed_1 at center with dissolve
        m "So you asked her out?"
        n wink_1 "Of course I did. I mean, she is a pretty lil'flower. I did it with the appropriate touch."
        e smirk_1 "So, you mean you asked her to get in M and take somethin', or what?"
        n smirk_1 "Uniform."
        e default_1 "Hm?"
        n smile_1 "She had our uniforms. It was plain easy. I discovered that she's a first-year too. I also know her class, her phone number, and... well, her name."
        scene cafe interno sudest pomeriggio with fade
        show norman default_1
        show bianca default_1 at left
        show edward default_1 at right
        show bianca at front
        b lookaway_1 "... So, this means she really is called Lily?"
        show norman at front
        show bianca at rear
        n default_1 "For me, she's Lily. I think she also likes it. You should call her Lily, while on the ground."
        m "Are you callin' us out for work?"
        n wink_1 "So, you do remember the few important things of life. Yeah, squad. I want you to investigate."
        show bianca at front
        show norman at rear
        b default_2 "Investigate... on what, exactly? You know, there wasn't anything special about those two."
        show norman at front
        show bianca at rear
        n default_1 "Let me finish the story. Talkin' with Lily, I found out that she has a prob."
        m "Which is...?"
        n smirk_1 "It seems she has lost her memory."
        show bianca at front
        show norman at rear
        b shock_1 "Are you serious, here?"
        show norman at front
        show bianca at rear
        n default_1 "To'lly."
        m "Wow. And did you get how she lost it?"
        n default_1 "Not how, but I found out WHERE. And that's the point."
        show edward at front
        show norman at rear
        e surprised_1 "Don't tell me."
        show norman at front
        show edward at rear
        n smile_1 "Oh, I sure tell you. 't was there."
        scene cafe retro sera bn with fade
        pause 0.5
        scene cafe interno sudest pomeriggio with fade
        show norman default_1
        show bianca default_1 at left
        show edward default_1 at right
        m "How could you find out something THAT important just stalkin' -{w=0.5} I mean, snooping around?"
        show norman at front
        n smirk_1 "I'd say I just... feel the vibes."
        m "Oh. Kay-kay, we actually call you Newz for a reason."
        n smile_1 "Yeah. Do you all feel ready? You must uncover what Phony's hidin'."
        show bianca at front
        show norman at rear
        b default_2 "Why him? We have the girl."
        b default_1 "... No, I think I get it. You want us to go after Phony, as he's the one that still retains memories. And you think that he may know something about Lily that can come in handy for us. Am I correct?"
        show norman at front
        show bianca at rear
        n default_1 "You are."
        show bianca at front
        show norman at rear
        b "There's still one thing that's bugging me. Do you know what ties Lily with Phony? Also, do you know this \"Phony\"'s name?"
        show norman at front
        show bianca at rear
        n default_1 "What do you think?"
        show bianca at front
        show norman at rear
        b lookaway_1 "I think you know both, but you're not telling, as you like keeping the important facts as long as possible from us to know. This time I won't ask if I'm right, as I am."
        show norman at front
        show bianca at rear
        n smile_1 "Brilliant, as always. Yes, I know both. BUT!{w=0.5} I won't tell you."
        show edward at front
        show bianca at rear
        e surprised_1 "But why? We need to know those things!"
        show bianca at front
        show edward at rear
        b default_1 "He's not telling, as he want us to behave as we don't know Phony. He thinks we must get information from Lily as blindly as possible. As it makes everything natural."
        show norman at front
        show bianca at rear
        n smile_2 "I love her when she is my subs."
        show bianca at front
        show norman at rear
        b angry_8 "I'm not your subs!"
        show norman at front
        show bianca at rear
        n smile_1 "Just jokin', sweetie. You're exceptional. Your mind is enchanting."
        show bianca at front
        show norman at rear
        b embarassed_1 "I'm not exceptional...! I mean...{w=0.3} well, you shouldn't flatter me, as... uhm, I..."
        m "Well, he's right. You're brilliant, Bianca."
        b "Oh... okay, thanks, but..."
        show edward at front
        show bianca at rear
        e smile_4 "Hahaha. He made it again."
        show bianca at front
        show edward at rear
        b "... Okay! So, now, we should get forward."
        stop music fadeout 2.0
        play music audio.myst_il_piano fadein 2.0
        show norman at front
        show bianca at rear
        n smile_1 "Well said! [nome_protagonista], do you remember what happens now?"
        m "I think... we agree on something?"
        n "You're close. Now there's the voting. Which means that everybody calls himself in or out. If we have the majority, we state a plan! After that, we begin our investigations. And finally..."
        show edward at front
        show norman at rear
        e "Finally, we get what we want. Do you remember, [nome_protagonista]?"
        "Not exactly..."
        m "Uhm, what do you mean by \"what we want\"?"
        show norman at front
        show edward at rear
        n smile_2 "Liter'ly that."
        show bianca at front
        show norman at rear
        b lookaway_3 "I often ask myself why am I in a group like this."
        show norman at front
        show bianca at rear
        n default_1 "That one's easy: we couldn't make what we're gonna do now."

        m "You mean the plan?"
        n default_1 "Indeed. Bianca is our intel."
        show bianca at front
        show norman at rear
        b default_1 "Whatever. Let's start this."
        "Norman has handed out some white notes. I think I must fill this with my vote."
        centered "{color=#000000}{size=80}{b}{cps=10}PHASE 1: VOTING{/cps}{/b}{/size}{/color}"
        show bianca at rear
        show norman at front
        menu:
            n "Everyone: do you agree on carrying this out?"
            "Yes":
                $vote_1 = "y"
            "No":
                $vote_1 = "n"

        n "Very good. So now, let's see... we have..."

        if vote_1 == "y":
            n "...4 yes, 0 no. Very well guys."
        if vote_1 == "n":
            n "...3 yes, 1 no. The majority needs to convince the minority."

        n "Are you all ready?"

        show norman at rear
        show edward at front
        e smile_1 "Ready when you are!"
        show bianca at front
        show edward at rear
        b "Yes, I'm ready."

        if vote_1 == "y":
            m "Of course. Let's do this."
        if vote_1 == "n":
            m "... Okay, let's see."

        scene cafe interno sudest pomeriggio
        stop music
        centered "{color=#000000}{size=80}{b}{cps=10}PHASE 2: INFORMATION SHARING{/cps}{/b}{/size}{/color}"

        show norman smirk_1
        show bianca default_1 at left
        show edward default_1 at right

        show norman at front

        play music audio.myst_infiltrazione

        label is_q1:

        ### QUESTION 1 ###
        # Options: 3
        # Time: 3
        ##################

            $ time = 3
            $ timer_range = 3
            $ timer_jump = "is_q1_timeout"
            n "So, let's warm up a bit! What is the name of the girl?"
            show screen countdown
            menu:
                n "What's is the name of the person we're lookin' for?{fast}"
                "Phony":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n surprised_1 "How can a girl be called \"Phony\"? It's rude!"
                    b lookaway_1 "I'd expect anything from you, guys. Especially from you, Newz."
                    n impressed_1 "I'd never do that!"
                    b default_1 "By the way, he never told us her name. We may ask for her name when we meet her, though."
                    n angry_1 "No, you should call her \"Lily\", as I already told you before!"
                    b unimpressed_1 "Yeah, yeah, whatever."
                    jump is_q2
                "Lily":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n smirk_1 "That's how I call her, but her true name is \"Lizzy\"!"
                    show bianca at front
                    show norman at rear
                    b lookaway_1 "He just isn't telling us. No matter how hard we try. We may ask for her name when we meet her, though."
                    n angry_1 "No, you should call her \"Lily\", as I already told you before!"
                    b unimpressed_1 "Yeah, yeah, whatever."
                    jump is_q2
                "You didn't tell":
                    hide screen countdown
                    play sound audio.quiz_esatto
                    n smile_2 "Nice, that's your first hit!"
                    $ plan_phase_1_score += 1
                    jump is_q2

        label is_q1_timeout:
            b default_1 "The name's Elise."
            n "That's correct. [nome_protagonista] follow our intel's example, and answer quick!"

        label is_q2:
        ### QUESTION 2 ###
        # Options: 3
        # Time: 5
        ##################
            $ time = 5
            $ timer_range = 5
            $ timer_jump = "is_q2_timeout"
            n "Okay now. What is your final objective?"
            show screen countdown
            menu:
                n "Okay now. What is our final objective?{fast}"
                "Talk with Elise and find out what has happened to her":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n smile_1 "Sorry, that's wrong!"
                    e surprised_1 "Really?"
                    b "Yes, it's partially wrong. The only one that may know what happened to Lily is Phony."
                    b "We must grasp the truth using the information he has."
                    jump is_q3
                "Talk with Phony and find out what has happened to Elise":
                    hide screen countdown
                    play sound audio.quiz_esatto
                    n "You're smart. Nice job."
                    $ plan_phase_1_score += 1
                    jump is_q3
                "Ask the girl out, of course":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n smile_3 "Hahaha, nice one."
                    b lookaway_1 "We must get acquainted with Phony, and find out what has happened to Elise."
                    n smile_1 "Yeah, that's right, but the [nome_protagonista] is funnier. I love him."
                    jump is_q3
        label is_q2_timeout:
            b default_1 "We must get acquainted with Phony, and find out what has happened to Elise."
            e "Oh, right. That was tough."
        label is_q3:
        ### QUESTION 3 ###
        # Options: 3
        # Time: 5
        ##################
            $ time = 5
            $ timer_range = 5
            $ timer_jump = "is_q3_timerout"
            n "How are you gonna make Phony spill what we want to know?"
            show screen countdown
            menu:
                n "How are you gonna make Phony spill what we want to know?{fast}"
                "We break into his house and threaten him":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n frown_1 "Bold, but too straightforward, don't you think?"
                    e disagree_1 "Also, a bit illegal, you know?"
                    n frown_1 "That's not the point."
                    b angry_4 "It IS the point, Norman."
                    n awkward_1 "You guys should be more flexible!"
                    b default_1 "We should make Lily introduce him to us. It may be hard, though."
                    n smile_1 "That's right. This is the reason we're plannin'!"
                    e smile_1 "Nothin' is hard for us. Just... complex. Right, Newz?"
                    n smile_2 "To'lly right."
                    jump is_q4
                "We look for him at school, it shouldn't be difficult":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n default_1 "If this was this easy, we wouldn't plan."
                    e "I think Phony is not telling us something that important, if we cannot find a workaround of sort."
                    b default_1 "We should make Elise introduce him to us. It may be hard, though."
                    n smile_1 "That's right. This is the reason we're plannin'!"
                    e smile_1 "Nothin' is hard for us. Just... complex. Right, Newz?"
                    n smile_2 "To'lly right."
                    jump is_q4
                "Making Lily bring him to us, someway":
                    hide screen countdown
                    play sound audio.quiz_esatto
                    n "That's right."
                    b default_1 "It may be hard, though."
                    n smile_1 "That's right. This is the reason we're plannin'!"
                    e smile_1 "Nothin' is hard for us. Just... complex. Right, Newz?"
                    n smile_2 "To'lly right."
                    $ plan_phase_1_score += 1
                    jump is_q4
        label is_q3_timeout:
            b default_1 "We should make Elise introduce him to us. It may be hard, though."
            n smile_1 "That's right. This is the reason we're plannin'!"
            e smile_1 "Nothin' is hard for us. Just... complex. Right, Newz?"
            n smile_2 "To'lly right."
        label is_q4:
        ### QUESTION 4 ###
        # Options: 4
        # Time: 5
        ##################
            $ time = 5
            $ timer_range = 5
            $ timer_jump = "is_q4_timeout"
            n "What data do we have on Lily?"
            show screen countdown
            menu:
                n "What data do we have on Lily?{fast}"
                "Name, school, phone number, home address":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n surprised_1 "I should have asked for her home address too, y'right!"
                    e surprised_1 "And you think she would have answered to that, too?"
                    b lookaway_1 "You guys should be serious during information recap, you know?"
                    b default_1 "We have her name, school, class and phone number."
                    n smirk_1 "Well, actually, it's me that has her phone number, not you."
                    e disagree_1 "Newz, you shouldn't keep all the girl for you, y'know...?"
                    b unimpressed_1 "... Just stop."
                    jump is_q5
                "Name, school, class, phone number":
                    hide screen countdown
                    play sound audio.quiz_esatto
                    b default_1 "I think this is right."
                    n smile_1 "And you both think right!"
                    $ plan_phase_1_score += 1
                    jump is_q5
                "Name, school, class, home address":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n surprised_1 "I should have asked for her home address too, y'right!"
                    e surprised_1 "And you think she would have answered to that, too?"
                    b lookaway_1 "You guys should be serious during information recap, you know?"
                    b default_1 "We have her name, school, class and phone number."
                    n smirk "Well, actually, I have her phone number, not you."
                    e disagree_1 "Newz, you shouldn't keep all the girl for you, y'know...?"
                    b unimpressed "... Just stop."
                    jump is_q5
        label is_q4_timeout:
            b default_1 "We have her name, school, class and phone number."
            n smirk "Well, actually, I have her phone number, not you."
            e disagree_1 "Newz, you shouldn't keep all the girl for you, y'know...?"
            b lookaway_1 "You guys should be serious during information recap, you know?"
        label is_q5:
        ### QUESTION 5 ###
        # Options: 4
        # Time: 5
        ##################
            $ time = 5
            $ timer_range = 5
            $ timer_jump = "is_q5_timeout"
            n "Final one! Where did Lily said she lost her memory?"
            show screen countdown
            menu:
                n "{fast}"
                "Near M":
                    hide screen countdown
                    play sound audio.quiz_esatto
                    n smile_1 "Bingo! Well played."
                    $ plan_phase_1_score += 1
                    jump is_q_end
                "This is what we must find out!":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n frown_1 "This is what I DID find out! It's important detail, y'know, you should keep it in mind!"
                    jump is_q_end
                "At school":
                    hide screen countdown
                    play sound audio.quiz_errato
                    n frown_1 "Wrong! It was behind M, in the back alley!"
                    b talk_1 "This is important detail, y'know, you should keep it in mind!"
                    jump is_q_end
        label is_q5_timeout:
            b default_1 "If I remind correctly, you said this happened in the alley behind M."
            n smile "You always remind things correctly, Bianca."

        label is_q_end:
            stop music fadeout 2.0
            n "Well, we're done!"
            e surprised_1 "That was quick!"
            b smile_1 "Very well, now we all recalled and shared the information we need."
            b default_1 "Now we should proceed onto the next phase, where I'll do my best to give you the intel you need."
            b smile_3 "So, let's start with the \"Plan Definition\" phase!"
            centered "{color=#000000}{size=80}{b}{cps=10}PHASE 3: PLAN DEFINITION{/cps}{/b}{/size}{/color}"
            play music audio.myst_indagini_allegra fadein 2.0
            b "Very well. First of all, we want to meet Lily. I'd say the best place is at school, after lessons."
            b "We can talk about Daniele losing his memory nearby her, and see if we get her attention."
            b "Then, we can mention Lily, her case, and the fact that we're worried about her. We can say that we'd like to share information with her if we ever were able to meet her."
            m "Wait, I have a question. How can we recognise her?"
            n "She's a pretty lil' flower, her hair are violet, and her eyes are of a lively purple."
            m "This last detail is far than enough to recognise her! Have you ever seen someone with purple eyes before?"
            e "Yeah, you really have a point on that, man!"
            m "Let's hope he gives us her trust. What next?"
            b "Well, we offer her something, somewhere."
            e "I'd say this is a good place. It's not far from school, after all."
            b "Yes, it should work. Can you keep her up here, Ed?"
            e "Of course, I can."
            b "Remember: the final objective we want to meet is, having Phony coming with us. As they're friends, we could ask her to bring him with us."
            m "You're right."
            e "Let's keep our final objective in mind."
            stop music fadeout 2.0
            play music audio.light_amici fadein 2.0
            b "Nice, I think there is nothing else to keep in mind. Do you feel ready for tomorrow?"
            e "By all means, Bianca!"
            m "I think so. I cannot wait to learn what they may know about the facts, so... yeah, just let's get this thing done!"
            n "Well said! By the way, gonna get back to work, now! See ya tomorrow!"
            m "See you, Newz, thank you for all your help!"
            hide norman with easeoutleft
            n "That's nothing, pal. Really. Have fun, tomorrow - I'll wait you here!"
            "\"Fun\" is not exactly what I expect, but of course, we'll be here."

            # SPAZIO PER LE USCITE CON GLI AMICI #

            stop music fadeout 2.0
            scene black with Fade(1.0,0.0,0.5)
            play music audio.myst_mistero_soave fadein 2.0
            "After that, Edward carried me back to home."
            "My mind was full of questions about the things we had discovered."
            "It was really strange that me and another girl had lost our memory at the same time. It was strange, and somewhat disturbing."
            "I tried to sleep, but there was no way. My mind just kept wondering about that girl."
            "Lily... why is this name so familiar to me? I couldn't tell. Weariness just slowly slipped this thought into darkness."
            "I couldn't sleep, neither think. The unpleasant feeling lingered the whole night."

            jump tuesday

label prologue:

    play music audio.light_viaggio
    scene ospedale stanza giorno
    with fade

    "{cps=*0.1}...{/cps}"

    "{cps=*0.25}...ungh... {/cps}{w=0.5}{cps=*0.5}where am I?{/cps}"

    "..."

    "I can't remember how I've ended up here.{w} My head hurts..."

    "...I cannot even remember what day is today."

    "Well, at least I should remember my name."

# QUI IL PERSONAGGIO SCEGLIE IL NOME #

    label scelta_nome:

        call screen inserisci_nome()

        if _return == "":
            p "I must struggle to remember at least that."
            jump scelta_nome
    
    $ nome_protagonista = _return

    "Okay, my name is [nome_protagonista], for sure."

    "I think I pretty much remember who I am, at least."

    "I still can't remember anything about my last days, though..."

    "..."

    "No matter how hard I try, it's no use. I can remember that I'm a student at [nome_scuola], that I'm a first-year, but nothing more from my last year. Damn."

    play sound audio.umani_passi_tacchi fadein 3.0
    pause 3.0
    show bianca sad_1 at frontcenter with dissolve
    stop sound
    b "[nome_protagonista]! I'm glad I found you."

    b "How do you feel?"

    menu:

        b "How do you feel?{fast}"

        "I'm fine, thanks":
            b smile_3 "I'm glad to hear that."
        "I could be better.":
            b sad_3 "I'm sorry to hear that."
        "Nothing important, really. How're you?":
            b shock_2 "A-are you sure?{w} Are you worried about me even when you've just passed out? It's so kind of you."
            b smile_4 "By the way, I'm fine!"

    m "So... for... exactly how many days I've been sleeping, Bianca?"
    "Bianca is one of my best friends at [nome_scuola]. She's smart, reliable, and hard-working."
    b default_1 "The whole night."
    m "Ugh."
    b sad_1 "I was worried, as we all couldn't understand what was going on..."
    m "What do you mean?"
    b default_1 "They said that you have been found unconscious near M. That you were not wounded by any means. That's it."
    "She's talking about \"Cafè Memoria\", for sure. We cut its name short as \"M\"."
    m "Hm. I actually feel fine, now. How strange."
    b "I've seen Edward coming here for you, too. I'm sure he's on his way here, as I informed him when medics told me that you were fine."
    b default_2 "Do you remember anything about what happened?"
    m "..."
    "I tried to get anything from my recent memory, but nothing came out."
    m "Absolutely nothing. I'm sorry. Do you know anything else that can help me remembering? Like, was anybody with me?"
    b default_1 "It seems you went there alone, around 23:30 PM. I called everyone, but nobody knew anything."
    m "I see. Well, I think it can't be helped, then. I hope it will come out with time."

    play sound audio.umani_passi fadein 2.0
    pause 2.0
    show bianca at cright with move
    show edward shocked_1 at frontcleft with dissolve
    show bianca at rear
    stop sound
    e "[nome_protagonista]! You're awake!"
    m "Edward! It's nice to meet you."
    "I've known Edward since childhood. He has been my best friend since then. He's kind, reserved and caring."
    e smile_4 "I'm so happy that you're ok! We should soon meet altogether at M -"
    e urgh_1 "I'm so happy that you're ok! We should soon meet altogether at M -{fast} I mean... somewhere, and take a cup of coffee..."
    m "Oh. No, please, don't worry about it.{w} I want to come back to M together too, regardless of what happened."
    m "It's our place.{w} Nobody can take it away from us."
    m "Also, I would like to try gathering some info. Or... just get back some of my memories."
    show bianca at front
    show edward at rear
    b sad_6 "I'm not sure it's a good idea, [nome_protagonista]. It may be dangerous."
    show edward at front
    show bianca at rear
    e sad_1 "Yeah, I'm worried, too. As long as we don't know what happened, we should find some other place, I think..."
    m "As long as we don't do anything, nobody will tell us. I'm sure I can get some of my memories back. Let's go there just after school. It can't be dangerous, while there are many people around."
    m "Don't you think?"

    b default_1 "No, not at all. But you have a point about your memories. So... I think we can go."
    show edward at front
    show bianca at rear
    e upset_2 "Don't go alone, though. I wanna be with you, okay?"
    m "Nice, it's set then."
    show bianca at front
    show edward at rear
    b default_1 "You should rest, now. You'll be released tomorrow, so we can see on Monday."
    show edward at front
    show bianca at rear
    e smile_6 "And I'm gonna keep you up!"
    m "Thanks, Ed. See you on Monday, then."
    show bianca at front
    show edward at rear
    b default_1 "16:00 P.M.! Get ready on time."
    m "Yeah, yeah, no problem!"
    "She always thinks somebody's gonna be late... well, as she's talking about me and Ed, she's probably right."

    jump monday

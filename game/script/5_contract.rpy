# FINALE: THE CONTRACT #
#
# Norman offers a contract: write the culprit's name, and that soul goes to hell in
# place of [nome_protagonista] and Elise. Every human name is a trap, because the people
# who hurt them were only Norman's hands. Writing the demon's true name is the checkmate.
#
# Clues to the true name, in story order:
#  - Monday quiz, perfect score: "the Goetia, seventy-two names, every name is a key"
#  - Tuesday dead end: "a duke never wears the same face twice"
#  - Wednesday dread run: "seventy names came before mine... I'm the seventy-first"
#  - Wednesday quiz, perfect score: "a name is a leash"
#  - Wednesday photo: "D A N" sprayed on the wall behind Norman
#  - The contract itself: "on my honour as a duke", and a hint after writing "Norman"

define contract_demon_names = ("dantalion", "dantalian")
define contract_norman_names = ("norman", "newz", "news", "newsman", "norm")
define contract_elise_names = ("elise", "lily", "liz", "lizzy", "lil", "lil'")
define contract_friends = {"bianca": "Bianca", "edward": "Edward", "ed": "Edward", "gain": "Gain", "phony": "Gain"}

default contract_name = ""
default contract_victim = ""
default contract_norman_tries = 0
default persistent.endings = set()

screen contract_sheet():
    modal True
    add Solid("#000000cc")
    frame:
        xalign 0.5
        yalign 0.45
        xsize 940
        background Solid("#e8dcc2")
        padding (60, 46)
        vbox:
            spacing 20
            text "CONTRACT" size 58 bold True color "#3b0a0a" xalign 0.5
            text "The undersigned delivers the soul written below,\nwhole and forever, in exchange for the life\nof the one called Elise, and for the stolen\nmemories of [nome_protagonista].":
                size 26
                color "#3b0a0a"
                text_align 0.5
                xalign 0.5
            text "Whoever is named here is the culprit, and shall answer for it.":
                size 22
                italic True
                color "#5a1a1a"
                xalign 0.5
            null height 6
            hbox:
                xalign 0.5
                spacing 14
                text "Name:" size 34 color "#3b0a0a" yalign 0.5
                frame:
                    background Solid("#3b0a0a18")
                    xsize 540
                    padding (12, 6)
                    input:
                        default ""
                        length 24
                        size 34
                        color "#830303"
                        allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' -"
            text "Write the name, then press Enter." size 18 color "#7a5a5a" xalign 0.5
            null height 6
            text "Signed in good faith,   {i}N.{/i}" size 24 color "#3b0a0a" xalign 1.0

label contract:
    $ renpy.block_rollback()
    n deadend smile_1 "Here's my last offer. And this time, it's in writing."
    n deadend smirk_1 "A contract. Old-fashioned, I know. I'm a traditional guy."
    n deadend default_1 "Write the name of the culprit. Whoever you write goes down, in your place and in hers."
    n deadend smile_3 "And you two go back to Friday night. Alive. Together. With every memory you lost."
    m "And what do you get out of it?"
    n deadend smile_1 "A soul, of course. What else would someone like me want?"
    "Someone like him. What {i}is{/i} he...?"
    n deadend wink_1 "I'll keep my word, on my honour as a duke. Choose carefully, [nome_protagonista]. A name on this paper is forever."

label contract_write:
    call screen contract_sheet
    $ contract_name = _return.strip()
    $ contract_key = contract_name.lower()
    if contract_key == "":
        n deadend pout_1 "A blank contract? Cute. Write something."
        jump contract_write
    if contract_key in contract_demon_names:
        jump contract_checkmate
    if contract_key in contract_norman_names:
        $ contract_norman_tries += 1
        jump contract_norman
    if contract_key == nome_protagonista.lower():
        jump contract_self
    if contract_key in contract_elise_names:
        jump contract_elise
    if contract_key in contract_friends:
        $ contract_victim = contract_friends[contract_key]
        jump contract_friend
    n deadend awkward_1 "\"[contract_name]\"? Never heard of them."
    n deadend default_1 "This story has a cast, you know. Pick someone from it."
    jump contract_write

label contract_norman:
    show norman deadend smile_3
    "The ink hissed and slid off the paper, like water on glass."
    if contract_norman_tries == 1:
        n "Ahahah! Me? Of course you'd try."
        n deadend smirk_1 "But \"Norman\" is just a coat I borrowed. A contract wants a {i}true{/i} name."
        n deadend smile_1 "Go on. Try again."
    else:
        n deadend pout_1 "Again? A coat is still a coat, no matter how many times you write it."
        n deadend smirk_1 "Fine, a freebie, since you amuse me: the seventy-first name in the old book. Do your homework."
    jump contract_write

label contract_friend:
    $ renpy.block_rollback()
    "I wrote [contract_victim]'s name. The paper drank the ink, as if it had been thirsty for it."
    show norman deadend evil_1 with dissolve
    n "Deal."
    play music audio.dark_incubo
    "Somewhere in the dark, [contract_victim] screamed my name. Then, nothing."
    n deadend smile_1 "Oh, don't make that face. Were they the one holding the knife? Maybe. Maybe not."
    n deadend smirk_1 "Either way, I was the one holding {i}them{/i}."
    m "...What?"
    n deadend smile_3 "Hands don't choose, [nome_protagonista]. You damned a hand, and let the will walk free."
    n deadend wink_1 "Pleasure doing business with you. Enjoy your Friday night!"
    scene cafe retro sera with Fade(2.0, 1.0, 2.0)
    play music audio.souls.felice_e_triste
    show elise casual default_1 with dissolve
    l casual shock_2 "...[nome_protagonista]? Why are you crying? It's just Friday night..."
    "I remembered everything. Every moment with her."
    "And for the rest of my life, I would remember that scream, too."
    $ persistent.endings.add("fair_trade")
    call ending_card("DEAD END", "A Fair Trade")
    return

label contract_elise:
    $ renpy.block_rollback()
    "I wrote her name. Why? Why did I...?"
    show norman deadend surprised_1 with dissolve
    n "Oh."
    n deadend smile_3 "Oh, that's {i}delicious{/i}. You traded her life... for her life!"
    play music audio.dark_incubo
    "The paper burned. And with it, every memory of her."
    scene cafe retro sera with Fade(2.0, 1.0, 2.0)
    "Friday night. I was standing alone in the alley behind Café Memoria."
    "I had the feeling that I was waiting for someone."
    "I just couldn't remember who."
    $ persistent.endings.add("paradox")
    call ending_card("DEAD END", "Paradox")
    return

label contract_self:
    $ renpy.block_rollback()
    "I wrote my own name."
    show norman deadend surprised_1 with dissolve
    n "..."
    n deadend pout_1 "Noble. Boring, but noble."
    n deadend smile_1 "Don't worry, I'll keep my side. She'll go back to Friday night, safe and sound."
    n deadend smirk_1 "She just won't remember anyone called [nome_protagonista]. Nobody will."
    play music audio.souls.elegante_e_malinconica
    scene cafe retro sera with Fade(2.0, 1.0, 2.0)
    "Friday night. Elise walked out of the alley behind Café Memoria, alone, humming to herself."
    "For a moment she stopped, and looked back, as if she had forgotten something."
    "Then she went home."
    $ persistent.endings.add("last_signature")
    call ending_card("DEAD END", "The Last Signature")
    return

label contract_checkmate:
    $ renpy.block_rollback()
    stop music
    "I wrote the name. Slowly. Letter by letter."
    "D. A. N. T. A. L. I. O. N."
    show norman deadend surprised_1 with vpunch
    n "..."
    n deadend dread_1 "Where... did you hear that name?"
    m "From you. The seventy-first name in the old book. A duke who wears a different face for everyone."
    m "And it was written on that wall, behind us, the night you took our memories."
    play music audio.myst_tensione
    n deadend angry_1 "That's not how this works! The contract is for the CULPRIT!"
    m "Exactly. Whose will was behind the knife? Who erased us? Who kept twisting everyone's memories, every time Gain got close to the truth?"
    m "You said it yourself. Hands don't choose."
    show norman deadend evil_1 with hpunch
    n "You little..."
    "The paper caught fire in his hands. Black fire, as cold as the void around us."
    n deadend dread_1 "Do you even know what you've done?! I gave you EVERYTHING back! I let you LIVE!"
    m "You gave back what you stole. That's not a gift."
    n deadend awkward_1 "..."
    n deadend smile_1 "...Heh."
    n deadend smirk_1 "Checkmate, huh? It's been a few centuries since someone managed that."
    n deadend smile_3 "Fine. A deal is a deal, and a duke always honours his contracts."
    n deadend wink_1 "Take good care of the lil' flower, [nome_protagonista]. And... thanks for the game."
    hide norman with Dissolve(4.0)
    "The darkness cracked like glass, and light poured in."
    jump true_ending

label true_ending:
    scene cafe retro notte with Fade(1.0, 0.5, 2.0)
    play music audio.souls.profonda_e_innamorata
    "Friday night. 23:30. The back alley of Café Memoria."
    show elise casual default_1 with dissolve
    "Elise was holding my hand. Exactly like I remembered."
    l casual shock_2 "[nome_protagonista]...? You look like you've seen a ghost."
    m "Something like that."
    "Nobody was waiting in the shadows. No knife. No photo. Just the two of us, and the hum of the city."
    l casual smile_3 "Come on. We promised we'd tell your friends about us, remember?"
    "I remembered. I remembered everything."

    scene cafe interno nordf pomeriggio with Fade(1.5, 0.5, 1.5)
    play music audio.light_amici
    "Monday. Café Memoria."
    show bianca smile_1 at left
    show elise smile_3 at cright
    show edward smile_4 at right
    with dissolve
    b "So you two have been together for weeks, and you never told us? I can't believe it."
    e "I KNEW something was up! I mean... I didn't, but I wanted to!"
    l embarassed_1 "Sorry... we wanted to keep it just for us, for a while."
    show gain smile_1 at cleft with easeinleft
    g "Mind if I join? Liz told me everything."
    e surprised_1 "Phony?!"
    g unimpressed_1 "...Gain."
    m "He's an old friend. A neighbour, actually. I'll explain later."
    m "By the way, where's Newz? Isn't he on shift today?"
    b default_2 "...Newz?"
    e surprised_1 "Who's Newz?"
    m "Norman. Tall, annoying, knows everything about everyone?"
    b lookaway_1 "Nobody called Norman works here, [nome_protagonista]. It's always been the owner and his daughter."
    "Nobody remembered him. Not a single one of them."
    "On the counter, next to the register, there was a paper napkin folded in two."
    "Inside, in a neat, old-fashioned handwriting: {i}Good game. - D.{/i}"
    l smile_1 "[nome_protagonista]? Your coffee's getting cold."
    m "Coming."
    $ persistent.endings.add("checkmate")
    call ending_card("TRUE END", "Checkmate")
    return

label ending_card(kind, title):
    stop music fadeout 3.0
    scene black with Fade(1.0, 0.5, 1.0)
    centered "{size=80}{b}[kind]{/b}{/size}\n\n{size=40}[title]{/size}"
    return

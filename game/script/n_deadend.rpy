label deadend_1:

    define body = "head"

    play music audio.umani_battito
    show cucina notte
    show tintred
    show cucina notte with vpunch
    pause 0.5
    m "{cps=20}What...{/cps}{w=0.5} what the fuck...!"
    "My heart is beating hard. I feel something on my back. My hands are freezing."
    show cucina notte with vpunch
    "I was shove on the ground. I felt weak."
    m "{cps=20}What's... what's happening...{/cps}"
    "I wanted to turn to see what was behind me."
    "I tried, but slumped again on the ground."
    show tintred
    "I brought my hand under me, trying to reach the point that hurt so much."
    "I couldn't reach it, but felt something, so I brought my hand out again, under my eyes."
    show cucina notte with hpunch
    m "WHAT'S THIS?! WHAT'S THIS?!?!"
    "A red, dense substance was on the tip of my fingers."
    "It can't... I't can't be..."
    play music audio.umani_battito_veloce
    "Blood.{w} This is blood."
    "I strived to put my hand beneath me, reaching the point that was hurting."
    "My clothes were drenched in that hot, dense substance."
    l "Eek! What are you... AAAAAAHHH!!"
    m "ELISE!! ELISE!!!"
    "My head is spinning... I... just... can't... keep my eyes... open..."
    "Cold is spreading everywhere in my body. Is... is it all over...?"
    show black with Fade(3,0,3)
    $deadend_counter = 1
    show norman deadend surprised_1
    play music audio.myst_inquietudine
    n "So... you ended up being killed, after all..."
    n deadend awkward_1 "I'm sorry! You cannot complain, though, I advised you!"
    n deadend smile_3 "Don't worry though! You can still fix that!"
    n deadend default_1 "After all, avoiding this dead end was quite difficult, as it came out of nothing and everything."
    stop music fadeout 1.0
    n deadend default_1 "Just remember that you may won't be enough lucky to go back fixing things... the next time."
    n deadend wink_1 "Good luck!"

    jump deadend_1_return

label deadend_2:
    scene lungomare nebbia with fade
    play music audio.myst_ombre_misteriose fadein(10.0)
    show elise default_1 with dissolve

    l embarassed_2 "What is worrying you this much, [nome_protagonista]?"
    m "I need your help."
    l shock_1 "My help...? And, how exactly?"
    m "We think that the one that made us lose our memories... is Gain."
    l scared_1 "And how do you think Gain is the one?"
    m "He was following you, with a gun."
    l scared_2 "You're wrong! He was not foll..."
    show elise scared_1 with vpunch
    hide elise scared_1 with dissolve

    "What the..."
    show lungomare nebbia with vpunch
    show tintred

    "Oh no... I... I was hit... I..."
    scene black with Fade(10.0,0.0,0.0)
    show norman deadend surprised_1
    play music audio.myst_inquietudine
    if(deadend_counter == 1):
        n "You're here again, I see..."
        n default_1 "My bad. You have only one occasion left. If you fail again..."
        n smile_3 "...I won't be able to bring you back!"
        stop music fadeout 1.0
        n deadend frown_1 "I hope you've understood who is the culprit, by now..."
        n deadend smile_1 "Good luck! Do your best!"
    else:
        n "So... you ended up being killed.."
        n deadend awkward_1 "I'm sorry! It's not your fault, after all."
        n deadend pout_1 "There is no way to avoid this ending, no matter what you do throughout the game."
        n "The only way to change this sad conclusion..."
        n "...is to get the game's source code."
        n deadend default_1 "Join {i}RectorNetwork{/i} from https://rectorstudio.games and ask for it, if you want to change your fate!"
        n "Since then... farewell!"

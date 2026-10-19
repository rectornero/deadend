label deadend_1_return:
    play sound audio.porta_campanello_leggero
    "Umgh..."
    play sound audio.porta_campanello_leggero_doppio
    "Uhn... ...! The door! The door just rang."
    scene cucina notte with fade
    "I jumped out of the chair and opened the door."
    scene appartamento notte with fade
    show elise scared_2 with dissolve
    "It's Elise... why I'm not surprised of that?"
    m "Hi Elise. Are you all right?"
    "I felt dizzy. It was like I was in shock after something."
    "Was it just the effect of falling asleep on the table?"
    l "Please, [nome_protagonista], can I come in?"
    m "Oh well..."
    play music audio.myst_ombre_misteriose fadein 60.0
    "What's this strange feeling?"
    l "... I can't? S-sorry for bothering you..."
    m "N-no, wait! Of course you can! Come in."
    scene cucina notte with fade
    show elise scared_1
    l "Thank you, [nome_protagonista]. I wasn't feeling safe, I don't know why."
    m "I'm not feeling safe too, to be honest."
    l embarassed_1 "Really? Well, I have the feeling that what Gain said was right. I... I heard footsteps over mine, while I was walking home. I got scared, and your house was the nearest in the place. Did something happen to you too?"
    l embarassed_1 "I'm really sorry... if this depends on me."
    m "No, it's... it's not you."
    "Is this actually true?"
    l embarassed_2 "I... I..."
    m "What's up?"
    l "I'd need the bathroom..."
    "Wait. Was it a deja-vu?"
    m "Oh! Well... yeah. It's over there."
    l "T-thanks..."
    hide elise with dissolve

    play sound audio.umani_battito_accelerazione_basso

    "No. Something isn't fine at all. I have a really bad feeling about this. I must keep my guard high."

    show cucina notte with Fade(1,1,1)

    "I locked the door, just to be sure."

    show elise relieved_1

    l "Thank you!"


    m "..."

    l scared_1 "Are you alright, [nome_protagonista]? Why are you staring the door?"

    m "I don't know. Just... I don't feel safe anymore."

    l shock_1 "You too?"

    m "Yes."

    l scared_2 "I'm sorry... It's my fault..."

    m "No, Elise, it's not your fault. Just... stay close to me, this night."

    l shock_2 "O-oh... well, y-yes... I will..."

    "I just feel that something bad would happen otherwhise."

    stop sound

label notte_insonne:

    play music audio.myst_mistero_meandri fadein (5.0)

    show black with Dissolve(5.0)

    "I would have been excited to be with Elise. I really liked her."

    "That night, though, was different for both."

    "We decided to stay awake in turns. I really needed a few hours of sleep after last night, so this was the only choice."

    "Elise was very kind, letting me sleep much more time than my actual turn."

    "Then, she felt asleep quietly while I sit besides her."

    "She totally trusted me somehow. I felt the same."

    "With her awake I felt protected, and so she did."

    "There was an unexplicable bond keeping us together. I couldn't really explain it."

    "It was not mere attraction. There was a strong attraction between us, but that was not the point."

    "Things were getting really strange."

    "Those were not the days I was used to by far."

    "A cold mantle enveloped everything."

    "What just did happen on last friday night? Why was I at Café Memoria? I couldn't remember."

    "I just remember that I was happy back them. That days felt warm and exciting."

    "Since that weirdo, Gain, got out the work \"culprit\", a dull feeling got into me."

    "Why? How could he say such a thing? I just lost my memory, how does this links with a culprit of any sort?"

    "There is no way for someone to steal your memory."

    "Oh wait. He even said that I should have talked with him."

    "What made him worry about me, I wonder? He was cold with my friends, so I just cannot get the thing."

    "I should ask Elise. She seems such a good girl. She may tell me something more about him."

    "That uneasy night finally came to an end."

    jump wednesday

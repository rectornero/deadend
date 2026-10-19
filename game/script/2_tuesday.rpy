label tuesday:
    scene scuola corridoio giorno
    play music audio.myst_il_piano fadein 2.0
    show edward default_1 at cright
    show bianca default_1 at cleft
    with dissolve
    e "Here we are! How do you feel about this, [nome_protagonista]?"
    m "Well, I'm glad that you all are helping me out finding what happened."
    b "We still have around three minutes to prepare. Do you all feel ready for this?"
    e "I'm here for that, you can count on me."
    m "Well, it's all for me, so I am."
    "To be honest, I feel dizzy since this morning. They're both here to help me, though, so I'll do my best to find out the truth!"
    b "I'll be leaving, then. Do you remember what we have planned to say?"
    menu:
        "We talk about how we found out about the girl losing her memory":
            b "No, don't do that. We shouldn't address the matter directly, can't you recall? Just talk about your case, and that you are worried about Lily, too."
        "We talk about me having lost my memory, and we mention that we are worried for the girl":
            b "That's right."
        "We ask Phony to follow us, as we have many questions for him":
            b "That's wrong. I know that we have a lot to ask to him, but, can't you recall? He's shy."
            e "We should get this result by telling about your case, and that we're worried about Lily."
    b "Very well. It's about time. See you later!"
    hide bianca with easeoutleft

    stop music fadeout 2.0
    play music audio.light_serenita fadein 2.0
    show edward default_1 at center with easeinright
    e "So, well, do you remember where is your locker, [nome_protagonista]?"
    m "I found it this morning, come with me."
    "Hmm, I wonder if we can... hey, wait! Those eyes... that's her! We're lucky."
    "So now, I must stay calm and stick with the plan."
    m "Ed, I would like to thank you for all the effort you are putting into helping me finding my memories back."
    "I did my best to keep my voice loud and clear, and to remark the word \"memories\"."
    e surprised_1 "Oh well, that's nothing. Why do you come up with..."
    "I swiftly winked to Edward."
    "Oh, well, s-sure! I mean, that's nothing! We absolutely... need to help you finding about your LOST MEMORIES."
    "Not so loud, Edward! She'll understand that there is something fishy, this way!"
    m "A-and, well, thinking about the fact that it seems to be not the only case makes me feel uncomfortable..."
    e "Yes, I've heard rumors about a girl losing her memory too. Do you know who she is?"
    m "I don't know her name, to be honest. But... I'd like to meet her. Maybe we can help each other out."
    "Is it working? I glanced over Edward shoulder, and met her eyes again. She had stopped, and turned over, looking back. Those eyes..."
    e "[nome_protagonista]...? Are you ok?"
    show scuola corridoio giorno with hpunch
    pause 0.5
    "Ugh. Not quite. My head is swirling."
    m "Y-yes. Uhm, I just... I think I'm just a bit tired."
    "I looked around for a place to sit, but there were not. My legs were shaking, so I slided to the lockers and sat down."
    e "Hey man! Are you really okay...?"
    m "Y-yeah, it's just that, to be honest, I wasn't sleeping this night and-"
    "My heart skipped a beat."
    show elise sad_1 at left with dissolve
    l "Hey... are... are you alright? Should I call the school nurse?"
    show scuola corridoio giorno with hpunch
    pause 0.5
    "My head is spinnning... why is this happening? This girl..."
    m "N-no thanks, I think I'm okay. I just..."
    show bianca default_1 at right with dissolve
    b "[nome_protagonista], may this be related with your memory loss?"
    "I really don't know now Bianca, why are you-{w=0.5}Oh, right. The plan."
    m "Y-yeah, maybe... I'd really like to share my thoughts with that girl, though..."
    "I tried to keep my eyes away from Elise, but just couldn't."
    l sad_2 "Well, I may be that girl..."
    "I'm feeling really bad lying to her. I don't know why!"
    m "Oh, really? That's... that's nice! What's your name?"
    l sad_3 "... My name is Elise. You can call me Lily, though."
    "Okay. It's done. We did it what we need. Didn't we? Can I stop being indirect with her?"
    b default_1 "It's nice to meet you, Lily. I think our friends needs a good cup of coffee, but I understand his need to talk. Would you like to come with us?"
    l scared_1 "Oh well, I don't know...! It's just... I have club activity after lessons, and..."
    m "Please, Lily, come with me."
    "What am I saying? I should sleep before doing important stuff with the group!"
    l shock_2 "O-oh. Well, if you need me that much, I think I..."
    e "You'll come then? That's cool! We know a nice place to have a really good cup of coffee. A friend of us is on shift, and we can get a fair price for anything!"
    l shock_1 "T-that's nice!"
    show gain angry_1 at cleft with easeinleft
    g angry_1 "What are you doing? Why are you still here?"
    l "Oh, uhm, Gain... this boy seems to have lost his memory too, so..."
    g angry_2 "..."
    "Hey, what's the matter? Why are you looking at me like that?!{w=0.5} - Oh wait. He may be Phony! He has phones, and is close to Elise, it seems."
    m "Y-yes, it happened last friday, and I'm still clueless..."
    g surprised_3 "..."
    l shock_2 "Really? It's... it's the same day."
    m "The same day?"
    g lookaway_1 "That's actually relevant. May we have a talk?"
    "This guy is sure strange!"
    e "Oh, sure thing! We're going to have a cup of coffee all together. You can join us!"
    g unimpressed_1 "Hmm.{w=0.5} No, I just want to ask the boy a few questions. That's all."
    e shocked_1 "Hey, what?! So you just want to ask and go away without even saying \"hi\"?"
    g default_1 "The fact is that we don't have time to waste."
    l sweat_4 "Well, Gain, I was just thinking that it could be a good idea to share thoughts all together. And... [nome_protagonista] isn't feeling too well, so..."
    g alarmed_1 "Oh, I see. Well, if that is the case..."
    b default_1 "So, it's set. Let's go."
    e orly_1 "Yeah, whatever..."
    "It's not a good moment to be picky, Edward, we have all we need to advance with the plan!"
    scene sottopassaggio giorno with fade
    play music audio.mezzi_macchina_interno_ovattato
    "While Edward and Bianca are on the front seats, I'm in the back lane with Lily and Gain."
    g "How far is this place, anyways?"
    e "Not that far, man, I've already said it a thousand  times!"
    l "Uhm..."
    m "Hey, Lily. What's up?"
    "She was mumbling to herself, seeming troubled."
    l "O-oh! It's just... the air conditioning is a bit... cold, so..."
    e "Oh, well! Sorry, lady! Gonna turn that down for you!"
    "...! Oh, my! Her hand just touched me. It's so cold!"
    b "You're also kinda slow while driving."
    e "Aren't you always suggesting to be careful on anything, Bianca?"
    b "Oh please, Edward, don't stretch it that much!"
    "Their small talk was flushing over me, while I was still embarassed by having touched Lily's hand."
    "I still don't understand those feelings."
    "My gaze run out with the lamposts. After a while, the car stopped."
    stop music
    scene cafe nord pomeriggio
    play sound audio.umani_passi
    pause 0.5
    stop sound
    play music audio.light_amici
    show bianca default_1 at left with dissolve
    show elise default_1 at cleft with dissolve
    show gain default_1 at cright with dissolve
    show edward default_1 at right with dissolve
    e smile_4 "Aaaand, here we are! Let's get inside!"
    g angry_1 "Wait a second. This is..."
    l sweat_7 "This is Memoria, isn't it?"
    g angry_1 "Are you"
    show cafe nord pomeriggio with hpunch
    g angry_1 "Are you{fast} MAD?!"
    e shocked_1 "WHAT'S UP?!"
    g angry_2 "Elise, let's go away."
    l sad_3 "But, Gain, ...please, wait..."
    b default_2 "Please, calm down. There is nothing to be worried about. We are here with you. There are many people. Nothing will happen."
    g unimpressed_1 "..."
    l "Take it easy, Gain... there is no real danger now, after all..."
    show norman smile_3 at center with dissolve
    n "Hiya, guyz! What are you waiting for?"
    m "Norman! What are you doing here? Aren't you on shift?"
    n "Pause time! I could hear you arguing from the inside, so I just popped out."
    g default_1 "And who are you, exactly?"
    n "Norman, \"Newsman\", Newz... call me how you like most! I'm the one that knows things. You're here to find out things, aren't you? And to take good coffee, I guess. You're in the right place for both!"
    g unimpressed_1 "A talkative one..."
    l "Gain...! {w=0.5} It's... nice to meet you, again, Norman."
    n wink_1 "The pleasure is mine, my sweet lil' flower."
    b "Well, we can go in, now. What are we waiting for?"
    g default_1 "... Are you okay with that, Liz?"
    l smile_4 "Of course, I am. Let's go."

    scene cafe interno nord pomeriggio with fade
    play sound audio.porta_campanelle
    show norman default_1 at center with dissolve
    show bianca default_1 at left with dissolve
    show elise default_1 at cleft with dissolve
    show gain default_1 at cright with dissolve
    show edward default_1 at right with dissolve
    pause 0.5
    stop sound
    b "So now, let's share what we know."
    play music audio.myst_indagini
    n "Gonna bring the coffee! Comin' back in a sec!"
    hide norman with easeoutright
    g "Well. My first question. Anybody of you knows who were at this place on friday, 23:20?"
    b "We don't. We hoped you knew something."
    g "That's bad."
    b "So? Do you know something that can help us?"
    show edward surprised_1 at right
    g unimpressed_1 "My second question. I think both your friend and Elise are not safe right now. Are you aware of the risks?"
    b default_2 "What do you mean by that?"
    "I think he means \"What if they gain their memory back?\" I'd like to listen to this conclusion from his mouth, though."
    g lookaway_1 "Lastly, I have a statement to share with you."
    stop music
    n "Coffee is read- whoah. What is this tense atmosphere I'm feeling here?"
    play music audio.myst_mistero_eco
    "I could feel it too. The way things were going were actually kind of strange. Gain, who was on the defensive since then, started with that array of questions out of the blue."
    "We were all surprised, and couldn't reply. There was, though, something bugging me about the situation. What could that be?"
    "Oh, right. I expected Bianca to take the lead, as it always happens when we hop in the fields of logic. She seemed slightly interdicted, but didn't say a thing. How strange. Was this tactics?"
    g unimpressed_1 "Who, among you... is the culprit?"
    stop music fadeout 2.0
    show edward surprised_1 at right
    show elise shock_1 at cleft
    show norman surprised_1
    show bianca shock_3
    "Wait... what?!"
    play music audio.myst_ombre_misteriose
    e "What do you... what..."
    n "Okay, that was unexpected."
    b "What are you implying with this?"
    l "Are you okay, Gain? Is... everything okay?"
    show cafe interno nord sera
    show edward surprised_1 at right
    show elise shock_1 at cleft
    show norman surprised_1
    show bianca shock_3
    show gain default_1 at cright
    g "It surely isn't. I'm close to certain."
    b unimpressed_1 "You're going a bit over your boundaries."
    m "Wait, Gain, what do you mean by that? Are you saying that we are all possible culprits... for what exactly?"
    g lookaway_1 "Not you, [nome_protagonista]. I'm talking about your friends."
    "He's totally out of it. He's really pissing me!"
    e argue_1 "How you dare speak those words to my friends! How you even dare coming with us to spill such nonsense?!"
    n unimpressed_1 "Please, Edward, cool down. Let's listen to your theory for a moment, pal. Explain. What does it drives you saying such a thing?"
    g default_1 "I have enough proof, which I'm not sharing. I'd... recommend [nome_protagonista] to come to my place and... talk with me. It is wise to do so."
    "What? Is he really thinking that I'm gonna go to some weirdo's place like him?"
    g "Now Lily, let's get out of here. We're not welcome anymore."
    l sad_2 "I'm... really sorry guys. Really, really sorry."
    hide elise with easeoutleft
    pause 0.1
    hide gain with easeoutleft
    stop music
    "I couldn't believe of what I heard. My head was pulsing. I needed to smash something... grr... that was... just UNBEARABLE!"
    show cafe interno nord sera with vpunch
    show cafe interno nord sera
    show edward surprised_1 at right
    show elise shock_1 at cleft
    show norman surprised_1
    show bianca shock_3
    show gain default_1 at cright
    m "WE CAN'T JUST LET THAT SLIP AWAY!"
    b default_1 "We won't. But this is not the time to get worked up, [nome_protagonista]. We need a clear mind to state the situation and extract as much information as possible."
    "How can she be so clear-minded when he just spit on us?!{w=0.5} Oh well, I shouldn't be surprised. We're talking about Bianca."
    m "Well, I think you're right. I'm just upset that he got what he wanted and we got nothing in return."
    b default_2 "That may be not true. His behaviour could be precious information."
    e shocked_1 "What do you mean by that?"
    play music audio.myst_indagini fadein 2.0
    b talk_1 "He mentioned a \"culprit\", while nobody ever talked about a crime to begin with. Isn't this a bit strange?"
    e surprised_1 "Oh, now that you make me think about it..."
    m "What do you think about this, Newz?"
    "I found it a bit strange that he was still not talking"
    n smirk_1 "I think that's quite catchy!"
    e "Catchy?"
    n smirk_1 "Enticing!"
    "Well, he was probably thinking about inappropriate terms, maybe... it's the Newz we know so well!"
    b default_1 "I'd say \"shady\", to the very least. We must cast our light on that shade and uncover the rest."
    m "Where \"the rest\" may be... what?"
    b talk_1 "If we're lucky enough, it may be what we're looking for."
    e default_1 "Wait Bianca, what are we looking for now?"
    b default_2 "Isn't that obvious? We're looking for {b}the culprit{/b}."
    stop music
    scene black with fade
    "... That was kind of an unexpected end, but it was an unexpected good result."
    "If there really was a culprit, and it seems there was, then our investigation was bringing us much closer to the truth."
    "I silently thought about that while eating something with the others. We were all silent, pondering."
    "We headed out together just after that. Newz's shift was over, too."
    scene cafe nordf notte with fade
    show edward default_1 at left with dissolve
    show bianca default_1 with dissolve
    show norman default_1 at right with dissolve
    m "So well, see you tomorrow guys. What's the plan for the day?"
    b "We meet here after school."
    e surprised_1 "Hey, isn't that Norman's line?"
    n smile_3 "Well, it's not that I've bought it! See you tomorrow 'noon then. I'm on shift in the morning, so we can hang around, if you like."
    b smile_3 "That would be nice."
    n "Oh, and watch your steps when coming back home!"
    m "...what?"
    n default_1 "I mean, after all that talkin' about a \"culprit\", I got worried for ya, y'know!"
    e shocked_1 "Well, you may be right! I'm gonna take you all home!"
    m "Wait, to bring me back you must double your route, so don't worry."
    e smile_1 "No, no, it's not a problem at all!"
    m "Take Bianca home. I'll go with Newz for a bit, then rush home!"
    "Norman also has a car. He usually don't like bringing me back home, though."
    n smile_3 "This time I'm gonna bring him home! I'm worried about the kid."
    e "Nice! So that's set!"
    m "Bye, Ed! Bye, Bianca!"
    b smile_4 "Bye, [nome_protagonista]! Take care!"
    e "Yeah, bye!"
    scene black with Fade(1.0,0,1.0)
    stop music fadeout 2.0
    pause 2.0
    scene incrociomain notte with fade
    play music audio.mezzi_macchina_interno_rumoroso
    show norman default_1
    m "We have arrived! Thanks a bunch, Newz!"
    n smile_3 "No worries. Oh well. I mean. Worry a"
    n evil_1 "No worries. Oh well, I mean. Worry a{fast} little bit"
    n smile_3 "No worries. Oh well. I mean. Worry a little bit{fast}."
    m "Eh?"
    n smile_4 "I mean, take care!"
    m "You've already said that! What's got into you tonight?"
    n smile_4 "Nothing, really! See you!"
    play sound audio.umani_passi
    pause 0.5
    stop sound
    "What a strange behaviour. He's usually not that caring. This \"culprit\" thing must have gotten into him."
    "Well, whatever. Let's get back home."
    scene cucina notte with fade
    stop music
    "And, here we are. Let's sit down and relax a bit!"
    play music audio.myst_mistero_soave
    "A train of thoughts started crossing my mind. I was tired, so it just passed there, without any conscious attention."
    "Eventually tireness overwhelmed me, and I got asleep with my head on the table."
    play sound audio.porta_campanello_leggero
    "Umgh..."
    play sound audio.porta_campanello_leggero_doppio
    "Uhn... ...! The door! That was the door, wasn't it?!"
    "I jumped out of the chair and opened the door."
    scene appartamento notte with fade
    show elise scared_2 with dissolve
    "W-WHAT?! What is she doing here?!"
    m "E-Elise, hi... is it all right?"
    "My heart was racing like crazy. Why, I wondered aimlessly."
    l "Please, [nome_protagonista], can I come in?"
    m "Oh well, of course you can!"
    "Can't you? ...really, though, what's the trouble?"
    scene cucina notte with fade
    l scared_1 "Thank you, [nome_protagonista]. I wasn't feeling safe, for some reason."
    m "What do you mean by that? Is something troubling you?"
    l embarassed_1 "I have the feeling that what Gain said was perfectly right. I... I heard footsteps over mine, while I was walking home. So, well, I got scared, and your house was the nearest in the place."
    m "Oh, right! About that, how do you know that? I never told!"
    l embarassed_1 "Sorry, I'm really sorry... Norman told me. I called him as I knew he is living in this zone. He said he was out, and that I should have gone to your place. He gave me your address."
    "What are you scheming, Newz?! Are you mad?! Well, not that I don't like your schemes, but..."
    l embarassed_2 "I... I..."
    m "What's up? Tell me!"
    l "I'd need the bathroom..."
    m "Oh! Well, of course! It's over there."
    l "T-thanks..."
    "What the fuck is happening here? Really, now!"

    "Okay, let's sum up things. Elise has come here, as she thinks she's heard footsteps following her."
    $ time = 0.5
    $ timer_range = 0.5
    $ timer_jump = "dodge_up_timeout"

    show screen hidden_countdown

    show screen dodge_up
    pause

    label dodge_up_timeout:
        hide screen dodge_up
        jump deadend_1


    label dodged_up:
        hide screen hidden_countdown
        hide screen dodge_up

        $ time = 0.5
        $ timer_range = 0.5
        $ timer_jump = "dodge_sx_timeout"
        show screen hidden_countdown

        show screen dodge_sx
        pause

    label dodge_sx_timeout:
        hide screen dodge_sx
        jump deadend_1

    label dodged_sx:
        hide screen hidden_countdown
        "You win"

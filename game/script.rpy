############################## INIZIALIZZAZIONE DATI ##############################

##### INIZIALIZZAZIONE DATI: GAMEPLAY #####

### INIZIALIZZAZIONE DATI: CASO 1 ###

define vote_1 = ""

define plan_overall_score = 0
define plan_phase_1_score = 0

##### INIZIALIZZAZIONE DATI: PERSONAGGI #####

### INIZIALIZZAZIONE DATI: TUTORIAL ###

define t = Character("Tutorial", who_color="#00ff6e", what_color = "#00ff6e", what_italic=True)

### INIZIALIZZAZIONE DATI: PROTAGONISTA ###

define ts = "#42a4f4"

# NARRATORE #
define narrator = Character(what_italic=True, what_color = "#d6d6d6")
define smartphone = Character("Smartphone", who_color = "#2f4260", what_color = "2ecc71")
# PERSONAGGIO #
define nome_protagonista = ""
define m = DynamicCharacter("nome_protagonista", who_color="#8e8e8e")
define gender = ""

### INIZIALIZZAZIONE DATI: BIANCA ###

# PERSONAGGIO #
define b = Character("Bianca", who_color="#ffffff", image="bianca")

# ESPRESSIONI #
image bianca angry_1 = LiveCrop((0, 0, 447, 1000), "bianca angry1")
image bianca angry_2 = LiveCrop((0, 0, 447, 1000), "bianca angry2")
image bianca angry_3 = LiveCrop((0, 0, 447, 1000), "bianca angry3")
image bianca angry_4 = LiveCrop((0, 0, 447, 1000), "bianca angry4")
image bianca angry_5 = LiveCrop((0, 0, 447, 1000), "bianca angry5")
image bianca angry_6 = LiveCrop((0, 0, 447, 1000), "bianca angry6")
image bianca angry_7 = LiveCrop((0, 0, 447, 1000), "bianca angry7")
image bianca angry_8 = LiveCrop((0, 0, 447, 1000), "bianca angry8")
image bianca blank_1 = LiveCrop((0, 0, 447, 1000), "bianca blank1")
image bianca bleh_1 = LiveCrop((0, 0, 447, 1000), "bianca bleh1")
image bianca default_1 = LiveCrop((0, 0, 447, 1000), "bianca default1")
image bianca default_2 = LiveCrop((0, 0, 447, 1000), "bianca default2")
image bianca disbelief_1 = LiveCrop((0, 0, 447, 1000), "bianca disbelief1")
image bianca disbelief_2 = LiveCrop((0, 0, 447, 1000), "bianca disbelief2")
image bianca embarassed_1 = LiveCrop((0, 0, 447, 1000), "bianca embarassed1")
image bianca embarassed_2 = LiveCrop((0, 0, 447, 1000), "bianca embarassed2")
image bianca embarassed_3 = LiveCrop((0, 0, 447, 1000), "bianca embarassed3")
image bianca embarassed_4 = LiveCrop((0, 0, 447, 1000), "bianca embarassed4")
image bianca embarassed_5 = LiveCrop((0, 0, 447, 1000), "bianca embarassed5")
image bianca embarassed_6 = LiveCrop((0, 0, 447, 1000), "bianca embarassed6")
image bianca guilty_1 = LiveCrop((0, 0, 447, 1000), "bianca guilty1")
image bianca lookaway_1 = LiveCrop((0, 0, 447, 1000), "bianca lookaway1")
image bianca lookaway_2 = LiveCrop((0, 0, 447, 1000), "bianca lookaway2")
image bianca lookaway_3 = LiveCrop((0, 0, 447, 1000), "bianca lookaway3")
image bianca pissed_1 = LiveCrop((0, 0, 447, 1000), "bianca pissed1")
image bianca pissed_2 = LiveCrop((0, 0, 447, 1000), "bianca pissed2")
image bianca pissed_3 = LiveCrop((0, 0, 447, 1000), "bianca pissed3")
image bianca sad_1 = LiveCrop((0, 0, 447, 1000), "bianca sad1")
image bianca sad_2 = LiveCrop((0, 0, 447, 1000), "bianca sad2")
image bianca sad_3 = LiveCrop((0, 0, 447, 1000), "bianca sad3")
image bianca sad_4 = LiveCrop((0, 0, 447, 1000), "bianca sad4")
image bianca sad_5 = LiveCrop((0, 0, 447, 1000), "bianca sad5")
image bianca sad_6 = LiveCrop((0, 0, 447, 1000), "bianca sad6")
image bianca sad_7 = LiveCrop((0, 0, 447, 1000), "bianca sad7")
image bianca sadsmile_1 = LiveCrop((0, 0, 447, 1000), "bianca sadsmile1")
image bianca sadsmile_2 = LiveCrop((0, 0, 447, 1000), "bianca sadsmile2")
image bianca sadsmile_3 = LiveCrop((0, 0, 447, 1000), "bianca sadsmile3")
image bianca shock_1 = LiveCrop((0, 0, 447, 1000), "bianca shock1")
image bianca shock_2 = LiveCrop((0, 0, 447, 1000), "bianca shock2")
image bianca shock_3 = LiveCrop((0, 0, 447, 1000), "bianca shock3")
image bianca smile_1 = LiveCrop((0, 0, 447, 1000), "bianca smile1")
image bianca smile_2 = LiveCrop((0, 0, 447, 1000), "bianca smile2")
image bianca smile_3 = LiveCrop((0, 0, 447, 1000), "bianca smile3")
image bianca smile_4 = LiveCrop((0, 0, 447, 1000), "bianca smile4")
image bianca smile_5 = LiveCrop((0, 0, 447, 1000), "bianca smile5")
image bianca smile_6 = LiveCrop((0, 0, 447, 1000), "bianca smile6")
image bianca smirk_1 = LiveCrop((0, 0, 447, 1000), "bianca smirk1")
image bianca talk_1 = LiveCrop((0, 0, 447, 1000), "bianca talk1")
image bianca unimpressed_1 = LiveCrop((0, 0, 447, 1000), "bianca unimpressed1")
image bianca wink_1 = LiveCrop((0, 0, 447, 1000), "bianca wink1")
image bianca wink_2 = LiveCrop((0, 0, 447, 1000), "bianca wink2")
image bianca wink_3 = LiveCrop((0, 0, 447, 1000), "bianca wink3")
image bianca worried_1 = LiveCrop((0, 0, 447, 1000), "bianca worried1")
image bianca yawn_1 = LiveCrop((0, 0, 447, 1000), "bianca yawn1")


### INIZIALIZZAZIONE DATI: EDWARD ###

# PERSONAGGIO #
define e = Character("Edward", who_color="#9e2e12", image="edward")

# ESPRESSIONI #
image edward argue_1 = LiveCrop((0, 0, 494, 1050), "edward argue1")
image edward default_1 = LiveCrop((0, 0, 494, 1050), "edward default1")
image edward disagree_1 = LiveCrop((0, 0, 494, 1050), "edward disagree1")
image edward glare_1 = LiveCrop((0, 0, 494, 1050), "edward glare1")
image edward mock_1 = LiveCrop((0, 0, 494, 1050), "edward mock1")
image edward orly_1 = LiveCrop((0, 0, 494, 1050), "edward orly1")
image edward sad_1 = LiveCrop((0, 0, 494, 1050), "edward sad1")
image edward sadsmile_1 = LiveCrop((0, 0, 494, 1050), "edward sadsmile1")
image edward shocked_1 = LiveCrop((0, 0, 494, 1050), "edward shocked1")
image edward smile_1 = LiveCrop((0, 0, 494, 1050), "edward smile1")
image edward smile_2 = LiveCrop((0, 0, 494, 1050), "edward smile2")
image edward smile_3 = LiveCrop((0, 0, 494, 1050), "edward smile3")
image edward smile_4 = LiveCrop((0, 0, 494, 1050), "edward smile4")
image edward smile_5 = LiveCrop((0, 0, 494, 1050), "edward smile5")
image edward smile_6 = LiveCrop((0, 0, 494, 1050), "edward smile6")
image edward smirk_1 = LiveCrop((0, 0, 494, 1050), "edward smirk1")
image edward smirk_2 = LiveCrop((0, 0, 494, 1050), "edward smirk2")
image edward surprised_1 = LiveCrop((0, 0, 494, 1050), "edward surprised1")
image edward unimpressed_1 = LiveCrop((0, 0, 494, 1050), "edward unimpressed1")
image edward upset_1 = LiveCrop((0, 0, 494, 1050), "edward upset1")
image edward upset_2 = LiveCrop((0, 0, 494, 1050), "edward upset2")
image edward upset_3 = LiveCrop((0, 0, 494, 1050), "edward upset3")
image edward upset_4 = LiveCrop((0, 0, 494, 1050), "edward upset4")
image edward urgh_1 = LiveCrop((0, 0, 494, 1050), "edward urgh1")
image edward wink_1 = LiveCrop((0, 0, 494, 1050), "edward wink1")
image edward wink_2 = LiveCrop((0, 0, 494, 1050), "edward wink2")


### INIZIALIZZAZIONE DATI: ELISE ###

# PERSONAGGIO #
define l = Character("Elise", who_color="#bf15bc", image="elise")

# ESPRESSIONI: DIVISA SCOLASTICA #
image elise angry_1 = LiveCrop((0, 0, 562, 960), "elise angry1")
image elise angry_2 = LiveCrop((0, 0, 562, 960), "elise angry2")
image elise angry_3 = LiveCrop((0, 0, 562, 960), "elise angry3")
image elise angry_4 = LiveCrop((0, 0, 562, 960), "elise angry4")
image elise angry_5 = LiveCrop((0, 0, 562, 960), "elise angry5")
image elise angry_6 = LiveCrop((0, 0, 562, 960), "elise angry6")
image elise crazy_1 = LiveCrop((0, 0, 562, 960), "elise crazy1")
image elise crazy_2 = LiveCrop((0, 0, 562, 960), "elise crazy2")
image elise default_1 = LiveCrop((0, 0, 562, 960), "elise default1")
image elise embarassed_1 = LiveCrop((0, 0, 562, 960), "elise embarassed1")
image elise embarassed_2 = LiveCrop((0, 0, 562, 960), "elise embarassed2")
image elise huh_1 = LiveCrop((0, 0, 562, 960), "elise huh1")
image elise huh_2 = LiveCrop((0, 0, 562, 960), "elise huh2")
image elise lookaway_1 = LiveCrop((0, 0, 562, 960), "elise lookaway1")
image elise pout_1 = LiveCrop((0, 0, 562, 960), "elise pout1")
image elise pout_2 = LiveCrop((0, 0, 562, 960), "elise pout2")
image elise pout_3 = LiveCrop((0, 0, 562, 960), "elise pout3")
image elise pout_4 = LiveCrop((0, 0, 562, 960), "elise pout4")
image elise relieved_1 = LiveCrop((0, 0, 562, 960), "elise relieved1")
image elise relieved_2 = LiveCrop((0, 0, 562, 960), "elise relieved2")
image elise sad_1 = LiveCrop((0, 0, 562, 960), "elise sad1")
image elise sad_2 = LiveCrop((0, 0, 562, 960), "elise sad2")
image elise sad_3 = LiveCrop((0, 0, 562, 960), "elise sad3")
image elise scared_1 = LiveCrop((0, 0, 562, 960), "elise scared1")
image elise scared_2 = LiveCrop((0, 0, 562, 960), "elise scared2")
image elise shock_1 = LiveCrop((0, 0, 562, 960), "elise shock1")
image elise shock_2 = LiveCrop((0, 0, 562, 960), "elise shock2")
image elise smile_1 = LiveCrop((0, 0, 562, 960), "elise smile1")
image elise smile_2 = LiveCrop((0, 0, 562, 960), "elise smile2")
image elise smile_3 = LiveCrop((0, 0, 562, 960), "elise smile3")
image elise smile_4 = LiveCrop((0, 0, 562, 960), "elise smile4")
image elise smile_5 = LiveCrop((0, 0, 562, 960), "elise smile5")
image elise smile_6 = LiveCrop((0, 0, 562, 960), "elise smile6")
image elise smirk_1 = LiveCrop((0, 0, 562, 960), "elise smirk1")
image elise smirk_2 = LiveCrop((0, 0, 562, 960), "elise smirk2")
image elise sweat_1 = LiveCrop((0, 0, 562, 960), "elise sweat1")
image elise sweat_2 = LiveCrop((0, 0, 562, 960), "elise sweat2")
image elise sweat_3 = LiveCrop((0, 0, 562, 960), "elise sweat3")
image elise sweat_4 = LiveCrop((0, 0, 562, 960), "elise sweat4")
image elise sweat_5 = LiveCrop((0, 0, 562, 960), "elise sweat5")
image elise sweat_6 = LiveCrop((0, 0, 562, 960), "elise sweat6")
image elise sweat_7 = LiveCrop((0, 0, 562, 960), "elise sweat7")
image elise sweat_8 = LiveCrop((0, 0, 562, 960), "elise sweat8")
image elise sweat_9 = LiveCrop((0, 0, 562, 960), "elise sweat9")
image elise sweat_10 = LiveCrop((0, 0, 562, 960), "elise sweat10")
image elise sweat_11 = LiveCrop((0, 0, 562, 960), "elise sweat11")
image elise tears_1 = LiveCrop((0, 0, 562, 960), "elise tears1")
image elise tears_2 = LiveCrop((0, 0, 562, 960), "elise tears2")
image elise tears_3 = LiveCrop((0, 0, 562, 960), "elise tears3")
image elise tears_4 = LiveCrop((0, 0, 562, 960), "elise tears4")
image elise tears_5 = LiveCrop((0, 0, 562, 960), "elise tears5")
image elise tears_6 = LiveCrop((0, 0, 562, 960), "elise tears6")
image elise tears_7 = LiveCrop((0, 0, 562, 960), "elise tears7")
image elise tears_8 = LiveCrop((0, 0, 562, 960), "elise tears8")
image elise tears_9 = LiveCrop((0, 0, 562, 960), "elise tears9")
image elise tears_10 = LiveCrop((0, 0, 562, 960), "elise tears10")
image elise wink_1 = LiveCrop((0, 0, 562, 960), "elise wink1")
image elise wink_2 = LiveCrop((0, 0, 562, 960), "elise wink2")
image elise wink_3 = LiveCrop((0, 0, 562, 960), "elise wink3")
image elise wink_4 = LiveCrop((0, 0, 562, 960), "elise wink4")
image elise shadowed_1 = LiveCrop((0, 0, 562, 960), "elise shadowed1")

# ESPRESSIONI: CASUAL #
image elise casual angry_1 = LiveCrop((0, 0, 568, 960), "elise casual angry1")
image elise casual angry_2 = LiveCrop((0, 0, 568, 960), "elise casual angry2")
image elise casual angry_3 = LiveCrop((0, 0, 568, 960), "elise casual angry3")
image elise casual angry_4 = LiveCrop((0, 0, 568, 960), "elise casual angry4")
image elise casual angry_5 = LiveCrop((0, 0, 568, 960), "elise casual angry5")
image elise casual angry_6 = LiveCrop((0, 0, 568, 960), "elise casual angry6")
image elise casual crazy_1 = LiveCrop((0, 0, 568, 960), "elise casual crazy1")
image elise casual crazy_2 = LiveCrop((0, 0, 568, 960), "elise casual crazy2")
image elise casual default_1 = LiveCrop((0, 0, 568, 960), "elise casual default1")
image elise casual embarassed_1 = LiveCrop((0, 0, 568, 960), "elise casual embarassed1")
image elise casual embarassed_2 = LiveCrop((0, 0, 568, 960), "elise casual embarassed2")
image elise casual huh_1 = LiveCrop((0, 0, 568, 960), "elise casual huh1")
image elise casual huh_2 = LiveCrop((0, 0, 568, 960), "elise casual huh2")
image elise casual lookaway_1 = LiveCrop((0, 0, 568, 960), "elise casual lookaway1")
image elise casual pout_1 = LiveCrop((0, 0, 568, 960), "elise casual pout1")
image elise casual pout_2 = LiveCrop((0, 0, 568, 960), "elise casual pout2")
image elise casual pout_3 = LiveCrop((0, 0, 568, 960), "elise casual pout3")
image elise casual pout_4 = LiveCrop((0, 0, 568, 960), "elise casual pout4")
image elise casual relieved_1 = LiveCrop((0, 0, 568, 960), "elise casual relieved1")
image elise casual relieved_2 = LiveCrop((0, 0, 568, 960), "elise casual relieved2")
image elise casual sad_1 = LiveCrop((0, 0, 568, 960), "elise casual sad1")
image elise casual sad_2 = LiveCrop((0, 0, 568, 960), "elise casual sad2")
image elise casual sad_3 = LiveCrop((0, 0, 568, 960), "elise casual sad3")
image elise casual scared_1 = LiveCrop((0, 0, 568, 960), "elise casual scared1")
image elise casual scared_2 = LiveCrop((0, 0, 568, 960), "elise casual scared2")
image elise casual shock_1 = LiveCrop((0, 0, 568, 960), "elise casual shock1")
image elise casual shock_2 = LiveCrop((0, 0, 568, 960), "elise casual shock2")
image elise casual smile_1 = LiveCrop((0, 0, 568, 960), "elise casual smile1")
image elise casual smile_2 = LiveCrop((0, 0, 568, 960), "elise casual smile2")
image elise casual smile_3 = LiveCrop((0, 0, 568, 960), "elise casual smile3")
image elise casual smile_4 = LiveCrop((0, 0, 568, 960), "elise casual smile4")
image elise casual smile_5 = LiveCrop((0, 0, 568, 960), "elise casual smile5")
image elise casual smile_6 = LiveCrop((0, 0, 568, 960), "elise casual smile6")
image elise casual smirk_1 = LiveCrop((0, 0, 568, 960), "elise casual smirk1")
image elise casual smirk_2 = LiveCrop((0, 0, 568, 960), "elise casual smirk2")
image elise casual sweat_1 = LiveCrop((0, 0, 568, 960), "elise casual sweat1")
image elise casual sweat_2 = LiveCrop((0, 0, 568, 960), "elise casual sweat2")
image elise casual sweat_3 = LiveCrop((0, 0, 568, 960), "elise casual sweat3")
image elise casual sweat_4 = LiveCrop((0, 0, 568, 960), "elise casual sweat4")
image elise casual sweat_5 = LiveCrop((0, 0, 568, 960), "elise casual sweat5")
image elise casual sweat_6 = LiveCrop((0, 0, 568, 960), "elise casual sweat6")
image elise casual sweat_7 = LiveCrop((0, 0, 568, 960), "elise casual sweat7")
image elise casual sweat_8 = LiveCrop((0, 0, 568, 960), "elise casual sweat8")
image elise casual sweat_9 = LiveCrop((0, 0, 568, 960), "elise casual sweat9")
image elise casual sweat_10 = LiveCrop((0, 0, 568, 960), "elise casual sweat10")
image elise casual sweat_11 = LiveCrop((0, 0, 568, 960), "elise casual sweat11")
image elise casual tears_1 = LiveCrop((0, 0, 568, 960), "elise casual tears1")
image elise casual tears_2 = LiveCrop((0, 0, 568, 960), "elise casual tears2")
image elise casual tears_3 = LiveCrop((0, 0, 568, 960), "elise casual tears3")
image elise casual tears_4 = LiveCrop((0, 0, 568, 960), "elise casual tears4")
image elise casual tears_5 = LiveCrop((0, 0, 568, 960), "elise casual tears5")
image elise casual tears_6 = LiveCrop((0, 0, 568, 960), "elise casual tears6")
image elise casual tears_7 = LiveCrop((0, 0, 568, 960), "elise casual tears7")
image elise casual tears_8 = LiveCrop((0, 0, 568, 960), "elise casual tears8")
image elise casual tears_9 = LiveCrop((0, 0, 568, 960), "elise casual tears9")
image elise casual tears_10 = LiveCrop((0, 0, 568, 960), "elise casual tears10")
image elise casual wink_1 = LiveCrop((0, 0, 568, 960), "elise casual wink1")
image elise casual wink_2 = LiveCrop((0, 0, 568, 960), "elise casual wink2")
image elise casual wink_3 = LiveCrop((0, 0, 568, 960), "elise casual wink3")
image elise casual wink_4 = LiveCrop((0, 0, 568, 960), "elise casual wink4")

# DEADEND #
image elise deadend casual sad_2 = LiveCrop((0, 0, 568, 960), "elise deadend casual sad2")
image elise deadend casual shock_1 = LiveCrop((0, 0, 568, 960), "elise deadend casual shock1")
image elise deadend casual smile_2 = LiveCrop((0, 0, 568, 960), "elise deadend casual smile2")

### INIZIALIZZAZIONE DATI: GAIN ###

# PERSONAGGIO #
define g = Character("Gain", who_color="#145ebf", image="gain")

# ESPRESSIONI #
image gain alarmed_1 = LiveCrop((0, 0, 503, 1000), "gain alarmed1")
image gain angry_1 = LiveCrop((0, 0, 503, 1000), "gain angry1")
image gain angry_2 = LiveCrop((0, 0, 503, 1000), "gain angry2")
image gain angry_3 = LiveCrop((0, 0, 503, 1000), "gain angry3")
image gain argue_1 = LiveCrop((0, 0, 503, 1000), "gain argue1")
image gain default_1 = LiveCrop((0, 0, 503, 1000), "gain default1")
image gain disbelief_1 = LiveCrop((0, 0, 503, 1000), "gain disbelief1")
image gain embarassed_1 = LiveCrop((0, 0, 503, 1000), "gain embarassed1")
image gain embarassed_2 = LiveCrop((0, 0, 503, 1000), "gain embarassed2")
image gain embarassed_3 = LiveCrop((0, 0, 503, 1000), "gain embarassed3")
image gain frown_1 = LiveCrop((0, 0, 503, 1000), "gain frown1")
image gain frown_2 = LiveCrop((0, 0, 503, 1000), "gain frown2")
image gain frown_3 = LiveCrop((0, 0, 503, 1000), "gain frown3")
image gain lookaway_1 = LiveCrop((0, 0, 503, 1000), "gain lookaway1")
image gain pout_1 = LiveCrop((0, 0, 503, 1000), "gain pout1")
image gain sad_1 = LiveCrop((0, 0, 503, 1000), "gain sad1")
image gain shy_1 = LiveCrop((0, 0, 503, 1000), "gain shy1")
image gain shy_2 = LiveCrop((0, 0, 503, 1000), "gain shy2")
image gain smile_1 = LiveCrop((0, 0, 503, 1000), "gain smile1")
image gain smile_2 = LiveCrop((0, 0, 503, 1000), "gain smile2")
image gain smile_3 = LiveCrop((0, 0, 503, 1000), "gain smile3")
image gain smile_4 = LiveCrop((0, 0, 503, 1000), "gain smile4")
image gain smile_5 = LiveCrop((0, 0, 503, 1000), "gain smile5")
image gain smile_6 = LiveCrop((0, 0, 503, 1000), "gain smile6")
image gain smile_7 = LiveCrop((0, 0, 503, 1000), "gain smile7")
image gain smirk_1 = LiveCrop((0, 0, 503, 1000), "gain smirk1")
image gain smirk_2 = LiveCrop((0, 0, 503, 1000), "gain smirk2")
image gain smug_1 = LiveCrop((0, 0, 503, 1000), "gain smug1")
image gain surprised_1 = LiveCrop((0, 0, 503, 1000), "gain surprised1")
image gain surprised_2 = LiveCrop((0, 0, 503, 1000), "gain surprised2")
image gain surprised_3 = LiveCrop((0, 0, 503, 1000), "gain surprised3")
image gain surprised_4 = LiveCrop((0, 0, 503, 1000), "gain surprised4")
image gain uneasy_1 = LiveCrop((0, 0, 503, 1000), "gain uneasy1")
image gain uneasy_2 = LiveCrop((0, 0, 503, 1000), "gain uneasy2")
image gain unimpressed_1 = LiveCrop((0, 0, 503, 1000), "gain unimpressed1")
image gain wink_1 = LiveCrop((0, 0, 503, 1000), "gain wink1")
image gain wink_2 = LiveCrop((0, 0, 503, 1000), "gain wink2")
image gain wink_3 = LiveCrop((0, 0, 503, 1000), "gain wink3")
image gain shadowed_1 = LiveCrop((0, 0, 503, 1000), "gain shadowed1")
image gain shadowed_1_sit = LiveCrop((0, 0, 503, 600), "gain shadowed1")


### INIZIALIZZAZIONE DATI: NORMAN ###

# PERSONAGGIO #
define n = Character("Norman", who_color="#07002d", image="norman")

# ESPRESSIONI #
image norman angry_1 = LiveCrop((0, 0, 858, 1000), "norman angry1")
image norman awkward_1 = LiveCrop((0, 0, 858, 1000), "norman awkward1")
image norman default_1 = LiveCrop((0, 0, 858, 1000), "norman default1")
image norman dread_1 = LiveCrop((0, 0, 858, 1000), "norman dread1")
image norman evil_1 = LiveCrop((0, 0, 858, 1000), "norman evil1")
image norman frown_1 = LiveCrop((0, 0, 858, 1000), "norman frown1")
image norman pout_1 = LiveCrop((0, 0, 858, 1000), "norman pout1")
image norman sad_1 = LiveCrop((0, 0, 858, 1000), "norman sad1")
image norman smile_1 = LiveCrop((0, 0, 858, 1000), "norman smile1")
image norman smile_2 = LiveCrop((0, 0, 858, 1000), "norman smile2")
image norman smile_3 = LiveCrop((0, 0, 858, 1000), "norman smile3")
image norman smirk_1 = LiveCrop((0, 0, 858, 1000), "norman smirk1")
image norman surprised_1 = LiveCrop((0, 0, 858, 1000), "norman surprised1")
image norman unimpressed_1 = LiveCrop((0, 0, 858, 1000), "norman unimpressed1")
image norman wink_1 = LiveCrop((0, 0, 858, 1000), "norman wink1")

# DEADEND #
image norman deadend angry_1 = LiveCrop((0, 0, 858, 1000), "norman deadend angry1")
image norman deadend default_1 = LiveCrop((0, 0, 858, 1000), "norman deadend default1")
image norman deadend awkward_1 = LiveCrop((0, 0, 858, 1000), "norman deadend awkward1")
image norman deadend default_1 = LiveCrop((0, 0, 858, 1000), "norman deadend default1")
image norman deadend dread_1 = LiveCrop((0, 0, 858, 1000), "norman deadend dread1")
image norman deadend evil_1 = LiveCrop((0, 0, 858, 1000), "norman deadend evil1")
image norman deadend pout_1 = LiveCrop((0, 0, 858, 1000), "norman deadend pout1")
image norman deadend smile_1 = LiveCrop((0, 0, 858, 1000), "norman deadend smile1")
image norman deadend smile_3 = LiveCrop((0, 0, 858, 1000), "norman deadend smile3")
image norman deadend smirk_1 = LiveCrop((0, 0, 858, 1000), "norman deadend smirk1")
image norman deadend surprised_1 = LiveCrop((0, 0, 858, 1000), "norman deadend surprised1")

### INIZIALIZZAZIONE DATI: PERCY ###

# PERSONAGGIO #
define p = Character("Percy", who_color="#2d0000", image="percy")

# ESPRESSIONI #
image percy alarmed_1 = LiveCrop((0, 0, 549, 1080), "percy alarmed1")
image percy alarmed_2 = LiveCrop((0, 0, 549, 1080), "percy alarmed2")
image percy angry_1 = LiveCrop((0, 0, 549, 1080), "percy angry1")
image percy angry_2 = LiveCrop((0, 0, 549, 1080), "percy angry2")
image percy argue_1 = LiveCrop((0, 0, 549, 1080), "percy argue1")
image percy default_1 = LiveCrop((0, 0, 549, 1080), "percy default1")
image percy embarassed_1 = LiveCrop((0, 0, 549, 1080), "percy embarassed1")
image percy embarassed_2 = LiveCrop((0, 0, 549, 1080), "percy embarassed2")
image percy evil_1 = LiveCrop((0, 0, 549, 1080), "percy evil1")
image percy evil_2 = LiveCrop((0, 0, 549, 1080), "percy evil2")
image percy failpoker_1 = LiveCrop((0, 0, 549, 1080), "percy failpoker1")
image percy frown_1 = LiveCrop((0, 0, 549, 1080), "percy frown1")
image percy frown_2 = LiveCrop((0, 0, 549, 1080), "percy frown2")
image percy lookaway_1 = LiveCrop((0, 0, 549, 1080), "percy lookaway1")
image percy pout_1 = LiveCrop((0, 0, 549, 1080), "percy pout1")
image percy sadsmile_1 = LiveCrop((0, 0, 549, 1080), "percy sadsmile1")
image percy sadsmile_2 = LiveCrop((0, 0, 549, 1080), "percy sadsmile2")
image percy smile_1 = LiveCrop((0, 0, 549, 1080), "percy smile1")
image percy smile_2 = LiveCrop((0, 0, 549, 1080), "percy smile2")
image percy smile_3 = LiveCrop((0, 0, 549, 1080), "percy smile3")
image percy smile_4 = LiveCrop((0, 0, 549, 1080), "percy smile4")
image percy smile_5 = LiveCrop((0, 0, 549, 1080), "percy smile5")
image percy smile_6 = LiveCrop((0, 0, 549, 1080), "percy smile6")
image percy smile_7 = LiveCrop((0, 0, 549, 1080), "percy smile7")
image percy smirk_1 = LiveCrop((0, 0, 549, 1080), "percy smirk1")
image percy smirk_2 = LiveCrop((0, 0, 549, 1080), "percy smirk2")
image percy smirk_3 = LiveCrop((0, 0, 549, 1080), "percy smirk3")
image percy surprised_1 = LiveCrop((0, 0, 549, 1080), "percy surprised1")
image percy surprised_2 = LiveCrop((0, 0, 549, 1080), "percy surprised2")
image percy surprised_3 = LiveCrop((0, 0, 549, 1080), "percy surprised3")
image percy uneasy_1 = LiveCrop((0, 0, 549, 1080), "percy uneasy1")
image percy uneasy_2 = LiveCrop((0, 0, 549, 1080), "percy uneasy2")
image percy uneasy_3 = LiveCrop((0, 0, 549, 1080), "percy uneasy3")
image percy unhappy_1 = LiveCrop((0, 0, 549, 1080), "percy unhappy1")
image percy unhappy_2 = LiveCrop((0, 0, 549, 1080), "percy unhappy2")
image percy unimpressed_1 = LiveCrop((0, 0, 549, 1080), "percy unimpressed1")
image percy unimpressed_2 = LiveCrop((0, 0, 549, 1080), "percy unimpressed2")
image percy upset_1 = LiveCrop((0, 0, 549, 1080), "percy upset1")
image percy urgh_1 = LiveCrop((0, 0, 549, 1080), "percy urgh1")
image percy urgh_2 = LiveCrop((0, 0, 549, 1080), "percy urgh2")
image percy urgh_3 = LiveCrop((0, 0, 549, 1080), "percy urgh3")
image percy urgh_4 = LiveCrop((0, 0, 549, 1080), "percy urgh4")
image percy wink_1 = LiveCrop((0, 0, 549, 1080), "percy wink1")
image percy wink_2 = LiveCrop((0, 0, 549, 1080), "percy wink2")
image percy wink_3 = LiveCrop((0, 0, 549, 1080), "percy wink3")
image percy wink_4 = LiveCrop((0, 0, 549, 1080), "percy wink4")



##### INIZIALIZZAZIONE DATI: AUDIO #####

### BGM ###

# LIGHT #
define audio.light_serenita = "/audio/bgm/Light/Carpe Diem.mp3"
define audio.light_amici = "/audio/bgm/Light/Cheery Monday.mp3"
define audio.light_natura = "/audio/bgm/Light/Fireflies and Stardust.mp3"
define audio.light_daily = "/audio/bgm/Light/Groundwork.mp3"
define audio.light_ingegno = "/audio/bgm/Light/Industrious Ferret.mp3"
define audio.light_serata = "/audio/bgm/Light/Porch Swing Days - faster.mp3"
define audio.light_serata_lenta = "/audio/bgm/Light/Porch Swing Days - slower.mp3.mp3"
define audio.light_dolcezza = "/audio/bgm/Light/Rainbows.mp3"
define audio.light_situazione_buffa = "/audio/bgm/Light/Teddy Bear Waltz.mp3"
define audio.light_spiaggia = "/audio/bgm/Light/Funin and Sunin.mp3"
define audio.light_viaggio = "/audio/bgm/Light/On My Way.mp3"
define audio.light_rilassamento = "/audio/bgm/Light/Fretless.mp3"
define audio.light_appuntamento = "/audio/bgm/Bright/Midday Dance.mp3"
define audio.light_ricordi_insieme = "/audio/bgm/Bright/Luminous Rain.mp3"

# DARK #
define audio.dark_mistero = "/audio/bgm/Dark_World/Ossuary 1 - A Beginning.mp3"
define audio.dark_tensione = "/audio/bgm/Dark_World/Ossuary 2 - Turn.mp3"
define audio.dark_indagini = "/audio/bgm/Dark_World/Ossuary 3 - Words.mp3"
define audio.dark_tensione2 = "/audio/bgm/Dark_World/Ossuary 4 - Animate.mp3"
define audio.dark_suspense = "/audio/bgm/Dark_World/Ossuary 5 - Rest.mp3"
define audio.dark_silenzio = "/audio/bgm/Dark_World/Ossuary 6 - Air.mp3"
define audio.dark_mistero2 = "/audio/bgm/Dark_World/Ossuary 7 - Resolve.mp3"
define audio.dark_logica = "/audio/bgm/Dark_World/Basic Implosion.mp3"
define audio.dark_distorsione = "/audio/bgm/Mad_Pianist/Piece for Disaffected Piano One.mp3"
define audio.dark_incubo = "/audio/bgm/Mad_Pianist/Piece for Disaffected Piano Two.mp3"
define audio.dark_assurdo = "/audio/bgm/Mad_Pianist/Modern Piano Gamma - Rushed.mp3"
define audio.dark_pericolo = "/audio/bgm/Mad_Pianist/Modern Piano Beta - Jackhammer.mp3"

# MYST #
define audio.myst_indagini = "/audio/bgm/Noir/On the Ground.mp3"
define audio.myst_mistero = "/audio/bgm/Noir/Comfortable Mystery 3.mp3"
define audio.myst_mistero_eco = "/audio/bgm/Noir/Comfortable Mystery 2.mp3"
define audio.myst_mistero_soave = "/audio/bgm/Noir/Comfortable Mystery.mp3"
define audio.myst_mistero_meandri = "/audio/bgm/Noir/Comfortable Mystery 4.mp3"
define audio.myst_indagini_allegra = "/audio/bgm/Noir/Dances and Dames.mp3"
define audio.myst_il_piano = "/audio/bgm/Noir/Deadly Roulette.mp3"
define audio.myst_quiz = "/audio/bgm/Noir/Enigma.mp3"
define audio.myst_in_azione = "/audio/bgm/Noir/Fast Talkin.mp3"
define audio.myst_in_silenzio = "/audio/bgm/Noir/I Knew a Guy.mp3"
define audio.myst_una_storia_di_stile_sax = "/audio/bgm/Noir/Night on the Docks - Sax.mp3" # TEMA DI NORMAN
define audio.myst_una_storia_di_stile_tromba = "/audio/bgm/Noir/Night on the Docks - Trumpet.mp3" # TEMA DI NORMAN
define audio.myst_una_storia_di_stile = "/audio/bgm/Noir/.Night on the Docksmp3" # TEMA DI NORMAN
define audio.myst_hacking_in = "/audio/bgm/Noir/Rollin at 5 - electronic.mp3"
define audio.myst_infiltrazione = "/audio/bgm/Noir/Rollin at 5.mp3"
define audio.myst_ombre_misteriose = "/audio/bgm/Mystery/Myst on the Moor.mp3"
define audio.myst_tensione_e_inquietudine = "/audio/bgm/Mystery/Satiate.mp3"
define audio.myst_inquietudine = "/audio/bgm/Mystery/Satiate Strings.mp3"
define audio.myst_tensione = "/audio/bgm/Mystery/Satiate Percussion.mp3"

# SOULS #
define audio.souls.delicata_e_misteriosa = "/audio/bgm/Elegant_Piano/Atlantean Twilight.mp3" # TEMA DI BIANCA
define audio.souls.gentile_e_rassicurante = "/audio/bgm/Elegant_Piano/Awaiting Return.mp3" # TEMA DI GAIN
define audio.souls.elegante_e_malinconica = "/audio/bgm/Elegant_Piano/Continue Life.mp3" # TEMA DI ELISE
define audio.souls.delicata_e_eccentrica = "/audio/bgm/Elegant_Piano/Moonstone.mp3"
define audio.souls.felice_e_triste = "/audio/bgm/Elegant_Piano/Sapphire Isle.mp3" # TEMA PRINCIPALE
define audio.souls.serena_e_armoniosa = "/audio/bgm/Elegant_Piano/Starry.mp3" # TEMA DI PERCY
define audio.souls.profonda_e_innamorata = "/audio/bgm/Elegant_Piano/Two Together.mp3"
define audio.souls.giovane_e_pura = "/audio/bgm/Elegant_Piano/Vision of Persistence.mp3"
define audio.souls.sicura_e_emotiva = "/audio/bgm/Elegant_Piano/White.mp3" # TITOLI DI CODA - HAPPY ENDING
define audio.souls.calda_e_rassicurante = "/audio/bgm/Elegant_Piano/Winter Chimes.mp3" # TEMA DI EDWARD


### EFFETTI ###

# AMBIENTE #

# ARMI #

# BAGNO #

# CUCINA #
define audio.cucina_tazzina_rumorosa = "/audio/sounds/Cucina/cup-set-down.mp3"
define audio.cucina_cucchiaino_modesto = "/audio/sounds/Cucina/spoon-stirring-soft.mp3"
define audio.cucina_cucchiaino_rumoroso = "/audio/sounds/Cucina/spoon-stirring-loud.mp3"
define audio.cucina_microonde_pronto = "/audio/sounds/Cucina/microwave-beep.mp3"
define audio.cucina_versare = "/audio/sounds/Cucina/pouring-coffee.mp3"

# DISPOSITIVI #
define audio.dispositivi_sveglia = "/audio/sounds/Dispositivi/alarm-clock.mp3"

# MEZZI #
define audio.mezzi_autobus_interno_chiacchiere = "/audio/sounds/Mezzi/bus-interior.mp3"
define audio.mezzi_macchina_interno_rumoroso = "/audio/sounds/Mezzi/car-interior.mp3"
define audio.mezzi_macchina_interno_ovattato = "/audio/sounds/Mezzi/car-interior-muffled.mp3"

# PORTA #
define audio.porta_chiusura = "/audio/sounds/Porta/door-close.mp3"
define audio.porta_campanello_leggero = "/audio/sounds/Porta/doorbell.mp3"
define audio.porta_campanello_leggero_doppio = "/audio/sounds/Porta/doorbell-double.mp3"
define audio.porta_apertura_chiave = "/audio/sounds/Porta/door-unlock-keys.mp3"
define audio.porta_campanelle = "/audio/sounds/Porta/shop-door-bell.mp3"


# PULSANTI #

# UMANI #
define audio.umani_passi = "/audio/sounds/Umani/footsteps.mp3"
define audio.umani_passi_tacchi = "/audio/sounds/Umani/footsteps-heels.mp3"
define audio.umani_battito = "/audio/sounds/Umani/heartbeat.mp3"
define audio.umani_battito_veloce = "/audio/sounds/Umani/heartbeat-fast.mp3"
define audio.umani_battito_accelerazione_basso = "/audio/sounds/Umani/heartbeat-speeding-up.mp3"
define audio.umani_passi_scala_legno_scendere = "/audio/sounds/Umani/wooden-stairs-down.mp3"

# QUIZ ##
define audio.quiz_esatto = "/audio/sounds/Altro/magic-chime.mp3"
define audio.quiz_errato = "/audio/sounds/Altro/wrong-buzzer.mp3"

### INIZIALIZZAZIONE DATI: AMBIENTE ###
define nome_scuola = "Soul Street Academy"


### DEADEND ###

define deadend_counter = 0

screen dodge_up():
        textbutton "{color=#ffffff}{b}DODGE{/b}{/color}" xpos 0.5 ypos 1 background "#ff0000" action Jump("dodged_up")

screen dodge_sx():
        textbutton "{color=#ffffff}{b}DODGE{/b}{/color}" xpos 10 ypos 0.5 background "#ff0000" action Jump("dodged_sx")

### DREAD RUN ###

screen dread_run():
        textbutton "{color=#ffffff}{b}RUN{/b}{/color}" xpos 0.5 ypos 0.5 background "#0000ff" action Jump("dread_run")

### NORMAN ENCOUNTER ###
define elise_coming = False


define dread_run_counter = 0
define slow_down_run = 0

image tintred:
  Solid("#830303")
  alpha 0.5

############################## SCREEN ##############################



####### FUNZIONI DI SISTEMA #######

### SETUP ###

# NOME DEL PROTAGONISTA #
screen inserisci_nome():
    window:
        hbox:
            null width 20
            vbox:
                null height 20
                text "{i}My name is...{/i}"
                null height 20
                input default ""

### TIMER ###

define timer_range = 0
define timer_jump = 0

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.2 xmaximum 300 left_bar "#54000090"  right_bar "#d6d6d690" at alpha_dissolve # This is the timer bar.

screen hidden_countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('hidden_countdown'), Jump(timer_jump)])

screen numeric_countdown:
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    if time <= 2:
        text str(time) xpos .1 ypos .1 color "#FF0000" size 100
    else:
        text str(time) xpos .1 ypos .1 size 100 at alpha_dissolve

### DA INSERIRE NEL CODICE: #######
#
### PREPARAZIONE
# $ time = 5 # the time the timer takes to count down to 0.
# $ timer_range = 5 # a number matching time (bar only)
# $ timer_jump = 'menu1_slow' # the label to jump to when time runs out
### AVVIO
# show screen countdown
#
### INTERRUZIONE O CHIUSURA
# hide screen countdown
###################################

############################## ANIMAZIONI ##############################

####### POSIZIONI #######

transform front:
    linear 0.2 zoom 1.05

transform rear:
    linear 0.2 zoom 0.95


transform frontcenter:
    center
    linear 0.2 zoom 1.05

transform rearcenter:
    center
    linear 0.2 zoom 0.95

transform frontleft:
    left
    linear 0.2 zoom 1.05

transform rearleft:
    left
    linear 0.2 zoom 0.95

transform frontright:
    right
    linear 0.2 zoom 1.05

transform rearright:
    right
    linear 0.2 zoom 0.95

transform cleft:
    xanchor 0.2 yanchor 1.0 xpos 0.2 ypos 1.0
transform frontcleft:
    xanchor 0.2 yanchor 1.0 xpos 0.2 ypos 1.0
    linear 0.2 zoom 1.05
transform rearcleft:
    xanchor 0.2 yanchor 1.0 xpos 0.2 ypos 1.0
    linear 0.2 zoom 0.95


transform cright:
    xanchor 0.8 yanchor 1.0 xpos 0.8 ypos 1.0
transform frontcright:
    xanchor 0.8 yanchor 1.0 xpos 0.8 ypos 1.0
    linear 0.2 zoom 1.05
transform rearcright:
    xanchor 0.8 yanchor 1.0 xpos 0.8 ypos 1.0
    linear 0.2 zoom 0.95

transform ccleft:
    xanchor 0.3 yanchor 1.0 xpos 0.3 ypos 1.0
transform frontccleft:
    xanchor 0.3 yanchor 1.0 xpos 0.3 ypos 1.0
    linear 0.2 zoom 1.05
transform rearccleft:
    xanchor 0.3 yanchor 1.0 xpos 0.3 ypos 1.0
    linear 0.2 zoom 0.95

transform ccright:
    xanchor 0.7 yanchor 1.0 xpos 0.7 ypos 1.0
transform frontccright:
    xanchor 0.7 yanchor 1.0 xpos 0.7 ypos 1.0
    linear 0.2 zoom 1.05
transform rearccright:
    xanchor 0.7 yanchor 1.0 xpos 0.7 ypos 1.0
    linear 0.2 zoom 0.95



####### ENTRATE SLIDING #######

transform enter:
    xanchor 0.5 yanchor 1.0 ypos 1.0 xpos -0.5
    linear 2.0 xpos 0.5

transform enter_left:
            xanchor 0.5 yanchor 1.0 ypos 1.0 xpos -0.5
            linear 2.0 xpos 0.2


############################################################ SCRIPT ############################################################


############################## PROLOGO ##############################

# Bene! Qui è dove tutto comincia. Lascerò dei commenti anche all'interno dello script, così da ricordarmi il senso di ogni scena.
# Se sei qui devi essere un amico, una persona fidata, oppure un hacker! In ogni caso, buona lettura! :P

label start:
#    jump test
    jump prologue

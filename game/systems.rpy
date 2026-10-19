############################## TIMED EVENTS ##############################
##
## Every timed interaction in the game lives here:
##  - countdown: the timer used by the quiz questions of the "Information sharing" phases
##  - qte_dodge / qte_sequence: the dodge minigame of Tuesday night
##  - dread_run / dread_run_sequence: the escape from Norman on Wednesday
##
## All timers are multiplied by persistent.timer_scale, which the player can change
## from Preferences ("Timers: Normal / Relaxed").

default persistent.timer_scale = 1.0
default persistent.seen_qte_tutorial = False

default deadend_counter = 0
default elise_coming = False
default dread_run_counter = 0

init python:

    def timer_seconds(base):
        """Applies the player's timer preference to a base duration."""
        return base * (persistent.timer_scale or 1.0)

    def timer_color(remaining, total):
        frac = remaining / float(total) if total else 0
        if frac > 0.5:
            return "#d6d6d6"
        if frac > 0.25:
            return "#e6a23c"
        return "#e74c3c"

    # direction: (glyph shown on screen, keys that count as that direction)
    QTE_DIRECTIONS = {
        "up": (u"↑", ["K_UP", "K_w"]),
        "left": (u"←", ["K_LEFT", "K_a"]),
        "right": (u"→", ["K_RIGHT", "K_d"]),
        "down": (u"↓", ["K_DOWN", "K_s"]),
    }

    # Norman's lines during the dread run, keyed by the number of RUN presses.
    # Each entry is a list of (deadend expression, line).
    DREAD_RUN_LINES = {
        10: [("angry_1", "You can't run from me!")],
        20: [("smile_3", "It's really useless!")],
        30: [("awkward_1", "You are not going anywhere, you know?")],
        40: [("evil_1", "There is nothing here. Nowhere to run.")],
        50: [("smirk_1", "At least I set you free, of course.")],
        55: [("smile_1", "Seventy names came before mine in the old book, you know. I'm the seventy-first."),
             ("smirk_1", "The last in line. Never the least.")],
        60: [("default_1", "So please, just slow down. Let's walk together and talk.")],
        70: [("dread_1", "I asked you to SLOW DOWN.")],
        71: [("smile_1", "Now, now, how kind of you.")],
        72: [("smile_1", "You do really like Elise, right?")],
        73: [("smile_1", "And you don't wanna lose her.")],
        74: [("smile_1", "Let's make a deal.")],
        75: [("smile_1", "You live with her happily forever after.")],
        76: [("smile_1", "Just, before that, you have to win my game.")],
        77: [("smile_1", "There is something you want to discover.")],
        78: [("smile_1", "Do you wanna know what is it?")],
        79: [("smile_1", "Well, I'll tell you.")],
        80: [("smile_1", "You know..."),
             ("smile_1", "Someone..."),
             ("default_1", "KILLED both you and Elise."),
             ("smile_3", "...oh, and it happened two times!"),
             ("default_1", "The important thing is, he or she will try again."),
             ("smile_1", "Would you like to be ready and save pretty lil' flower, when the time comes?"),
             ("default_1", "Well then, play my game. Find out who the culprit is."),
             ("smile_3", "Come to Café Memoria at midnight if you want some hints!")],
        81: [("smile_3", "Go now, run!"),
             ("smile_3", "Run back to your world!"),
             ("smile_3", "Run back to your loved one!")],
    }
    DREAD_RUN_TOTAL = 82

####### TRANSFORMS #######

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

transform timer_pulse:
    zoom 1.0
    ease 0.25 zoom 1.08
    ease 0.25 zoom 1.0
    repeat

transform qte_flash:
    alpha 0.0
    linear 0.06 alpha 1.0

transform qte_arrow_in:
    zoom 1.8 alpha 0.0
    easein 0.15 zoom 1.0 alpha 1.0

transform run_button_pop:
    zoom 1.3
    easeout 0.12 zoom 1.0

####### STYLES #######

style timer_frame:
    background Solid("#000000aa")
    padding (24, 12)
    xsize 460

style timer_label:
    size 22
    color "#d6d6d6"
    bold True

style qte_title:
    size 64
    bold True
    color "#ffffff"
    outlines [(4, "#830303", 0, 0)]

style qte_arrow:
    size 200
    bold True
    color "#ffffff"
    outlines [(6, "#830303", 0, 0)]

style qte_pad_button:
    background Solid("#00000099")
    hover_background Solid("#830303cc")
    xysize (90, 90)
    padding (0, 0)

style qte_pad_button_text:
    size 52
    bold True
    color "#ffffff"
    xalign 0.5
    yalign 0.5

style run_button:
    background Solid("#1a237ecc")
    hover_background Solid("#3949abee")
    padding (40, 18)

style run_button_text:
    size 44
    bold True
    color "#ffffff"

####### QUIZ COUNTDOWN #######
##
## Usage, inside a quiz question:
##     show screen countdown(5, "label_to_jump_on_timeout")
##     menu: ...
## and "hide screen countdown" in every answer.

screen countdown(seconds, jump_to):
    zorder 10
    default total = timer_seconds(seconds)
    default remaining = timer_seconds(seconds)

    timer 0.05 repeat True action If(remaining > 0.05,
        true=SetScreenVariable("remaining", remaining - 0.05),
        false=[Hide("countdown"), Play("sound", audio.quiz_errato), Jump(jump_to)])

    frame at alpha_dissolve:
        style "timer_frame"
        xalign 0.5
        yalign 0.12
        vbox:
            spacing 8
            hbox:
                xfill True
                text "TIME" style "timer_label"
                if remaining / total <= 0.25:
                    text "{:.1f}".format(remaining) style "timer_label" color timer_color(remaining, total) xalign 1.0 at timer_pulse
                else:
                    text "{:.1f}".format(remaining) style "timer_label" color timer_color(remaining, total) xalign 1.0
            bar:
                value remaining
                range total
                xfill True
                ysize 12
                left_bar Solid(timer_color(remaining, total))
                right_bar Solid("#ffffff22")

## Shows how well the group shared information at the end of a quiz.
screen quiz_results(score, total):
    zorder 10
    frame at alpha_dissolve:
        style "timer_frame"
        xalign 0.5
        yalign 0.12
        vbox:
            spacing 6
            text "INFORMATION SHARED" style "timer_label" xalign 0.5
            text "[score] / [total]" size 48 bold True xalign 0.5 color ("#2ecc71" if score == total else ("#e6a23c" if score * 2 >= total else "#e74c3c"))

####### DODGE (Tuesday night) #######

screen qte_dodge(direction, seconds):
    modal True
    zorder 20
    default total = timer_seconds(seconds)
    default remaining = timer_seconds(seconds)

    timer 0.02 repeat True action If(remaining > 0.02,
        true=SetScreenVariable("remaining", remaining - 0.02),
        false=Return(False))

    add Solid("#83030355") at qte_flash

    for d, info in QTE_DIRECTIONS.items():
        for k in info[1]:
            key k action Return(d == direction)

    vbox:
        align (0.5, 0.36)
        spacing 4
        text "DODGE!" style "qte_title" xalign 0.5
        text QTE_DIRECTIONS[direction][0] style "qte_arrow" xalign 0.5 at qte_arrow_in
        bar:
            value remaining
            range total
            xsize 460
            ysize 14
            xalign 0.5
            left_bar Solid("#ff3b30")
            right_bar Solid("#ffffff33")

    # Clickable pad, for players without a keyboard.
    grid 3 3:
        align (0.5, 0.94)
        spacing 6
        null
        textbutton QTE_DIRECTIONS["up"][0] style "qte_pad_button" action Return(direction == "up")
        null
        textbutton QTE_DIRECTIONS["left"][0] style "qte_pad_button" action Return(direction == "left")
        null
        textbutton QTE_DIRECTIONS["right"][0] style "qte_pad_button" action Return(direction == "right")
        null
        textbutton QTE_DIRECTIONS["down"][0] style "qte_pad_button" action Return(direction == "down")
        null

## Runs a sequence of dodges that get faster each time.
## Sets _return to True if every dodge succeeded, False at the first miss.
label qte_sequence(rounds=4, start=1.4, step=0.2, fastest=0.7):
    $ renpy.block_rollback()
    $ qte_round = 0
    $ qte_last = None
    while qte_round < rounds:
        $ qte_direction = renpy.random.choice([d for d in QTE_DIRECTIONS if d != qte_last])
        $ qte_last = qte_direction
        call screen qte_dodge(qte_direction, max(fastest, start - step * qte_round))
        if not _return:
            return False
        $ qte_round += 1
        with hpunch
        pause 0.35
    return True

####### DREAD RUN (Wednesday) #######

screen dread_run(presses, total):
    modal True
    zorder 15
    default pos = (renpy.random.uniform(0.25, 0.75), renpy.random.uniform(0.3, 0.7))

    add Solid("#000000") alpha min(0.8, presses / float(total) * 0.8)

    key "K_SPACE" action Return(True)
    key "K_RETURN" action Return(True)

    textbutton "RUN":
        style "run_button"
        pos pos
        anchor (0.5, 0.5)
        action Return(True)
        at run_button_pop

    vbox:
        align (0.5, 0.06)
        spacing 4
        text "ESCAPE" style "timer_label" xalign 0.5
        bar:
            value min(presses, total * 0.9)
            range total
            xsize 420
            ysize 10
            left_bar Solid("#3949ab")
            right_bar Solid("#ffffff22")
        text "Click RUN or press Space" size 18 color "#aaaaaa" xalign 0.5

label dread_run_sequence:
    $ renpy.block_rollback()
    $ dread_run_counter = 0
    while dread_run_counter < DREAD_RUN_TOTAL:
        call screen dread_run(dread_run_counter, DREAD_RUN_TOTAL)
        $ dread_run_counter += 1
        play sound audio.umani_passi
        if dread_run_counter in DREAD_RUN_LINES:
            stop sound
            if dread_run_counter == 70:
                show black with hpunch
            $ dr_lines = list(DREAD_RUN_LINES[dread_run_counter])
            while dr_lines:
                $ dr_expr, dr_text = dr_lines.pop(0)
                $ renpy.show("norman deadend " + dr_expr)
                $ renpy.transition(dissolve)
                n "[dr_text]"
            hide norman with dissolve
    stop sound
    return

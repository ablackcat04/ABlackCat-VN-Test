init:
    $ style.default.font = "Taipei.ttf"
    $ style.default.language = "Taipei"
    define config.default_music_volume = 0.3
    define config.default_sfx_volume = 0.4
    define config.default_voice_volume = 1.0

    default FBI = False


init python:
    style.default.layout = "greedy"



# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define C = Character("Aiko")
define M = Character("Music Player")
define F = Character("FBI")

define FBIv = "audio/FBI open up e.ogg"

define Polar = "audio/ps.ogg"
define BC = "audio/-1BC.ogg"

# define I = renpy.music.is_playing(channel='music')

image Aiko = "Aiko Casual Cat Frown.png"
image Aiko angry = "Aiko_Casual_Cat_Closed_Smile.png"
image PS = "PS.png"

image FBIm movie = Movie(fps=60,play="FBI_Video.webm",loop=False,channel='Movie')




# The game starts here.

label start:

    $ FBI = False

    camera:
        perspective True

    show Aiko:
        zoom 0.4

    play voice "audio/voice/Hi, I_m Aiko, your music playing assistant.ogg"
    C "Hi, I'm Aiko, your music playing assistant."

    play voice "audio/voice/Now, I_ll play my favorite song.ogg"
    C "Now, I'll play my favorite song."

    play music Polar noloop volume 1.0


    show PS at right:
        zoom 0.4
        xoffset -150
        yoffset -500

    M "Playing \"Polarize System by ABlackCat\" ,click to skip"

    hide PS

    if (renpy.music.is_playing(channel='music')):

        $ FBI = True

        stop music fadeout 1.5

        pause 1.2

        show Aiko angry:
            blur 1.0

        play voice "audio/voice/Why you stop my favorite song.ogg"
        C "Why you stop my favorite song!??"

        play voice "audio/voice/How dare you.ogg"
        C "How dare you!??"

        play voice "audio/voice/I_ll call FBI to arrest you.ogg"
        C "I'll call FBI to arrest you!!!"

        hide Aiko


    else :
        M "press to Play \"iron door.ogg\" *3 "

    $ C = 0



    while C<3:

        play sound "audio/iron door.ogg" volume 0.25


        pause 0.22

        $ C = C+1

label FBI:

    if FBI:

        # play sound FBIv

        show FBIm movie

        F "FBI open up!!"

        "You were arrested by FBI"

        "Bad End"

    else :

        "You finished the game!!"
        "good job!!"

    # This ends the game.

    hide FBI movie
    with dissolve
    stop Movie fadeout 3

    return

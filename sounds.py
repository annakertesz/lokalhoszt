from pygame import *
mixer.init()
soundtrack = mixer.music.load('sounds/newsoundtrack.wav')
intro_music = mixer.music.load('sounds/bensound-retrosoul.wav')
sound = {
    'block': mixer.Sound('sounds/block.wav'),
    'swing': mixer.Sound('sounds/swing.wav'),
    'hit1': mixer.Sound('sounds/hit1.wav'),
    'hit2': mixer.Sound('sounds/hit2.wav')
    'hit3': mixer.Sound('sounds/hit3.wav'),
    'hit4': mixer.Sound('sounds/hit4.wav'),
    'hit5': mixer.Sound('sounds/hit5.wav'),
    'headbutt': mixer.Sound('sounds/headbutt.wav'),
    'kick1': mixer.Sound('sounds/kick1.wav'),
    'kick2': mixer.Sound('sounds/kick2.wav'),
    'kick3': mixer.Sound('sounds/kick3.wav'),
    'kick4': mixer.Sound('sounds/kick4.wav'),
    'spin1': mixer.Sound('sounds/spin1.wav'),
    'empty_kick': mixer.Sound('sounds/kick_empty.wav')
}

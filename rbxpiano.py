import sys
import requests 
import json
import emoji
import keyboard
import time
import random
from colorama import just_fix_windows_console
from colorama import Fore
just_fix_windows_console()

sng = sys.argv[1]
bpm = sys.argv[2]
get1 = requests.get(f"https://raw.githubusercontent.com/ZipsterMX5/rbxpiano/refs/heads/main/songs/{sng}.json")
get2 = get1.json()
bpm = int(get2["bpm"]) * 1.9
legitmode1 = False
legitmode2 = False

print(Fore.YELLOW + emoji.emojize(":warning:") + '  To avoid distortion of the song, set the value "Transpose"/"Transposition" to ' + get2["transpose"] + "! If your piano does not have this function, sorry, we will probably build it in soon.")

answer = input(Fore.WHITE + 'Probably, at a high level of play, the judge may notice your illegitimacy. In order to make auto-play harder to notice, you can turn on the legitimate mode (y/n): ')
if answer != "y" and answer != "n":
    print(Fore.RED + emoji.emojize(":no_entry:") + ' Oops! You didn\'t write either "y" or "n" so we don\'t even know what to do in this case...')
if answer == "n":
    print(Fore.YELLOW + emoji.emojize(":warning:") + ' Okay, we warned you that you could be identified very easily.')
else:
    legitmode1 = True

answer = input(Fore.WHITE + 'Write "y" when you are ready to start the production, if you want to cancel the production then write "n":')
if answer != "y" and answer != "n":
    print(Fore.RED + emoji.emojize(":no_entry:") + ' Oops! You didn\'t write either "y" or "n" so we don\'t even know what to do in this case...')
if answer == "n":
    print(Fore.WHITE + emoji.emojize(":waving_hand:") + ' Goodbye! We look forward to seeing you later!')
    exit()
if answer == "y":
    print(Fore.GREEN + '3')
    time.sleep(1)
    print(Fore.YELLOW + '2')
    time.sleep(1)
    print(Fore.RED + '1')
    time.sleep(1)
    print(Fore.WHITE + emoji.emojize(":musical_keyboard:") + ' Now playing the song ' + get2["name"] + ' by ' + get2["author"] + ' at ' + get2["bpm"] + ' BPM.')

idx = 0
nnotes = [" ", "-", "[", "]"]
sng = get2["song"]
while idx < len(sng):
    if not sng[idx] in nnotes:     
        keyboard.press_and_release(sng[idx])
    else:
        if sng[idx] == ' ' and not sng[idx + 1] == '-':
            time.sleep(60 / bpm)
        if sng[idx] == '-':
            time.sleep(60 / bpm)
        if idx + 1 < len(sng):
            if sng[idx] == ']' and sng[idx + 1] != ' ':
                time.sleep(60 / bpm / 2)
        if sng[idx] == ']' and legitmode1:
            legitmode2 = True
        if sng[idx] == '[' and legitmode1:
            legitmode2 = False
    idx += 1
    if legitmode2:
        time.sleep(random.random() / 14)
        if random.randint(0,25) == 1:
            time.sleep(random.random() / 7)
8fllll8lk
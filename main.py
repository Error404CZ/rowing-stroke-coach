import pynput
import keyboard
import time

firstTimeS = 0
secondTimeS = 0
expoTimeS = 0

countS = 0

def strokes_Timer():
    global firstTimeS
    global secondTimeS
    global expoTimeS

    secondTimeS = time.time()
    expoTimeS = secondTimeS - firstTimeS
    print(1/expoTimeS*60)
    firstTimeS = time.time()

def count_Strokes():
    global countS
    countS += 1
    print(countS)

while True:
    keyboard.wait('space')
    strokes_Timer()
    count_Strokes()
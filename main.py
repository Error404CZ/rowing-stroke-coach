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

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def stop_Watch():
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)


start_time = time.time()
while True:
    keyboard.wait('space')
    strokes_Timer()
    count_Strokes()
    stop_Watch()
    print()
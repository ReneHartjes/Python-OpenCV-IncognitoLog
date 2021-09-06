import cv2 as cv
import numpy as np
import pyautogui
import time
from tkinter import *
import os


chromey = cv.imread('Spartal/Chromium.png', cv.IMREAD_UNCHANGED)
fft = cv.imread('Spartal/ffxt.png', cv.IMREAD_UNCHANGED)
Window = cv.imread('Spartal/Windowsb.png', cv.IMREAD_UNCHANGED)


while 1:



    screeny = pyautogui.screenshot('Evalvscreen.png')
    screeny = np.array(screeny)
    screeny = cv.cvtColor(screeny, cv.COLOR_RGB2BGR)
    time.sleep(0.05)
    res = cv.matchTemplate(chromey, screeny, cv.TM_CCOEFF_NORMED)
    Max = cv.minMaxLoc(res)




    if Max[1] >= 0.85:


        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        print(current_time)


        scren = pyautogui.screenshot('Numpero.png')
        scren.save(f"s {current_time}.png")




    time.sleep(0.05)
    resy = cv.matchTemplate(fft, screeny, cv.TM_CCOEFF_NORMED)
    Maxy = cv.minMaxLoc(resy)



    time.sleep(0.0001)

    if Maxy[1] >= 0.85:


        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        print(current_time)


        scren = pyautogui.screenshot('Numpero.png')
        scren.save(f"s {current_time}.png")



    time.sleep(0.05)
    res = cv.matchTemplate(Window, screeny, cv.TM_CCOEFF_NORMED)
    Maxim = cv.minMaxLoc(res)



    time.sleep(0.0001)

    if Maxim[1] >= 0.9:


        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        print(current_time)


        scren = pyautogui.screenshot('Numpero.png')
        scren.save(f"s {current_time}.png")


    time.sleep(0.0001)

    time.sleep(3)





import matplotlib
from PIL import ImageGrab
from PIL import Image
import time
import pyautogui as p
import random
i=0

f = open("Numbers2.txt", "w")


for z in range(1000) :
    num = z
    f.write('"')
    f.write("% s" %num)
    f.write('"')
    f.write(',')
    z+=1
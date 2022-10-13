from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C
import framebuf
import random 
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=200000)
oled = SSD1306_I2C(128, 64, i2c)   
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
inLoop = True
lst = [0]
word = []
sentence = []
finalWord = ""
while inLoop:
    del lst[0]
    if lst == ['.', '.', '.', '-', '-', '-', '.', '.', '.']:
        print("SOS")
    elif lst == ['.', '-']:
        word.append("A")
    elif lst == ['-', '.', '.', '.']:
        word.append("B")
    elif lst == ['-', '.', '-', '.']:
        word.append("C")
    elif lst == ['-', '.', '.']:
        word.append("D")
    elif lst == ['.']:
        word.append("E")
    elif lst == ['.', '.', '-', '.']:
        word.append("F")
    elif lst == ['-', '-', '.']:
        word.append("G")
    elif lst == ['.', '.', '.', '.']:
        word.append("H")
    elif lst == ['.', '.']:
        word.append("I")
    elif lst == ['.', '-', '-', '-']:
        word.append("J")
    elif lst == ['-', '.', '-']:
        word.append("K")
    elif lst == ['.', '-', '.', '.']:
        word.append("L")
    elif lst == ['-', '-']:
        word.append("M")
    elif lst == ['-', '.']:
        word.append("N")
    elif lst == ['-', '-', '-']:
        word.append("O")
    elif lst == ['.', '-', '-', '.']:
        word.append("P")
    elif lst == ['-', '-', '.', '-']:
        word.append("Q")
    elif lst == ['.', '-', '.']:
        word.append("R")
    elif lst == ['.', '.', '.']:
        word.append("S")
    elif lst == ['-']:
        word.append("T")
    elif lst == ['.', '.', '-']:
        word.append("T")
    elif lst == ['.', '.', '.', '-']:
        word.append("V")
    elif lst == ['.', '-', '-']:
        word.append("W")
    elif lst == ['-', '.', '.', '-']:
        word.append("X")
    elif lst == ['-', '.', '-', '-']:
        word.append("Y")
    elif lst == ['-', '-', '.', '.']:
        word.append("Z")
    elif lst == ['.', '-', '.', '-']:
        word.append(" ")
    sentence += word
    for y in word:
        finalWord += str(y)
        print(finalWord)
        oled.text("code", 0, 0)
        oled.text("translator", 0, 10)
        oled.text("v1.1", 0, 20)
        oled.text(str(finalWord), 0, 40)
        oled.show()
    word.clear()
    lst.clear()
    checkButton = True
    while checkButton:
        if button.value():
            time.sleep(0.05)
            if button.value():
                time.sleep(0.21)
                if button.value():
                    if button.value():
                        time.sleep(0.5)
                        if button.value():
                            time.sleep(1)
                            if button.value:
                                checkButton = False
                            else:
                                checkButton = True
                        else:
                            lst.append("-")
                else:
                    lst.append(".")
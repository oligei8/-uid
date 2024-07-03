import pyautogui as pag
import threading
import keyboard
import time
pag.FAILSAFE=True

def key_press(key):
   print(key.name)
keyboard.on_press(key_press)
keyboard.wait('a')
def click():
    while 1:
        pag.click(698, 638)
        time.sleep(0.5) 
        color1 = pag.pixel(698, 638)
        color2 = pag.pixel(849,617)
        if color1 == (203, 0, 0):
            pag.click(698, 638)
            time.sleep(7)
        if color2 == (0,204,13):
            pag.click(849,617)
            time.sleep(15)
        #time.sleep(2)
t = threading.Thread(target=click,daemon=True)
t.start()
keyboard.wait('p')

    
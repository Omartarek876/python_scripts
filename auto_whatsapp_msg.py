import pyautogui
import time
import os

# Move mouse to confirm the position (for debugging)
# while True:
#     x, y = pyautogui.position()
#     print(x, y)

pyautogui.hotkey('win')
time.sleep(1)
pyautogui.write('what')
# time.sleep(1)  # Added delay to ensure the 'what' search completes

# Force use of ImageNotFoundException
mypath = os.path.dirname(os.path.realpath(__file__)) + '\\what.png'
print(mypath)

try:
    isfind = None
    while isfind is None:
        isfind = pyautogui.locateOnScreen(mypath)
except pyautogui.ImageNotFoundException:
    print("Image not found")

pyautogui.hotkey('enter')
time.sleep(2)

pyautogui.hotkey('ctrl', 'f')
pyautogui.write('omy')
time.sleep(1)

pyautogui.press('down')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('hello')
pyautogui.press('enter')

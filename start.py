import pyautogui
import time
import os

app_list = [ "whatsapp" , "vscode" , "git bash"]
path_list = [ "\\what.png" , "\\vs.png" , "\\git.png"]
for app in app_list : 
    pyautogui.hotkey('alt', 'space')
    time.sleep(2)
    pyautogui.hotkey('n')
    time.sleep(1)
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write(app)
    time.sleep(1)
    # for icon in path_list : 
    #     mypath = os.path.dirname(os.path.realpath(__file__)) + icon
    #     print(mypath)
    #     time.sleep(2)

    #     try:
    #         isfind = None
    #         while isfind is None:
    #             isfind = pyautogui.locateOnScreen(mypath)
    #     except pyautogui.ImageNotFoundException:
    #         print("Image not found")
    
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('win' , 'left')
    time.sleep(2)




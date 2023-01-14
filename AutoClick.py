import pyautogui
import keyboard
import time


print("hello welcome to auto click create by ZeusX#6953")
time.sleep(2)
print("for start/stop press F9 ")

running = False

def on_press_f9(event):
    global running
    running = not running
    print('Start/Stop')

keyboard.on_press_key('f9', on_press_f9)

while True:
    if running:
        pyautogui.click()
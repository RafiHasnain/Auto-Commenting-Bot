import pyautogui
import time

comments = ["Hi","this is bot","I am showing of my Python skills"]

time.sleep(5)

for i in range(10):
    pyautogui.typewrite(comments[i%7])
    pyautogui.typewrite("\n")
    time.sleep(2)
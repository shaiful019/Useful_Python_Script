import pyautogui
import time

comments = ["Hello", "This  is a bot", "This comment is being generate automatically", "Isn't it cool?", "What do you think?", "A simple python script for autocomment", "Hola", "Konnichiwa", "Ohayo gujaimas"]

time.sleep(5)

for i in range(len(comments)):
    print(comments[i])
    s = str(comments[i])
    pyautogui.typewrite(s)
    pyautogui.typewrite("\n")
    time.sleep(2)



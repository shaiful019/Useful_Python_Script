import pyautogui
import time

# Make a list of some comments
comments = ["Hello", "This  is a bot", "This comment is being generate automatically", "Isn't it cool?", "What do you think?", "A simple python script for autocomment", "Hola", "Konnichiwa", "Ohayo gujaimas"]

# Pause for 5 second so that we can put our cursor on desired point
time.sleep(5)

for i in range(len(comments)):
    pyautogui.typewrite(comments[i])
    pyautogui.typewrite("\n")  # For pressing the Enter button
    time.sleep(3)  # Pause for 3 seconds



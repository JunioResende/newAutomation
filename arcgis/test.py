

from time import sleep
import pyautogui

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

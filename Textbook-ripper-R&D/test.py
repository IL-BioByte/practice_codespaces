import pyautogui
import time

print("Move your mouse to the desired position. You have 5 seconds...")
time.sleep(5)  
x, y = pyautogui.position() 
print(f"Coordinates: ({x}, {y})")



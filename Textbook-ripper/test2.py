import pyautogui
import time

# Replace these with your coordinates
top_left = (487, 264)
right_bottom = (828, 838)

# Calculate width and height
width = right_bottom[0] - top_left[0]
height = right_bottom[1] - top_left[1]

# Add a brief delay to set up the window properly
time.sleep(2)  # Gives you time to focus on the document viewer

# Take a screenshot of the specified region
screenshot = pyautogui.screenshot(region=(top_left[0], top_left[1], width, height))
screenshot.save("test_region_capture.png")
print("Screenshot saved as test_region_capture.png")

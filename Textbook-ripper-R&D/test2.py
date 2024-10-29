import mss
from PIL import Image

# Define coordinates
top_left = (460, 220)
right_bottom = (830, 830)

# Calculate width and height
width = right_bottom[0] - top_left[0]
height = right_bottom[1] - top_left[1]

with mss.mss() as sct:
    # Define the region for capture
    monitor = {
        "top": top_left[1],
        "left": top_left[0],
        "width": width,
        "height": height
    }

    # Capture the region
    screenshot = sct.grab(monitor)

    # Convert to a PIL Image and save
    img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
    img.save("mss_test_capture.png")
    print("Screenshot saved as mss_test_capture.png")

import argparse
import os
import tempfile
import pyautogui
import img2pdf
import mss
from PIL import Image
import time

def screenshot(top_left, right_bottom, next_page, total_page):
    rect_size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
    images = []
    temp_dir = tempfile.mkdtemp()

    with mss.mss() as sct:
        for i in range(total_page):
            page_num = "{}".format(i).zfill(len(str(total_page)))
            file_name = os.path.join(temp_dir, 'book-page-{}.png'.format(page_num))
            images.append(file_name)

            # Move to the next page button and click
            pyautogui.moveTo(*next_page, duration=1)
            pyautogui.click()
            time.sleep(1)  # Delay to ensure page loads fully

            # Capture the region using mss
            monitor = {
                "top": top_left[1],
                "left": top_left[0],
                "width": rect_size[0],
                "height": rect_size[1]
            }
            screenshot = sct.grab(monitor)
            img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
            img.save(file_name)

    return images

def image2pdf(images):
    with open("book.pdf", "wb") as f:
        f.write(img2pdf.convert(images))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take book screenshots.')
    parser.add_argument('top_left', type=str)
    parser.add_argument('right_bottom', type=str)
    parser.add_argument('next_button', type=str)
    parser.add_argument('total_page', type=int)

    args = parser.parse_args()

    top_left = tuple(map(int, args.top_left.split(',')))
    right_bottom = tuple(map(int, args.right_bottom.split(',')))
    next_button = tuple(map(int, args.next_button.split(',')))
    total_page = args.total_page

    print("Take book screenshot at {} {} and next at {} with {} pages".format(
        top_left, right_bottom, next_button, total_page
    ))

    images = screenshot(top_left, right_bottom, next_button, total_page)
    image2pdf(images)

    print("Done, book saved in book.pdf.")

from bot import click_if_exists, found
from pyautogui import hotkey, click, moveTo, press
from pyperclip import copy
from time import sleep, time
import os
from random import random
from PIL import ImageGrab
import subprocess


print (os.getcwd())

search_bar_location = (811, 358)

picture_locations = (
    (789, 576),
    (988, 571),
    (1278, 594),
    (766, 838),
    (942, 850),
    (1260, 829),
    (780, 1011),
    (976, 1011),
    (1224, 1011)
    )

query = input("Pick yer poison > ")
if query == 'q':
    quit()
time_to_spend = float(input("How many minutes? > "))
end = time() + time_to_spend * 60
url = 'https://huggingface.co/spaces/dalle-mini/dalle-mini'
tabs = 0

if not os.path.exists(f"image_library\\{query}"):
    os.makedirs(f"image_library\\{query}")

if not os.path.exists(f"image_library\\{query}\\best"):
    os.makedirs(f"image_library\\{query}\\best")

if not os.path.exists(f"image_library\\{query}\\worst"):
    os.makedirs(f"image_library\\{query}\\worst")

save_location = os.getcwd() + f"\\image_library\\{query}"

while time() < end:
    # open the site
    click_if_exists("luigi_chrome.png")
    hotkey("ctrl", "t")
    tabs += 1
    sleep(1)
    copy(url)
    hotkey("ctrl", "v")
    hotkey("enter")
    # enter the query
    copy(query)
    sleep(3)
    moveTo(782, 410)
    click()
    '''
    while not click_if_exists("search_bar.png"):
        print("looking for the search bar...")
        pass
    '''
    sleep(1)
    hotkey("ctrl", "v")
    moveTo(1321, 420)
    click()
print("done with main part")
sleep(1)
for i in range(tabs - 1):
    sleep(0.5)
    hotkey("ctrl", "shift", "tab")
while found("minimized_container.png"):
    pass

count = 0
# copy(f"{query}_{round(random() * pow(10, 10))}")

for i in range(tabs):
    if not found("too_much_traffic.png"):
        while found("minimized_container.png"):
            pass
        for index, coordinates in enumerate(picture_locations):
            x, y = coordinates
            moveTo(x, y)
            sleep(0.1)
            click(button = 'right')
            sleep(0.5)
            for i in range(3):
                press("down")
            press("enter")
            grabbed_image = False
            while not grabbed_image:
                try:
                    image = ImageGrab.grabclipboard()
                    image.save(f"image_library\\{query}\\{query} {round(random() * pow(10, 10))}.png", "PNG")
                    grabbed_image = True
                except OSError:
                    print("Couldn't grab the image, trying again...")
                    sleep(0.5)
            count += 1
        sleep(0.5)
        hotkey("ctrl", "tab")
sleep(0.5)
hotkey("ctrl", "shift", "tab")
for i in range(tabs):
    hotkey("ctrl", "w")
    sleep(0.2)
subprocess.Popen(r'explorer /select,"{1}\image_library\{0}"'.format(query, os.getcwd()))

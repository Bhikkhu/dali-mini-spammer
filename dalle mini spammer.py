from bot import click_if_exists, found
from pyautogui import hotkey, click, moveTo
from pyperclip import copy
from time import sleep, time
import os
from random import random

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
    sleep(4)
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
for i in range(tabs):
    for index, coordinates in enumerate(picture_locations):
        x, y = coordinates
        moveTo(x, y)
        sleep(0.1)
        click(button = 'right')
        sleep(2)
        click_if_exists("save_image_as.png")
        sleep(2)
        copy(f"{query}_{round(random() * pow(10, 10))}")
        hotkey("ctrl", "v")
        sleep(0.1)
        click_if_exists("file_bar.png", double = True)
        sleep(1)
        copy(save_location)
        hotkey("ctrl", "v")
        hotkey("enter")
        sleep(1)
        hotkey("alt", "s")
        count += 1
    sleep(0.5)
    hotkey("ctrl", "tab")
sleep(0.5)
hotkey("ctrl", "shift", "tab")

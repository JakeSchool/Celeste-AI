import pyautogui
import keyboard

TAS_PATH = "E:\SteamGames\steamapps\common\Celeste\Celeste.tas"

keyboard.wait("ctrl+alt+p")

with open(TAS_PATH, "w+") as file:
    file.write("10,L,J")
    keyboard.send("ctrl+p")
    keyboard.send("[")
    print("test")

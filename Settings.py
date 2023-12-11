import os
import sys

def RelativePath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

HOME_PATH = os.getcwd()
PICTURE_PATH = os.path.join(HOME_PATH, "pictures")

TITLE = "Roulette"
if os.name == "nt":
    FONT_NAME = RelativePath("C:\\Users\\Bao Cao\\Documents\\py project\\pyGame\\pygame-1.9.6\\Roulette\\Arial.ttf")
else:
    FONT_NAME = "Arial.ttf"

WIDTH = 1920
HEIGHT = 1080
FRAME_PER_SEC = 144

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

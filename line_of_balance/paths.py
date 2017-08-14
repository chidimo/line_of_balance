"""paths"""

import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_PATH)
os.chdir("output")
OUT_PATH = os.getcwd()

INPUT_PATH = os.path.abspath(os.path.join(BASE_PATH, "input.txt"))

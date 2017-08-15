"""paths"""

import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
root.withdraw()
NAME = fd.asksaveasfilename()
PDF = NAME + ".pdf"
PNG = NAME + ".png"

EXCEL_PATH = fd.asksaveasfilename() + ".xlsx"

INPUT_PATH = fd.askopenfilename()

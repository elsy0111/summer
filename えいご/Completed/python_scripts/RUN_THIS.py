import csv
import random

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Database")
root.geometry("1200x600")
root.configure(bg='black')
root.attributes('-fullscreen', True)  

csv_file = open("python_scripts/only_words_all(238-287)_nobr.csv", "r", encoding="UTF-8", errors="", newline="" )


#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

f = list(f)
random.shuffle(f)


def export_eng(row):
    cls_eng = ttk.Label(text="-----------------", font=('游明朝 Light', 300), foreground = "black",background= "black")
    cls_eng.place(relx = 0.5, y = 300, anchor = CENTER)
    eng = ttk.Label(text=row[0], font=('游明朝 Light', 75 ), foreground = "white",background= "black")
    eng.place(relx = 0.5, y = 400, anchor = CENTER)
    print(row[0])

def export_jp(row):
    cls_jp = ttk.Label(text="------------------", font=('游明朝 Light', 250), foreground = "black",background = "black")
    cls_jp.place(relx = 0.5, y = 700, anchor = CENTER)
    jp = ttk.Label(text=row[1], font=('游明朝 Light', 60 ), foreground = "white",background = "black")
    jp.place(relx = 0.5, y = 600, anchor = CENTER)

def loop():
    raw = f[random.randint(0, len(f))]
    root.after(10,export_eng(raw))
    root.after(10,export_jp(raw))
    root.after(1100,loop) #change speed
    root.mainloop()

root.after(100,loop)
root.mainloop()



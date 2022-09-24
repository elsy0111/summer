from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Database")
root.geometry("1200x600")
root.state("zoomed")
root.configure(bg='black')
root.attributes('-fullscreen', True)  


# ウィジェットの作成
eng = ttk.Label(text="Text", font=('游明朝 Light', 75 ), foreground = "white",background= "black")
jp = ttk.Label(text="文章", font=('游明朝 Light', 75 ), foreground = "white",background = "black")
eng.place(relx = 0.5, y = 300, anchor = CENTER)
jp.place(relx = 0.5, y = 500, anchor = CENTER)

# ウィンドウの表示開始
root.mainloop()
import tkinter as tk
import random

root = tk.Tk()
root.geometry("200x100")

def dispLabel():
    kuji = ['いつもありがとう','ゲームいっぱいしようね','就活大変だけど一緒に頑張ろうね','頑張りすぎに気を付けて','今日も頑張ろう','困ったらいつでも言って','気が利くところ見習いたい']
    lbl.configure(text=random.choice(kuji))

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH",command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()

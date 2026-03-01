'''
 * Project Name: python_game
 * NAME: 
 * Made by Jaejun
 * Date: 26. 3. 1.
 * Desc: 그냥 내 스타일대로
 객체 지향형으로 코딩
'''
import tkinter
from tkinter import Tk


class Example(Tk):
    FNT = ("Times New Roman", 60)
    COLOR = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

    @staticmethod
    def pkey(e, cvs):
        k = e.keysym
        if "1" <= k and k <= "7":
            c = int(k) - 1
            cvs.delete("all")
            cvs['bg'] = Example.COLOR[c]
            cvs.create_text(300, 150, text=Example.COLOR[c], fill="white", font=Example.FNT)

    def __init__(self):
        super().__init__()
        self.title("1 ~ 7 키를 눌러 보자")
        self.cvs = tkinter.Canvas(width=600, height=300)
        self.bind("<Key>", lambda e: Example.pkey(e, self.cvs))
        self.cvs.pack()


if __name__ == "__main__":
    Example().mainloop()

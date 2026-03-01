'''
 * Project Name: python_game
 * NAME: 
 * Made by Jaejun
 * Date: 26. 3. 1.
 * Desc: 
'''
import tkinter
from tkinter import Tk


class Ninja:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0


class Game:
    def __init__(self):
        self.scene = "타이틀"
        self.ninja = Ninja()

        self.list = tkinter.PhotoImage(file="./image/illust.png")  # 생성된 순서에 따라 영향을 받음 canvas
        self.bg = tkinter.PhotoImage(file="./image/bg.png")
        self.ninja_list = [
            tkinter.PhotoImage(file="./image/ninja0.png"),
            tkinter.PhotoImage(file="./image/ninja1.png"),
            tkinter.PhotoImage(file="./image/ninja2.png"),
            tkinter.PhotoImage(file="./image/ninja3.png")
        ]

    def get_ninja(self):
        return self.ninja

    def set_title(self):
        self.scene = "타이틀"

    def set_game(self):
        self.scene = "게임"

    def get_status(self):
        return self.scene

    def get_background(self) -> tkinter.PhotoImage:
        return self.bg

    def get_list_image(self) -> tkinter.PhotoImage:
        return self.list

    def get_ninja_image_list(self) -> list[tkinter.PhotoImage]:
        return self.ninja_list


class NinjaRun(Tk):
    Game = None

    @staticmethod
    def pkey(e, cvs):
        if e.keysym == "space":
            NinjaRun.Game.set_game()

        if e.keysym == "Return":
            NinjaRun.Game.set_title()

    def main(self):
        self.cvs.delete("all")
        self.cvs.create_image(480, 320, image=NinjaRun.Game.get_background())
        if NinjaRun.Game.get_status() == "타이틀":
            self.cvs.create_image(480, 320, image=NinjaRun.Game.get_list_image())
            self.cvs.create_text(480, 180, text="N i n j a r u n", font=("System", 100), fill="lime")
            self.cvs.create_text(480, 420, text="press [SPACE] key", font=("System", 40), fill="cyan")

        if NinjaRun.Game.get_status() == "게임":
            ninja = NinjaRun.Game.get_ninja()
            ninja.x = ninja.x + 40
            if ninja.x > 960: ninja.x = 0
            ninja.a = ninja.a + 1
            self.cvs.create_image(ninja.x, 400, image=NinjaRun.Game.get_ninja_image_list()[ninja.a % 4])

        self.after(100, self.main)

    def __init__(self):
        super().__init__()
        self.title("N i n j a r u n")
        self.cvs = tkinter.Canvas(width=960, height=640)
        self.bind("<Key>", lambda e: NinjaRun.pkey(e, self.cvs))
        NinjaRun.Game = Game()
        self.cvs.pack()


if __name__ == "__main__":
    game = NinjaRun()
    game.main()
    game.mainloop()

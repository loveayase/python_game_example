'''
 * Project Name: python_game
 * NAME: 
 * Made by Jaejun
 * Date: 26. 3. 1.
 * Desc: 
'''

import tkinter


def move(e):
    cvs.delete('all')
    cvs.create_oval(e.x - 25, e.y - 25, e.x + 25, e.y + 25, fill="blue", outline="cyan")


root = tkinter.Tk()
root.title("커서를 따라 다니는 도형")
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=800, height=400)
cvs.pack()
root.mainloop()

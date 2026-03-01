'''
 * Project Name: python_game
 * NAME: image
 * Made by Jaejun
 * Date: 26. 3. 1.
 * Desc: 
'''
import tkinter

n = 0


def count(root: tkinter.Tk, cvs: tkinter.Canvas):
    global n
    n = n + 1
    cvs.delete("all")
    cvs.create_text(200, 100, text=n, font=("System", 80))
    root.after(1000, count, root, cvs) # 매개변수를 전달하는 방식으로 변경



root = tkinter.Tk()
root.title("실시간 처리")
cvs = tkinter.Canvas(width=400, height=200)
cvs.pack()
count(root, cvs) # 매개변수를 전달하는 방식으로 변경
root.mainloop()

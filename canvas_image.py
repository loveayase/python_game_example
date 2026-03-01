'''
 * Project Name: python_game
 * NAME: image
 * Made by Jaejun
 * Date: 26. 3. 1.
 * Desc: 
'''

import tkinter

root = tkinter.Tk()
root.title("캔버스에 이미지를 표시해보자")
cvs = tkinter.Canvas(width=1080, height=720)
img = tkinter.PhotoImage(file="./image/chap3_illust.png")
cvs.create_image(540, 360, image=img)
cvs.pack()
root.mainloop()

'''
 * Project Name: python_game
 * NAME: 
 * Made by Jaejun
 * Date: 26. 3. 1.
 * Desc: 
'''
import tkinter

root = tkinter.Tk()
root.title("배열로 색을 정의해보자")
cvs = tkinter.Canvas(width=840, height=160)
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i, color in enumerate(rainbow):
    # 예제와 다르게 enumerate를 사용하여 처리
    X = i * 120
    cvs.create_rectangle(X, 0, X + 120, 160, fill=color, width=0)

cvs.pack()
root.mainloop()

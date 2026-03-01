'''
 * Project Name: python_game
 * NAME: 
 * Made by Jaejun
 * Date: 26. 3. 1.
 * Desc: 
'''

import tkinter

root = tkinter.Tk()
root.title("2차원 배열로 색을 정의해보자")
cvs = tkinter.Canvas(width=800, height=600, bg="black")

color = [
    ["brown", "#FF0000", "orange", "gold"], # Hex 코드를 사용하여 처리
    ["darkgreen", "green", "limegreen", "lime"],
    ["navy", "blue", "skyblue", "cyan"]
]

for y, row in enumerate(color):
    for x, color in enumerate(row):
        # 예제와 다르게 enumerate를 사용하여 처리
        X = x * 200
        Y = y * 200
        cvs.create_oval(X, Y, X + 200, Y + 200, fill=color)

cvs.pack()
root.mainloop()

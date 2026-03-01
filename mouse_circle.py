'''
 * Project Name: python_game
 * NAME: 
 * Made by Jaejun
 * Date: 26. 3. 1.
 * Desc: 전역 변수를 global을 이용해서 코딩하는것의 장점이 무엇인가?
 내가 너무 객체지향적으로 생각하는 것일까
'''
import math
import tkinter
from multiprocessing.sharedctypes import class_cache

mx = 400
my = 300


def move(e):
    global mx, my
    mx = e.x
    my = e.y


cx = 400
cy = 300
cr = 50
distance = [5, 5]


def calc_distance():
    # 좀더 자연스럽게 움직이도록 해보자
    global cx, cy, distance

    x = abs(mx - cx)
    y = abs(my - cy)
    dis = math.sqrt(x * x + y * y)
    if dis == 0:
        dis = 1

    distance[0] = (y / dis) * 5
    distance[1] = (x / dis) * 5

    if cy > my: cy -= distance[0]
    if cy < my: cy += distance[0]
    if cx > mx: cx -= distance[1]
    if cx < mx: cx += distance[1]


def main():
    global cx, cy
    calc_distance()
    cvs.delete('all')
    cvs.create_oval(cx - cr, cy - cr, cx + cr, cy + cr, fill="blue", outline="cyan")

    root.after(50, main)


root = tkinter.Tk()
root.title("커서를 따라오는 도형")
root.resizable(False, False)
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=800, height=600, bg="black")
cvs.pack()
main()
root.mainloop()

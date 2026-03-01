'''
 * Project Name: python_game
 * NAME: 
 * Made by Jaejun
 * Date: 26. 3. 1.
 * Desc: 
'''

import tkinter
from tkinter import Tk
import math


class Example(Tk):
    DISTANCE = 10
    RECT_LIST = [
        {
            'x': 200,
            'y': 200,
            'w': 80,
            'h': 120,
        },
        {
            'x': 400,
            'y': 300,
            'w': 240,
            'h': 120,
        }
    ]

    @staticmethod
    def move(e, cvs):
        Example.RECT_LIST[0]['x'] = e.x
        Example.RECT_LIST[0]['y'] = e.y
        col = "red"
        if abs(Example.RECT_LIST[0]['x'] - Example.RECT_LIST[1]['x']) <= (
                Example.RECT_LIST[0]['w'] + Example.RECT_LIST[1]['w']) / 2 and abs(
            Example.RECT_LIST[0]['y'] - Example.RECT_LIST[1]['y']) <= (
                Example.RECT_LIST[0]['h'] + Example.RECT_LIST[1]['h']) / 2:
            col = 'pink'

        cvs.delete("RED_RECT")
        cvs.create_rectangle(Example.RECT_LIST[0]['x'] - Example.RECT_LIST[0]['w'] / 2,
                             Example.RECT_LIST[0]['y'] - Example.RECT_LIST[0]['h'] / 2,
                             Example.RECT_LIST[0]['x'] + Example.RECT_LIST[0]['w'] / 2,
                             Example.RECT_LIST[0]['y'] + Example.RECT_LIST[0]['h'] / 2,
                             fill=col, outline="white", tag="RED_RECT")

    def __init__(self):
        super().__init__()
        self.title("사각형을 사용한 충돌 판정")
        self.cvs = tkinter.Canvas(width=800, height=600, background="black")
        self.bind("<Motion>", lambda e: Example.move(e, self.cvs))
        self.cvs.pack()
        self.cvs.create_rectangle(Example.RECT_LIST[0]['x'] - Example.RECT_LIST[0]['w'] / 2,
                                  Example.RECT_LIST[0]['y'] - Example.RECT_LIST[0]['h'] / 2,
                                  Example.RECT_LIST[0]['x'] + Example.RECT_LIST[0]['w'] / 2,
                                  Example.RECT_LIST[0]['y'] + Example.RECT_LIST[0]['h'] / 2,
                                  fill="red", outline="white", tag="RED_RECT")

        self.cvs.create_rectangle(Example.RECT_LIST[1]['x'] - Example.RECT_LIST[1]['w'] / 2,
                                  Example.RECT_LIST[1]['y'] - Example.RECT_LIST[1]['h'] / 2,
                                  Example.RECT_LIST[1]['x'] + Example.RECT_LIST[1]['w'] / 2,
                                  Example.RECT_LIST[1]['y'] + Example.RECT_LIST[1]['h'] / 2,
                                  fill="blue", outline="white")


if __name__ == "__main__":
    Example().mainloop()

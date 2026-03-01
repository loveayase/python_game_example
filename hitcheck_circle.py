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
    CIRCLE_LIST = [
        {
            'x': 200,
            'y': 200,
            'd': 60,
        },
        {
            'x': 500,
            'y': 300,
            'd': 120,
        }
    ]

    @staticmethod
    def pkey(e, cvs):
        if e.keysym == "Up": Example.CIRCLE_LIST[0]['y'] -= Example.DISTANCE
        if e.keysym == "Down": Example.CIRCLE_LIST[0]['y'] += Example.DISTANCE
        if e.keysym == "Left": Example.CIRCLE_LIST[0]['x'] -= Example.DISTANCE
        if e.keysym == "Right": Example.CIRCLE_LIST[0]['x'] += Example.DISTANCE

        d = math.sqrt((Example.CIRCLE_LIST[0]['x'] - Example.CIRCLE_LIST[1]['x']) * (
                Example.CIRCLE_LIST[0]['x'] - Example.CIRCLE_LIST[1]['x']) + (
                              Example.CIRCLE_LIST[0]['y'] - Example.CIRCLE_LIST[1]['y']) * (
                              Example.CIRCLE_LIST[0]['y'] - Example.CIRCLE_LIST[1]['y']))
        col = "red"
        if d <= Example.CIRCLE_LIST[0]['d'] + Example.CIRCLE_LIST[1]['d']: col = "pink"
        cvs.delete("RED_CIRCLE")
        cvs.create_oval(
            Example.CIRCLE_LIST[0]['x'] - Example.CIRCLE_LIST[0]['d'],
            Example.CIRCLE_LIST[0]['y'] - Example.CIRCLE_LIST[0]['d'],
            Example.CIRCLE_LIST[0]['x'] + Example.CIRCLE_LIST[0]['d'],
            Example.CIRCLE_LIST[0]['y'] + Example.CIRCLE_LIST[0]['d'],
            fill=col, outline="white", tag="RED_CIRCLE"
        )

    def __init__(self):
        super().__init__()
        self.title("원을 사용한 충돌 판정")
        self.cvs = tkinter.Canvas(width=800, height=600, background="black")
        self.bind("<Key>", lambda e: Example.pkey(e, self.cvs))
        self.cvs.pack()
        self.cvs.create_oval(
            Example.CIRCLE_LIST[0]['x'] - Example.CIRCLE_LIST[0]['d'],
            Example.CIRCLE_LIST[0]['y'] - Example.CIRCLE_LIST[0]['d'],
            Example.CIRCLE_LIST[0]['x'] + Example.CIRCLE_LIST[0]['d'],
            Example.CIRCLE_LIST[0]['y'] + Example.CIRCLE_LIST[0]['d'],
            fill="red", outline="white", tag="RED_CIRCLE"
        )

        self.cvs.create_oval(
            Example.CIRCLE_LIST[1]['x'] - Example.CIRCLE_LIST[1]['d'],
            Example.CIRCLE_LIST[1]['y'] - Example.CIRCLE_LIST[1]['d'],
            Example.CIRCLE_LIST[1]['x'] + Example.CIRCLE_LIST[1]['d'],
            Example.CIRCLE_LIST[1]['y'] + Example.CIRCLE_LIST[1]['d'],
            fill="blue", outline="white")


if __name__ == "__main__":
    Example().mainloop()

from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr. Stick Man Races for the Exit")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=600, height=600,highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 600
        self.canvas_width = 600
        self.bg = PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\pink_background.gif")
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0,6):
            for y in range(0, 6):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True
    def mainloop(self):
        while 1:
            time.sleep(0.05)
            letter=PhotoImage(file="letter.gif")
            bck=PhotoImage(file="black.gif")
            crush1=PhotoImage(file="crush1.gif")
            crush2 = PhotoImage(file="crush2.gif")
            ball = PhotoImage(file="ball.gif")
            a=self.canvas.create_image(100,100,image=letter,anchor='nw')
            self.tk.update_idletasks()
            time.sleep(2)
            self.canvas.itemconfig(a, state='hidden')
            b=self.canvas.create_image(0,0,image=bck,anchor='nw')
            c=self.canvas.create_image(100,100,image=crush1,anchor='nw')
            self.tk.update_idletasks()
            time.sleep(0.20)
            self.canvas.itemconfig(c, state='hidden')
            d=self.canvas.create_image(150,150,image=crush2,anchor='nw')
            self.tk.update_idletasks()
            time.sleep(0.20)
            self.canvas.itemconfig(d, state='hidden')
            e=self.canvas.create_image(200,200,image=ball,anchor='nw')
            self.tk.update_idletasks()
            time.sleep(0.20)
            self.canvas.itemconfig(e, state='hidden')
            self.tk.update_idletasks()
            time.sleep(180)

g=Game()
g.mainloop()

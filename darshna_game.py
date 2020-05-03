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
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            else:
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
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)
            
class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
def within_x(co1, co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
        return True
    else:
        return False
    
def within_y(co1, co2):
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y2):
        return True
    else:
        return False
    
def collided_left(co1, co2):
    if within_y(co1, co2):
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False

def collided_right(co1, co2):
    if within_y(co1, co2):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False
def collided_top(co1, co2):
    if within_x(co1, co2):
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
            return True
    return False
def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if y_calc >= co2.y1 and y_calc <= co2.y2:
            return True
    return False

class Sprite:
    def __init__(self, game):
        self.game = game 
        self.endgame = False
        self.coordinates = None
    def move(self):
        pass
    def coords(self):
        return self.coordinates


class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, \
                                              image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + width, y + height)

        
class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
        self.images_left = [PhotoImage(file="runman_b1.gif"),PhotoImage(file="runman_b2.gif"),PhotoImage(file="runman_b3.gif")]
        self.images_right = [PhotoImage(file="runman_f1.gif"),PhotoImage(file="runman_f2.gif"),PhotoImage(file="runman_f3.gif")]
        self.image = game.canvas.create_image(600, 570,image=self.images_left[0], anchor='nw')
        self.x = -2
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)
    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2
    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2
    def jump(self, evt):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0
    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1
        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image,image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image,image=self.images_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image,image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(self.image,image=self.images_right[self.current_image])
    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates
    def move(self):
        self.animate()
        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4
        if self.y > 0:
            self.jump_count -= 1
        co = self.coords()
        left = True
        right = True
        top = True
        bottom = True
        falling = True
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False
        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if top and self.y < 0 and collided_top(co, sprite_co):
                self.y = -self.y
                top = False
            if bottom and self.y > 0 and collided_bottom(self.y,co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                    bottom = False
                    top = False
            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and collided_bottom(1, co, sprite_co):
                falling = False
            if left and self.x < 0 and collided_left(co, sprite_co):
                self.x = 0
                left = False
                if sprite.endgame:
                    self.end(sprite)
            if right and self.x > 0 and collided_right(co, sprite_co):
                self.x = 0
                right = False
                if sprite.endgame:
                    self.end(sprite)

        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            self.y = 4
        self.game.canvas.move(self.image, self.x, self.y)
    def end(self, sprite):
        self.game.running = False
        sprite.opendoor()
        time.sleep(1)
        self.game.canvas.itemconfig(self.image, state='hidden')
        sprite.closedoor()

class DoorSprite(Sprite):
    def __init__(self, game, x, y, width, height):
        Sprite.__init__(self, game)
        self.closed_door = PhotoImage(file="door_close.gif")
        self.open_door=PhotoImage(file="door_open.gif")
        self.image = game.canvas.create_image(x, y,image=self.closed_door, anchor='nw')
        self.coordinates = Coords(x, y, x + (width / 2), y + height)
        self.endgame = True
    def opendoor(self):
        self.game.canvas.itemconfig(self.image, image=self.open_door)
        self.game.tk.update_idletasks()
    def closedoor(self):
        self.game.canvas.itemconfig(self.image,image=self.closed_door)
        self.game.tk.update_idletasks()
    

g=Game()
platform1 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar1.gif"), 0, 580, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar2.gif"),147, 540, 66, 10)
platform3 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar2.gif"),247, 500, 66, 10)
platform4 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar2.gif"),165, 450, 66, 10)
platform5 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\lvl2.gif"),47, 400, 100, 10)
platform6 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar3.gif"),170, 350, 32, 10)
platform7 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar2.gif"),215, 350, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar3.gif"),290, 300, 32, 10)
platform9 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar3.gif"),335, 270, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar3.gif"),375, 240, 32, 10)
platform11 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\lvl3.gif"),415, 210, 100, 10)
platform12 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar2.gif"),330, 180, 66, 10)
platform13= PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar3.gif"),285, 155, 32, 10)
platform14 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\lvl4.gif"),170,130, 100, 10)
platform15 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar2.gif"),95, 100, 32, 10)
platform16 = PlatformSprite(g, PhotoImage(file="C:\\Users\\ROSE THOMAS\\Desktop\\python_class\\stickman\\bar2.gif"),20, 60, 66, 10)

g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)
g.sprites.append(platform11)
g.sprites.append(platform12)
g.sprites.append(platform13)
g.sprites.append(platform14)
g.sprites.append(platform15)
g.sprites.append(platform16)
door =DoorSprite(g,55,370,40,35)
door1=DoorSprite(g,180,100,40,35)
door2=DoorSprite(g,420,180,40,35)
g.sprites.append(door)
sf = StickFigureSprite(g)
g.sprites.append(sf)
g.mainloop()




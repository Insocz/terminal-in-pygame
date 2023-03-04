import pygame
from text import Text
from surface import Surface
from keys import key,fun_key

pygame.init()

class App:
    def __init__(self) -> None:
        #screen setup
        if True:
            self.screen = pygame.display.set_mode((800,800))
            pygame.display.set_caption("App")

            icon = pygame.image.load("game_icon.svg")
            pygame.display.set_icon(icon)

            self.clock = pygame.time.Clock()

        #var
        if True:
            self.num = 0
            self.backnum = 0

            self.last_key = None

            self.write_list = [" ",""]

            self.write = ""

            self.x = 15
            self.y = 5

            #dirs for combinatet characters
            if True:
                self.fun_list = [
                    "backspace",
                    "escape",
                    "shift",
                    "left ctrl",
                    "right ctrl",
                    "left alt",
                    "right alt",
                    "caps lock",
                    "pause",
                    "home",
                ]

                self.shift_list = {
                    ";": "˚",
                    "=":"%",
                    "ú":"/",
                    ")":"(",
                    "ů":'"',
                    "§":"!",
                    ",":"?",
                    ".":":",
                    "-":"_",
                    "\\":"|",
                }

                self.alphabet = [
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "o",
                    "p",
                    "q",
                    "r",
                    "s",
                    "t",
                    "u",
                    "v",
                    "w",
                    "x",
                    "y",
                    "z"
                ]

        self.gruop = pygame.sprite.Group()

        self.path_line = Text("/home $ ",self.gruop,(self.x,self.y))

        self.com_line = Text(self.write,self.gruop,(self.x + self.path_line.image.get_width(),self.y))

        self.loop()

    def loop(self):
        while True:
            #looking for X to quit
            if True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

            self.write_def()
            self.key_def()

            self.screen.fill((25,25,25))
            self.gruop.update()
            pygame.display.update()
            self.clock.tick(60)

    def key_def(self):

        self.key = key()
        self.fun_key = fun_key()

        #write lovercase
        if (self.key != None and self.key != self.last_key) and not(self.fun_key in self.fun_list):
                self.write_list.insert(-2,str(self.key))

        #fun keys
        if self.fun_key != None:
            #shift
            if self.fun_key == "shift" and (self.key != None and self.key != self.last_key):
                if self.key in self.alphabet:
                    self.write_list.insert(-2,str(self.key.capitalize()))

            #backspace
            if self.fun_key == "backspace":
                if len(self.write_list) >= 3 and self.backnum == 5:
                    self.write_list.pop(-2)
                if self.backnum == 5:
                    self.backnum = 0
                if self.last_fun_key != "backspace":
                    self.backnum = 0

                self.backnum += 1
            
            #enter
            elif self.fun_key == "enter" and self.fun_key != self.last_fun_key:
                Text("/home $ ",self.gruop,(self.x,self.y))
                Text(self.write.replace("|"," ",-2),self.gruop,(self.x + self.path_line.image.get_width(),self.y))

                self.y += 25
                self.path_line.rect.centery += 25
                self.com_line.rect.centery += 25
                
                self.write_list = [" ",""]

        self.last_key = self.key
        self.last_fun_key = self.fun_key

    def write_def(self):
            if self.write_list[-2] == " " and self.num == 20:
                self.write_list[-2] = "|"
                self.num = 0
            elif self.num == 20:
                self.write_list[-2] = " "
                self.num = 0

            self.num += 1

            self.write = ""
            self.write = self.write.join(self.write_list[0:-1])

            self.com_line.write = self.write

App()
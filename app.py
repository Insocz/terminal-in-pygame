import pygame, pathlib, os
from text import Text

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

        self.gruop = pygame.sprite.Group()

        self.path_line = Text("/home $ ",self.gruop,(self.x,self.y))

        self.com_line = Text(self.write,self.gruop,(self.x + self.path_line.image.get_width(),self.y))

        self.loop()

    def loop(self):
        while True:

            self.key = None

            #looking for X to quit
            if True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.unicode.isprintable():
                            self.key = event.unicode
                        else:
                            self.key = pygame.key.name(event.key)

            self.write_def()
            self.key_def()

            self.screen.fill((25,25,25))
            self.gruop.update()
            pygame.display.update()
            self.clock.tick(60)

    def key_def(self):

        self.back = pygame.key.get_pressed()

        #backspace
        if self.back[pygame.K_BACKSPACE]:
            if len(self.write_list) >= 3 and self.backnum == 5:
                self.write_list.pop(-2)
            if self.backnum == 5 or not(self.last_key):
                self.backnum = 0

            self.backnum += 1

        #write lovercase
        if self.key != None:
            #enter
            if self.key == "return":
                Text("/home $ ",self.gruop,(self.x,self.y))
                Text(self.write.replace("|"," ",-2),self.gruop,(self.x + self.path_line.image.get_width(),self.y))

                self.y += 25
                self.path_line.rect.centery += 25
                self.com_line.rect.centery += 25
                
                self.write_list = [" ",""]

            #tab
            elif self.key == "tab":
                self.write_list.insert(-2,"    ")                

            elif self.key != "backspace":
                self.write_list.insert(-2,str(self.key))

        self.last_key = self.back[pygame.K_BACKSPACE]

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
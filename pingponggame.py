from pygame import *
from random import randint

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

back = (200, 255, 255)
window.fill(back)

#Superclass
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height, color):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.seed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    pass

white = (255, 255, 255)
pad_1 = Player()
pad_2 = Player()
ball = GameSprite()

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
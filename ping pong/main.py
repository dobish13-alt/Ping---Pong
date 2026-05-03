from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_h - 148:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_h - 148:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        pass

win_w = 700
win_h = 500

window = display.set_mode((win_w, win_h))

display.set_caption("Ping Pong")

background = transform.scale(image.load("unnamed.png"), (win_w, win_h))

player_left = Player("rocket.png", 5, 10, 36, 143, 10)
player_right = Player("rocket.png", win_w - 41, win_h - 153, 36, 143, 10)

clock = time.Clock()
FPS = 60
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:
        player_left.update_left()
        player_right.update_right()

        window.blit(background, (0, 0))
        player_left.reset()
        player_right.reset()

            
    display.update()
    clock.tick(FPS)
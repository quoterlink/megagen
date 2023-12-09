import pygame
from random import randint

pygame.init()

back = (131, 30, 10)
mw = pygame.display.set_mode((700,700))

clock = pygame.time.Clock()


racket_x = 200
racket_y = 330

game_over = False

dx = 3
dy = 3
game = True
finish = False

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 600:
            self.rect.y += self.speed



class Player2(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed


neu = Player("r2.png", 12, 600, 4, 40,100)
wri = Player2("r.png", 650, 600, 4, 40,100)
tar = GameSprite("ten.png", 350, 350, 25, 50, 50)

pygame.font.init()
font = pygame.font.Font(None, 35)
l1 = font.render('ПЕРВЫЙ ИГРОК НЕ ХАРОШ', True, (0,0,0))
l2 = font.render('ВТОРОЙ ИГРОК НЕ ХАРОШ', True, (0,0,0))


while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    mw.fill(back)
    tar.rect.x += dx
    tar.rect.y += dy
    if tar.rect.y > 675 or tar.rect.y < 25:
        dy *= -1
    if pygame.sprite.collide_rect(neu, tar) or pygame.sprite.collide_rect(wri, tar):
        dx *= -1
    if tar.rect.x < 0:
        finish = True
        mw.blit(l1, (200, 350))
        game_over = True

    if tar.rect.x > 700:
        finish = True
        mw.blit(l2, (200, 350))
        game_over = True

    neu.reset()
    wri.reset()
    neu.update()
    wri.update()
    tar.reset()
    tar.update()

    pygame.display.update()
    clock.tick(60)
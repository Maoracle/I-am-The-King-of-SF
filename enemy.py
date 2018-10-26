#敌方英雄
import pygame
from random import*

class Axe(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/axe.png").convert_alpha()
        #斧王死亡画面
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/axe_down1.png").convert_alpha(),\
            pygame.image.load("images/axe_down2.png").convert_alpha(), \
            pygame.image.load("images/axe_down3.png").convert_alpha(), \
            pygame.image.load("images/axe_down4.png").convert_alpha() \
            ])
            
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)
        self.speed = 2
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)
        
class Tide(pygame.sprite.Sprite):
    energy = 6
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/tide.png").convert_alpha()
        self.image_hit = pygame.image.load("images/tide_hit.png").convert_alpha()
        #潮汐死亡画面
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/tide_down1.png").convert_alpha(),\
            pygame.image.load("images/tide_down2.png").convert_alpha(), \
            pygame.image.load("images/tide_down3.png").convert_alpha(), \
            pygame.image.load("images/tide_down4.png").convert_alpha() \
            ])
            
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-10 * self.height, 0)
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = Tide.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = Tide.energy
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-10 * self.height, 0)
              

class Roshan(pygame.sprite.Sprite):
    energy = 15
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/roshan.png").convert_alpha()
        self.image_hit = pygame.image.load("images/roshan_hit.png").convert_alpha()
        #Roshan死亡画面
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/roshan_down1.png").convert_alpha(),\
            pygame.image.load("images/roshan_down2.png").convert_alpha(), \
            pygame.image.load("images/roshan_down3.png").convert_alpha(), \
            pygame.image.load("images/roshan_down4.png").convert_alpha(), \
            pygame.image.load("images/roshan_down5.png").convert_alpha() \
            ])
            
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-15 * self.height, -5 * self.height)
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = Roshan.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = Roshan.energy
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-15 * self.height, -5 * self.height)          

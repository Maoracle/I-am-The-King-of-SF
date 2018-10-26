#玩家控制的影魔
import pygame

class ShadowFriend(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        #影魔图片
        self.image1 = pygame.image.load("images/sf1.png").convert_alpha()
        self.image2 = pygame.image.load("images/sf2.png").convert_alpha()
        #影魔死亡图片
        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.image.load("images/me_destroy_1.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_2.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_3.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_4.png").convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width)//2, \
                        self.height - self.rect.height - 45
        self.speed = 10
        self.active = True
        #影魔无敌属性
        self.invincible_image = pygame.image.load("images/sf0.png").convert_alpha()
        self.invincible = False
        #给图片添加mask属性从而更好地进行碰撞检测
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0
            
    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True

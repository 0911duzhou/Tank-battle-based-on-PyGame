import pygame

"""
作者:嘟粥
修改时间:2022.12.02
模块描述：
该模块是子弹类
子弹类继承了pygame的精灵类，进而实现子弹的相关功能
"""


# 子弹类（继承精灵类）
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 将子弹”上下左右“的图片进行加载
        self.bullet_up = pygame.image.load(r".\image\bullet_up.png")
        self.bullet_down = pygame.image.load(r".\image\bullet_down.png")
        self.bullet_left = pygame.image.load(r".\image\bullet_left.png")
        self.bullet_right = pygame.image.load(r".\image\bullet_right.png")

        self.dir_x, self.dir_y = 0, 0  # 子弹方向
        self.speed = 6  # 速度
        self.life = False  # 生命
        self.strong = False  # 碎石

        self.bullet = self.bullet_up
        self.rect = self.bullet.get_rect()
        self.rect.left, self.rect.right = 3 + 12 * 24, 3 + 24 * 24
        self.times = 90

    # 改变图片方法 根据给的方向改变相应的图片
    def changeImage(self, dir_x, dir_y):
        self.dir_x, self.dir_y = dir_x, dir_y

        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet = self.bullet_up
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet = self.bullet_down
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet = self.bullet_left
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet = self.bullet_right

    # 子弹移动方法 根据子弹的方向进行移动，当检测到在边缘则将其生命消失
    def move(self):
        self.rect = self.rect.move(self.speed * self.dir_x,
                                   self.speed * self.dir_y)
        # 碰撞地图边缘  将子弹消失
        if self.rect.top < 3:
            self.life = False
        if self.rect.bottom > 630 - 3:
            self.life = False
        if self.rect.left < 3:
            self.life = False
        if self.rect.right > 630 - 3:
            self.life = False

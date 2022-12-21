import pygame
from PIL import Image, ImageSequence


class GameGifSprite(pygame.sprite.Sprite):
    """
    小鸟游戏精灵
    """

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 使用pillow的image打开GIF动图
        pillow_image = Image.open(image_name)
        index = 1
        # 使用pillow的ImageSequence获取GIF动图所有帧对应的迭代器
        for frame in ImageSequence.all_frames(pillow_image):
            # 以png格式保存在./images/bird/文件夹下面，文件名以gif1、gif2......等为后缀名
            frame.save(f"./init/gif{index}.png", quality=100)
            index = index + 1


g = GameGifSprite('th1.gif')

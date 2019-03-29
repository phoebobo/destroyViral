import pygame
import random
from pygame.locals import *
from random import randrange
from airplane import Airplane
from bullet import Bullet
#颜色
white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0,0,255)

if __name__ == '__main__':
    pygame.init()  #初始化
    pygame.mixer.init()

    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption('消灭病毒')
    # window_image = pygame.image.load('')
    # pygame.display.set_icon(window_image)
    #帧率设置
    clock = pygame.time.Clock()
    # 左上角计算分数
    # countObj = pygame.font.SysFont('方正兰亭超细黑简体',30)
    countObj = pygame.font.Font(None, 50)
    # countObj.set_bold(True)  #加粗
    textObj = countObj.render('SCORE:0', True, (255, 0, 0))
    textRectObj = textObj.get_rect()
    screen.blit(textObj,textRectObj)
    # 这个是计算分数
    count_num = 0
    #创建飞机
    airplane = Airplane(screen)
    #子弹容器
    bullet_sprites = pygame.sprite.RenderUpdates()  # 创建sprite容器  树
    AddEnemy = pygame.USEREVENT + 1  #添加子弹的时间
    pygame.time.set_timer(AddEnemy, 1000)

    pygame.display.flip()
    while True:
        clock.tick(60)
        screen.fill((48,144,144))  #背景色
        screen.blit(airplane.image,airplane.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == AddEnemy:
                bullet_sprites.add(Bullet(screen, airplane))
        # 获取键盘状态
        pressed_keys = pygame.key.get_pressed()
        #调用方法更新
        airplane.update(pressed_keys)
        #场景动画更新
        bullet_sprites.update()
        bullet_updates = bullet_sprites.draw(screen)
        pygame.display.update(bullet_updates)

        #子弹和病毒组的碰撞
        hit_list = pygame.sprite.groupcollide(bullet_sprites, viral_sprites, True, False)
        if hit_list:
            bullet_sprites[0].kill()
        # 得分多少
        textObj = countObj.render('SCORE:%d' % count_num, False, (255, 0, 0))  # 显示得分内容
        textRectObj = textObj.get_rect()
        screen.blit(textObj, textRectObj)  # 这是得分
        pygame.display.flip()
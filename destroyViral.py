import pygame
import random
from pygame.locals import *
from random import randrange
from airplane import Airplane
from bullet import Bullet

def loadgameover(scorenum):#绘出GAME OVER

  my_font=pygame.font.SysFont(None,50)
  levelstr='GAME OVER'
  over_screen=my_font.render(levelstr, True, (255, 0, 0))
  screen.blit(over_screen, (300,240))
  highscorestr='YOUR SCORE IS '+str(scorenum)
  over_screen=my_font.render(highscorestr, True, (255, 0, 0))
  screen.blit(over_screen, (280,290))

  # if scorenum>int(highscore):#写入最高分
  #   highscorestr='YOUR HAVE GOT THE HIGHEST SCORE!'
  #   text_screen=my_font.render(highscorestr, True, (255, 0, 0))
  #   screen.blit(text_screen, (100,340))
  #   highfile=open('highscore','w')
  #   highfile.writelines(str(scorenum))
  #   highfile.close()

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
    #画圆
    pygame.draw.rect(screen, [255, 0, 0], [250, 150, 300, 200], 0)
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
            elif event.type == pygame.K_BACKSPACE:
                loadgameover(count_num)
        # 获取键盘状态
        pressed_keys = pygame.key.get_pressed()
        #调用方法更新
        airplane.update(pressed_keys)
        #场景动画更新
        bullet_sprites.update()
        bullet_updates = bullet_sprites.draw(screen)
        pygame.display.update(bullet_updates)

        #子弹和病毒组的碰撞
        # hit_list = pygame.sprite.groupcollide(bullet_sprites, viral_sprites, True, False)
        # if hit_list:
        #     bullet_sprites[0].kill()
        #     count_num += bullet_sprites[0].damage
        # 得分多少
        textObj = countObj.render('SCORE:%d' % count_num, False, (255, 0, 0))  # 显示得分内容
        textRectObj = textObj.get_rect()
        screen.blit(textObj, textRectObj)  # 这是得分
        pygame.display.flip()
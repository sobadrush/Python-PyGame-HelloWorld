import sys
import pygame

from pygame.locals import QUIT

pygame.init() # 初始化 Pygame

screen_surface = pygame.display.set_mode((640, 480)) # 設定視窗大小
pygame.display.set_caption('Pygame HelloWorld') # 設定視窗標題
screen_surface.fill((200, 200, 200)) # 設定背景顏色

headFont = pygame.font.SysFont('arial', 64) # 設定字型和大小
headFont.set_bold(True) # 設定為粗體
text_surface = headFont.render('Hello World!', True , (0, 0, 255)) # 設定【文字內容】、【是否反鋸齒】、【顏色】

# blit: 用於將一個 Surface 對象（通常是圖像）繪製到另一個 Surface 對象上
screen_surface.blit(text_surface, (300, 300)) # source 要繪製的圖像、dest 繪製的位置 

# pygame.display.flip() # 更新整個畫面，無論是否有變化
pygame.display.update() # 部分畫面需要更新，這將更有效率。如果沒有提供任何參數，pygame.display.update() 將行為與 pygame.display.flip() 相同，更新整個畫面

# 進入遊戲迴圈
while True:
    for event in pygame.event.get(): # 取得所有事件
        if event.type == QUIT: # 如果事件是按下視窗的關閉按鈕
            pygame.quit() # 關閉 Pygame
            sys.exit() # 關閉程式
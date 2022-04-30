import sys
import pygame

#画像の読み込み

PLAYER_WIDTH = 44


#main 関数
def main():

    #ウィンドウを作成
    pygame.init()
    pygame.display.set_caption('トライアルゲーム')
    surface = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()

    #無限ループ
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        surface.fill((184,228,240), (0,0,800,520))
        surface.fill((142,128,106), (0,520,800,80))
                
        pygame.display.update()
        clock.tick(10)
                


main()
                

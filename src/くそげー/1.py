# coding: utf-8
import pygame
from pygame.locals import *
import sys



SCREEN_SIZE = (640, 480)  # 画面サイズ

# pygameを初期化
pygame.init()
# screen_sizeの画面を作成
screen = pygame.display.set_mode(SCREEN_SIZE)
# タイトルバーの文字列をセット
pygame.display.set_caption("ウィンドウの作成")

# ゲームループ
while True:
    screen.fill((0, 0, 255))
    pygame.display.update()
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

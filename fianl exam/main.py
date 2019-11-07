import cv2
import numpy as np
import pygame
from color_manip import *
from bar import *
from utils import *



cap = cv2.VideoCapture(0)

pygame.init()
pygame.display.set_caption(u"clown")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Clown:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.wear = False

    def update(self, now, faces):
        if not now:
            return
        nx, ny = now
        x = self.x
        y = self.y

        if x <= nx and nx <= x+200 and y <= ny and ny <= y+200:
            self.wear = True

        if self.wear:
            for fx, fy, fw, fh in faces:
                self.x = fx + 65
                self.y = fy - 100
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# t = TrackBar('1', 'b')

a = Clown(10, 10, pygame.transform.scale(pygame.image.load("1.png"), (200, 200)))
b = Clown(300, 10, pygame.transform.scale(pygame.image.load("2.png"), (200, 200)))
c = Clown(590, 10, pygame.transform.scale(pygame.image.load("3.png"), (200, 200)))

hat = [a, b, c]

GAME_PLAY = 1
GAME_WIN = 2

gm = GAME_PLAY

running = True
while running:
    for event in pygame.event.get():
        # 離開遊戲.
        if event.type == pygame.QUIT:
            running = False
    # update
    ## opencv
    ret, frame = cap.read()
    frame = flip(frame, 1)
    ## color detect
    _, mask, _ = color_detect(frame, (0, 0, 255), 50)
    cent = get_color_pos(mask)
    cv2.imshow('1', mask)
    # cv2.imshow('2', inv)
    ## face detect
    faces = face_detect(frame)

    ## game logic
    for i in hat:
        i.update(cent, faces)

    # win
    wear_cnt = 0
    for i in hat:
        if i.wear:
            wear_cnt += 1

    if wear_cnt == 3:
        gm = GAME_WIN

    # draw
    back = cvimage_to_pygame(frame)
    back = pg_resize(back, 800, 600)
    screen.blit(back, (0,0))

    for i in hat:
        i.draw()

    if gm == GAME_WIN:
        showFont(screen, "You Win", 300, 250, 'simhei', 50, (255, 0, 0))

    pygame.display.update()
    clock.tick(60)

cap.release()
cv2.destroyAllWindows()
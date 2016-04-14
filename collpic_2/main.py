#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Authors: Nosov Mikhail, viver_117, Konstantin Guk
# Consultant: grishnan
# E-mails: mikhail1920@mail.com, viver12366@gmail.com, 1996artes@mail.ru, grishnan@gmail.com
# License: GNU GPL v3.0
# Description by Eng: Program «Collection picture»
# Description by Rus: Программа «Собери картинку»

from classes import *

pygame.init()

screen = pygame.display.set_mode((SIZE_SCREEN, SIZE_SCREEN))
pygame.display.set_caption("Collection picture")

field = Field()

while True:
  gotoGame = False
  
  ''' обработчик событий '''
  for event in pygame.event.get():
    if event.type == pygame.QUIT: pygame.quit(); sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      gotoGame = True
      
  if gotoGame: break
  
  screen.fill(WHITE)
  field.drawField(screen)
  field.assignment(screen)
  (gx, gy) = field.fromLocalToGlobal(SIZE_FIELD - 1, SIZE_FIELD - 1)
  screen.blit(field.pics[-1], (gx, gy, SIZE_CHIP, SIZE_CHIP))

  pygame.display.update()

field.randomMix()

while True:
  
  ''' обработчик событий '''
  for event in pygame.event.get():
    if event.type == pygame.QUIT: pygame.quit(); sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mousex, mousey = event.pos
      field.makeMove(mousex, mousey)
      print(field.matrix)
  
  ''' отрисовка игрового поля '''
  screen.fill(WHITE)
  field.drawField(screen)
  field.assignment(screen)

  pygame.display.update()

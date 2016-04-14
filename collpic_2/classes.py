import pygame, sys, os, random, pygame.gfxdraw
from consts import *

class Field():
  def __init__(self):
    self.matrix = [] # список для хранения структуры игрового поля
    ''' Инициализация главной структуры данных '''
    for i in range(0, SIZE_FIELD):
      self.matrix.append([])
      for j in range(0, SIZE_FIELD):
        self.matrix[i].append(j+SIZE_FIELD*i)
    self.matrix[-1][-1] = None
    
    self.initmatrix = self.matrix                      # копия начальной структуры игрового поля
    self.pics       = []                               # хранилище картинок
    self.indexNone  = (SIZE_FIELD - 1, SIZE_FIELD - 1) # индекс пустой клетки
    self.level      = ["1", "2", "3", "4"]
	
    ''' заполнение хранилища картинок '''
    random.shuffle(self.level)
    if (SIZE_FIELD == 3): self.address = os.path.join("pics", "300x300")
    if (SIZE_FIELD == 4): self.address = os.path.join("pics", "400x400")
    if (SIZE_FIELD == 5): self.address = os.path.join("pics", "500x500", self.level)
	
	
    for i in range(0, SIZE_FIELD**2):
      self.pics.append(pygame.image.load(os.path.join(self.address, str(i) + ".jpg"))) # Заполнение полей в поле
    
  def fromGlobalToLocal(self, gx, gy): # Перевод из глобальной в локальную
    lx = int((gx - MARGIN_FIELD - WIDTH_BORDER)/(SIZE_CHIP + GAP_CHIP))
    ly = int((gy - MARGIN_FIELD - WIDTH_BORDER)/(SIZE_CHIP + GAP_CHIP))
    return (lx, ly)
    
  def fromLocalToGlobal(self, lx, ly): # Перевод из локальной в глобальную
    gx = MARGIN_FIELD + WIDTH_BORDER + (SIZE_CHIP + GAP_CHIP) * lx
    gy = MARGIN_FIELD + WIDTH_BORDER + (SIZE_CHIP + GAP_CHIP) * ly
    return (gx, gy)

  def drawField(self, screen): # Нарисовать поле
    pygame.gfxdraw.box(screen, (MARGIN_FIELD, MARGIN_FIELD, LENGTH_BORDER, LENGTH_BORDER), BLACK)
    pygame.gfxdraw.box(screen, (MARGIN_FIELD + WIDTH_BORDER, MARGIN_FIELD + WIDTH_BORDER, LENGTH_BORDER - 2 * WIDTH_BORDER, LENGTH_BORDER - 2 * WIDTH_BORDER), WHITE)
    for i in range(1, SIZE_FIELD):
      x = y = MARGIN_FIELD + WIDTH_BORDER + i * SIZE_CHIP + (i - 1) * GAP_CHIP
      pygame.gfxdraw.box(screen, (x, MARGIN_FIELD + WIDTH_BORDER, GAP_CHIP, LENGTH_BORDER - 2 * WIDTH_BORDER), BLACK)
      pygame.gfxdraw.box(screen, (MARGIN_FIELD + WIDTH_BORDER, y, LENGTH_BORDER - 2 * WIDTH_BORDER, GAP_CHIP), BLACK)
      
  def assignment(self, screen): # Заполнение поля фишками
    for ly in range(0, SIZE_FIELD):
      for lx in range(0, SIZE_FIELD):
        (gx, gy) = self.fromLocalToGlobal(lx, ly)
        if self.matrix[ly][lx] != None:
          screen.blit(self.pics[self.matrix[ly][lx]], (gx, gy, SIZE_CHIP, SIZE_CHIP))

  def makeMove(self, gx, gy): # Сделать один ход
    lx, ly = self.fromGlobalToLocal(gx, gy)
    for j in range(0, SIZE_FIELD):
      for i in range(0, SIZE_FIELD):
        if self.matrix[j][i] == None: index = (i, j)
    if ((lx == index[0] - 1 or lx == index[0] + 1) and ly == index[1]) or ((ly == index[1] - 1 or ly == index[1] + 1) and lx == index[0]):
      tmp = self.matrix[ly][lx]
      self.matrix[ly][lx] = None
      self.matrix[index[1]][index[0]] = tmp
      self.indexNone = (lx, ly)
      
  def findRandNeighbor(self): # Найти случайного соседа с пустой клеткой
    indexNone = self.indexNone
    neighbors = [] # список соседей
    if indexNone[0] - 1 >= 0: neighbors.append((indexNone[0] - 1, indexNone[1]))
    if indexNone[0] + 1 <= SIZE_FIELD - 1: neighbors.append((indexNone[0] + 1, indexNone[1]))
    if indexNone[1] - 1 >= 0: neighbors.append((indexNone[0], indexNone[1] - 1))
    if indexNone[1] + 1 <= SIZE_FIELD - 1: neighbors.append((indexNone[0], indexNone[1] + 1))
    random.shuffle(neighbors)
    return neighbors[0]

  def randomMix(self): # Случайное перемешивание фишек в поле
    for i in range(0, QUALITYMIX):
      neighbor = self.findRandNeighbor()
      
      tmp = self.matrix[neighbor[1]][neighbor[0]]
      self.matrix[neighbor[1]][neighbor[0]] = None
      self.matrix[self.indexNone[1]][self.indexNone[0]] = tmp
      self.indexNone = neighbor

  def isFinish(self): # Проверить, закончилась ли игра
    if self.matrix == self.initmatrix:
      return True
    else:
      return False

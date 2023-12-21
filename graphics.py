import pygame
from settings import *
import math
from debug import debug
from world import World
from bacteria import Bacteria

class Board():
    def __init__(self, matrix, food_matrix):
        self.disp_surf = pygame.display.get_surface()
        self.tilesize = WIDTH/(len(matrix))
        # self.offset = (self.tilesize, self.tilesize)
        self.offset = (0,0)
        self.matrix = matrix
        self.food_matrix = food_matrix
        self.dim = len(self.matrix)

    def disp(self):
        ts = self.tilesize
        offset = pygame.Vector2(self.offset)
        dim = self.dim
        matrix = self.matrix
        food_matrix = self.food_matrix
 
        rect = pygame.rect.Rect(offset.x, offset.y, WIDTH - 2*offset.x, HEIGHT - 2*offset.y)
        pygame.draw.rect(self.disp_surf, "darkgray", rect)
        
        for i in range(dim):
            for j in range(dim):
                if food_matrix[i][j] == "f":
                    color = "black"
                    rect = pygame.rect.Rect(offset.x + j * ts, offset.y + i * ts, ts, ts)
                    pygame.draw.rect(self.disp_surf, color, rect)
                if matrix[i][j] == 1: 
                    color = "black"
                    rect = pygame.rect.Rect(offset.x + j * ts, offset.y + i * ts, ts, ts)
                    pygame.draw.rect(self.disp_surf, color, rect)
                elif type(matrix[i][j]) != int:
                    color = pygame.Color(matrix[i][j].color)
                    rect = pygame.rect.Rect(offset.x + j * ts, offset.y + i * ts, ts, ts)
                    pygame.draw.rect(self.disp_surf, color, rect)

    def update(self, matrix):
        self.matrix = matrix



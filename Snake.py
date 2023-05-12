import pygame

class Snake():
    def __init__(self, surface):
        self.screen = surface
        self.x_position = 0
        self.y_position = 0
        self.image = pygame.image.load("snake_head.png")
        self.speed = 5
        self.length = 5

    def draw(self):
        self.screen.blit(self.image, (self.x_position, self.y_position))
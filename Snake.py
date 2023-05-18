import pygame

class Snake():
    def __init__(self, surface):
        self.screen = surface
        self.x_position = 200
        self.y_position = 200
        self.head = pygame.image.load("snake_head.png")
        self.body = pygame.image.load("green_sphere.png")
        self.body_seg_positions =[(40,10),(20,30)]
        self.speed = 5
        self.length = 5

    def draw(self):
        # Blit in reverse order so that the body does not overlap the head
        for item in self.body_seg_positions:
            self.screen.blit(self.body, item)
        self.screen.blit(self.head, (self.x_position, self.y_position))

    def get_head_width(self):
        return self.head.get_width()

    def get_head_height(self):
        return self.head.get_height()

    def set_head_xpos(self, xpos):
        setattr(self, "x_position", xpos)

    def set_head_ypos(self, ypos):
        setattr(self, "y_position", ypos)

    def set_body_pos(self):
        pass

import pygame
import time

class Cursor():
    def __init__(self, surface, x_start,y_start):
        self.screen = surface
        self.position_x = x_start
        self.position_y = y_start
        self.move_speed = 10
        self.size = 10
        self.image = pygame.image.load("player.png")

    def draw(self):
        """This method is used to draw the object onto the screen"""
        # pygame.draw.circle(self.screen, "green", [self.position_x, self.position_y], self.size)
        self.screen.blit(self.image, (self.position_x, self.position_y))

    def move_right(self):
        setattr(self, "position_x", self.position_x + self.move_speed)

    def move_left(self):
        setattr(self, "position_x", self.position_x - self.move_speed)

    def move_up(self):
        setattr(self, "position_y", self.position_y - self.move_speed)

    def move_down(self):
        setattr(self, "position_y", self.position_y + self.move_speed)

    def get_posx(self):
        """Returns the current x coordinate position of the cursor"""
        return self.position_x
    def get_posy(self):
        """Returns the current y coordinate position of the cursor"""
        return self.position_y

    def get_width(self):
        return self.image.get_width()

# class to handle the projectile that is being shot

class Projectile():
    def __init__(self, surface, position):
        self.projectile_speed = 10
        self.fire_distance = 300
        self.start_posx = position[0]
        self.start_posy = position[1]
        self.position_x = position[0]
        self.position_y = position[1]
        self.size = 10
        # the surface that we are drawing the projectile onto
        self.screen = surface
        self.image = pygame.image.load("bullet.png")

    def draw_projectile(self):
        """Draws the projectile onto the screen then after it has reached it's maximum allowed travel distance returns the informative text 'delete'"""
        self.screen.blit(self.image, (self.position_x, self.position_y))
        setattr(self, "position_y", self.position_y - self.projectile_speed)
        if self.start_posy - self.position_y > self.fire_distance:
            return "delete"

    def fired(self, position):
        start_pos = position

    def get_width(self):
        return self.image.get_width()
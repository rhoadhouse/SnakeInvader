import pygame
import numpy
value = 0

class Snake():
    def __init__(self, surface, start_pos):
        self.screen = surface
        self.position_x = start_pos[0]
        self.position_y = start_pos[1]
        self.head = pygame.image.load("snake_head.png")
        self.body = pygame.image.load("green_sphere.png")
        self.length = 10
        self.body_seg_positions =[(self.position_x - x*self.body.get_width(),self.position_y) for x in range(0,self.length)]
        self.move_speed = self.body.get_width()/2
        self.vect_list = [(0,0) for x in range(0, self.length)]


    def draw(self):
        # head is the first item in the list
        index = 0
        for item in self.body_seg_positions:
            if index == 0:
                self.screen.blit(self.head, item)
            else:
                self.screen.blit(self.body, item)
            index += 1

    def get_head_width(self):
        return self.head.get_width()

    def get_head_height(self):
        return self.head.get_height()

    def move_right(self):
        self.set_velocity((1,0))
        self.set_body_pos()

    def move_left(self):
        self.set_velocity((-1,0))
        self.set_body_pos()

    def move_up(self):
        self.set_velocity((0,-1))
        self.set_body_pos()

    def move_down(self):
        self.set_velocity((0,1))
        self.set_body_pos()
        global value
        value += 1
        print(value)

    def add_body_segment(self):
        pass

    def delete_body_segment(self):
        pass


    def set_body_pos(self):
        def add_vec_to_pos(self, index):
            return (self.body_seg_positions[index][0] + self.vect_list[index][0],self.body_seg_positions[index][1] + self.vect_list[index][1])
        list = [add_vec_to_pos(self, index) for index in range(0, self.length)]
        setattr(self, "body_seg_positions", list)

    def set_velocity(self, direction):
        """expects a tuple as an input representing the vector direction that the body is taking"""
        self.vect_list.pop(-1)
        self.vect_list.insert(0,(direction[0]*self.move_speed, direction[1]*self.move_speed))


snake = Snake(0, [0,0])
print(snake.vect_list)
snake.set_velocity((1,-1))
snake.set_body_pos()
print(snake.vect_list)
print(snake.body_seg_positions)
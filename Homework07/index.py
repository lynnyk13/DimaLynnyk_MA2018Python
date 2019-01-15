#Clone of 2048 game

import poc_2048_gui
from random import randrange
from random import random


Up = 1
Down = 2
Left = 3
Right = 4


OFFSETS = {Up: (1, 0),
           Down: (-1, 0),
           Left: (0, 1),
           Right: (0, -1)
           }


def merge(line):
    line_length = len(line)
    result_line = [0] * line_length
    last_index = 0

    for current_index in range(line_length):
        if line[current_index] != 0:
            result_line[last_index] = line[current_index]
            last_index += 1

    for key in range(line_length-1):
        if result_line[key] is result_line[key+1]:
            result_line[key] = result_line[key] * 2
            result_line.pop(key+1)
            result_line.append(0)

    return result_line


class TwentyFortyEight:

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.is_occupied = False
        self.is_changed = False
        self.reset()

    def reset(self):
        self.grid = [[0 for dummy_col in range(self.grid_width)] for dummy_row in range(self.grid_height)]

    def __str__(self):
        return str(self.grid)

    def get_grid_height(self):
        return self.grid_height

    def get_grid_width(self):
        return self.grid_width

    def move(self, direction):
        offset = OFFSETS[direction]
        temp_grid = []

#up
        if direction == 1:
            for row in range(self.grid_width):
                start = 0
                temp_list = []
                for dummy_col in range(self.grid_height):
                    temp_list.append(self.grid[start][row])
                    start += offset[0]
                temp_list = merge(temp_list)
                temp_grid.append(temp_list)
            for row in range(self.grid_height):
                for col in range(self.grid_width):
                    self.grid[row][col] = temp_grid[col][row]

#down
        elif direction == 2:
            for row in range(self.grid_width):
                start = self.grid_height - 1
                temp_list = []
                for dummy_col in range(self.grid_height):
                    temp_list.append(self.grid[start][row])
                    start += offset[0]
                temp_list = merge(temp_list)
                temp_grid.append(temp_list)
            for row in range(self.grid_height):
                for col in range(self.grid_width):
                    self.grid[row][col] = temp_grid[col][self.grid_height-1 - row]

#left
        elif direction == 3:
            for col in range(self.grid_height):
                start = 0
                temp_list = []
                for dummy_row in range(self.grid_width):
                    temp_list.append(self.grid[col][start])
                    start += offset[1]
                temp_list = merge(temp_list)
                temp_grid.append(temp_list)
            for row in range(self.grid_height):
                for col in range(self.grid_width):
                    self.grid[row][col] = temp_grid[row][col]

#right
        elif direction == 4:
            for col in range(self.grid_height):
                start = self.grid_width - 1
                temp_list = []
                for dummy_row in range(self.grid_width):
                    temp_list.append(self.grid[col][start])
                    start += offset[1]
                temp_list = merge(temp_list)
                temp_grid.append(temp_list)
            for row in range(self.grid_height):
                for col in range(self.grid_width):
                    self.grid[row][col] = temp_grid[row][self.grid_width - 1 - col]

        total_num = 1
        for value in self.grid:
            for val_el in value:
                total_num *= val_el
                if total_num == 0:
                    self.is_occupied = False
                    break
                else:
                    self.is_occupied = True

        if self.is_changed or not self.is_occupied:
            self.new_tile()
            self.is_change = False

    def new_tile(self):
        probabilities = []
        for dummy_i in range(100):
            if dummy_i < 90:
                probabilities.append(2)
            else:
                probabilities.append(4)
        while True:
            random_row = randrange(0, self.grid_height)
            random_col = randrange(0, self.grid_width)
            if self.grid[random_row][random_col] is 0:
                self.set_tile(random_row, random_col,probabilities[int(random() * 100)])
                break

    def set_tile(self, row, col, value):

        self.grid[row][col] = value

    def get_tile(self, row, col):
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

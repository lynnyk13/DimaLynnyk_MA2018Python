import poc_zombie_gui
import random
import poc_grid
import poc_queue


EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 7
ZOMBIE = 8


class Apocalypse(poc_grid.Grid):

    def __init__(self, grid_height, grid_width, obstacle_list=None, zombie_list=None, human_list=None):

        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):

        self._human_list = []
        self._zombie_list = []
        poc_grid.Grid.clear(self)

    def add_zombie(self, row, col):

        self._zombie_list.append((row, col))

    def num_zombies(self):

        return len(self._zombie_list)

    def zombies(self):

        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):

        self._human_list.append((row, col))

    def num_humans(self):

        return len(self._human_list)

    def humans(self):

        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):

        self._height = self.get_grid_height()
        self._width = self.get_grid_width()

        self._visited = poc_grid.Grid(self._height, self._width)
        self._distance_field = [[self._height * self._width for dummy_col in range(
            self._width)] for dummy_row in range(self._height)]
        self._boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            for cell in self._human_list:
                self._boundary.enqueue((cell[0], cell[1]))
                self._visited.set_full(cell[0], cell[1])
                self._distance_field[cell[0]][cell[1]] = 0
        elif entity_type == ZOMBIE:
            for cell in self._zombie_list:
                self._boundary.enqueue((cell[0], cell[1]))
                self._visited.set_full(cell[0], cell[1])
                self._distance_field[cell[0]][cell[1]] = 0

        while self._boundary.__len__():
            current_cell = self._boundary.dequeue()
            neighbors = self.four_neighbors(current_cell[0], current_cell[1])
            for neighbor in neighbors:
                if self._visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]):
                    self._visited.set_full(neighbor[0], neighbor[1])
                    self._boundary.enqueue(neighbor)
                    self._distance_field[neighbor[0]][neighbor[1]
                                                      ] = self._distance_field[current_cell[0]][current_cell[1]] + 1
        return self._distance_field

    def move_humans(self, zombie_distance_field):

        next_human_list = []
        for current_cell in self._human_list:
            current_distance = zombie_distance_field[current_cell[0]
                                                     ][current_cell[1]]
            distance_list = [[current_cell], [], []]
            neighbors = self.eight_neighbors(current_cell[0], current_cell[1])
            for neighbor in neighbors:
                dummy_idx = zombie_distance_field[neighbor[0]
                                                  ][neighbor[1]] - current_distance
                if 0 <= dummy_idx < 3:
                    distance_list[dummy_idx].append(neighbor)

            if len(distance_list[2]) > 0:
                next_cell = random.choice(distance_list[2])
            elif len(distance_list[1]) > 0:
                next_cell = random.choice(distance_list[1])
            else:
                next_cell = random.choice(distance_list[0])
            next_human_list.append(next_cell)
        self._human_list = next_human_list

    def move_zombies(self, human_distance_field):

        next_zombie_list = []
        for current_cell in self._zombie_list:
            neighbors = self.four_neighbors(current_cell[0], current_cell[1])
            current_distance = human_distance_field[current_cell[0]
                                                    ][current_cell[1]]
            distance_list = [[current_cell], []]

            for neighbor in neighbors:
                dummy_idx = current_distance - \
                    human_distance_field[neighbor[0]][neighbor[1]]
                if dummy_idx >= 0:
                    distance_list[dummy_idx].append(neighbor)

            if len(distance_list[1]) > 0:
                next_cell = random.choice(distance_list[1])
            else:
                next_cell = random.choice(distance_list[0])

            next_zombie_list.append(next_cell)
        self._zombie_list = next_zombie_list


poc_zombie_gui.run_gui(Apocalypse(30, 40))

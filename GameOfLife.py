from random import random
import uuid
import pygame


class Cell:
    def __init__(self, is_alive=False, neighbour=0):
        self.is_alive = is_alive
        self.value = 0
        self.id = uuid.uuid1()
        self.neighbour_count = neighbour

    def __str__(self):
        return "(" + str(self.is_alive) + "," + str(self.value) + ")"


class View:

    def __init__(self):
        self.board = None
        self.screen = pygame.display.set_mode([550, 500])

    def set_board(self, b):
        self.board = b

    def draw_cell(self, x, y, square_size, tuple):
        upper_left_point = x * square_size, y * square_size
        upper_right_point = (x + 1) * square_size, y * square_size
        lower_left_point = x * square_size, (y + 1) * square_size
        lower_right_point = (x + 1) * square_size, (y + 1) * square_size

        pointlist = [upper_left_point,
                     upper_right_point,
                     lower_right_point,
                     lower_left_point]

        pygame.draw.polygon(self.screen, tuple, pointlist, width=0)

    def draw(self):
        square_size = 20  # example
        for y, row in enumerate(self.board):
            for x, val in enumerate(row):
                if val.is_alive:
                    if val.neighbour_count == 3:
                        self.draw_cell(x, y, square_size, (255, 255, 255))
                    else:
                        self.draw_cell(x, y, square_size, (0, 230, 240))
                else:
                    self.draw_cell(x, y, square_size, (0, 0, 0))
        pygame.display.flip()


class Model:
    def __init__(self, dimension):
        self.dimension = dimension
        self.board = self.generate_new_random_board()
        self.map = dict(
            (cell.id, (i, j)) for i, x in enumerate(self.board) for j, cell in enumerate(x))

    def generate_new_random_board(self, prob=0.85):
        board = [[Cell(False) for j in range(self.dimension)] for i in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(self.dimension):
                rand_val = random()
                if rand_val < prob:
                    board[i][j].is_alive = False
                    board[i][j].value = 0
                else:
                    board[i][j].is_alive = True
                    board[i][j].value = 1
        return board

    def set_board_by_predicate(self, predicate):
        self.board = [[Cell(True) if predicate(i, j) else Cell(False)
                       for j in range(self.dimension)] for i in range(self.dimension)]
        self.map = dict(
            (cell.id, (i, j)) for i, x in enumerate(self.board) for j, cell in enumerate(x))

    def count_in_range(self, lower_i, upper_i, lower_j, upper_j):
        counter = 0
        for i in range(lower_i, upper_i + 1):
            for j in range(lower_j, upper_j + 1):
                if self.board[i][j].value == 1:
                    counter += 1
        return counter

    def get_number_of_living_neighbours(self, cell):
        alive_neighbours = 0
        i, j = self.map[cell.id]
        current_value = self.board[i][j].value
        # need to calculate the number of all living cells minus the my the value at i,j (in order not to count
        # myself as my neighbour)
        if 0 < i < self.dimension - 1 and 0 < j < self.dimension - 1:  # both index's are inside the frame
            alive_neighbours = self.count_in_range(i - 1, i + 1, j - 1, j + 1) - current_value
        elif i == 0 and 0 < j < self.dimension - 1:  # i =0 and j is inside the frame
            alive_neighbours = self.count_in_range(i, i + 1, j - 1, j + 1) - current_value
        elif i == self.dimension - 1 and 0 < j < self.dimension - 1:  # i = n-1 and j is inside the frame
            alive_neighbours = self.count_in_range(i - 1, i, j - 1, j + 1) - current_value
        elif j == 0 and 0 < i < self.dimension - 1:  # j = 0 and i is inside the frame
            alive_neighbours = self.count_in_range(i - 1, i + 1, j, j + 1) - current_value
        elif j == self.dimension - 1 and 0 < i < self.dimension - 1:  # j = n-1 and i is inside the frame
            alive_neighbours = self.count_in_range(i - 1, i + 1, j - 1, j) - current_value
        # 4 special cases:
        elif i == 0 and j == 0:
            alive_neighbours = self.count_in_range(i, i + 1, j, j + 1) - current_value
        elif i == 0 and j == self.dimension - 1:
            alive_neighbours = self.count_in_range(i, i + 1, j - 1, j) - current_value
        elif j == 0 and i == self.dimension - 1:
            alive_neighbours = self.count_in_range(i - 1, i, j, j + 1) - current_value
        else:
            alive_neighbours = self.count_in_range(i - 1, i, j - 1, j) - current_value
        return alive_neighbours

    def kill_cell(self, cell):
        cell.is_alive = False
        cell.value = 0

    # not sure about this
    def live_on(self, cell):
        cell.is_alive = True
        cell.value = 1

    def cells_evolution(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                alive_neighbours = self.get_number_of_living_neighbours(self.board[i][j])
                self.board[i][j].neighbour_count = alive_neighbours
                if self.board[i][j].is_alive:
                    if alive_neighbours < 2:  # kill cell
                        self.kill_cell(self.board[i][j])
                    elif alive_neighbours > 3:
                        self.kill_cell(self.board[i][j])
                else:
                    if alive_neighbours == 3:
                        self.live_on(self.board[i][j])


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        pygame.init()
        pygame.display.set_caption("Conway's game of life")


    def generate_universe(self):
        self.model.generate_new_random_board()

    def set_view_surface(self):
        self.view.set_board(self.model.board)

    def evolution_cycle(self):
        self.model.cells_evolution()
        self.view.draw()

    def run_evolution(self):
        running = True
        miliseconds = 100
        while running:
            self.evolution_cycle()
            pygame.time.delay(miliseconds)
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()


def main():
    model = Model(20)
    view = View()
    controller = Controller(model, view)
    controller.generate_universe()
    controller.set_view_surface()
    controller.run_evolution()


main()

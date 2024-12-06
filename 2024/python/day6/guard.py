import argparse

def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def find_starting_point(grid, chars):
    for row_index, row in enumerate(grid):
        for col_index, element in enumerate(row):
            if element in chars:
                return((row_index, col_index), element)
    return None

import itertools

class Navigator:
    """
    class for storing and cycling through the navigator of a 2D text maze
    """
    def __init__(self, grid, obstacle):
        self.maze = grid
        self.mazeHeight = len(grid)
        self.mazeWidth = len(grid[0])
        self.obstacle = obstacle

    def is_escaping(self, x, y):
        return not (0 <= x < self.mazeWidth and 0 <= y < self.mazeHeight)
     
    def is_valid_move(self, x, y):
        # later, include an is_escaping check?
        return not (self.maze[y][x] == self.obstacle)

    def go_up(self, current_pos):
        x, y = current_pos
        return (x, y - 1)

    def go_right(self, current_pos):
        x, y = current_pos
        return (x + 1, y)

    def go_down(self, current_pos):
        x, y = current_pos
        return (x, y + 1)

    def go_left(self, current_pos):
        x, y = current_pos
        return (x - 1, y)

    def next_step(self, current_pos):
        """
        employs a cyclic iterator to traverse through the directions
        """
        directions = [self.go_up, self.go_right, self.go_down, self.go_left]
        direction_cycle = itertools.cycle(directions)
        
        for _ in range(4):
            direction = next(direction_cycle)
            new_pos = direction(current_pos)
            x, y = new_pos
            
            if self.is_escaping(x, y):
                return new_pos, True
            
            if self.is_valid_move(x, y):
                return new_pos, False
        
        return None, False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find the traversal path of a text maze.")
    parser.add_argument('file_path', help="Path to the text file containing the maze.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)
    # print (grid)
    curr, orientation = find_starting_point(grid, ('^', 'v', '<', '>'))

    print(f'guard starting at {curr}, pointing: {orientation}')
    navigator = Navigator(grid, '#')

    goal = False
    count = 1

    while not goal:
        count += 1
        curr, goal = navigator.next_step(current_pos=curr)

        if not curr:
            print('Trapped!')
            break

    print(f'Traversed maze in {count} steps')
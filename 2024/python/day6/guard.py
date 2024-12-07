import argparse
import itertools

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

class Navigator:
    """
    class for storing and cycling through the navigator of a 2D text maze
    """
    def __init__(self, grid, obstacle, start_direction='^'):
        self.maze = grid
        self.mazeHeight = len(grid)
        self.mazeWidth = len(grid[0])
        self.obstacle = obstacle

        # Set the initial direction based on the input character
        self.directions = [self.go_up, self.go_right, self.go_down, self.go_left]
        self.startIndex = self.get_direction_index(start_direction)
        self.currentIndex = self.startIndex

        # store the locations and directions of the traversal
        self.pathTraversed = {
            'go_up': set(),
            'go_right': set(),
            'go_down': set(),
            'go_left': set()
        }

        # flag to identify loop; let the client program deal with it
        self.trappedInLoop = False

    def is_cycle(self, dir, pos):
        """
        check if the position and direction match something
        in the traversal history. True implies being trapped
        in a cycle.
        """
        key = dir.__name__
        if pos in self.pathTraversed[key]:
            return True
        else:
            self.pathTraversed[key].add(pos)
            return False

    def is_escaping(self, x, y):
        return not (0 <= x < self.mazeWidth and 0 <= y < self.mazeHeight)
     
    def is_valid_move(self, x, y):
        return not (self.maze[x][y] == self.obstacle)

    def go_up(self, current_pos):
        x, y = current_pos
        return (x-1, y)

    def go_right(self, current_pos):
        x, y = current_pos
        return (x, y+1)

    def go_down(self, current_pos):
        x, y = current_pos
        return (x+1, y)

    def go_left(self, current_pos):
        x, y = current_pos
        return (x, y-1)

    def next_step(self, current_pos):
        """
        employs a cyclic iterator to traverse through the directions
        """
        direction_cycle = itertools.cycle(self.directions[self.currentIndex:]
                                           + self.directions[:self.currentIndex])
        
        for _ in range(4):
            direction = next(direction_cycle)
            # print(direction.__name__)
            new_pos = direction(current_pos)
            x, y = new_pos
            
            if self.is_escaping(x, y):
                return new_pos, True
            
            if self.is_valid_move(x, y):
                self.currentIndex = self.directions.index(direction)
                self.trappedInLoop = self.is_cycle(direction, new_pos)
                return new_pos, False
        
        return None, False
    
    def get_direction_index(self, start_direction):
            return ['^', '>', 'v', '<'].index(start_direction)

def PART_ONE(grid, debug=False):
    curr, orientation = find_starting_point(grid, ('^', 'v', '<', '>'))

    print(f'guard starting at {curr}, pointing: {orientation}')
    navigator = Navigator(grid, '#')

    goal = False
    count = 1
    visited = set()

    while not goal:
        count += 1
        visited.add(curr)
        
        if debug:
            grid[curr[0]][curr[1]] = 'X'

        curr, goal = navigator.next_step(current_pos=curr)
        if debug:
            print(f'move {count}, position {curr}')

        if not curr:
            print('Trapped!')
            break

    print(f'Traversed {len(visited)} locations in {count} steps')

    if debug:
        xes = 0
        for row in grid:
            xes += row.count('X')
            # print(row)
        print(f'{xes} X\'s in maze')

def PART_TWO(grid, debug=True):
    starting_point, orientation = find_starting_point(grid, ('^', 'v', '<', '>'))
    print(f'guard starting at {starting_point}, pointing: {orientation}')
    
    spaces = []
    for row_index, row in enumerate(grid):
        for col_index, element in enumerate(row):
            if element == '.':
                spaces.append((row_index, col_index))

    success = 0
    while len(spaces) > 0:
        r, c = spaces.pop(0)
        if debug:
            print(f'trying obstacle at: {r}, {c} ...')
        grid[r][c] = '#'
        navigator = Navigator(grid, '#')
        curr = starting_point
        steps = 1
        goal = False
        while not goal:
            steps += 1
            curr, goal = navigator.next_step(current_pos=curr)
            if not curr:
                print('Trapped!')
                break
            if navigator.trappedInLoop:
                print(f'guard trapped at {r}, {c}')
                success += 1
                break
        if goal and debug:
            print(f'guard escaped after {steps} steps')
        grid[r][c] = '.'

    print(f'trapped the guard in {success} different arrangements')



if __name__ == '__main__':
    debug = False
    parser = argparse.ArgumentParser(description="Find the traversal path of a text maze.")
    parser.add_argument('file_path', help="Path to the text file containing the maze.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    PART_ONE(grid, debug)
    PART_TWO(grid, True)

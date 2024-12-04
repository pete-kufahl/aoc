import argparse

def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def find_word(grid, word='XMAS'):
    """
    find the first letter in the grid and then proceed
     along each of the 8 directions, until a character-mismatch or
     out-of-bounds occurs
    """
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),   # up, down, left, right
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # up-left, up-right, down-left, down-right
    ]
    rows, cols = len(grid), len(grid[0])
    results = []
    first_char = word[0] # 'X'

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == first_char:
                for delta_r, delta_c in directions:
                    found = True
                    for i in range(1, len(word)):
                        new_row, new_col = row + delta_r * i, col + delta_c * i
                        # Check if the new position is within bounds and matches the word
                        in_bounds = (0 <= new_row < rows and 0 <= new_col < cols)
                        if not in_bounds or grid[new_row][new_col] != word[i]:
                            found = False
                            break
                    if found:
                        results.append((row, col, delta_r, delta_c))
    return results

def find_crosses(grid):
    """
    X-MAS shapes all have one forward diagonal MAS / SAM and one backward diagonal MAS / SAM
    count all cases where a forward diagonal has the same 'A' as a backward diagonal
    match character-by-character (i.e. tuple-to-tuple)
    """
    rows, cols = len(grid), len(grid[0])
    forward_centers, backward_centers = set(), set()

    # find forward diagonals
    for row in range(rows-2):
        for col in range(cols-2):
            forward = (grid[row][col], grid[row+1][col+1], grid[row+2][col+2])
            if forward == ('M', 'A', 'S') or forward == ('S', 'A', 'M'):
                forward_centers.add((row+1,col+1))

    # find backward diagonals
    for row in range(rows-2):
        for col in range(2, cols):
            backward = (grid[row][col], grid[row+1][col-1], grid[row+2][col-2])
            if backward == ('M', 'A', 'S') or backward == ('S', 'A', 'M'):
                backward_centers.add((row+1,col-1))

    return len(forward_centers & backward_centers)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find all occurrences of 'XMAS' in a word search puzzle.")
    parser.add_argument('file_path', help="Path to the text file containing the word search puzzle.")
    args = parser.parse_args()
    grid = read_grid(args.file_path)

    results = find_word(grid, 'XMAS')
    print(f'the puzzle has {len(results)} cases of XMAS')

    results3 = find_crosses(grid)
    print(f'the puzzle has {results3} cases of X-MAS crosses')

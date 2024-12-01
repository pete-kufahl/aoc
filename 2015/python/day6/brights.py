import numpy as np

if __name__ == "__main__":

    file_name = "input.txt"
    grid = np.full((1000, 1000), 0)
    instrs = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:

                parts = line.strip().split(' ')
                # toggle 756,965 through 812,992
                # turn on 489,959 through 759,964
                if len(parts) in [4, 5]:
                    instrs += 1
                    if parts[0] == 'turn':
                        start = parts[2].split(',')
                        x0 = int(start[0])
                        y0 = int(start[1])
                        end = parts[4].split(',')
                        x1 = int(end[0])
                        y1 = int(end[1])
                        if parts[1] == 'on':
                            for x in range(x0, x1+1):
                                for y in range(y0, y1 + 1):
                                    grid[x, y] = grid[x, y] + 1
                        elif parts[1] == 'off':
                            for x in range(x0, x1+1):
                                for y in range(y0, y1 + 1):
                                    grid[x, y] = max(0, grid[x, y] - 1)
                        else:
                            raise RuntimeError('unknown turn on/off/? line', line)
                    elif parts[0] == 'toggle':
                        start = parts[1].split(',')
                        x0 = int(start[0])
                        y0 = int(start[1])
                        end = parts[3].split(',')
                        x1 = int(end[0])
                        y1 = int(end[1])
                        for x in range(x0, x1+1):
                                for y in range(y0, y1 + 1):
                                    grid[x, y] = grid[x, y] + 2
                    else:
                        raise RuntimeError('unknown line', line)
                    
        total = np.sum(grid)
        print(f'after {instrs} instructions, {total} total brightness level')

    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except IOError:
        print("An error occurred while reading the file.")
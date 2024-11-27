
if __name__ == "__main__":

    file_name = "input.txt"

    try:
        i = 0
        total_paper = 0
        total_ribbon = 0
        with open(file_name, 'r') as file:
            for line in file:
                i += 1
                dims = line.strip().split('x')
                if len(dims) == 3:
                    try:
                        x1, x2, x3 = map(int, dims)
                        sides = [x1 * x2, x1 * x3, x2 * x3]
                        # surface area of the box, which is 2*l*w + 2*w*h + 2*h*l
                        surface_area = 2 * sum(sides)
                        # the area of the smallest side
                        minimum = min(sides)
                        total_paper += surface_area + minimum

                        # shortest distance around its sides, or the smallest perimeter of any one face
                        perims = [2 * x1 + 2 * x2, 2 * x1 + 2 * x3, 2 * x2 + 2 * x3]
                        smallest_perim = min(perims)
                        # cubic feet of volume of the present
                        bow = x1 * x2 * x3
                        total_ribbon += smallest_perim + bow
                    except ValueError:
                        print(f'invalid integers at line {i}: {str(dims)}')
                else:
                    print(f'line {i} does not contain 3 numbers separated by x\'s')

        print(f'total paper needed for {i} gifts: {total_paper} ft^3')
        print(f'total ribbon needed is {total_ribbon} ft')

    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except IOError:
        print("An error occurred while reading the file.")
    


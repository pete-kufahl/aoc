if __name__ == "__main__":
    moves = 0
    santa, robo_santa = (0, 0), (0, 0)
    visited = {(0, 0)}  # Set of visited positions, initialized with (0, 0)

    with open('input.txt') as f:
        for char in f.read():  # Read the entire file at once
            if char not in '<^>v':  # Ignore invalid characters
                continue
            
            moves += 1
            # Determine which character corresponds to which Santa
            is_santa = moves % 2 == 1

            # Update the position based on the direction
            if char == '<':  # Move left
                if is_santa:
                    santa = (santa[0] - 1, santa[1])
                else:
                    robo_santa = (robo_santa[0] - 1, robo_santa[1])
            elif char == '>':  # Move right
                if is_santa:
                    santa = (santa[0] + 1, santa[1])
                else:
                    robo_santa = (robo_santa[0] + 1, robo_santa[1])
            elif char == '^':  # Move up
                if is_santa:
                    santa = (santa[0], santa[1] + 1)
                else:
                    robo_santa = (robo_santa[0], robo_santa[1] + 1)
            elif char == 'v':  # Move down
                if is_santa:
                    santa = (santa[0], santa[1] - 1)
                else:
                    robo_santa = (robo_santa[0], robo_santa[1] - 1)

            # Add the new position to the visited set
            visited.add(santa if is_santa else robo_santa)


    num_visited = len(visited)
    print (f'total houses visited after {moves} moves is {num_visited}')
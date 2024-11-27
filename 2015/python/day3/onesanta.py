if __name__ == "__main__":
    moves = 0
    x, y = 0, 0
    key = str(x) + "_" + str(y)
    visited = set([key])
    
    with open('input.txt') as f:
        while True:
            char = f.read(1)          
            if not char:
                break
            if char == '<':
                x -= 1
            elif char == '^':
                y += 1
            elif char == '>':
                x += 1
            elif char == 'v':
                y -= 1
            else:
                continue
            moves += 1
            key = str(x) + "_" + str(y)
            visited.add(key)

    num_visited = len(visited)
    print (f'total houses visited after {moves} moves is {num_visited}')
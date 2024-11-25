if __name__ == "__main__":
    ret, num = 0, 0
    basement = False

    with open('input.txt') as f:
        while True:
            char = f.read(1)          
            if not char:
                break
            if char == '(':
                ret += 1
            elif char == ')':
                ret -= 1
                if ret == -1 and not basement:
                    print (f'basement entered at position {num+1}')
                    basement = True
            else:
                pass
            num += 1
    print (f'final floor after {num} characters is {ret}')



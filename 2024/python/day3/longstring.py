import re

def find_MUL_in_chunks(file_path, chunk_size=1024):
    """
    this function uses a regex pattern to match the contents of a file to
    mul(X, Y) commands, where X and Y are integers.
    the yield keyword is used to return the latest match (the X and Y values,
    courtesy of the odd re.Match.groups() function)
    """
    pattern = re.compile(r"mul\((-?\d+),(-?\d+)\)")
    buffer = ""
    
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:  # End of file
                break
            
            # find multiple pattern matches in buffer
            buffer += chunk
            matches = list(pattern.finditer(buffer))
            
            # process matches and track where the last complete match ends
            last_match_end = 0
            for match in matches:
                # ensure the match is fully within the buffer
                if match.end() <= len(buffer):  
                    last_match_end = match.end()
                    yield match.groups()
            
            # keep any incomplete match at the end of the buffer
            buffer = buffer[last_match_end:]
        
        # remaining matches in the buffer
        matches = list(pattern.finditer(buffer))
        for match in matches:
            yield match.groups()

if __name__ == '__main__':

    file_path = 'input.txt'
    X = []
    Y = []

    # print("Found cases of 'mul(X, Y)':")
    for x, y in find_MUL_in_chunks(file_path):
        # print(f"X = {x}, Y = {y}")
        X.append(int(x))
        Y.append(int(y))
    if len(X) > 1:
        sumprod = sum([ a * b for a, b in zip(X, Y) ])
        print(f'sum of the {len(X)} products is {sumprod}')

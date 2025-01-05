import argparse

def PART_ONE(filepath, debug=False):
    """
    the string inside the parameter filepath (a file to be read a character at a time) describes 'files'
    and 'memory spaces'. Compact and compute a checksum.
    """
    diskMap = {}    # (int) map-index --> (file-id, file-size)
    gapMap = {}
    input_idx = -1
    map_idx = 0
    fileID = filesize = space = 0
    with open(filepath) as f:
        while True:
            char = f.read(1)          
            if (not char) or (char == '\n'):
                break
            input_idx += 1
            # evens -> file of size char
            # odds -> memory space of size char
            if input_idx % 2:
                space = int(char)
                debug and print(f'at map index {map_idx}, free space of {space}')
                gapMap[map_idx] = space
                map_idx += space
            else:
                filesize = int(char)
                debug and print(f'at map index {map_idx}, file id {fileID} of size {filesize}')
                diskMap[map_idx] = (fileID, filesize)
                fileID += 1
                map_idx += filesize

    if debug:
        i = 0
        disk_str = ""
        while i < map_idx:
            if i in diskMap:
                fid, fsize = diskMap[i]
                for _ in range(fsize):
                    disk_str += str(fid)
                    i += 1
            else:
                disk_str += '.'
                i += 1
        print (disk_str)
        for k, v in diskMap.items():
            print (f'file id {v[0]}, map index {k}, size {v[1]}')
        for l, w in gapMap.items():
            print (f'map index {l}, gap of size {w}')

    uncompressed = sorted(diskMap.keys())
    print(uncompressed)
    print(uncompressed[-1])
    
    checksum: int = 0    # python just handles big integers
    while len(gapMap) > 0 and len(diskMap) > 0:
        gap_ptr = 0
        file_idx = uncompressed[-1]
        fid, fsize = diskMap[file_idx]


        




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Compact string and compute checksum.")
    parser.add_argument('file_path', help="Path to the text file containing the one-line string.")
    args = parser.parse_args()
    
    PART_ONE(args.file_path, True)
    # PART_TWO(args.file_path, True)
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
                # debug and print(f'at map index {map_idx}, free space of {space}')
                gapMap[map_idx] = space
                map_idx += space
            else:
                filesize = int(char)
                # debug and print(f'at map index {map_idx}, file id {fileID} of size {filesize}')
                diskMap[map_idx] = (fileID, filesize)
                fileID += 1
                map_idx += filesize

    debug and print (f'map index at start of compression = {map_idx}')
    if debug:
        print_disc(diskMap, map_idx)
        """ for k, v in diskMap.items():
            print (f'file id {v[0]}, map index {k}, size {v[1]}')
        for l, w in gapMap.items():
            print (f'map index {l}, gap of size {w}') """

    uncompressed = sorted(diskMap.keys())
    gaps = sorted(gapMap.keys())
    
    checksum: int = 0    # python just handles big integers
    cidx = 0

    end = map_idx
    while cidx < end:
        if cidx in diskMap:
            fid, fsize = diskMap[cidx]
            for _ in range(fsize):
                debug and print(f'file content at {cidx}, fid = {fid}, size = {fsize}, end index: {end}')
                checksum += (cidx * fid)
                cidx += 1
        elif cidx in gapMap:
            lastfile = uncompressed[-1]
            firstgap = cidx
            fid, fsize = diskMap[lastfile]
            gapsize = gapMap[firstgap]
            while (gapsize > 0) and (fsize > 0):
                debug and print(f'gap at {cidx} (size={gapsize}), moving file {fid} from {lastfile} (size= {fsize}), end index: {end} -> {end-1}')
                gapsize -= 1
                fsize -= 1
                checksum += (cidx * fid)
                end -= 1
                cidx += 1
            if gapsize > 0:
                gapMap.pop(firstgap)    # update gapmap - remove old gap
                gapMap[cidx] = gapsize  # update gapmap - replace with smaller gap
                debug and print(f'new GAP of {gapsize} starting at {cidx}')
                diskMap.pop(uncompressed.pop(-1))    # remove file
            elif fsize > 0:
                gapMap.pop(firstgap)                # remove gap
                diskMap[lastfile] = (fid, fsize)    # update filemap with smaller file
                debug and print(f'leftover FILE id={fid}, size={fsize}')
            else:
                debug and print(f'file perfectly filled gap at {cidx-1}')
                gapMap.pop(firstgap)    # remove gap
                diskMap.pop(uncompressed.pop(-1))    # remove file
        else:
            print(f'index {cidx} not registered in diskmap or gapmap, i don\'t know what to do!')
            cidx += 1

        debug and print_disc(diskMap, end)
        if uncompressed:
            lid, lsize = diskMap[uncompressed[-1]]
            while (end - 1) > (uncompressed[-1] + lsize - 1):
                debug and print('leftover gap at end! adjusting ...')
                end -= 1
                debug and print_disc(diskMap, end)

    print (f'final checksum is {checksum}') 

def print_disc(diskMap, map_idx):
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
    print (disk_str, map_idx)           
   

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Compact string and compute checksum.")
    parser.add_argument('file_path', help="Path to the text file containing the one-line string.")
    args = parser.parse_args()
    
    PART_ONE(args.file_path, False)
    # PART_TWO(args.file_path, True)
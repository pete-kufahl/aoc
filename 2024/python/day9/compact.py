import argparse

def PART_ONE(filepath, debug=False):
    """
    the string inside the parameter filepath (a file to be read a character at a time) describes 'files'
    and 'memory spaces'. Compact (moving file segments) and compute a checksum.
    """
    diskMap, gapMap, map_idx = build_files_and_gaps(filepath)

    debug and print (f'map index at start of compression = {map_idx}')
    debug and print_disc(diskMap, map_idx)

    uncompressed = sorted(diskMap.keys())   
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
            _, lsize = diskMap[uncompressed[-1]]
            while (end - 1) > (uncompressed[-1] + lsize - 1):
                debug and print('leftover gap at end! adjusting ...')
                end -= 1
                debug and print_disc(diskMap, end)

    print (f'final checksum is {checksum}') 

def PART_TWO(filepath, debug=False):
    """
    the string inside the parameter filepath (a file to be read a character at a time) describes 'files'
    and 'memory spaces'. Compact (moving whole files) and compute a checksum.
    """
    diskMap, gapMap, map_idx = build_files_and_gaps(filepath)

    debug and print (f'map index at start of compression = {map_idx}')
    if debug:
        print_disc(diskMap, map_idx)

    # optimize: 
    #. attempt to move whole files to the leftmost gap that could fit the file
    #. attempt to move each file exactly once in order of decreasing file ID number
    compressedMap = {}
    filesToMove = sorted(diskMap.keys())    # sorted by location --> also sorted by file id
    gapsToFill = sorted(gapMap.keys())
    for loc in reversed(filesToMove):
        moved = False
        fid, fsize = diskMap[loc]
        for gloc in gapsToFill:
            if gloc >= loc:     # only look left
                break
            gsize = gapMap[gloc]
            if gsize >= fsize:
                compressedMap[gloc] = diskMap[loc]
                moved = True
                gsize -= fsize
                if gsize > 0:
                    gapMap.pop(gloc)
                    gapMap[gloc + fsize] = gsize
                else:
                    gapMap.pop(gloc)
                break
        if moved:
            # update gaps, lazy way
            gapsToFill = sorted(gapMap.keys())
        else:
            # in compressed map, leave file in place
            compressedMap[loc] = diskMap[loc]
        if debug:
            print(f'checked file {fid} (original location {loc}), placed in {gloc if moved else loc}')
            print_disc(compressedMap, map_idx)

    # compute checksum
    checksum = 0
    compressed = sorted(compressedMap.keys())
    cidx = 0
    _, lsize = compressedMap[compressed[-1]]
    end = compressed[-1] + lsize
    while cidx < end:
        if cidx in compressedMap:
            fid, fsize = compressedMap[cidx]
            for _ in range(fsize):
                checksum += (cidx * fid)
                cidx += 1
        else:
            cidx += 1
    print (f'final checksum is {checksum}') 

def build_files_and_gaps(filepath):
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
    return diskMap, gapMap, map_idx

def print_disc(diskMap, map_idx):
    """
    this debug is only accurate if diskMap is updated where the gaps are filled.
    for now, it serves its purpose in watching behavior at map_idx during compression.
    """
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
    PART_TWO(args.file_path, False)
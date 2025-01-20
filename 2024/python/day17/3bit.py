import argparse


def read_file(file_path):
    return None, None

def PART_ONE(registers, instructions, debug):
    pass


def PART_TWO(registers, instructions, debug):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="predict activity of 3-bit computer")
    parser.add_argument('file_path', help="path to the text file containing registers and instructions")
    args = parser.parse_args()
    
    registers, instructions = read_file(args.file_path)

    PART_ONE(registers, instructions, debug=False)
    print()

import argparse

def get_input(file_path):
    known_values = {}

    with open(file_path, 'r') as file:
        for line in file:
            if line.isspace():
                break
            
    return [], []

def PART_ONE(gates, knowns, debug):
    ...

def PART_TWO(gates, knowns, debug):
    ...

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="compute logic gate array output")
    parser.add_argument('file_path', help="path to the text file containing the gates and initial values")
    args = parser.parse_args()
    gates, knowns = get_input(args.file_path)
    PART_ONE(gates, knowns, False)
    print()
    PART_TWO(gates, knowns, True)
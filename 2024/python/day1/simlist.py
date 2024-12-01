import sys

def parse_line(line):
    """ interpret lines like: 
        57643   17620
    """
    parts = line.split()    # handles multiple whitespaces
    l1 = parts[0].strip()
    l2 = parts[1].strip()
    return int(l1), int(l2)

if __name__ == "__main__":

    file_name = "input.txt"
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    try:
        sum_sim = 0
        arr1 = []
        arr2 = []

        with open(file_name, 'r') as file:
            for line in file:
                l1, l2 = parse_line(line)
                arr1.append(l1)
                arr2.append(l2)
        
        for num in set(arr1):
            sum_sim += arr2.count(num) * arr1.count(num) * num

        print(f'total similarity of lists is {sum_sim}')

    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except IOError:
        print("An error occurred while reading the file.")
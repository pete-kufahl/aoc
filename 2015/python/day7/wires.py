import sys

def evaluate_wire(wire, wire_map):
    """
    Recursively evaluates the value of a wire.
    """
    # print(f'evaluating wire {wire}, type {type(wire)}, is it a digit? {wire.isdigit()}')

    # If the wire is already computed (it's a constant or result), return its value
    if wire.isdigit():
        # print(f'evaluating {wire} as {int(wire)} ...')
        return int(wire)
    
    # If the wire is already computed (it's a constant or result), return its value
    if isinstance(wire_map[wire], int):
        return wire_map[wire]
    
    # Get the current expression for the wire
    expression = wire_map[wire]
    
    if 'AND' in expression:
        operand1, operand2 = expression.split(' AND ')
        wire_map[wire] = evaluate_wire(operand1.strip(), wire_map) & evaluate_wire(operand2.strip(), wire_map)
    elif 'OR' in expression:
        operand1, operand2 = expression.split(' OR ')
        wire_map[wire] = evaluate_wire(operand1.strip(), wire_map) | evaluate_wire(operand2.strip(), wire_map)
    elif 'NOT' in expression:
        operand = expression.split('NOT ')[1].strip()
        wire_map[wire] = ~evaluate_wire(operand, wire_map) & 0xFFFF  # Apply bitwise NOT and limit to 16 bits
    elif 'RSHIFT' in expression:
        operand, shift = expression.split(' RSHIFT ')
        wire_map[wire] = evaluate_wire(operand.strip(), wire_map) >> int(shift.strip())
    elif 'LSHIFT' in expression:
        operand, shift = expression.split(' LSHIFT ')
        wire_map[wire] = evaluate_wire(operand.strip(), wire_map) << int(shift.strip())
    else:
        if expression.strip().isdigit():
            # If the wire is just a number, return it as an integer
            wire_map[wire] = int(expression.strip())    
        else:
            # Handle the case where it's a direct copy assignment (e.g., "lx -> a")
            wire_map[wire] = evaluate_wire(expression.strip(), wire_map)

    return wire_map[wire]


def parse_line(line, wire_map):
    expression, wire = line.split(' -> ')
    expression = expression.strip()
    wire = wire.strip()
    
    # If the expression is just a number, convert it to an integer
    if expression.isdigit():
        wire_map[wire] = int(expression)
    else:
        # Otherwise, store the expression as a string
        wire_map[wire] = expression

    return

if __name__ == "__main__":

    file_name = "input.txt"
    wire_map = {}

    # alternate input file
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            for line in file:
                parse_line(line, wire_map)
                
        # Evaluate the value for each wire we are interested in
        for wire in wire_map:
            # Only evaluate a wire if it hasn't been computed yet
            if not isinstance(wire_map[wire], int):
                evaluate_wire(wire, wire_map)

        # Print the result
        """
        for wire, value in wire_map.items():
            print(f"{wire}: {value}") 
        """
        ans = wire_map['a']
        print(f'the value on wire a is {ans}')
        bns = wire_map['b']
        print(f'the value on wire b is {bns}')

    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except IOError:
        print("An error occurred while reading the file.")
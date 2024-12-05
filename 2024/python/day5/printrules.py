from collections import defaultdict, deque
import argparse

def parse_file(file_path):
    rules = []
    updates = []
    
    # read everything into a list
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # split the file content into two sections
    # search for the first occurrence of '\n' (a blank line) in the lines list
    blank_line_index = lines.index('\n') if '\n' in lines else len(lines)
    rules_section = lines[:blank_line_index]
    updates_section = lines[blank_line_index + 1:]
    
    # parse the rules section
    for line in rules_section:
        line = line.strip()
        if line:
            parts = line.split('|')
            rules.append((int(parts[0]), int(parts[1])))
    
    # parse the updates section
    for line in updates_section:
        line = line.strip()
        if line:
            updates.append(list(map(int, line.split(','))))
    
    return rules, updates

def middle_element(arr):
    if len(arr) % 2 == 0:
        raise ValueError("The list must have an odd number of elements.")
    idx = len(arr) // 2
    return arr[idx]

def reorder_update(update, rules):
    """
    in order to use the set of applicable_rules, store them as edges in a directed graph.
     each element of update is a node.
    then, traverse the graph (topological sort), using DFS since the goal is to visit all
     vertices. 
    DFS -> stack for next vertices to be visited
    """
    # first, find all of the applicable rules (i.e. rules that apply to every element
    #   in update, and no elements outside of update)
    update_els = set(update)
    applicable_rules = [(x, y) for x, y in rules if x in update_els and y in update_els]
   
    # graph of rules
    graph = defaultdict(list)       # node-to-node directed (k->v) relationships
    incoming = defaultdict(int)     # number of (unvisited) INCOMING edges per node
    
    for x, y in applicable_rules:
        graph[x].append(y)
        incoming[y] += 1
        if x not in incoming:
            incoming[x] = 0
    
    # DFS traversal, storing ordered path of nodes
    # start with nodes with 0 incoming edges
    nodes_to_visit = deque([node for node in update if incoming[node] == 0])
    reordered = []
    while nodes_to_visit:
        node = nodes_to_visit.popleft()
        reordered.append(node)
        
        for neighbor in graph[node]:
            incoming[neighbor] -= 1
            if incoming[neighbor] == 0:
                nodes_to_visit.append(neighbor)

    return reordered

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Interpret printing rules and filter updates.")
    parser.add_argument('file_path', help="Path to the text file containing the data.")
    args = parser.parse_args()

    # file_path = 'example.txt'
    rules, updates = parse_file(args.file_path)

    """
    print("Rules:")
    print(rules)
    print("\nUpdates:")
    print(updates)
    """

    middles = []
    corrected_middles = []
    for update in updates:
        allowed = True
        for before, element in enumerate(update):
            applicable_rules = [rule for rule in rules if rule[0] == element]
            for appl in applicable_rules:
                if appl[1] in update and update.index(appl[1]) < before:
                    allowed = False
                    break
        if allowed:
            print('allowing ', str(update))
            middles.append(middle_element(update))
        else:
            reordered = reorder_update(update, rules)
            if reordered:
                print(f'corrected this: {str(update)} into this {str(reordered)}')
                corrected_middles.append(middle_element(reordered))
    
    print(f'1) sum of the middle elements of printable updates: {sum(middles)}')
    print(f'2) sum of the middle elements of corrected updates: {sum(corrected_middles)}')

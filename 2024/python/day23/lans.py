import argparse
from collections import defaultdict

def get_edges(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            edges.append(line.strip().split('-'))
    return edges

def map_connections(edges):
    connections = defaultdict(set)
    for a, b in edges:
        connections[a].add(b)
        connections[b].add(a)
    return connections

def find_3el_networks(connections):
    """
    given a set of connections, build a container of networks were 3 nodes are connected
    in a network, i.e., each node is directly connected to the 2 other nodes
    """
    networks = set()
    for a in connections:
        for b in connections[a]:
            for c in connections[b]:
                # triangular connection set
                if a != c and a in connections[c]:
                    # avoid dupes by sorting the node-strings and adding the resulting tuple
                    networks.add(tuple(sorted([a, b, c])))
    return networks

def find_nel_networks(connections):
    """
    given a set of connections, build a container of networks were all nodes are connected
    in a network, i.e., each node is directly connected to the other nodes
    """
    networks = set()
    for c in connections:
        search_neighbors(connections, networks, c, {c})
    return networks

def search_neighbors(connections, networks, node, required_set):
    """
    recursive function that checks connections 
    """
    key = tuple(sorted(required_set))
    if key in networks:
        return
    networks.add(key)

    for neighbor in connections[node]:
        if neighbor in required_set:
            continue
        if not (required_set.issubset(connections[neighbor])):
            continue
        # found a new node that's not in the set of fully-connected nodes
        #. but is connected to everyone else
        required_set.add(neighbor)
        search_neighbors(connections, networks, neighbor, required_set | {neighbor})



def PART_ONE(edges, debug):
    """
    given a list of two-compuer connections, coutn how many 3-node networks exist
    with the condition that at least one computer's name starts with t
    """
    debug and print(edges)
    connections = map_connections(edges)
    networks = find_3el_networks(connections)
    debug and print(networks)
    ans = len([n for n in networks if any(node.startswith('t') for node in n)])
    print(f'{ans} such networks in the list of edges')


def PART_TWO(edges, debug):
    """
    given a list of two-computer connections, find the largest network of computers
    where all nodes are connected with each other
    generate the password for this group
    """
    connections = map_connections(edges)
    networks = find_nel_networks(connections)
    debug and print(networks)
    biggest = max(networks, key=len)
    passwd = ",".join(sorted(biggest))
    print(f'password from biggest network is {passwd}')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="find connected networks")
    parser.add_argument('file_path', help="path to the text file containing the 2-computer connections")
    args = parser.parse_args()
    edges = get_edges(args.file_path)
    PART_ONE(edges, False)
    print()
    PART_TWO(edges, True)
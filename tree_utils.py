def generate_tree(depth=3):
    """Create a simple tree structure for pathfinding"""
    tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': ['H'],
        'H': []
    }
    return tree

def find_path(tree, start, goal, path=None):
    """Depth-First Search to find a path from start to goal"""
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for node in tree.get(start, []):
        if node not in path:
            new_path = find_path(tree, node, goal, path)
            if new_path:
                return new_path
    return None

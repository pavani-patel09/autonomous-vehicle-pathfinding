from tree_utils import generate_tree, find_path

def main():
    print("Autonomous Vehicle Pathfinding Running...")
    
    tree = generate_tree(depth=3)
    path = find_path(tree, start='A', goal='H')
    
    print("Optimal path:", path)

if __name__ == "__main__":
    main()

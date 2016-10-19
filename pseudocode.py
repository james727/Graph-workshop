# Pseudocode for BFS and DFS. Syntax errors abound

def breadth_first_search( starting_node ):
    to_visit = queue()
    already_visited = set()
    to_visit.push( starting_node )

    while to_visit is not empty:
        current_node = queue.pop()
        new_neighbors = get_neigboring_nodes( current_ node )

        for neighbors in new_neighbors:
            if neighbor not in visited:
                to_visit.push( neighbor )
                already_visited.add( neighbors )    

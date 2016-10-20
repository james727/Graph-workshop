def get_neighbors( coords, pool ):
    m, n = len( pool ), len( pool[0] )
    x, y = coords
    return [ [ x + i, y + j ] for i, j in ( ( 1, 0 ), ( -1, 0 ), ( 0, 1 ), ( 0, -1 ) ) 
            if 0 <= x + i < m and 0 <= y + j < n and pool[ x + i ][ y + j ] != 'X' ]

def lifeguard_within_k_steps( pool, starting_coords, k ):
    queue = [ ( 0, starting_coords ) ] # set up data structures
    visited = set()

    while len( queue ) != 0:
        current_distance, current_location = queue.pop( 0 ) # inefficient, should use deque
        if current_distance > k: return False # if we've gone more than k steps, fail
        if pool[ current_location[ 0 ] ][ current_location[ 1 ] ] == "L": return True

        potential_neighbors = get_neighbors( current_location, pool )
        unvisited_neighbors = [ n for n in potential_neighbors if n not in visited ]

        for neighbor in unvisited_neighbors:
            queue.append( ( current_distance + 1, neighbor ) )
            visited.add( neighbor )

def good_pool_layout( pool, k ):
    # Returns true if every empty cell in the pool can be reached
    # by an "L" cell within k steps

    # Loop over all cells in the pool
    for x, row in enumerate( pool ):
        for y, val in enumerate( row ):
            coords = ( x, y )
            if val == "": # For open water, check if lifeguard is close
                if not lifeguard_within_k_steps( pool, coords, k ): return False
    return True # if we made it through, the pool is good

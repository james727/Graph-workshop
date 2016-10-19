def get_neighbors( pool_coords, pool ):
    x, y = pool_coords
    max_x, max_y = len( pool ), len( pool[ 0 ] )
    potential_neighbors = [ ( x + 1, y ), ( x - 1, y ), ( x, y + 1 ), ( x, y - 1 ) ]
    pool_bounds_filter = lambda z: 0 <= z[ 0 ] < max_x and 0 <= z[ 1 ] < max_y
    rope_filter = lambda z: pool[ z[ 0 ] ][ z[ 1 ] ] != "X"
    return filter( rope_filter, filter( pool_bounds_filter, potential_neighbors ) )

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

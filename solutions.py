# Solutions to the 2 exercises presented in workshop

def paint_splash( pixels, click_point, target_color ):
    # Inputs:
    # pixels: [ [ int ] ]
    # click_point: ( int, int )
    # target_color: int
    num_rows = len( pixels )
    num_cols = len( pixels[ 0 ] )

    def neighbors( point ):
        x, y = point
        potential_neighbors = [ ( x + 1, y ), ( x - 1, y ), ( x, y + 1 ), ( x, y - 1 ) ]
        bounds_filter = lambda z: 0 <= z[ 0 ] < num_rows and 0 <= z[ 1 ] < num_cols # check bounds of pixels
        color_filter = lambda z: pixels[ z[ 0 ] ][ z[ 1 ] ] == pixels[ x ][ y ] # only same color is connected
        return filter( color_filter, filter( bounds_filter, potential_neighbors ) )

    queue = [ click_point ] # could use deque but this should be fast enough
    visited = set() # we'll track visited pixels in a hash set for fast lookup

    while len( queue ) > 0:
        current = queue.pop( 0 ) # inefficient, should use deque in practice
        new_neighbors = [ pixel for pixel in neighbors( current ) if pixel not in visited ]
        pixels[ current[ 0 ] ][ current[ 1 ] ] = target_color

        # For this solution we're modifying the graph as we search through. Another solution
        # could have a function get_subgraph that returned all connected nodes to a particular
        # starting point. Then you could iterate over the connected nodes and flip the color
        # to target_color.

        for neighbor in new_neighbors:
            queue.append( neighbor )
            visited.add( neighbor ) # adding visited here for efficiency

    return pixels # we're modifying in place, but returning here for clarity

def min_square_sum( n ):
    # Inputs:
    # n: int
    squares = set( [ x ** 2 for x in range( 1, n // 2 + 2 ) ] ) # we'll be checking for membership here
    visited = set()
    queue = [ ( n, 1 ) ]

    def neighbors( m ):
        return [ m - ( i ** 2 ) for i in range(1, int( val ** 0.5 ) + 1 ) ]

    while len( queue ) > 0:
        val, level = queue.pop( 0 ) # inefficient, should use deque in practice
        if val in squares: return level # Sanity check - if n is perfect square, will return 1
        new_neighbors = [ neighbor for neighbor in neighbors( val ) if neighbor not in visited ]

        for neighbor in new_neighbors:
            queue.append( ( neighbor, level + 1 ) )
            visited.add( neighbor )

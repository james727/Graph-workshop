import random
import solutions

MAX_DIM = 10
MAX_COLORS = 3
MAX_NUM = 1000

def gen_paint_test():
    rows = random.randint( 2, MAX_DIM )
    columns = random.randint( 2, MAX_DIM )
    num_colors = random.randint( 2, MAX_COLORS )

    pixels = [ [ random.randint( 0, num_colors ) for _ in range( columns ) ] for _ in range( rows ) ]
    target_color = random.randint( 0, num_colors )
    click_point = ( random.randint( 0, rows - 1 ), random.randint( 0, columns - 1 ) )
    return pixels, click_point, target_color

def gen_squares_test():
    return random.randint( 1, MAX_NUM )

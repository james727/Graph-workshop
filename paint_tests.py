import gentests, solutions, paint_your_solution, copy

VERBOSE_FAIL = True # if true, will print the inputs and expected results for failed tests
NUM_TESTS = 20 # number of random tests to generate

def run_a_test():
    pixels, click_point, target_color = gentests.gen_paint_test()
    solution = solutions.paint_splash( copy.deepcopy( pixels ), click_point, target_color )
    test_solution = paint_your_solution.paint_splash( copy.deepcopy( pixels ), click_point, target_color )
    test_passed = solution == test_solution
    return test_passed, pixels, click_point, target_color, solution, test_solution

def print_failed_test( pixels, click_point, target_color, solution, test_solution ):
    print "Test failed for mouse click at {} with target color {}\n".format( click_point, target_color )
    print "Input pixels:"
    for row in pixels: print "  " + " ".join( [ str( x ) for x in row ] )
    print "Your output:"
    for row in test_solution: print "  " + " ".join( [ str( x ) for x in row ] )
    print "Correct output:"
    for row in solution: print "  " + " ".join( [ str( x ) for x in row ] )
    print

def run_tests():
    pass_counter = 0
    for i in range( NUM_TESTS ):
        pass_flag, pixels, click_point, target_color, solution, test_solution = run_a_test()
        if ( not pass_flag ) and VERBOSE_FAIL:
            print_failed_test( pixels, click_point, target_color, solution, test_solution )
        pass_counter += 1 if pass_flag else 0
    print "Tests completed: passed {}/{} ({})".format( pass_counter, NUM_TESTS, "%.0f%%"%(( pass_counter + 0.0 ) * 100 / NUM_TESTS ) )

if __name__ == "__main__":
    run_tests()

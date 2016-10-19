import gentests, solutions, squares_your_solution

VERBOSE_FAIL = True # if true, will print the inputs and expected results for failed tests
NUM_TESTS = 20 # number of random tests to generate

def run_a_test():
    n = gentests.gen_squares_test()
    solution = solutions.min_square_sum( n )
    test_solution = squares_your_solution.min_square_sum( n )
    test_passed = solution == test_solution
    return test_passed, n, solution, test_solution

def print_failed_test( n, solution, test_solution ):
    print "Test failed for n = {}".format( n )
    print "Your solution: {}".format( test_solution )
    print "Actual solution: {}".format( solution )
    print

def run_tests():
    pass_counter = 0
    for i in range( NUM_TESTS ):
        pass_flag, n, solution, test_solution = run_a_test()
        if ( not pass_flag ) and VERBOSE_FAIL:
            print_failed_test( n, solution, test_solution )
        pass_counter += 1 if pass_flag else 0
    print "Tests completed: passed {}/{} ({})".format( pass_counter, NUM_TESTS, "%.0f%%"%(( pass_counter + 0.0 ) * 100 / NUM_TESTS ) )

if __name__ == "__main__":
    run_tests()

# Graph applications workshop
This repository contains materials for a workshop on graphs given at the Recurse Center on October 19, 2016. It includes source code for all examples discussed, the presentation document, and skeleton code for participants to fill in their own solutions and run tests on them.

## Running the tests
Enter your solutions for the two examples discussed in class in the files `paint_your_solution.py` and `squares_your_solution.py`. Run `paint_tests.py` and `squares_tests.py` to check your answers. A couple notes:

1. Feel free to adjust the params in the testing code to run more / less test cases
2. Test cases are randomly generated at runtime, so it won't be the same tests each time. If you want to ensure the same tests are run, feel free to seed the random number generator in `gentests.py` to a constant of your choosing.

## Other files
My solutions are in the file `solutions.py`. Feel free to take a gander if you'd like (and if you've already completed your own solutions). As usual I've sacrificed some performance for code clarity. The solution to the lifeguard example discussed in workshop is in the `lifeguard_example.py` file.

## Further resources
I credit most of my facility with graphs to the atrociously-named [Intro to Algorithms](https://www.udacity.com/course/intro-to-algorithms--cs215) course on Udacity. While you may think from the name that this course is a survey introduction to algorithms (I certainly did), that's not actually the case. It's really all about graphs and network analysis. It covers a lot more material than this workshop, and if you complete all the exercises I'm confident you'll be completely comfortable with working with graph algorithms by the end of the course.

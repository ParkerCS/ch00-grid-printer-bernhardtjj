# Looks good.
# You could just make a loop to run all those functions.

'''
Grid Printer Exercise
Printing a Grid (adapted from Downey, “Think Python”, ex. 3.5)

Goal:
Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
hints
A couple features to get you started...

use print("+", end = " ") to print continuous line without carriage return

A print function with no arguments ends the current line and goes to the next line:

Simple string manipulation:
You can put two strings together with the plus operator:

"this" + "that" ===>  'thisthat'
Particularly useful if they have been assigned names:
plus = '+'
minus = '-'

You can also multiply strings:
'+' * 10 ===> '++++++++++'
'''


def printer_function():
    """It prints the square."""
    print("\
+ - - - - + - - - - +\n\
|         |         |\n\
|         |         |\n\
|         |         |\n\
|         |         |\n\
+ - - - - + - - - - +\n\
|         |         |\n\
|         |         |\n\
|         |         |\n\
|         |         |\n\
+ - - - - + - - - - +\
")

    print("Just kidding.")

    for row in range(11):
        if row == 0 or row == 5 or row == 10:
            p1 = "+"
            p2 = "-"
        else:
            p1 = "|"
            p2 = " "
        for b in range(2):
            print(p1, end=' ')
            for i in range(4):
                print(p2, end=" ")
        print(p1)


printer_function()
'''
Part 2
Making it more general

Make it a function
One of the points of writing functions is so you can write code that does similar things, but customized to input parameters. So what if we want to be able to print that grid at an arbitrary size?

Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.

For example,

print_grid(3) would print a small grid:

+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
print_grid(15) prints a larger grid:

+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
'''


def printer_function(num):
    """It prints the square again."""
    for row in range(num + 2):
        if row == 0 or row == 1 + num // 2 or row == num + 1:
            p1 = "+"
            p2 = "-"
        else:
            p1 = "|"
            p2 = " "
        for b in range(2):
            print(p1, end=' ')
            for i in range(num // 2):
                print(p2, end=" ")
        print(p1)


printer_function(1)
printer_function(3)
printer_function(5)
printer_function(7)
printer_function(9)
printer_function(11)
printer_function(15)

'''
Part 3:
Even more general...

A function with two parameters
Write a function that draws a similar grid with a specified number of rows and columns, and each cell a given size.

for example, print_grid2(3,4) results in:

+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
What to do about rounding? – you decide.

Another example: print_grid2(5,3):

+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
'''


def printer_function(boxes, num):
    """It prints the square again again."""
    max_rows = num * boxes + boxes + 1
    for row in range(max_rows):
        if row % (max_rows // boxes):
            p1 = "|"
            p2 = " "
        else:
            p1 = "+"
            p2 = "-"
        for b in range(boxes):
            print(p1, end=' ')
            for i in range(num):
                print(p2, end=" ")
        print(p1)


printer_function(3, 4)
printer_function(5, 3)

from time import time
start_time = time()
import sys
from random import randint, random
from os import path

def main():
    sudoku_str = ""
    lst = import_sudoku()
    for i in lst:
        if i != "": 
            sudoku_str += to_str(mask(to_lst(i))) + "\n"
            l = "{0:.0f}".format((time() - start_time)*1000)[1:]
            print("Solved {0:.1f}% | {1}s {2}ms".format((lst.index(i)+1)/len(lst)*100, int(time() - start_time), l), end='\r')

    with open(path.join(path.abspath("Sudokus"), "unsolved.txt"), "w") as f: f.write(sudoku_str)

def import_sudoku():
    with open(path.join(path.abspath("Sudokus"), "solved.txt"), "r") as f:
        sudoku = []
        i = 0
        for line in f:
            sudoku += line
            i += 1
        return "".join(sudoku).split("\n")


def generate_random_list(num, lst):
    index = randint(0, len(lst) - 1)
    result = [list(lst).pop(index)]
    if(num > 1):
        result.extend(generate_random_list(num - 1, lst))
    return result

def mask(sudoku):
    for rowNum in range(9):
        row = sudoku[rowNum]
        offset = randint(0, 1)
        maskIndices = generate_random_list(5 + offset, range(9))
        for i in maskIndices:
            row[i] = 0
    return sudoku

def to_lst(sudoku):
    return [ list( sudoku[ i:i + 9 ] ) for i in range( 0, 81, 9 ) ]

def to_str(sudoku):
    return "".join([str(n) for i in sudoku for n in i])

if __name__ == '__main__':
    main()
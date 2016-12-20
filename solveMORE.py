from time import time
start_time = time()
from sys import stdout, argv
from os import path
from main import solve

def main(n):
    lst = "".join(import_sudoku()).split("\n")
    open(path.join(path.abspath("Sudokus"), "solved.txt"), "w").close()
    cnt = 0
    n = int(n)
    while cnt < n:
        try:
            solve(lst[cnt])
        except SystemExit as e:
            export_sudoku(str(e))
            l = "{0:.0f}".format((time() - start_time)*1000)[1:]
            print("Solved {0:.1f}% | {1}s {2}ms".format(((cnt+1)/n)*100, int(time() - start_time), l), end='\r')
            cnt += 1
    print("Solved 100.0% | {0}s {1}ms".format(int(time() - start_time), l))

def import_sudoku():
    with open(path.join(path.abspath("Sudokus"), "unsolved.txt"), "r") as f:
        sudoku = []
        for line in f:
            sudoku += line
        return(sudoku)

def export_sudoku(sudoku):
    with open(path.join(path.abspath("Sudokus"), "solved.txt"), "a") as f:
        f.write(sudoku + "\n")

if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        main(1)
from time import time
from sys import stdout, argv, exit
from itertools import islice
import unsolve, unsolveMORE, solveMORE

def check_errors(a, b):
    # return zero if a and b are in the same row, column or box
    # (a//9 == b//9) returns zero if a/9 and b/9 are the same
    # ((a-b) % 9 == 0) returns zero if a and b are a (multiple of 9) apart, e.g. 9, 18, 27, 36
    # (a//27 == b//27 and (a%9)//3 == (b%9)//3) returns zero both are true:
    #   (a//27 == b//27) returns zero if a/27 and b/27 are the same, same box
    #   (a%9)//3 == (b%9)//3) returns zero if (a is multiple of 9)/3 is equal to (b is multiple of 9)/3, checks if a and b are in same 3*3 box
    return((a//9 == b//9) or ((a-b) % 9 == 0) or ((a//27 == b//27) and ((a%9)//3 == (b%9)//3)))

def solve(sudoku): # solves a sudoku problem
    a = sudoku.find("0") # gets location of first 0 in str
    if a == -1: exit(sudoku) # returns the solved sudoku once all zeros have been replaced
    excluded_numbers = set() # a set is used because "in" operator is a lot more efficient in sets and because sets have no dublicates
    for b in range(81):
        if check_errors(a, b):
            excluded_numbers.add(sudoku[b])

    for char in "123456789":
        if char not in excluded_numbers:
            '''
            if char is not an excluded number then replace that unkown with the first number in the list that isn't in the same 
            row, column or zone. E.g. replace 0 with 7. Then recalculate with that number solved (pass in sudoku with 127 
            instead of 120) and do this all again until no zeros left.
            '''
            solve(sudoku[:a] + char + sudoku[a+1:])

def show(sudoku):
    if len(sudoku) == 0: return()
    print("\nOne line: " + str(sudoku) + "\n")
    print("    +-----------------------+")
    cnt = 0
    for i in [ str(sudoku)[i:i + int(81//9)] for i in range(0, 81, 81//9) ]: # split str(sudoku) into length 9 parts
        print("    |", end="")
        for n in [ i[n:n + 9//3] for n in range(0, 9, 9//3) ]: # split into i into length 3 parts
            for j in n: # split n into length 1 parts
                print(" " + j, end="")
            print(" |", end="")
        cnt += 1
        if cnt in (3, 6): print("\n    |-------+-------+-------|")
        else: print("")
    print("    +-----------------------+")

def import_sudoku():
    try:
        with open("sudoku.txt", "r") as f:
            sudoku = ""
            for i in f.read():
                if i in "0123456789":
                    sudoku += i
                if i == ".":
                    sudoku += "0"
            return(sudoku)
    except IOError:
        with open("sudoku.txt", "w+") as f:
            f.write("""+-----------------------+
| . . . | . . . | . . . |
| . . . | . . . | . . . |
| . . . | . . . | . . . |
|-------+-------+-------|
| . . . | . . . | . . . |
| . . . | . . . | . . . |
| . . . | . . . | . . . |
|-------+-------+-------|
| . . . | . . . | . . . |
| . . . | . . . | . . . |
| . . . | . . . | . . . |
+-----------------------+""")
            sudoku = ""
            for i in f.read():
                if i in "0123456789":
                    sudoku += i
                if i == ".":
                    sudoku += "0"
            return(sudoku)

def man():
    print("""
    SYNOPSIS
        main.py [OPTIONS] [AMOUNT]
    
    OPTIONS
        SUDOKU
            Solves SUDOKU, where SUDOKU is of length 81 and is in one line format where zeros represent unkowns.
            example: 241700530573004180096001040734000600000006325602810000005080071320059800008647200

        -s (--show)
            Shows sudoku.txt

        -i (--import)
            Solves a sudoku problem from sudoku.txt

        -sM (--solveMORE)
            Solves [AMOUNT] of sudoku in unsolved.txt and writes answers to solved.txt

        -u (--unsolve)
            Unsolves an [AMOUNT] of sudoku in solved.txt and writes to screen

        -uQ (--unsolveQUICK)
            Shows an [AMOUNT] of unsolved sudoku problems from unsolved.txt

        -uA (--unsolveALL)
            Unsolves all the sudoku from solved.txt and writes to unsolved.txt
    """)




if __name__ == '__main__':
    if len(argv) == 2:
        
        if len(argv[1]) == 81:
            start_time = time()
            try: solve(argv[1])
            except SystemExit as e:
                show(str(e))
                print("\n{0}s {1:.0f}ms".format(int(time() - start_time), (time() - start_time)*1000))
        
        elif argv[1] in ("-uA", "--unsolveALL"):
            unsolveMORE.main()
        
        elif argv[1] in ("-i", "--import"):
            start_time = time()
            try: solve(import_sudoku())
            except SystemExit as e:
                show(str(e))
                print("\n{0}s {1:.0f}ms".format(int(time() - start_time), (time() - start_time)*1000))
                 
        elif argv[1] in ("-s", "--show"):
            show(import_sudoku())
        
        elif argv[1] in ("-sM", "--solveMORE"):
            solveMORE.main(1)
            
        elif argv[1] in ("-u", "--unsolve"):
            start_time = time()
            show(unsolve.main(1))
            print("\n{0}s {1:.0f}ms".format(int(time() - start_time), (time() - start_time)*1000))
            
        elif argv[1] in ("-uQ" "--unsolveQUICK"):
            start_time = time()
            show(unsolve.main(1, "-uQ"))
            print("\n{0}s {1:.0f}ms".format(int(time() - start_time), (time() - start_time)*1000))
        
        else: man()
    
    elif len(argv) == 3:
        if argv[1] in ("-sM", "--solveMORE"):
                solveMORE.main(argv[2])
            
        elif argv[1] in ("-u", "--unsolve"):
            start_time = time()
            for i in unsolve.main(int(argv[2])).split("\n"):
                show(i)
            print("\n{0}s {1:.0f}ms".format(int(time() - start_time), (time() - start_time)*1000))

        elif argv[1] in ("-uQ" "--unsolveQUICK"):
            start_time = time()
            unsolved = unsolve.main(int(argv[2]), "-uQ").split("\n")
            for i in unsolved:
                show(i)
            print("\n{0}s {1:.0f}ms".format(int(time() - start_time), (time() - start_time)*1000))
        
        else: man()

    else: man()

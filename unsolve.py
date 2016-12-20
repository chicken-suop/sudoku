from time import time
import sys
from random import randint, randrange, random
from os import path

def main(k, option = ""):
    if option == "-uQ": lines = reservoir_sample(k, "unsolved.txt")
    else: lines = reservoir_sample(k)
    
    unsolved = ""
    for line in lines:
        unsolved += ("".join([str(n) for i in mask([list(line[i:i + 9]) for i in list(range(0, 81, 9))]) for n in i]) + "\n")
    return(unsolved.strip("\n"))
    
def reservoir_sample(k, direct = "solved.txt"):
    with open(path.join(path.abspath("Sudokus"), direct), "r") as stream:
        lines = []
        n = 0
        for line in stream:
            n += 1
            if len(lines) < k:
                lines.append(line.strip("\n"))
            else:
                s = int(random() * n)
                if s < k:
                    lines[s] = line.strip("\n")
        return lines

def generateRandomList(num):
    result = [list(range(9)).pop(randint(0, 8))]
    if num > 1:
        result.extend(generateRandomList(num - 1))
    return result

def mask(line):
    # Good code:
    for rowNum in range(9):
        row = line[rowNum]
        mask_indices = generateRandomList(5 + randint(0, 1))
        for i in mask_indices:
            row[i] = '0'
    return line

if __name__ == '__main__':
    if len(sys.argv) == 2:
        start_time = time()
        print(main(int(sys.argv[1])))
        l = "{0:.0f}".format((time() - start_time)*1000)[1:]
        print("\n{0}s {1}ms".format(int(time() - start_time), l))
        
    else:
        start_time = time()
        print(main(1))
        l = "{0:.0f}".format((time() - start_time)*1000)[1:]
        print("\n{0}s {1}ms".format(int(time() - start_time), l))
# unsolve version 1
# Doesn't work, converted to new version "unsolve.py"

from random import shuffle
def is_valid(line):
    row_amount = 0
    for row in [line[i:i + 9] for i in range(0, 81, 9)]:
        row_amount += len(set(row))
    
    col_amount = 0
    for column in [line[n::9] for n in range(9)]:
        col_amount += len(set(column))
    
    box_amount = 0
    for box in [''.join(d) for d in [[[line[i:i + 9] for i in range(0, 81, 9)][i+l][n:n+3] for l in range(0, 7, 3) for n in range(0, 7, 3) for i in range(3)][i:i+3] for i in range(0, 27, 3)]]:
        box_amount += len(set(box))
    
    if row_amount + col_amount + box_amount == 243:
        return True
        print("True")


def unsolve(line):
    line = list(line)
    shuffle(line)
    for pos in range(81):
        var = line[pos]
        line[pos] = '0'
        if is_valid(''.join(line)) != True:
            line[pos] = var
    return(''.join(line))
            
        

line = "354296781216587439897143562569832174781964253423715896942658317178329645635471928"
show(line)
show(unsolve(line))
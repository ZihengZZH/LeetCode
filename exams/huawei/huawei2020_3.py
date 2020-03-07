import sys


matrix = [[0] * 8 for _ in range(8)]
step_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
}


'''
black == 1
white == 2
'''
def begin():
    matrix[3][4] = 1
    matrix[4][3] = 1
    matrix[3][3] = 2
    matrix[4][4] = 2

def display():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def turn(ii, jj, value2turn):
    turn_count = 0
    value = 2 if value2turn == 1 else 1
    if matrix[ii-1][jj-1] == matrix[ii+1][jj+1] == value:
        matrix[ii][jj] = value
        turn_count += 1
    elif matrix[ii-1][jj+1] == matrix[ii+1][jj-1] == value:
        matrix[ii][jj] = value
        turn_count += 1
    elif matrix[ii][jj-1] == matrix[ii][jj+1] == value:
        matrix[ii][jj] = value
        turn_count += 1
    elif matrix[ii-1][jj] == matrix[ii+1][jj] == value:
        matrix[ii][jj] = value
        turn_count += 1
    return turn_count

def move(ii, jj, black=True):
    matrix[ii][jj] = 1 if black else 2
    num2turn = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if black and matrix[i][j] == 2:
                num2turn += turn(i, j, 2)
            elif not black and matrix[i][j] == 1:
                num2turn += turn(i, j, 1)
    # display()
    if num2turn == 0:
        return False
    else:
        return True

def count(black=True):
    num = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and black:
                num += 1
            elif matrix[i][j] == 2 and not black:
                num += 1
    return num

if __name__ == '__main__':
    begin()
    # display()
    line = sys.stdin.readline().strip()
    steps = line.split(',')
    # steps = ['F5', 'F4', 'F3', 'D6']
    for kk in range(len(steps)):
        if kk % 2 == 0:
            black = True
        else:
            black = False
        step = steps[kk]
        if step == '00':
            continue
        ii, jj = int(step[1])-1, step_dict[step[0]]-1
        if not move(ii, jj, black=black):
            print("ERROR %d:%s" % (kk, step))
    print("OK %d:%d" % (count(black=True), count(black=False)))

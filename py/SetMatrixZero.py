'''

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

'''

# Firstly to find the locations of all zeros
# Then to change the row and column
def setZeros(matrix):
    zeros = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zeros.append((i,j))
    print(zeros)
    for (x,y) in zeros:
        matrix[x] = [0]*len(matrix[x])
        for z in range(len(matrix)):
            matrix[z][y] = 0
    return

if __name__ == "__main__":
    matrix = [[2,2,10],[1,0,2],[1,0,2]]
    print(matrix)
    setZeros(matrix)
    print(matrix)
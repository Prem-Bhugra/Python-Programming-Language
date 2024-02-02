"""Transpose of a matrix"""
# matrix = [[2,3],[6,7],[9,0]]
# matrix = [[1,2,3],[4,5,6]]
matrix = [[2,4,6],[3,6,9],[1,2,3]]
transpose = []
i = 0
while i < len(matrix[0]):
    column = []
    for lists in matrix:
        column.append(lists[i])
    transpose.append(column)
    i += 1
print(transpose)
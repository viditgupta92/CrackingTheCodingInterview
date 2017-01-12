# starts with top right corner element of the matrix
def sorted_matrix_search(mat, item):
    row = 0
    col = len(mat[0]) - 1
    flag = 0
    while row < len(mat) and col >= 0:
        if item == mat[row][col]:
            flag = 1
            break
        elif item < mat[row][col]:
            col -= 1
        else:
            row += 1
    print(flag)

#sorted_matrix_search([[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]],55)


#starts with bottom left corner element of the matrix
def sorted_matrix_search_alternate(mat, item):
    row = len(mat) - 1
    col = 0
    flag = 0
    while col <= len(mat[0]) - 1 and row >= 0:
        if item == mat[row][col]:
            flag = 1
            break
        elif item < mat[row][col]:
            row -= 1
        else:
            col += 1
    print(flag)

sorted_matrix_search_alternate([[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]],5)
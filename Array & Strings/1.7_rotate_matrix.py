def print_matrix(mat,r,c):
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end = " ")
        print("\n")

def rotate_matrix_1(mat):
    row = len(mat)
    col = len(mat[0])
    new_mat = [[0 for x in range(row)] for y in range(col)]
    for i in range(row):
        col_value = (col - 1) - i
        for j in range(col):
            new_mat[j][col_value] = mat[i][j]
    print_matrix(new_mat,row,col)

rotate_matrix_1((['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']))
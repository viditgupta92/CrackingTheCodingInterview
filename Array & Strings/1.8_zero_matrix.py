def print_matrix(mat,r,c):
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end = " ")
        print("\n")

def nullify_row_col(mat,num,length,type):
    if type == 'r':
        for i in range(length):
            mat[num][i] = 0
    else:
        for i in range(length):
            mat[i][num] = 0

def zero_matrix(mat):
    row_len = len(mat)
    col_len = len(mat[0])
    row = [0 for each in range(row_len)]
    col = [0 for each in range(col_len)]
    for i in range(row_len):
        for j in range(col_len):
            if mat[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(row_len):
        if row[i] == 1:
            nullify_row_col(mat,i,col_len,'r')

    for j in range(col_len):
        if col[j] == 1:
            nullify_row_col(mat,j,row_len,'c')
    print_matrix(mat,row_len,col_len)

zero_matrix(([1,2,3,4],[5,6,0,8],[9,10,11,12],[13,14,15,0]))
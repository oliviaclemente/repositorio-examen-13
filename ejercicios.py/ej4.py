def rotar(mat):
  if not mat or not len(mat):
    return
  n= len(mat)
  for i in range(n):
    for j in range(i):
      temp= mat[i][j]
      mat[i][j]= mat[j][i]
      mat[j][i]= temp
    for i in range(n):
      for j in range(n//2):
        temp= mat[i][j]
        mat[i][j]= mat[j][n-j-1]
        mat[i][n-j-1]= temp

if __name__='__main__':
  mat= [[7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]]
  rotate(mat)
  F
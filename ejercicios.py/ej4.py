def rotar(mat):
  if not mat or not len(mat):
    return
  n= len(mat)
  for i in range(n):
    for j in range(i):
      temp= mat
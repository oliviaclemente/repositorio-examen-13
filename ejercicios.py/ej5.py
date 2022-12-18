def luck_check(string):
  tem1= 0
  temp2= 0
  for i in range(len(string)//2):
    tem1 += int(string[x])
    tem2= += int(string[len(string)-1-x])
    print(tem1,tem2)
  if tem1 == temp2:
    return True
  else:
    return False
  print(luck_check("567993"))
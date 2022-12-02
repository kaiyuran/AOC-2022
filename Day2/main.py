inputs = open('2.txt', 'r')
ogstring = inputs.read()
ilist = (ogstring.split('\n'))
inputs.close()
score = 0
win = 6
lose = 0
tie = 3
for x in range(len(ilist)):
  ilist[x] = (ilist[x]).split()
  print(ilist[x])
  if ilist[x][0] == 'A':
    if (ilist[x][1]) == 'X':
      score +=(3+lose)
      print('added is '+ str(3+lose))
    elif (ilist[x][1]) == 'Y':
      score +=(1+tie)
      print('added is '+ str(1+tie))
    elif (ilist[x][1]) == 'Z':
      score +=(2+win)
      print('added is '+ str(win+2))
  elif ilist[x][0] == 'B':
    if (ilist[x][1]) == 'X':
      score +=(1+lose)
      print('added is '+ str(3+lose))
    elif (ilist[x][1]) == 'Y':
      score +=(2+tie)
      print('added is '+ str(1+tie))
    elif (ilist[x][1]) == 'Z':
      score +=(3+win)
      print('added is '+ str(win+2))
  elif ilist[x][0] == 'C':
    if (ilist[x][1]) == 'X':
      score +=(2+lose)
      print('added is '+ str(3+lose))
    elif (ilist[x][1]) == 'Y':
      score +=(3+tie)
      print('added is '+ str(1+tie))
    elif (ilist[x][1]) == 'Z':
      score +=(1+win)
      print('added is '+ str(win+2))
print(ilist)
print(score)
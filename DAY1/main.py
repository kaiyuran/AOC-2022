ilist = (open('1.txt', 'r')).read().split('\n\n')
count = 0
for x in range(len(ilist)):
  ilist[x] = ilist[x].split("\n")
  for y in range(len(ilist[x])):
    count += int(ilist[x][y])
  ilist[x] = count
  count = 0
ilist.sort()
counting = ilist[-1]+ilist[-2]+ilist[-3]
print(counting)

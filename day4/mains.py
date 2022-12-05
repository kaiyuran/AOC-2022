count = 0
ilist = (open(r'C:\Users\kaiyu\Documents\GitHub\AOC-2022\day4\4.txt', 'r')).read().replace("\n", ",").split(',')
for x in range(len(ilist)):
    ilist[x] = ilist[x].split("-")
fl = []
sl = []
for x in range(len(ilist)-1):
    if x%2 == 0:
        fl = list(range(int(ilist[x][0]), (int(ilist[x][1]))+1))
        sl = list(range(int(ilist[x+1][0]), (int(ilist[x+1][1]))+1))
        print(fl)
        print(sl)
        for y in range(len(fl)):
            if (fl[y] in sl):
                count +=1
                break
print(count)
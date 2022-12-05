count = 0
ilist = (open(r'C:\Users\kaiyu\Documents\GitHub\AOC-2022\day4\4s.txt', 'r')).read().replace("\n", ",").split(',')
for x in range(len(ilist)):
    ilist[x] = ilist[x].split("-")
for x in range(len(ilist)-1):
    print(x)
    if x%2 == 0:
        if ((int(ilist[x][0]) >= int(ilist[x+1][0])) and (int(ilist[x][1]) <= int(ilist[x+1][1]))) or ((int(ilist[x+1][0]) >= int(ilist[x][0])) and (int(ilist[x+1][1]) <= int(ilist[x][1]))):
            count += 1
            print("dup")
print(count)

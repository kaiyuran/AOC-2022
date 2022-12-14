ilist = (open(r'C:\Users\kaiyu\Documents\GitHub\AOC-2022\Day5\5s.txt', 'r')).read().split('\n\n')
crates = [ilist[0].split("\n")]
count = 0
for x in range(len(crates)):
    crates[x] = (str(crates[x]).replace("    ",'x'))
    crates[x] = list(crates[x])
    while True:
        try:
            crates[x].remove("[")
        except:
            break
    while True:
        try:
            crates[x].remove("]")
        except:
            break
    while True:
        try:
            crates[x].remove("'")
        except:
            break
    while True:
        try:
            crates[x].remove(" ")
        except:
            break
    for z in range(1,10):
        while True:
            try:
                crates[x].remove(str(z))
            except:
                break
    crates[0].pop()
string = ''
print(crates)
for x in crates[0]:
    string += x
nlist = (string.split(','))
for x in range(len(nlist)):
    nlist[x] = list(nlist[x])
finalist = [[0]*(3) for x in range(3)]
print(finalist)
for x in range(len(nlist)):
    for y in range(len(nlist[x])):
        if count < (len(nlist)):
            finalist[count][x] = nlist[x][y]
            count +=1
        else:
            count = 0
            # print(x,y, count)
            finalist[count][x] = nlist[x][y]
            count += 1
print(finalist)
for x in range(len(finalist)):
    while True:
        try:
            finalist[x].remove('x')
        except:
            break

controls = [ilist[1].split("\n")]#make the inputs of controls easier to work with
controls = controls[0]
for x in range(len(controls)):
    controls[x] = controls[x].split(" ")
    controls[x].remove("move")
    controls[x].remove("from")
    controls[x].remove("to")
    for y in range(len(controls[x])):
        controls[x][y] = int(controls[x][y])







print(finalist)
movingcrates = []
for x in controls:
    print("this is control {}".format(x))
    # print(movingcrates)
    cratesnum = x[0]
    # print(cratesnum, type(cratesnum))
    crateorigin = (x[1]-1)
    # print(crateorigin, type(crateorigin))
    cratesdes = (x[2]-1)
    # print(cratesdes, type(cratesdes))
    for y in range(cratesnum):
        movingcrates.append(finalist[crateorigin][y])
        # print(movingcrates)
    for z in range(cratesnum):
        finalist[cratesdes].insert(0,(movingcrates[(z)]))
        finalist[crateorigin].remove(movingcrates[(z)])
        # print(finalist)
    movingcrates = []



# print(movingcrates)
# print(finalist)

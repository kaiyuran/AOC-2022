ilist = (open(r'C:\Users\kaiyu\Documents\GitHub\AOC-2022\Day3\3.txt', 'r')).read().split('\n')
dupdeleted = []
dups = []

for x in (ilist):
    x = [((x)[:len(x)//2]),((x)[len(x)//2:])]
    x[0] = list(x[0])
    for a in x[0]:
        if a not in dupdeleted:
            dupdeleted.append(a)
            # print(dupdeleted)
    for y in dupdeleted:
        if y in x[1]:
            dups.append(y)
    dupdeleted = []

tsum = 0
for x in dups:#sum finder
    if x == 'a':
        tsum += 1
    elif x == 'b':
        tsum += 2
    elif x == 'c':
        tsum += 3
    elif x == 'd':
        tsum += 4
    elif x == 'e':
        tsum += 5
    elif x == 'f':
        tsum += 6
    elif x == 'g':
        tsum += 7
    elif x == 'h':
        tsum += 8
    elif x == 'i':
        tsum += 9
    elif x == 'j':
        tsum += 10
    elif x == 'k':
        tsum += 11
    elif x == 'l':
        tsum += 12
    elif x == 'm':
        tsum += 13
    elif x == 'n':
        tsum += 14
    elif x == 'o':
        tsum += 15
    elif x == 'p':
        tsum += 16
    elif x == 'q':
        tsum += 17
    elif x == 'r':
        tsum += 18
    elif x == 's':
        tsum += 19
    elif x == 't':
        tsum += 20
    elif x == 'u':
        tsum += 21
    elif x == 'v':
        tsum += 22
    elif x == 'w':
        tsum += 23
    elif x == 'x':
        tsum += 24
    elif x == 'y':
        tsum += 25
    elif x == 'z':
        tsum += 26
    elif x == 'A':
        tsum += 27
    elif x == 'B':
        tsum += 28
    elif x == 'C':
        tsum += 29
    elif x == 'D':
        tsum += 30
    elif x == 'E':
        tsum += 31
    elif x == 'F':
        tsum += 32
    elif x == 'G':
        tsum += 33
    elif x == 'H':
        tsum += 34
    elif x == 'I':
        tsum += 35
    elif x == 'J':
        tsum += 36
    elif x == 'K':
        tsum += 37
    elif x == 'L':
        tsum += 38
    elif x == 'M':
        tsum += 39
    elif x == 'N':
        tsum += 40
    elif x == 'O':
        tsum += 41
    elif x == 'P':
        tsum += 42
    elif x == 'Q':
        tsum += 43
    elif x == 'R':
        tsum += 44
    elif x == 'S':
        tsum += 45
    elif x == 'T':
        tsum += 46
    elif x == 'U':
        tsum += 47
    elif x == 'V':
        tsum += 48
    elif x == 'W':
        tsum += 49
    elif x == 'X':
        tsum += 50
    elif x == 'Y':
        tsum += 52
    elif x == 'Z':
        tsum += 52
print(tsum)
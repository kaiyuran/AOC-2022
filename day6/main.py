import math
while True:
    print('hi')
    a = float(input())
    b = float(input())
    c = float(input())
    total = (b**2-(4*a*c))
    try:
        print('this is the sqrt   ', math.sqrt(total))
    except:
        print('negative ')
        pass
    # print(total)
    # try:
    #     total = math.sqrt(total)
    #     if total > 0:
    #         print('two roots')
    #         print(total)
    #     else:
    #         print('one root')
    #         print(total)
    # except:
    #     print('no roots')
    #     print(total)

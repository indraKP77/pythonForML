#First GUI
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

i = 0
while i<6:
    for item in picture[i]:
        if item == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    i+=1
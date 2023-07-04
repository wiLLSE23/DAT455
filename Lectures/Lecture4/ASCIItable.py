def simpleASCII():
    for i in range(0,32):
        row = ""
        for j in range(0,8):
            row = row + str(i+j*32) + ' ' + chr(i +j*32) + '\t'
        print(row)

simpleASCII()
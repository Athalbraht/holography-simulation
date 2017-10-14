import matplotlib.pyplot as plt

try:
    file = open("test.data", "r")
    tab = file.readlines()
    res = int(float(tab[0])**0.5)
    print(res)
    data2 = []
    for tb in tab[1:]:
        temp = tb.split()
        temp = [float(i) for i in temp]
        data2.append([])
        for i in range(res):
            data2[-1].append([])
            for j in range(res):
                data2[-1][i].append(temp[i+j*res])
                
    #print(data2[1])    
    _temp = data2[0]           
    for frame in data2[1:]:
        for i in range(res):
            for j in range(res):
                _temp[i][j] += frame[i][j]        
   # print(_temp)
    plt.imshow(_temp, interpolation="bicubic", cmap='gray')
finally:
    file.close()
    plt.show()

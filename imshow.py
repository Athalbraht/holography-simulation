import matplotlib.pyplot as plt

try:
    file = open("test.data", "r")
    tab = file.readlines()
    res = int(float(tab[0])**0.5)
    data = tab[1].split()
    print(res)
    data = [float(i) for i in data]
    data2=[]
    for i in range(res):
        data2.append([])
        for j in range(res):
            data2[i].append(data[i+j*res])

    plt.imshow(data2, interpolation="lanczos", cmap='gray')
finally:
    file.close()
    plt.show()

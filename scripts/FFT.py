import numpy as np


def FFT2Dc(c_img):
    size = c_img.shape
    new_img = np.zeros(size)

    for i in range(size[0]):
        for j in range(size[1]):
            new_img[i][j] =  np.exp(i*np.pi*(i+j))
    ft = np.fft.fft2(new_img*c_img)
    return np.absolute(new_img*ft)


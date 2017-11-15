#!/usr/bin/env python3
import os
import sys
import matplotlib.pyplot as plt

cp = os.getcwd()[:-10]
sys.path.insert(0,cp)

import scripts.image_converter as ic
import scripts.FFT as ft
import scripts.prop as prop
import numpy as np

im = ic.change_type('{}'.format(sys.argv[1]), 'fft_test.png','L')

############ TEST ###########
im = np.ones((400,400))
px_size = 0.1
px_n = im.shape[1]
x = np.linspace(-px_size * px_n / 2, px_size * px_n / 2, num = px_n, endpoint = True)
dx = x[1] - x[0]
fS = 1 / dx
df = fS / px_n
fx = np.arange(-fS / 2, fS / 2, step = df)
print(fx.shape)
im[50][50] = 0.9
#im[13][9] = 0.9
#############################

plt.imshow(im)
plt.title('im')
plt.show()
plt.clf()

im_fft = np.fft.ifftshift(np.fft.fft2(np.fft.fftshift(im)))

plt.imshow(np.abs(im_fft))
plt.title('fft_A')
plt.show()
plt.clf()

plt.imshow(np.angle(im_fft))
plt.title('fft_phi')
plt.show()
plt.clf()

n = im_fft.shape
S = np.zeros(n)


def H(fx, fy, z, l=0.5):
    square_root = np.sqrt(np.complex(1) - (l**2 * fx**2) - (l**2 * fy**2))
    temp = np.exp(1j * 2 * np.pi * z / l * square_root)
    temp[np.isnan(temp)] = 0
    return temp

fX, fY = np.meshgrid(fx,fx)
S = H(fX,fY, 10)

plt.imshow(np.abs(S),cmap='gray')
plt.title('S_A')
plt.show()
plt.clf()
plt.imshow(np.angle(S),cmap='gray')
plt.title('S_phi')
plt.show()
plt.clf()


im_ifft = np.fft.ifft2(S*im_fft)
plt.imshow(np.abs(im_ifft)**2,cmap='gray')
plt.title('ifft_A')
plt.show()
plt.clf()
plt.imshow(np.angle(im_ifft),cmap='gray')
plt.title('ifft_phi')
plt.show()
plt.clf()

R_fft = np.fft.fft2(im_ifft)
plt.imshow(np.abs(R_fft),cmap='gray')
plt.title('R_fft_A')
plt.show()
plt.imshow(np.angle(R_fft),cmap='gray')
plt.title('R_fft_phi')
plt.show()

def H(fx, fy, z, wavelength=0.5):
    square_root = np.sqrt(np.complex(1) - (wavelength**2 * fx**2) - (wavelength**2 * fy**2))
    temp = np.exp(-1j * 2 * np.pi * z / wavelength * square_root)
    temp[np.isnan(temp)] = 0 # replace nan's with zeros
    return temp
fX, fY = np.meshgrid(fx,fx)
S = H(fX,fY, 10)

plt.imshow(np.abs(S),cmap='gray')
plt.title('S*_A')
plt.show()
plt.clf()
plt.imshow(np.angle(S),cmap='gray')
plt.title('S*_phi')
plt.show()
plt.clf()

R_ifft = np.fft.ifft2(S*R_fft)
plt.imshow(np.abs(R_ifft),cmap='gray')
plt.title('R_ifft_A')
plt.show()
plt.clf()
plt.imshow(np.angle(R_ifft),cmap='gray')
plt.title('R_ifft_phi')
plt.show()
plt.clf()
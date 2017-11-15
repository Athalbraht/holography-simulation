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

if len(sys.argv) >1:
    im = ic.change_type('{}'.format(sys.argv[1]), 'fft_test.png','L')
else:
    ############ TEST ###########
    im = np.ones((200,200))
    sp = int(im.shape[1]/2)
    for i in range(10):
        for j in range(10):
            im[sp+i][sp+j] = 0.7
    #im[13][9] = 0.9
    #############################

plt.imshow(im, interpolation='lanczos',cmap='gray')
plt.title('im')
plt.show()
plt.clf()

im_fft = np.fft.fft2(im)

plt.imshow(np.abs(im_fft), interpolation='lanczos',cmap='gray')
plt.title('fft_A')
plt.show()
plt.clf()

plt.imshow(np.angle(im_fft), interpolation='lanczos',cmap='gray')
plt.title('fft_phi')
plt.show()
plt.clf()

n = im_fft.shape
S = np.zeros(n)

for i in range(n[0]):
    for j in range(n[1]):
        S[i][j] = np.exp(0.055j*(i**2+j**2))
S[np.isnan(S)] = 0

plt.imshow(np.abs(S), interpolation='lanczos',cmap='gray')
plt.title('S_A')
plt.show()
plt.clf()
plt.imshow(np.angle(S), interpolation='lanczos',cmap='gray')
plt.title('S_phi')
plt.show()
plt.clf()


im_ifft = np.fft.ifft2(S*im_fft)
plt.imshow(np.abs(im_ifft)**2, interpolation='lanczos',cmap='gray')
plt.title('ifft_A')
plt.show()
plt.clf()
plt.imshow(np.angle(im_ifft), interpolation='lanczos',cmap='gray')
plt.title('ifft_phi')
plt.show()
plt.clf()

R_fft = np.fft.fft2(im_ifft)
plt.imshow(np.abs(R_fft), interpolation='lanczos',cmap='gray')
plt.title('R_fft_A')
plt.show()
plt.imshow(np.angle(R_fft), interpolation='lanczos',cmap='gray')
plt.title('R_fft_phi')
plt.show()

for i in range(n[0]):
    for j in range(n[1]):
        S[i][j] = np.exp(-0.055j*(i**2+j**2))
S[np.isnan(S)] = 0

plt.imshow(np.abs(S), interpolation='lanczos',cmap='gray')
plt.title('S*_A')
plt.show()
plt.clf()
plt.imshow(np.angle(S), interpolation='lanczos',cmap='gray')
plt.title('S*_phi')
plt.show()
plt.clf()

R_ifft = np.fft.ifft2(S*R_fft)
plt.imshow(np.abs(R_ifft), interpolation='lanczos',cmap='gray')
plt.title('R_ifft_A')
plt.show()
plt.clf()
plt.imshow(np.angle(R_ifft), interpolation='lanczos',cmap='gray')
plt.title('R_ifft_phi')
plt.show()
plt.clf()
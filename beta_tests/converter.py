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

im = ic.change_type('{}examples/cache/{}'.format(cp, sys.argv[1]), '{}examples/cache/g_{}'.format(cp, sys.argv[1]),'L')


n = im.shape[1]
print(n)
l = 0.9
a = 0.002
z = 10
p_size = 0.1
x = np.linspace(-p_size*n/2, p_size*n/2, num = n)
dx = x[1] - x[0]
fs = 1/dx
df = fs/n
f = np.arange(-fs/2, fs/2, step=df)
fx, fy = np.meshgrid(f,f)
p = prop.propagator(l, z, fx, fy)
print(p.shape)
#plt.imshow(np.angle(p),interpolation='lanczos',cmap='gray')

q1 = np.fft.ifftshift(np.fft.fft2(np.fft.fftshift(im)))
print(q1.shape)
q2 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(q1*p)))
print(q2.shape)
#_new = ft.FFT2Dc(im)

plt.imshow(np.abs(q2)**2,cmap='gray')
plt.savefig('{}/examples/cache/{}_holo.png'.format(cp,sys.argv[1][:-4]))
plt.show()
plt.clf()

zz=1
for i in range(400):
    z-=0.1
    p2 = prop.propagator(l,z,fx,fy)


    q3 = np.fft.ifftshift(np.fft.fft2(np.fft.fftshift(im)))
    print(q1.shape)
    q4 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(q3*p2)))
    print(q2.shape)
    plt.imshow(np.abs(q4),cmap='gray')
    plt.savefig('test/{}.png'.format(i))
    plt.clf()


import Holopy.Engine.propagator as prop
import Holopy.Engine.image_converter as im_conv
import numpy as np

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm


def render(_path, z, res, wavel,ss,n,dx,dx2):
    img = im_conv.convert_image(_path, 'L', (500,500))

    zn = prop.z_const(img, z)
    ss = prop.z_const(img, ss)
    #zn = random_s(img, 0.0002,0.002)
    holo = prop.holo_arr(img, zn, res, res, wavel)

    prop.save_holo(holo, '/home/anon/Desktop/holo.png', res)
    temp = 0.

    obj = prop.reholo_arr(holo, zn, res, res, wavel)
    prop.save_holo(obj, '/home/anon/Desktop/obj11.png', res, 'Reconstruct image')

    holo2, res2 = prop.holo_arr_s(img, ss,zn , res, res, wavel)
    obj,res3 = prop.reholo_arr_s(holo, ss,zn, res, res, wavel)
    prop.save_holo(holo, '/home/anon/Desktop/holo2.png', res2)
    prop.save_holo(obj, '/home/anon/Desktop/obj112.png', res3, 'Reconstruct image')
    print(res3)

    for i in range(10):
        img = im_conv.convert_image('/home/anon/Desktop/{}.png'.format(i), 'L', (28,28))
        holo = prop.holo_arr(img, zn, res, res, wavel)
        holo = norm(holo,0.,1.)
        im_conv.holo_to_png(holo**3,'/home/anon/Desktop/{}{}.png'.format(i,i))
    temp = []
    temp2 =[]
    temp3 = []
    z2=prop.z_const(img,0.001)
    z3= -zn*1.2
    dx2 = (2*(zn[1][1]*1.2))/(n+1)
    #for i in range(n):
       # obj = prop.reholo_arr(holo, z3, res, res, wavel)
       # yy = obj[int(holo.shape[1] / 2)]
      #  yy= list(yy)
      #  temp3.append(yy)
      #  z3 += dx2
   # temp3 = np.rot90(temp3)
   # plt.imshow(temp3,cmap='gray')
   # plt.show()
   # plt.clf()

    for i in range(n):
        holo = prop.holo_arr(img, z2, res, res, wavel)
        obj = prop.reholo_arr(holo, z2, res, res, wavel)
        xx = holo[int(holo.shape[1]/2)]
        yy = obj[int(holo.shape[1] / 2)]
        xx = list(xx)
        yy= list(yy)
        temp.append(xx)
        temp2.append(yy)
        z2 += dx
        if i%10==0:
            print(i)
    temp = np.array(temp)
    temp=np.rot90(temp)
    temp2 = np.array(temp2)
    temp2 = np.rot90(temp2)

    plt.imshow(temp,cmap='gray')
    plt.show()
    plt.clf()
    plt.imshow(temp2,cmap='gray')
    plt.show()
    return holo
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
    cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
    ax.set_xlabel('X')
    ax.set_xlim(-40, 40)
    ax.set_ylabel('Y')
    ax.set_ylim(-40, 40)
    ax.set_zlabel('Z')
    ax.set_zlim(-100, 100)
    plt.show()
def random_s(_obj, _min, _max):
    x, y = _obj.shape
    obj = np.random.rand(x,y)
    obj += -(np.min(obj))
    obj /= np.max(obj)/(_max - _min)
    obj += _min
    return obj

def norm(obj, _min, _max):
    x, y = obj.shape
    _obj = obj
    _obj += -(np.min(obj))
    _obj /= np.max(obj)/(_max - _min)
    _obj += _min
    return _obj

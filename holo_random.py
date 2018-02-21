import Holopy.Engine.propagator as prop
import Holopy.Engine.image_converter as im_conv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def render(_path, z, res, wavel):
    img = im_conv.convert_image(_path, 'L', (500,500))

    zn = random_s(img, 0.01, 0.05)
    holo = prop.holo_arr(img, zn, res, res, wavel)
    plot_3d(img,30)
    flat(img,30)

    prop.save_holo(holo, '/home/anon/Desktop/holo.png', res)
    obj = prop.reholo_arr(holo, zn, res, res, wavel)
    prop.save_holo(obj, '/home/anon/Desktop/obj2.png', res, 'Reconstruct image')

    return None

def random_s(_obj, _min, _max):
    x, y = _obj.shape
    obj = np.random.rand(x,y)
    obj += -(np.min(obj))
    obj /= np.max(obj)/(_max - _min)
    obj += _min
    return obj

def plot_3d(_obj,res):
    x = np.linspace(0,res,_obj.shape[1])
    X,Y = np.meshgrid(x, x)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, _obj, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_xlabel('X [mm]')
    ax.set_ylabel('Y [mm]')
    ax.set_zlabel('Z [mm]')
    plt.show()

def flat(_obj,res):
    plt.imshow(_obj, interpolation='lanczos')
    plt.xlabel('X [px]')
    plt.ylabel('Y [px]')
    plt.show()


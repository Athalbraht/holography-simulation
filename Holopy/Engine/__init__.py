__all__ = ['propagator', 'image_converter']


if __name__ == "__main__":
    import image_converter
    import propagator
    import numpy as np
    import os
    import subprocess as sp
    from sys import argv
    import matplotlib.pyplot as plt

    '''
    from sys import argv
    _object = image_converter.convert_image(argv[1], 'L')
    z = propagator.z_const(_object, float(argv[3]))

    hologram = propagator.holo_arr(_object, z, float(argv[4]), float(argv[4]), float(argv[5]))

    rhologram = propagator.reholo_arr(hologram, z, float(argv[4]), float(argv[4]), float(argv[5]))
    propagator.save_holo(hologram, argv[2], float(argv[4]))
    propagator.save_holo(rhologram, argv[2]+'.png', float(argv[4]), 'reconstruct')
    image_converter.holo_to_png(hologram, argv[2]+'x.png')
    '''
    path = argv[1]
    a= image_converter.convert_image('{}'.format(path),'L', (200 ,200) )
    b = propagator.holo_arr(a, propagator.z_const(a,0.08 ), 0.002, 0.002, 500e-9)
    temp = np.zeros((200, a.shape[0]))
    z0= 0.001
    for i in range(200):
        b = propagator.holo_arr(a, propagator.z_const(a,z0), 0.002,0.002, 500e-9 )
        z0 += 0.001
        temp[i] = b[70]
    propagator.save_holo(b, 'x.png',10 )
    c = propagator.holo_arr(b,propagator .z_const(a,1.2), 0.002,0.002, 500e-9)
    propagator.save_holo(c,'y.png',10 )
    plt .imshow(temp,cmap='gray' )
    plt.show()

    '''
    folders = [ sp.check_output('ls {}/{}/'.format(path,i),shell=True).split() for i in range(10) ]
    for i, folder in enumerate(folders):
        os.system('mkdir {}/{}_holo'.format(path, i))
        for j, item in enumerate(folder):
            a=image_converter.convert_image('{}/{}/{}'.format(path, i, item.decode()),'L',(28,28))
            b = propagator.holo_arr(a,propagator.z_const(a,0.74), 0.0032,0.0032,500e-9)
            image_converter.holo_to_png(b,'{}/{}_holo/{}.png'.format(path, i, j))
     '''







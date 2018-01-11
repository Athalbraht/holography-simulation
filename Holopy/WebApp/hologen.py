import sys

cp = sys.argv[0][:-19]
sys.path.insert(0,cp)

from Engine import *


def get_holo(path, new_path,new2_path, zz, res, wave):
    _object = image_converter.convert_image(path,'L', (500,500))
    z = propagator.z_const(_object, zz)
    hologram = propagator.holo_arr(_object, z, res, res, wave)
    ##Optimal params
    #size2 = _object.shape[0]*_object.shape[1]
    #_z = 2*size2/(wave*)
    ##
    rehologram = propagator.reholo_arr(hologram, z, res, res, wave)
    propagator.save_holo(hologram, new_path, res)
    propagator.save_holo(rehologram, new2_path, res, 'Reconstruct')

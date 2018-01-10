import os
import sys

cp = os.getcwd()
sys.path.insert(0,cp)

from Engine import *


def get_holo(path, new_path,new2_path, zz, res, wave):
    _object = image_converter.convert_image(path)
    z = propagator.z_const(_object, zz)
    hologram = propagator.holo_arr(_object, z, res, res, wave)
    rehologram = propagator.reholo_arr(hologram, z, res, res, wave)
    propagator.save_holo(hologram, new_path, res)
    propagator.save_holo(rehologram, new2_path, res, 'Reconstruct')
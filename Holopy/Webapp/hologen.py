from Holopy.Engine import *

def get_holo(path, new_path,new2_path, zz, res, wave, sph,z0):
    _object = image_converter.convert_image(path,'L', (500,500))
    z = propagator.z_const(_object, zz)
    res2 = res
    if sph=='Spherical waves':
        res2 = zz*res/(z0) + res
    hologram = propagator.holo_arr(_object, z, res, res, wave)
    rehologram = propagator.reholo_arr(hologram, z, res, res, wave)
    propagator.save_holo(hologram, new_path, res2)
    propagator.save_holo(rehologram, new2_path, res, 'Reconstruct')
    return None

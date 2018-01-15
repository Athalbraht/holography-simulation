

__all__ = ['propagator', 'image_converter']

if __name__ == "__main__":
    import image_converter
    import propagator
    import numpy as np
    from sys import argv
    _object = image_converter.convert_image(argv[1], 'L')
    z = propagator.z_const(_object, float(argv[3]))
    
    hologram = propagator.holo_arr(_object, z, float(argv[4]), float(argv[4]), float(argv[5]))
    
    rhologram = propagator.reholo_arr(hologram, z, float(argv[4]), float(argv[4]), float(argv[5]))
    propagator.save_holo(hologram, argv[2], float(argv[4]))
    propagator.save_holo(rhologram, argv[2]+'.png', float(argv[4]), 'reconstruct')
    image_converter.holo_to_png(hologram, argv[2]+'x.png')





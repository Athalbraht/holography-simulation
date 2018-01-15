import numpy as np
import sys
import subprocess
cp = sys.argv[0][:-19]
sys.path.insert(0,cp)
from Engine import *


def generate_dataset(path, zz, ar, w ):
    for folder in range(10):
        with open('{}/{}.data'.format(path, folder),'w') as sample:
            n = subprocess.check_output('ls {}/{}/'.format(path, folder), shell=True).decode().split('\n')
            for file in range(len(n)-2):
                _object = image_converter.convert_image('{}/{}/{}'.format(path, folder, n[file]), 'L')
                z = propagator.z_const(_object, zz)
                hologram = propagator.holo_arr(_object, z, ar, ar, w)
                #propagator.save_holo(hologram, 'x.png', ar)
                data = hologram.flatten()
                for i in data:
                    sample.write('{} '.format(i))
                sample.write('\n')
                #print(n[file])
                print('{}/{}'.format(file, len(n)))

def generate_dataset_png(path, zz, ar, w ):
    for folder in range(10):

        n = subprocess.check_output('ls {}/{}/'.format(path, folder), shell=True).decode().split('\n')
        for file in range(len(n)-2):
            _object = image_converter.convert_image('{}/{}/{}'.format(path, folder, n[file]), 'L')
            z = propagator.z_const(_object, zz)
            hologram = propagator.holo_arr(_object, z, ar, ar, w)
            #propagator.save_holo(hologram, 'x.png', ar)
            image_converter.holo_to_png(hologram, '{}/{}/{}.png'.format(path, str(folder)+'_holo', file))
            print('{}/{}'.format(file, len(n)))

def generate_dataset_bin(path, zz, ar, w ):
    for folder in range(10):
        with open('{}/{}.bin'.format(path, folder),'wb') as sample:
            n = subprocess.check_output('ls {}/{}/'.format(path, folder), shell=True).decode().split('\n')
            for file in range(len(n)-2):
                _object = image_converter.convert_image('{}/{}/{}'.format(path, folder, n[file]), 'L')
                z = propagator.z_const(_object, zz)
                hologram = propagator.holo_arr(_object, z, ar, ar, w)
                #propagator.save_holo(hologram, 'x.png', ar)
                data = hologram.flatten()
                for i in data:
                    tmp = '{} '.format(i)
                    sample.write(tmp.encode())
                sample.write('\n'.encode())
                print(n[file])
                print('{}/{}'.format(file, len(n)))







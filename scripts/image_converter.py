from PIL import Image
import numpy as np

def change_type(path,new_path,_type):
    image = Image.open(path)
    _image = image.convert(_type)
    #:_image.save(new_path)
    pixels = _image.load()
    
    im_to_arr = np.zeros(_image.size)
    I = np.ones(_image.size)

    for i in range(im_to_arr.shape[0]):
        for j in range(im_to_arr.shape[1]):
            im_to_arr[i][j] = float(pixels[i,j])

    _object =  (im_to_arr - np.min(im_to_arr))/(np.max(im_to_arr) - np.min(im_to_arr))
    
    return _object





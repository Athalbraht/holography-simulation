import numpy as np
from PIL import Image

def convert_image(path, _type='L', size=(500,500)):
    image = Image.open(path)
    image.thumbnail(size)
    image = image.convert(_type)#default convert to grayscale

    pixels = image.load()#getting pixels data

    px_array = np.zeros(image.size)

    #rewriting pixels values to array
    for i in range(px_array.shape[0]):
        for j in range(px_array.shape[1]):
            px_array[i][j] = float(pixels[i,j])

    #normalization
    _object = (px_array - np.min(px_array))/(np.max(px_array) - np.min(px_array))
    I = np.ones(size)
    #_object = I - _object
    return _object




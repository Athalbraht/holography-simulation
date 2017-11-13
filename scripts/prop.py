import numpy as np

def propagator(l, z, fx, fy):
    sq = np.sqrt(np.complex(1)- (l**2 * fx**2)-(l**2 * fy**2))
    temp = np.exp(1j * 2 * np.pi * z/l *sq)
    temp[np.isnan(temp)] = 0
    return temp

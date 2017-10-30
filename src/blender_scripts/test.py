import bpy

object = bpy.data.objects['Suzanne']
radius = 2.0
resolution = 30
file = open("/home/anon/Desktop/test.txt", 'w')

import mathutils
from mathutils import Vector
def pointInsideMesh(point,ob):
    axes = [ mathutils.Vector((1,0,0)) ]
    outside = False
    for axis in axes:
        mat = ob.matrix_world
        mat.invert()
        orig = mat*point
        count = 0
        while True:
            dd,location,normal,index = ob.ray_cast(orig,orig+axis*10000.0)
            if index == -1: break
            count += 1
            orig = location + axis*0.00001
        if count%2 == 0:
            outside = True
            break
    return not outside

bla = radius/resolution

out = ""

for z in range(-resolution, resolution):
    for y in range(-resolution, resolution):
        for x in range(-resolution, resolution):
            loc = Vector((x*bla, y*bla, z*bla))
            print(loc)
            if(pointInsideMesh(loc, object) == True):
                out += '1'
            else:
                out += '0'
        out += '\n'
    out += '\n'
file.write(out)
file.close()

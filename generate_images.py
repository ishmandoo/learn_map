import bpy
import mathutils
import random
import math
import pickle

#running blender headless
#blender -b -P /Users/Jenny/Desktop/my_script.py

#bpy.ops.wm.open_mainfile(filepath="file_path")

print("starting")
pi = math.pi

cam = bpy.data.objects['Camera']
path = "/home/ben/jects/learn_map/blenderpics/"

positions = []

def renderImage(name):
    scene = bpy.data.scenes['Scene']
    bpy.data.scenes['Scene'].render.filepath = path + str(name) + ".jpg"
    scene.render.resolution_x = 128
    scene.render.resolution_y = 128

    #bpy.ops.render.render( write_still=True )
    #opengl render looks like crap but is waaayyyyyyy faster
    bpy.ops.render.opengl(write_still=True)


for i in range(1000):
    x_pos = 0.0 + random.uniform(-5,5)
    cam.location = mathutils.Vector((x_pos, -10.0, 3.5))
    positions.append(x_pos)

    renderImage(i)


pickle.dump( positions, open( "positions.p", "wb" ) )
print("done")

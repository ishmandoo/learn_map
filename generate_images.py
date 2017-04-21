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
path = "/home/ben/projects/learn_map/blenderpics/"

positions = []

def renderImage(name):
    scene = bpy.data.scenes['Scene']
    bpy.data.scenes['Scene'].render.filepath = path + str(name) + ".jpg"
    scene.render.resolution_x = 64
    scene.render.resolution_y = 64

    #bpy.ops.render.render( write_still=True )
    #opengl render looks like crap but is waaayyyyyyy faster
    bpy.ops.render.opengl(write_still=True)


for i in range(1000):
    y_pos = 0.0 + random.uniform(-2,2)
    cam.location = mathutils.Vector((0.0, y_pos, 2.0))
    positions.append(y_pos)

    renderImage(i)


pickle.dump( positions, open( "positions.p", "wb" ) )
print("done")

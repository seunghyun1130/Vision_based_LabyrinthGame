import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram,compileShader
import numpy as np
import pyrr
import pywavefront as pwf
from assets import *

pg.init()
window_width = 600
window_height = 600
pg.display.set_mode((window_width,window_height),pg.OPENGL|pg.DOUBLEBUF)
clock = pg.time.Clock()

glClearColor(0,0.0,0.0,1)

with open("shaders/vertex.txt",'r') as f:
    vertex_src = f.readlines()
with open("shaders/fragment.txt",'r') as f:
    fragment_src = f.readlines()
shader = compileProgram(compileShader(vertex_src,GL_VERTEX_SHADER),
                        compileShader(fragment_src,GL_FRAGMENT_SHADER))
glUseProgram(shader)

#get a handle to the rotation matrix from the shader
MODEL_LOC = glGetUniformLocation(shader,"model")
VIEW_LOC = glGetUniformLocation(shader,"view")
PROJ_LOC = glGetUniformLocation(shader,"projection")
LIGHT_LOC = glGetUniformLocation(shader,"lightPos")

glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_CULL_FACE)

########################MODELS######################################
BOARD_MODEL = ObjModel("models/large_board.obj")
WALL_MODEL = ObjModel("models/wall.obj")
BALL_MODEL = ObjModel("models/ball.obj")
########################TEXTURES####################################
BOARD = Texture("textures/white.png")
WALL = Texture("textures/black_wall.png")
BALL = Texture("textures/ball.png")

####################################################################

#(field of view, aspect ratio,near,far)
camera_distance = 45
Rendering_distance = 720*20
aspect_width = 600
aspect_height = 600

cameraPos = pyrr.Vector3([0,0,450*2])
up = pyrr.Vector3([0.0,1.0,0.0]) 
cameraRight = pyrr.vector.normalise(pyrr.vector3.cross(up, cameraPos))
cameraUp = pyrr.vector3.cross(cameraPos, cameraRight)
viewMatrix = pyrr.matrix44.create_look_at(cameraPos, pyrr.Vector3([0,0,0]), cameraUp)
projection = pyrr.matrix44.create_perspective_projection_matrix(camera_distance,aspect_width/aspect_height,320,Rendering_distance)
glUniformMatrix4fv(PROJ_LOC,1,GL_FALSE,projection)
glUniformMatrix4fv(VIEW_LOC,1,GL_FALSE,viewMatrix)

lightPosition = pyrr.Vector3([0.0,0.0,0.0])
glUniform3f(LIGHT_LOC,0.0,0.0,450.0*1.75) #Light at top center of the board
#glUniform3f(LIGHT_LOC,-400.0,200.0,300.0)
# /*******************************************************************************************
# *
# *   raylib [shaders] example - basic lighting
# *
# *   NOTE: This example requires raylib OpenGL 3.3 or ES2 versions for shaders support,
#     *         OpenGL 1.1 does not support shaders, recompile raylib to OpenGL 3.3 version.
# *
# *   NOTE: Shaders used in this example are #version 330 (OpenGL 3.3).
# *
# *   This example has been created using raylib 2.5 (www.raylib.com)
# *   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# *
# *   Example contributed by Chris Camacho (@codifies) and reviewed by Ramon Santamaria (@raysan5)
# *
# *   Chris Camacho (@codifies -  http://bedroomcoders.co.uk/) notes:
# *
# *   This is based on the PBR lighting example, but greatly simplified to aid learning...
# *   actually there is very little of the PBR example left!
# *   When I first looked at the bewildering complexity of the PBR example I feared
# *   I would never understand how I could do simple lighting with raylib however its
# *   a testement to the authors of raylib (including rlights.h) that the example
# *   came together fairly quickly.
# *
# *   Copyright (c) 2019 Chris Camacho (@codifies) and Ramon Santamaria (@raysan5)
# *
# ********************************************************************************************/

from raylib.static import *
from dataclasses import dataclass
from enum import Enum
from typing import Any
import math




def MatrixRotateX(angle):
    result = MatrixIdentity();

    cosres = math.cos(angle);
    sinres = math.sin(angle);

    result.m5 = cosres;
    result.m6 = -sinres;
    result.m9 = sinres;
    result.m10 = cosres;

    return result;



def MatrixRotateY(angle):
    result = MatrixIdentity()

    cosres = math.cos(angle);
    sinres = math.sin(angle);

    result.m0 = cosres;
    result.m2 = sinres;
    result.m8 = -sinres;
    result.m10 = cosres;

    return result;


def MatrixIdentity():
    result = ffi.new("struct Matrix *",[ 1.0, 0.0, 0.0, 0.0,0.0, 1.0, 0.0, 0.0,    0.0, 0.0, 1.0, 0.0,   0.0, 0.0, 0.0, 1.0 ])
    return result



def MatrixRotateZ(angle):
    result = MatrixIdentity();

    cosres = math.cos(angle);
    sinres = math.sin(angle);

    result.m0 = cosres;
    result.m1 = -sinres;
    result.m4 = sinres;
    result.m5 = cosres;

    return result


def MatrixMultiply(left,  right):
    result = ffi.new("struct Matrix *")
    result.m0 = left.m0*right.m0 + left.m1*right.m4 + left.m2*right.m8 + left.m3*right.m12;
    result.m1 = left.m0*right.m1 + left.m1*right.m5 + left.m2*right.m9 + left.m3*right.m13;
    result.m2 = left.m0*right.m2 + left.m1*right.m6 + left.m2*right.m10 + left.m3*right.m14;
    result.m3 = left.m0*right.m3 + left.m1*right.m7 + left.m2*right.m11 + left.m3*right.m15;
    result.m4 = left.m4*right.m0 + left.m5*right.m4 + left.m6*right.m8 + left.m7*right.m12;
    result.m5 = left.m4*right.m1 + left.m5*right.m5 + left.m6*right.m9 + left.m7*right.m13;
    result.m6 = left.m4*right.m2 + left.m5*right.m6 + left.m6*right.m10 + left.m7*right.m14;
    result.m7 = left.m4*right.m3 + left.m5*right.m7 + left.m6*right.m11 + left.m7*right.m15;
    result.m8 = left.m8*right.m0 + left.m9*right.m4 + left.m10*right.m8 + left.m11*right.m12;
    result.m9 = left.m8*right.m1 + left.m9*right.m5 + left.m10*right.m9 + left.m11*right.m13;
    result.m10 = left.m8*right.m2 + left.m9*right.m6 + left.m10*right.m10 + left.m11*right.m14;
    result.m11 = left.m8*right.m3 + left.m9*right.m7 + left.m10*right.m11 + left.m11*right.m15;
    result.m12 = left.m12*right.m0 + left.m13*right.m4 + left.m14*right.m8 + left.m15*right.m12;
    result.m13 = left.m12*right.m1 + left.m13*right.m5 + left.m14*right.m9 + left.m15*right.m13;
    result.m14 = left.m12*right.m2 + left.m13*right.m6 + left.m14*right.m10 + left.m15*right.m14;
    result.m15 = left.m12*right.m3 + left.m13*right.m7 + left.m14*right.m11 + left.m15*right.m15;

    return result


#//----------------------------------------------------------------------------------
#// Types and Structures Definition
#//----------------------------------------------------------------------------------

MAX_LIGHTS = 4         #// Max dynamic lights supported by shader
lightsCount = 0

#// Light type

LIGHT_DIRECTIONAL=0
LIGHT_POINT=1


class Light:
    def __init__(self, type,  position,  target, color,  shader):
        global lightsCount
        if lightsCount >= MAX_LIGHTS:
            raise Exception("Too many lights")
        self.enabled = True
        self.type = type
        self.position = position
        self.target = target
        self.color = color
        self.shader = shader

        #// TODO: Below code doesn't look good to me,
        #                        // it assumes a specific shader naming and structure
        #                                                       // Probably this implementation could be improved
        self.enabledName = f"lights[{lightsCount}].enabled"
        self.typeName = f"lights[{lightsCount}].type"
        self.posName = f"lights[{lightsCount}].position"
        self.targetName = f"lights[{lightsCount}].target"
        self.colorName = f"lights[{lightsCount}].color"
        # enabledName = '0' + str(lightsCount)
        # typeName = '0' + str(lightsCount)
        # posName = '0' + str(lightsCount)
        # targetName = '0' + str(lightsCount)
        # colorName = '0' + str(lightsCount)

        self.enabledLoc = GetShaderLocation(shader, self.enabledName.encode('utf-8'))
        self.typeLoc = GetShaderLocation(shader, self.typeName.encode('utf-8'))
        self.posLoc = GetShaderLocation(shader, self.posName.encode('utf-8'))
        self.targetLoc = GetShaderLocation(shader, self.targetName.encode('utf-8'))
        self.colorLoc = GetShaderLocation(shader, self.colorName.encode('utf-8'))

        self.UpdateLightValues()

        lightsCount += 1

#// Send light properties to shader
#                            // NOTE: Light shader locations should be available
    def UpdateLightValues(self):
        #// Send to shader light enabled state and type
        SetShaderValue(shader, self.enabledLoc, ffi.new("int *",self.enabled), UNIFORM_INT)
        SetShaderValue(shader, self.typeLoc, ffi.new("int *",self.type), UNIFORM_INT)

        #// Send to shader light position values
        position = [ self.position.x, self.position.y, self.position.z]
        SetShaderValue(shader, self.posLoc, ffi.new("struct Vector3 *",position), UNIFORM_VEC3)

        #// Send to shader light target position values
        target =[  self.target.x, self.target.y, self.target.z ]
        SetShaderValue(shader, self.targetLoc, ffi.new("struct Vector3 *",target), UNIFORM_VEC3)

        #// Send to shader light color values
        color = [self.color[0]/255.0, self.color[1]/255.0,  self.color[2]/255.0, self.color[3]/255.0]
        SetShaderValue(shader, self.colorLoc, ffi.new("struct Vector4 *",color), UNIFORM_VEC4)



def Vector3Zero():
    return ffi.new("struct Vector3 *",[ 0, 0, 0])

#// Initialization
#//--------------------------------------------------------------------------------------
screenWidth = 800;
screenHeight = 450;

SetConfigFlags(FLAG_MSAA_4X_HINT);  # Enable Multi Sampling Anti Aliasing 4x (if available)
InitWindow(screenWidth, screenHeight, b"raylib [shaders] example - basic lighting")

#// Define the camera to look into our 3d world
cameraPtr = ffi.new("struct Camera3D *")
camera = cameraPtr[0]
camera.position = [ 2.0, 2.0, 6.0 ] #    // Camera position
camera.target = [ 0.0, 0.5, 0.0]#      // Camera looking at point
camera.up = [ 0.0, 1.0, 0.0]#          // Camera up vector (rotation towards target)
camera.fovy = 45.0 #                                // Camera field-of-view Y
camera.type = CAMERA_PERSPECTIVE #                   // Camera mode type

                                                                   #// Load models
modelA = LoadModelFromMesh(GenMeshTorus(0.4, 1.0, 16, 32))
modelB = LoadModelFromMesh(GenMeshCube(1.0, 1.0, 1.0))
modelC = LoadModelFromMesh(GenMeshSphere(0.5, 32, 32))

#// Load models texture
texture = LoadTexture(b"resources/texel_checker.png")

#// Assign texture to default model material
modelA.materials[0].maps[MAP_DIFFUSE].texture = texture
modelB.materials[0].maps[MAP_DIFFUSE].texture = texture
modelC.materials[0].maps[MAP_DIFFUSE].texture = texture

shader = LoadShader(b"resources/shaders/glsl330/basic_lighting.vs",
                        b"resources/shaders/glsl330/basic_lighting.fs");

#// Get some shader loactions
shader.locs[LOC_MATRIX_MODEL] = GetShaderLocation(shader, b"matModel");
shader.locs[LOC_VECTOR_VIEW] = GetShaderLocation(shader, b"viewPos");

#// ambient light level
ambientLoc = GetShaderLocation(shader, b"ambient");
v = ffi.new("struct Vector4 *", [ 0.2, 0.2, 0.2, 1.0 ])
SetShaderValue(shader, ambientLoc, v, UNIFORM_VEC4);



angle = 6.282;

#// All models use the same shader
modelA.materials[0].shader = shader
modelB.materials[0].shader = shader
modelC.materials[0].shader = shader

#// Using 4 point lights, white, red, green and blue
lights = [0] * 4
#lights[0] = Light(LIGHT_POINT,  ffi.new("struct Vector3 *",[ 400, 400, 400 ]), Vector3Zero(), WHITE, shader)
lights[0] = Light(LIGHT_POINT,  ffi.new("struct Vector3 *",[ 4, 2, 4 ]), Vector3Zero(), WHITE, shader)
lights[1] = Light(LIGHT_POINT, ffi.new("struct Vector3 *",[4, 2, 4 ]), Vector3Zero(), RED, shader)
lights[2] = Light(LIGHT_POINT, ffi.new("struct Vector3 *",[ 0, 4, 2 ]), Vector3Zero(), GREEN, shader)
lights[3] = Light(LIGHT_POINT, ffi.new("struct Vector3 *",[ 0, 4, 2 ]), Vector3Zero(), BLUE, shader)

SetCameraMode(camera, CAMERA_ORBITAL) #// Set an orbital camera mode

SetTargetFPS(60)                      # // Set our game to run at 60 frames-per-second
#//--------------------------------------------------------------------------------------

#// Main game loop
while not WindowShouldClose():            #// Detect window close button or ESC key
    #// Update
    #//----------------------------------------------------------------------------------
    if IsKeyPressed(KEY_W):  lights[0].enabled = not lights[0].enabled
    if IsKeyPressed(KEY_R):  lights[1].enabled = not lights[1].enabled
    if IsKeyPressed(KEY_G):  lights[2].enabled = not lights[2].enabled
    if IsKeyPressed(KEY_B):  lights[3].enabled = not lights[3].enabled

    UpdateCamera(cameraPtr);              #// Update camera

    #// Make the lights do differing orbits
    angle -= 0.02
    lights[0].position.x = math.cos(angle)*4.0
    lights[0].position.z = math.sin(angle)*4.0
    lights[1].position.x = math.cos(-angle*0.6)*4.0
    lights[1].position.z = math.sin(-angle*0.6)*4.0
    lights[2].position.y = math.cos(angle*0.2)*4.0
    lights[2].position.z = math.sin(angle*0.2)*4.0
    lights[3].position.y = math.cos(-angle*0.35)*4.0
    lights[3].position.z = math.sin(-angle*0.35)*4.0

    lights[0].UpdateLightValues()
    lights[1].UpdateLightValues()
    lights[2].UpdateLightValues()
    lights[3].UpdateLightValues()


    #// Rotate the torus

    modelA.transform = MatrixMultiply(modelA.transform, MatrixRotateX(-0.025))[0]
    modelA.transform = MatrixMultiply(modelA.transform, MatrixRotateZ(0.012))[0]



    #// Update the light shader with the camera view position
    cameraPos = [ camera.position.x, camera.position.y, camera.position.z ]
    SetShaderValue(shader, shader.locs[LOC_VECTOR_VIEW], ffi.new("struct Vector3 *",cameraPos), UNIFORM_VEC3)
    #//----------------------------------------------------------------------------------

    #// Draw
    #//----------------------------------------------------------------------------------
    BeginDrawing()

    ClearBackground(RAYWHITE)

    BeginMode3D(camera)

    #// Draw the three models
    DrawModel(modelA, [0,0,0], 1.0, WHITE)
    DrawModel(modelB, [-1.6,0,0], 1.0, WHITE)
    DrawModel(modelC, [ 1.6,0,0], 1.0, WHITE)

    #// Draw markers to show where the lights are
    if lights[0].enabled: DrawSphereEx(lights[0].position[0], 0.2, 8, 8, WHITE)
    if lights[1].enabled: DrawSphereEx(lights[1].position[0], 0.2, 8, 8, RED)
    if lights[2].enabled: DrawSphereEx(lights[2].position[0], 0.2, 8, 8, GREEN)
    if lights[3].enabled: DrawSphereEx(lights[3].position[0], 0.2, 8, 8, BLUE)

    DrawGrid(10, 1.0)

    EndMode3D()

    DrawFPS(10, 10)

    DrawText(b"Keys RGB & W toggle lights", 10, 30, 20, DARKGRAY)

    EndDrawing()
#//----------------------------------------------------------------------------------


#// De-Initialization
#//--------------------------------------------------------------------------------------
UnloadModel(modelA) #        // Unload the modelA
UnloadModel(modelB) #        // Unload the modelB
UnloadModel(modelC) #        // Unload the modelC

UnloadTexture(texture)     #// Unload the texture
UnloadShader(shader)       #// Unload shader

CloseWindow();              #// Close window and OpenGL context

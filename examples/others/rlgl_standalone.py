#*******************************************************************************************
#
#   raylib [rlgl] example - Using rlgl module as standalone module
#
#   rlgl library is an abstraction layer for multiple OpenGL versions (1.1, 2.1, 3.3 Core, ES 2.0)
#   that provides a pseudo-OpenGL 1.1 immediate-mode style API (rlVertex, rlTranslate, rlRotate...)
#
#   WARNING: This example is intended only for PLATFORM_DESKTOP and OpenGL 3.3 Core profile.
#       It could work on other platforms if redesigned for those platforms (out-of-scope)
#
#   DEPENDENCIES:
#       glfw3     - Windows and context initialization library
#       rlgl.h    - OpenGL abstraction layer to OpenGL 1.1, 3.3 or ES2
#       glad.h    - OpenGL extensions initialization library (required by rlgl)
#       raymath.h - 3D math library
#
#   WINDOWS COMPILATION:
#       gcc -o rlgl_standalone.exe rlgl_standalone.c -s -Iexternal\include -I..\..\src  \
#           -L. -Lexternal\lib -lglfw3 -lopengl32 -lgdi32 -Wall -std=c99 -DGRAPHICS_API_OPENGL_33
#
#   APPLE COMPILATION:
#       gcc -o rlgl_standalone rlgl_standalone.c -I../../src -Iexternal/include -Lexternal/lib \
#           -lglfw3 -framework CoreVideo -framework OpenGL -framework IOKit -framework Cocoa
#           -Wno-deprecated-declarations -std=c99 -DGRAPHICS_API_OPENGL_33
#
#
#   LICENSE: zlib/libpng
#
#   This example is licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#   BSD-like license that allows static linking with closed source software:
#
#   Copyright (c) 2014-2023 Ramon Santamaria (@raysan5)
#
#   This software is provided "as-is", without any express or implied warranty. In no event
#   will the authors be held liable for any damages arising from the use of this software.
#
#   Permission is granted to anyone to use this software for any purpose, including commercial
#   applications, and to alter it and redistribute it freely, subject to the following restrictions:
#
#     1. The origin of this software must not be misrepresented you must not claim that you
#     wrote the original software. If you use this software in a product, an acknowledgment
#     in the product documentation would be appreciated but is not required.
#
#     2. Altered source versions must be plainly marked as such, and must not be misrepresented
#     as being the original software.
#
#     3. This notice may not be removed or altered from any source distribution.
#
#*******************************************************************************************/

# NOTE: rlgl can be configured just re-defining the following values:
# define RL_DEFAULT_BATCH_BUFFER_ELEMENTS   8192    # Default internal render batch elements limits
# define RL_DEFAULT_BATCH_BUFFERS              1    # Default number of batch buffers (multi-buffering)
# define RL_DEFAULT_BATCH_DRAWCALLS          256    # Default number of batch draw calls (by state changes: mode, texture)
# define RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS    4    # Maximum number of textures units that can be activated on batch drawing (SetShaderValueTexture())
# define RL_MAX_MATRIX_STACK_SIZE             32    # Maximum size of internal Matrix stack
# define RL_MAX_SHADER_LOCATIONS              32    # Maximum number of shader locations supported
# define RL_CULL_DISTANCE_NEAR              0.01    # Default projection matrix near cull distance
# define RL_CULL_DISTANCE_FAR             1000.0    # Default projection matrix far cull distance

import sys
import dataclasses
import pyray
from raylib import ffi, rl
from raylib.defines import (
    GLFW_TRUE,
    GLFW_SAMPLES, GLFW_DEPTH_BITS, GLFW_CONTEXT_VERSION_MAJOR, GLFW_CONTEXT_VERSION_MINOR, GLFW_OPENGL_PROFILE,
    GLFW_OPENGL_CORE_PROFILE, GLFW_OPENGL_FORWARD_COMPAT, RL_PROJECTION, RL_MODELVIEW, DEG2RAD, RL_LINES, RL_TRIANGLES,
    GLFW_KEY_ESCAPE, GLFW_PRESS,
)
from raylib.colors import (
    RAYWHITE,
    RED,
    DARKGRAY
)

#----------------------------------------------------------------------------------
# Structures Definition
#----------------------------------------------------------------------------------
# Color, 4 components, R8G8B8A8 (32bit)
@dataclasses.dataclass
class Color:
    r: int
    g: int
    b: int
    a: int


# Camera type, defines a camera position/orientation in 3d space
@dataclasses.dataclass
class Camera:
    position: pyray.Vector3       # Camera position
    target: pyray.Vector3         # Camera target it looks-at
    up: pyray.Vector3             # Camera up vector (rotation over its axis)
    fovy: float             # Camera field-of-view apperture in Y (degrees) in perspective, used as near plane width in orthographic
    projection: int         # Camera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC


#----------------------------------------------------------------------------------
# Module specific Functions Declaration
#----------------------------------------------------------------------------------
# static void ErrorCallback(int error, const char *description)
# static void KeyCallback(GLFWwindow *window, int key, int scancode, int action, int mods)

# Drawing functions (uses rlgl functionality)
# static void DrawGrid(int slices, float spacing)
# static void DrawCube(Vector3 position, float width, float height, float length, Color color)
# static void DrawCubeWires(Vector3 position, float width, float height, float length, Color color)
# static void DrawRectangleV(Vector2 position, Vector2 size, Color color)

# NOTE: We use raymath to get this functionality but it could be implemented in this module
#static Matrix MatrixIdentity(void)
#static Matrix MatrixOrtho(double left, double right, double bottom, double top, double near, double far)
#static Matrix MatrixPerspective(double fovy, double aspect, double near, double far)
#static Matrix MatrixLookAt(Vector3 eye, Vector3 target, Vector3 up)


# GLFW3: Error callback
@ffi.callback("void(int, const char *)")
def ErrorCallback(error: int, description: bytes):
    print("%s" % description, file=sys.stderr)


# GLFW3: Keyboard callback
@ffi.callback("void(GLFWwindow *, int, int, int, int)")
def KeyCallback(window: 'GLFWwindow', key: int, scancode: int, action: int, mods: int):
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        rl.glfwSetWindowShouldClose(window, GLFW_TRUE)


# Draw rectangle using rlgl OpenGL 1.1 style coding (translated to OpenGL 3.3 internally)
def DrawRectangleV(position: 'raylib.Vector2', size: 'raylib.Vector2', color: Color):
    rl.rlBegin(RL_TRIANGLES)
    rl.rlColor4ub(color.r, color.g, color.b, color.a)
    rl.rlVertex2f(position.x, position.y)
    rl.rlVertex2f(position.x, position.y + size.y)
    rl.rlVertex2f(position.x + size.x, position.y + size.y)
    rl.rlVertex2f(position.x, position.y)
    rl.rlVertex2f(position.x + size.x, position.y + size.y)
    rl.rlVertex2f(position.x + size.x, position.y)
    rl.rlEnd()


# Draw a grid centered at (0, 0, 0)
def DrawGrid(slices: int, spacing: float):
    half_slices = slices // 2

    rl.rlBegin(RL_LINES)
    for i in range(half_slices * -1, half_slices+1):
        if i == 0:
            rl.rlColor3f(0.5, 0.5, 0.5)
            rl.rlColor3f(0.5, 0.5, 0.5)
            rl.rlColor3f(0.5, 0.5, 0.5)
            rl.rlColor3f(0.5, 0.5, 0.5)
        else:
            rl.rlColor3f(0.75, 0.75, 0.75)
            rl.rlColor3f(0.75, 0.75, 0.75)
            rl.rlColor3f(0.75, 0.75, 0.75)
            rl.rlColor3f(0.75, 0.75, 0.75)

        rl.rlVertex3f(float(i)*spacing, 0.0, float(half_slices)*-1.0*spacing)
        rl.rlVertex3f(float(i)*spacing, 0.0, float(half_slices)*spacing)

        rl.rlVertex3f(float(half_slices)*-1.0*spacing, 0.0, float(i)*spacing)
        rl.rlVertex3f(float(half_slices)*spacing, 0.0, float(i)*spacing)
    rl.rlEnd()


# Draw cube
# NOTE: Cube position is the center position
def DrawCube(position: 'raylib.Vector3', width: float, height: float, length: float, color: Color):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    rl.rlPushMatrix()


    # NOTE: Be careful! Function order matters (rotate -> scale -> translate)
    rl.rlTranslatef(position.x, position.y, position.z)
    #rlScalef(2.0f, 2.0f, 2.0f)
    #rlRotatef(45, 0, 1, 0)

    rl.rlBegin(RL_TRIANGLES)
    rl.rlColor4ub(color.r, color.g, color.b, color.a)

    # Front Face -----------------------------------------------------
    rl.rlVertex3f(x-width/2, y-height/2, z+length/2)  # Bottom Left
    rl.rlVertex3f(x+width/2, y-height/2, z+length/2)  # Bottom Right
    rl.rlVertex3f(x-width/2, y+height/2, z+length/2)  # Top Left

    rl.rlVertex3f(x+width/2, y+height/2, z+length/2)  # Top Right
    rl.rlVertex3f(x-width/2, y+height/2, z+length/2)  # Top Left
    rl.rlVertex3f(x+width/2, y-height/2, z+length/2)  # Bottom Right

    # Back Face ------------------------------------------------------
    rl.rlVertex3f(x-width/2, y-height/2, z-length/2)  # Bottom Left
    rl.rlVertex3f(x-width/2, y+height/2, z-length/2)  # Top Left
    rl.rlVertex3f(x+width/2, y-height/2, z-length/2)  # Bottom Right

    rl.rlVertex3f(x+width/2, y+height/2, z-length/2)  # Top Right
    rl.rlVertex3f(x+width/2, y-height/2, z-length/2)  # Bottom Right
    rl.rlVertex3f(x-width/2, y+height/2, z-length/2)  # Top Left

    # Top Face -------------------------------------------------------
    rl.rlVertex3f(x-width/2, y+height/2, z-length/2)  # Top Left
    rl.rlVertex3f(x-width/2, y+height/2, z+length/2)  # Bottom Left
    rl.rlVertex3f(x+width/2, y+height/2, z+length/2)  # Bottom Right

    rl.rlVertex3f(x+width/2, y+height/2, z-length/2)  # Top Right
    rl.rlVertex3f(x-width/2, y+height/2, z-length/2)  # Top Left
    rl.rlVertex3f(x+width/2, y+height/2, z+length/2)  # Bottom Right

    # Bottom Face ----------------------------------------------------
    rl.rlVertex3f(x-width/2, y-height/2, z-length/2)  # Top Left
    rl.rlVertex3f(x+width/2, y-height/2, z+length/2)  # Bottom Right
    rl.rlVertex3f(x-width/2, y-height/2, z+length/2)  # Bottom Left

    rl.rlVertex3f(x+width/2, y-height/2, z-length/2)  # Top Right
    rl.rlVertex3f(x+width/2, y-height/2, z+length/2)  # Bottom Right
    rl.rlVertex3f(x-width/2, y-height/2, z-length/2)  # Top Left

    # Right face -----------------------------------------------------
    rl.rlVertex3f(x+width/2, y-height/2, z-length/2)  # Bottom Right
    rl.rlVertex3f(x+width/2, y+height/2, z-length/2)  # Top Right
    rl.rlVertex3f(x+width/2, y+height/2, z+length/2)  # Top Left

    rl.rlVertex3f(x+width/2, y-height/2, z+length/2)  # Bottom Left
    rl.rlVertex3f(x+width/2, y-height/2, z-length/2)  # Bottom Right
    rl.rlVertex3f(x+width/2, y+height/2, z+length/2)  # Top Left

    # Left Face ------------------------------------------------------
    rl.rlVertex3f(x-width/2, y-height/2, z-length/2)  # Bottom Right
    rl.rlVertex3f(x-width/2, y+height/2, z+length/2)  # Top Left
    rl.rlVertex3f(x-width/2, y+height/2, z-length/2)  # Top Right

    rl.rlVertex3f(x-width/2, y-height/2, z+length/2)  # Bottom Left
    rl.rlVertex3f(x-width/2, y+height/2, z+length/2)  # Top Left
    rl.rlVertex3f(x-width/2, y-height/2, z-length/2)  # Bottom Right
    rl.rlEnd()
    rl.rlPopMatrix()


#Draw cube wires
def DrawCubeWires(position: 'raylib.Vector3', width: float, height: float, length: float, color: Color):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    rl.rlPushMatrix()

    rl.rlTranslatef(position.x, position.y, position.z)
    #rlRotatef(45, 0, 1, 0)

    rl.rlBegin(RL_LINES)
    rl.rlColor4ub(color.r, color.g, color.b, color.a)

    # Front Face -----------------------------------------------------
    # Bottom Line
    rl.rlVertex3f(x-width/2, y-height/2, z+length/2)  # Bottom Left
    rl.rlVertex3f(x+width/2, y-height/2, z+length/2)  # Bottom Right

    # Left Line
    rl.rlVertex3f(x+width/2, y-height/2, z+length/2)  # Bottom Right
    rl.rlVertex3f(x+width/2, y+height/2, z+length/2)  # Top Right

    # Top Line
    rl.rlVertex3f(x+width/2, y+height/2, z+length/2)  # Top Right
    rl.rlVertex3f(x-width/2, y+height/2, z+length/2)  # Top Left

    # Right Line
    rl.rlVertex3f(x-width/2, y+height/2, z+length/2)  # Top Left
    rl.rlVertex3f(x-width/2, y-height/2, z+length/2)  # Bottom Left

    # Back Face ------------------------------------------------------
    # Bottom Line
    rl.rlVertex3f(x-width/2, y-height/2, z-length/2)  # Bottom Left
    rl.rlVertex3f(x+width/2, y-height/2, z-length/2)  # Bottom Right

    # Left Line
    rl.rlVertex3f(x+width/2, y-height/2, z-length/2)  # Bottom Right
    rl.rlVertex3f(x+width/2, y+height/2, z-length/2)  # Top Right

    # Top Line
    rl.rlVertex3f(x+width/2, y+height/2, z-length/2)  # Top Right
    rl.rlVertex3f(x-width/2, y+height/2, z-length/2)  # Top Left

    # Right Line
    rl.rlVertex3f(x-width/2, y+height/2, z-length/2)  # Top Left
    rl.rlVertex3f(x-width/2, y-height/2, z-length/2)  # Bottom Left

    # Top Face -------------------------------------------------------
    # Left Line
    rl.rlVertex3f(x-width/2, y+height/2, z+length/2)  # Top Left Front
    rl.rlVertex3f(x-width/2, y+height/2, z-length/2)  # Top Left Back

    # Right Line
    rl.rlVertex3f(x+width/2, y+height/2, z+length/2)  # Top Right Front
    rl.rlVertex3f(x+width/2, y+height/2, z-length/2)  # Top Right Back

    # Bottom Face  ---------------------------------------------------
    # Left Line
    rl.rlVertex3f(x-width/2, y-height/2, z+length/2)  # Top Left Front
    rl.rlVertex3f(x-width/2, y-height/2, z-length/2)  # Top Left Back

    # Right Line
    rl.rlVertex3f(x+width/2, y-height/2, z+length/2)  # Top Right Front
    rl.rlVertex3f(x+width/2, y-height/2, z-length/2)  # Top Right Back
    rl.rlEnd()
    rl.rlPopMatrix()



# Initialization
#--------------------------------------------------------------------------------------
screenWidth: int = 800
screenHeight: int = 450

# GLFW3 Initialization + OpenGL 3.3 Context + Extensions
#--------------------------------------------------------
rl.glfwSetErrorCallback(ErrorCallback)

if not rl.glfwInit():
    print("GLFW3: Can not initialize GLFW")
    exit(1)

print("GLFW3: GLFW initialized successfully")

rl.glfwWindowHint(GLFW_SAMPLES, 4)
rl.glfwWindowHint(GLFW_DEPTH_BITS, 16)

# WARNING: OpenGL 3.3 Core profile only
rl.glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3)
rl.glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3)
rl.glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)
#glfwWindowHint(GLFW_OPENGL_DEBUG_CONTEXT, GL_TRUE)
#if defined(__APPLE__)
rl.glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GLFW_TRUE)
#endif

window = rl.glfwCreateWindow(screenWidth, screenHeight, b"rlgl standalone", ffi.NULL, ffi.NULL)

if not window:
    print("Cannot create GLFW3 Window.")
    rl.glfwTerminate()
    exit(2)

print("GLFW3: Window created successfully")

rl.glfwSetWindowPos(window, 200, 200)

rl.glfwSetKeyCallback(window, KeyCallback)

rl.glfwMakeContextCurrent(window)
rl.glfwSwapInterval(0)

# Load OpenGL 3.3 supported extensions
rl.rlLoadExtensions(ffi.addressof(rl, 'glfwGetProcAddress'))
#--------------------------------------------------------

# Initialize OpenGL context (states and resources)
rl.rlglInit(screenWidth, screenHeight)

# Initialize viewport and internal projection/modelview matrices
rl.rlViewport(0, 0, screenWidth, screenHeight)
rl.rlMatrixMode(RL_PROJECTION)                        # Switch to PROJECTION matrix
rl.rlLoadIdentity()                                   # Reset current matrix (PROJECTION)
rl.rlOrtho(0, screenWidth, screenHeight, 0, 0.0, 1.0) # Orthographic projection with top-left corner at (0,0)
rl.rlMatrixMode(RL_MODELVIEW)                         # Switch back to MODELVIEW matrix
rl.rlLoadIdentity()                                   # Reset current matrix (MODELVIEW)

rl.rlClearColor(245, 245, 245, 255)                   # Define clear color
rl.rlEnableDepthTest()                                # Enable DEPTH_TEST for 3D

camera = Camera(
    position = pyray.Vector3(5.0, 5.0, 5.0),    # Camera position
    target = pyray.Vector3(0.0, 0.0, 0.0),      # Camera looking at point
    up = pyray.Vector3(0.0, 1.0, 0.0),          # Camera up vector (rotation towards target)
    fovy = 45.0,                                # Camera field-of-view Y
    projection=rl.CAMERA_PERSPECTIVE)

cubePosition = pyray.Vector3(0.0, 0.0, 0.0)        # Cube default position (center)
#--------------------------------------------------------------------------------------

RLGL_SET_MATRIX_MANUALLY = True

# Main game loop
while not rl.glfwWindowShouldClose(window):
    # Update
    #----------------------------------------------------------------------------------
    #camera.position.x += 0.01f
    #----------------------------------------------------------------------------------

    # Draw
    #----------------------------------------------------------------------------------
    rl.rlClearScreenBuffers()             # Clear current framebuffer

    # Draw '3D' elements in the scene
    #-----------------------------------------------
    # Calculate projection matrix (from perspective) and view matrix from camera look at
    matProj = rl.MatrixPerspective(camera.fovy*DEG2RAD, float(screenWidth)/float(screenHeight), 0.01, 1000.0)
    matView = rl.MatrixLookAt(camera.position, camera.target, camera.up)

    rl.rlSetMatrixModelview(matView)    # Set internal modelview matrix (default shader)
    rl.rlSetMatrixProjection(matProj)   # Set internal projection matrix (default shader)

    DrawCube(cubePosition, 2.0, 2.0, 2.0, Color(*RED))
    DrawCubeWires(cubePosition, 2.0, 2.0, 2.0, Color(*RAYWHITE))
    DrawGrid(10, 1.0)

    # Draw internal render batch buffers (3D data)
    rl.rlDrawRenderBatchActive()
    #-----------------------------------------------

    # Draw '2D' elements in the scene (GUI)
    #-----------------------------------------------

    if RLGL_SET_MATRIX_MANUALLY:
        matProj = rl.MatrixOrtho(0.0, screenWidth, screenHeight, 0.0, 0.0, 1.0)
        matView = rl.MatrixIdentity()
        rl.rlSetMatrixModelview(matView)    # Set internal modelview matrix (default shader)
        rl.rlSetMatrixProjection(matProj)   # Set internal projection matrix (default shader)
    else:   # Let rlgl generate and multiply matrix internally
        rl.rlMatrixMode(RL_PROJECTION)                            # Enable internal projection matrix
        rl.rlLoadIdentity()                                       # Reset internal projection matrix
        rl.rlOrtho(0.0, screenWidth, screenHeight, 0.0, 0.0, 1.0) # Recalculate internal projection matrix
        rl.rlMatrixMode(RL_MODELVIEW)                             # Enable internal modelview matrix
        rl.rlLoadIdentity()                                       # Reset internal modelview matrix

    DrawRectangleV(pyray.Vector2(10.0, 10.0), pyray.Vector2(780.0, 20.0), Color(*DARKGRAY))

    # Draw internal render batch buffers (2D data)
    rl.rlDrawRenderBatchActive()
    #-----------------------------------------------

    rl.glfwSwapBuffers(window)
    rl.glfwPollEvents()
    #----------------------------------------------------------------------------------

# De-Initialization
#--------------------------------------------------------------------------------------
rl.rlglClose()                    # Unload rlgl internal buffers and default shader/texture

rl.glfwDestroyWindow(window)      # Close window
rl.glfwTerminate()                # Free GLFW3 resources
#--------------------------------------------------------------------------------------

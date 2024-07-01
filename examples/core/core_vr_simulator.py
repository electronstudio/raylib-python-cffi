import pyray
import raylib

GLSL_VERSION = 330

# Initialization
screenWidth = 800
screenHeight = 450

# NOTE: screenWidth/screenHeight should match VR device aspect ratio
pyray.init_window(screenWidth, screenHeight, "raylib [core] example - vr simulator")

# VR device parameters definition
device = pyray.VrDeviceInfo(
    # Oculus Rift CV1 parameters for simulator
    2160,                  # Horizontal resolution in pixels
    1200,                  # Vertical resolution in pixels
    0.133793,              # Horizontal size in meters
    0.0669,                # Vertical size in meters
    0.04678,             # Screen center in meters
    0.041,         # Distance between eye and display in meters
    0.07,       # Lens separation distance in meters
    0.07,       # IPD (distance between pupils) in meters

    # NOTE: CV1 uses fresnel-hybrid-asymmetric lenses with specific compute shaders
    # Following parameters are just an approximation to CV1 distortion stereo rendering
    [1.0, 0.22, 0.24, 0.0],     # Lens distortion constant parameters
    [0.996, -0.004, 1.014, 0.0]   # Chromatic aberration correction parameters
)

# Load VR stereo config for VR device parameters (Oculus Rift CV1 parameters)
config = pyray.load_vr_stereo_config(device)

# Distortion shader (uses device lens distortion and chroma)
distortion = pyray.load_shader(pyray.ffi.NULL, f"resources/distortion{GLSL_VERSION}.fs")

# Update distortion shader with lens and distortion-scale parameters
pyray.set_shader_value(distortion, 2, pyray.ffi.new('char []', b"leftLensCenter"),  pyray.SHADER_UNIFORM_VEC2)
pyray.set_shader_value(distortion, 2,pyray.ffi.new('char []', b"rightLensCenter"),  pyray.SHADER_UNIFORM_VEC2)
pyray.set_shader_value(distortion, 2,pyray.ffi.new('char []', b"leftScreenCenter"),  pyray.SHADER_UNIFORM_VEC2)
pyray.set_shader_value(distortion, 2,pyray.ffi.new('char []', b"rightScreenCenter"),  pyray.SHADER_UNIFORM_VEC2)

pyray.set_shader_value(distortion, 2,pyray.ffi.new('char []', b"scale"),  pyray.SHADER_UNIFORM_VEC2)
pyray.set_shader_value(distortion, 2,pyray.ffi.new('char []', b"scaleIn"),  pyray.SHADER_UNIFORM_VEC2)
pyray.set_shader_value(distortion, 4,pyray.ffi.new('char []', b"deviceWarpParam"),  pyray.SHADER_UNIFORM_VEC4)
pyray.set_shader_value(distortion, 4,pyray.ffi.new('char []', b"chromaAbParam"),  pyray.SHADER_UNIFORM_VEC4)

# Initialize framebuffer for stereo rendering
# NOTE: Screen size should match HMD aspect ratio
target = pyray.load_render_texture(device.hResolution, device.vResolution)

# The target's height is flipped (in the source Rectangle), due to OpenGL reasons
sourceRec = pyray.Rectangle(0.0, 0.0, target.texture.width, -target.texture.height)
destRec = pyray.Rectangle(0.0, 0.0, pyray.get_screen_width(), pyray.get_screen_height())

# Define the camera to look into our 3D world
camera = pyray.Camera3D(
    pyray.Vector3(5.0, 2.0, 5.0),    # Camera position
    pyray.Vector3(0.0, 2.0, 0.0),      # Camera looking at point
    pyray.Vector3(0.0, 1.0, 0.0),          # Camera up vector
    60.0,                               # Camera field-of-view Y
    pyray.CAMERA_PERSPECTIVE       # Camera projection type
)

cubePosition = pyray.Vector3(0.0, 0.0, 0.0)

pyray.disable_cursor()                # Limit cursor to relative movement inside the window

pyray.set_target_fps(90)              # Set our game to run at 90 frames-per-second

# Main game loop
while not pyray.window_should_close():     # Detect window close button or ESC key
    # Update
    pyray.update_camera(camera, pyray.CAMERA_FIRST_PERSON)

    # Draw
    pyray.begin_texture_mode(target)
    pyray.clear_background(pyray.RAYWHITE)
    pyray.begin_vr_stereo_mode(config)
    pyray.begin_mode_3d(camera)

    pyray.draw_cube(cubePosition, 2.0, 2.0, 2.0, pyray.RED)
    pyray.draw_cube_wires(cubePosition, 2.0, 2.0, 2.0, pyray.MAROON)
    pyray.draw_grid(40, 1.0)

    pyray.end_mode_3d()
    pyray.end_vr_stereo_mode()
    pyray.end_texture_mode()

    pyray.begin_drawing()
    pyray.clear_background(pyray.RAYWHITE)
    pyray.begin_shader_mode(distortion)
    pyray.draw_texture_pro(target.texture, sourceRec, destRec, pyray.Vector2(0.0, 0.0), 0.0, pyray.WHITE)
    pyray.end_shader_mode()
    pyray.draw_fps(10, 10)
    pyray.end_drawing()

# De-Initialization
pyray.unload_vr_stereo_config(config)   # Unload stereo config
pyray.unload_render_texture(target)     # Unload stereo render fbo
pyray.unload_shader(distortion)         # Unload distortion shader
pyray.close_window()                    # Close window and OpenGL context

from pyray import *
import raylib as rl

#------------------------------------------------------------------------------------
# Define custom functions required for the example
#------------------------------------------------------------------------------------
# Load custom render texture, create a writable depth texture buffer
def LoadRenderTextureDepthTex(width, height):

    target =  RenderTexture()

    target.id = rl_load_framebuffer(width, height)   # Load an empty framebuffer

    if target.id > 0:

        rl_enable_framebuffer(target.id)

        # Create color texture (default to RGBA)
        target.texture.id = rl_load_texture(None, width, height, PixelFormat.PIXELFORMAT_UNCOMPRESSED_R8G8B8A8, 1)
        target.texture.width = width
        target.texture.height = height
        target.texture.format = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R8G8B8A8
        target.texture.mipmaps = 1

        # Create depth texture buffer (instead of raylib default renderbuffer)
        target.depth.id = rl_load_texture_depth(width, height, False)
        target.depth.width = width
        target.depth.height = height
        target.depth.format = 19       #DEPTH_COMPONENT_24BIT?
        target.depth.mipmaps = 1

        # Attach color texture and depth texture to FBO
        rl_framebuffer_attach(target.id, target.texture.id, rl.RL_ATTACHMENT_COLOR_CHANNEL0, rl.RL_ATTACHMENT_TEXTURE2D, 0)
        rl_framebuffer_attach(target.id, target.depth.id, rl.RL_ATTACHMENT_DEPTH, rl.RL_ATTACHMENT_TEXTURE2D, 0)

        # Check if fbo is complete with attachments (valid)
        if rl_framebuffer_complete(target.id):
            print(f"FBO: [{target.id}] Framebuffer object created successfully")

        rl_disable_framebuffer()

    else:
        print("FBO: Framebuffer object can not be created")

    return target


# Unload render texture from GPU memory (VRAM)
def UnloadRenderTextureDepthTex(target):

    if target.id > 0:

        # Color texture attached to FBO is deleted
        rl_unload_texture(target.texture.id)
        rl_unload_texture(target.depth.id)

        # NOTE: Depth texture is automatically
        # queried and deleted before deleting framebuffer
        rl_unload_framebuffer(target.id)



screenWidth = 800
screenHeight = 450

init_window(screenWidth, screenHeight, "raylib [shaders] example - write depth buffer")

# The shader inverts the depth buffer by writing into it by `gl_FragDepth = 1 - gl_FragCoord.z`
shader = load_shader("","resources/shaders/glsl330/write_depth.fs")

# Use Customized function to create writable depth texture buffer
target = LoadRenderTextureDepthTex(screenWidth, screenHeight)

# Define the camera to look into our 3d world
camera = Camera3D()
camera.position = (2.0, 2.0, 3.0)     # Camera position
camera.target = (0.0, 0.5, 0.0)     # Camera looking at point
camera.up = (0.0, 1.0, 0.0)           # Camera up vector (rotation towards target)
camera.fovy = 45.0                                # Camera field-of-view Y
camera.projection = CameraProjection.CAMERA_PERSPECTIVE              # Camera projection type


set_target_fps(60)                   # Set our game to run at 60 frames-per-second
#--------------------------------------------------------------------------------------

# Main game loop
while not window_should_close():        # Detect window close button or ESC key

    # Update
    #----------------------------------------------------------------------------------
    update_camera(camera, CameraMode.CAMERA_ORBITAL)
    #----------------------------------------------------------------------------------

    # Draw
    #----------------------------------------------------------------------------------

    # Draw into our custom render texture (framebuffer)
    begin_texture_mode(target)
    clear_background(WHITE)

    begin_mode_3d(camera)
    begin_shader_mode(shader)
    draw_cube_wires_v((0.0, 0.5, 1.0) , (1.0,1.0, 1.0), RED)
    draw_cube_v((0.0, 0.5, 1.0) , (1.0, 1.0, 1.0) , PURPLE)
    draw_cube_wires_v((0.0, 0.5, -1.0), (1.0, 1.0, 1.0) , DARKGREEN)
    draw_cube_v((0.0, 0.5, -1.0) , (1.0, 1.0, 1.0) , YELLOW)
    draw_grid(10, 1.0)
    end_shader_mode()
    end_mode_3d()
    end_texture_mode()

    # Draw into screen our custom render texture
    begin_drawing()
    clear_background(RAYWHITE)

    draw_texture_rec(target.texture, Rectangle(0, 0, screenWidth, -screenHeight) , (0, 0) , WHITE)
    draw_fps(10, 10)
    end_drawing()


# De-Initialization
#--------------------------------------------------------------------------------------
UnloadRenderTextureDepthTex(target)
unload_shader(shader)

close_window()        # Close window and OpenGL context



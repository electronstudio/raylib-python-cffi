
import pyray as ray


screen_width = 800
screen_height = 450

ray.init_window(screen_width, screen_height, "raylib [models] example - model animation")

# Define the camera to look into our 3d world
camera = ray.Camera3D()
camera.position = ray.Vector3( 10.0, 10.0, 10.0 ) # Camera position
camera.target = ray.Vector3( 0.0, 0.0, 0.0 )      # Camera looking at point
camera.up = ray.Vector3( 0.0, 1.0, 0.0 )          # Camera up vector (rotation towards target)
camera.fovy = 45.0                                # Camera field-of-view Y
camera.projection = ray.CAMERA_PERSPECTIVE        # Camera mode type

model   = ray.load_model("resources/models/iqm/guy.iqm")                    # Load the animated model mesh and basic data
texture = ray.load_texture("resources/models/iqm/guytex.png")         # Load model texture and set material
ray.set_material_texture(model.materials, ray.MATERIAL_MAP_ALBEDO, texture)     # Set model material map texture

position = ( 0., 0., 0. )            # Set model position

# Load animation data
count = ray.ffi.new("unsigned int *", 1)
anims = ray.load_model_animations("resources/models/iqm/guyanim.iqm", count)
anim_frame_counter = 0

ray.set_target_fps(60)                   # Set our game to run at 60 frames-per-second
#--------------------------------------------------------------------------------------

# Main game loop
while not ray.window_should_close():        # Detect window close button or ESC key
	# Update
	#----------------------------------------------------------------------------------
	ray.update_camera(camera, ray.CAMERA_FREE)

	# Play animation when spacebar is held down
	if ray.is_key_down(ray.KEY_SPACE):
		anim_frame_counter+=1
		ray.update_model_animation(model, anims[0], anim_frame_counter)
		if anim_frame_counter >= anims[0].frameCount:
			anim_frame_counter = 0
	
	#----------------------------------------------------------------------------------

	# Draw
	#----------------------------------------------------------------------------------
	ray.begin_drawing()

	ray.clear_background(ray.RAYWHITE)

	ray.begin_mode_3d(camera)

	ray.draw_model_ex(model, position, ray.Vector3( 1.0, 0.0, 0.0 ), -90.0, ray.Vector3( 1.0, 1.0, 1.0 ), ray.WHITE)

	for i in range(model.boneCount):
		ray.draw_cube(anims[0].framePoses[anim_frame_counter][i].translation, 0.2, 0.2, 0.2, ray.RED)

	ray.draw_grid(10, 1.0)         # Draw a grid

	ray.end_mode_3d()

	ray.draw_text("PRESS SPACE to PLAY MODEL ANIMATION", 10, 10, 20, ray.MAROON)
	ray.draw_text("(c) Guy IQM 3D model by @culacant", screen_width - 200, screen_height - 20, 10, ray.GRAY)
	
	ray.draw_fps(10, 400)

	ray.end_drawing()
	#----------------------------------------------------------------------------------


# De-Initialization
#--------------------------------------------------------------------------------------
ray.unload_texture(texture)     # Unload texture

# Unload model animations data
for anim in anims:
	ray.unload_model_animation(anim)

ray.unload_model(model)         # Unload model

ray.close_window()              # Close window and OpenGL context
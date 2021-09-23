from typing import Any

class PyRay:
    def pointer(self, struct):
        return ffi.addressof(struct)

    BLEND_ADDITIVE: int
    BLEND_ADD_COLORS: int
    BLEND_ALPHA: int
    BLEND_CUSTOM: int
    BLEND_MULTIPLIED: int
    BLEND_SUBTRACT_COLORS: int
    def begin_blend_mode(self, mode: int) -> None:
        """Begin blending mode (alpha, additive, multiplied, subtract, custom)"""
        ...
    def begin_drawing(self) -> None:
        """Setup canvas (framebuffer) to start drawing"""
        ...
    def begin_mode_2d(self, camera: Camera2D) -> None:
        """Begin 2D mode with custom camera (2D)"""
        ...
    def begin_mode_3d(self, camera: Camera3D) -> None:
        """Begin 3D mode with custom camera (3D)"""
        ...
    def begin_scissor_mode(self, x: int, y: int, width: int, height: int) -> None:
        """Begin scissor mode (define screen area for following drawing)"""
        ...
    def begin_shader_mode(self, shader: Shader) -> None:
        """Begin custom shader drawing"""
        ...
    def begin_texture_mode(self, target: RenderTexture) -> None:
        """Begin drawing to render texture"""
        ...
    def begin_vr_stereo_mode(self, config: VrStereoConfig) -> None:
        """Begin stereo rendering (requires VR simulator)"""
        ...
    CAMERA_CUSTOM: int
    CAMERA_FIRST_PERSON: int
    CAMERA_FREE: int
    CAMERA_ORBITAL: int
    CAMERA_ORTHOGRAPHIC: int
    CAMERA_PERSPECTIVE: int
    CAMERA_THIRD_PERSON: int
    CUBEMAP_LAYOUT_AUTO_DETECT: int
    CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE: int
    CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR: int
    CUBEMAP_LAYOUT_LINE_HORIZONTAL: int
    CUBEMAP_LAYOUT_LINE_VERTICAL: int
    CUBEMAP_LAYOUT_PANORAMA: int
    def change_directory(self, dir: str) -> bool:
        """Change working directory, return true on success"""
        ...
    def check_collision_box_sphere(self, box: BoundingBox, center: Vector3, radius: float) -> bool:
        """Check collision between box and sphere"""
        ...
    def check_collision_boxes(self, box1: BoundingBox, box2: BoundingBox) -> bool:
        """Check collision between two bounding boxes"""
        ...
    def check_collision_circle_rec(self, center: Vector2, radius: float, rec: Rectangle) -> bool:
        """Check collision between circle and rectangle"""
        ...
    def check_collision_circles(self, center1: Vector2, radius1: float, center2: Vector2, radius2: float) -> bool:
        """Check collision between two circles"""
        ...
    def check_collision_lines(self, startPos1: Vector2, endPos1: Vector2, startPos2: Vector2, endPos2: Vector2, collisionPoint: Any) -> bool:
        """Check the collision between two lines defined by two points each, returns collision point by reference"""
        ...
    def check_collision_point_circle(self, point: Vector2, center: Vector2, radius: float) -> bool:
        """Check if point is inside circle"""
        ...
    def check_collision_point_rec(self, point: Vector2, rec: Rectangle) -> bool:
        """Check if point is inside rectangle"""
        ...
    def check_collision_point_triangle(self, point: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> bool:
        """Check if point is inside a triangle"""
        ...
    def check_collision_ray_box(self, Ray_0: Ray, BoundingBox_1: BoundingBox) -> bool:
        """_Bool CheckCollisionRayBox(struct Ray, struct BoundingBox);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_ray_sphere(self, Ray_0: Ray, Vector3_1: Vector3, float_2: float) -> bool:
        """_Bool CheckCollisionRaySphere(struct Ray, struct Vector3, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_ray_sphere_ex(self, Ray_0: Ray, Vector3_1: Vector3, float_2: float, Vector3_pointer_3: Any) -> bool:
        """_Bool CheckCollisionRaySphereEx(struct Ray, struct Vector3, float, struct Vector3 *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_recs(self, rec1: Rectangle, rec2: Rectangle) -> bool:
        """Check collision between two rectangles"""
        ...
    def check_collision_spheres(self, center1: Vector3, radius1: float, center2: Vector3, radius2: float) -> bool:
        """Check collision between two spheres"""
        ...
    def clear_background(self, color: Color) -> None:
        """Set background color (framebuffer clear color)"""
        ...
    def clear_directory_files(self) -> None:
        """Clear directory files paths buffers (free memory)"""
        ...
    def clear_dropped_files(self) -> None:
        """Clear dropped files paths buffer (free memory)"""
        ...
    def clear_window_state(self, flags: int) -> None:
        """Clear window configuration state flags"""
        ...
    def close_audio_device(self) -> None:
        """Close the audio device and context"""
        ...
    def close_audio_stream(self, AudioStream_0: AudioStream) -> None:
        """void CloseAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def close_window(self) -> None:
        """Close window and unload OpenGL context"""
        ...
    def codepoint_to_utf8(self, codepoint: int, byteLength: Any) -> str:
        """Encode codepoint into utf8 text (char array length returned as parameter)"""
        ...
    def color_alpha(self, color: Color, alpha: float) -> Color:
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        ...
    def color_alpha_blend(self, dst: Color, src: Color, tint: Color) -> Color:
        """Get src alpha-blended into dst color with tint"""
        ...
    def color_from_hsv(self, hue: float, saturation: float, value: float) -> Color:
        """Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
        ...
    def color_from_normalized(self, normalized: Vector4) -> Color:
        """Get Color from normalized values [0..1]"""
        ...
    def color_normalize(self, color: Color) -> Vector4:
        """Get Color normalized as float [0..1]"""
        ...
    def color_to_hsv(self, color: Color) -> Vector3:
        """Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
        ...
    def color_to_int(self, color: Color) -> int:
        """Get hexadecimal value for a Color"""
        ...
    def compress_data(self, data: str, dataLength: int, compDataLength: Any) -> str:
        """Compress data (DEFLATE algorithm)"""
        ...
    def decompress_data(self, compData: str, compDataLength: int, dataLength: Any) -> str:
        """Decompress data (DEFLATE algorithm)"""
        ...
    def directory_exists(self, dirPath: str) -> bool:
        """Check if a directory path exists"""
        ...
    def disable_cursor(self) -> None:
        """Disables cursor (lock cursor)"""
        ...
    def draw_billboard(self, camera: Camera3D, texture: Texture, position: Vector3, size: float, tint: Color) -> None:
        """Draw a billboard texture"""
        ...
    def draw_billboard_rec(self, camera: Camera3D, texture: Texture, source: Rectangle, position: Vector3, size: float, tint: Color) -> None:
        """Draw a billboard texture defined by source"""
        ...
    def draw_bounding_box(self, box: BoundingBox, color: Color) -> None:
        """Draw bounding box (wires)"""
        ...
    def draw_circle(self, centerX: int, centerY: int, radius: float, color: Color) -> None:
        """Draw a color-filled circle"""
        ...
    def draw_circle_3d(self, center: Vector3, radius: float, rotationAxis: Vector3, rotationAngle: float, color: Color) -> None:
        """Draw a circle in 3D world space"""
        ...
    def draw_circle_gradient(self, centerX: int, centerY: int, radius: float, color1: Color, color2: Color) -> None:
        """Draw a gradient-filled circle"""
        ...
    def draw_circle_lines(self, centerX: int, centerY: int, radius: float, color: Color) -> None:
        """Draw circle outline"""
        ...
    def draw_circle_sector(self, center: Vector2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
        """Draw a piece of a circle"""
        ...
    def draw_circle_sector_lines(self, center: Vector2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
        """Draw circle sector outline"""
        ...
    def draw_circle_v(self, center: Vector2, radius: float, color: Color) -> None:
        """Draw a color-filled circle (Vector version)"""
        ...
    def draw_cube(self, position: Vector3, width: float, height: float, length: float, color: Color) -> None:
        """Draw cube"""
        ...
    def draw_cube_texture(self, texture: Texture, position: Vector3, width: float, height: float, length: float, color: Color) -> None:
        """Draw cube textured"""
        ...
    def draw_cube_v(self, position: Vector3, size: Vector3, color: Color) -> None:
        """Draw cube (Vector version)"""
        ...
    def draw_cube_wires(self, position: Vector3, width: float, height: float, length: float, color: Color) -> None:
        """Draw cube wires"""
        ...
    def draw_cube_wires_v(self, position: Vector3, size: Vector3, color: Color) -> None:
        """Draw cube wires (Vector version)"""
        ...
    def draw_cylinder(self, position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
        """Draw a cylinder/cone"""
        ...
    def draw_cylinder_wires(self, position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
        """Draw a cylinder/cone wires"""
        ...
    def draw_ellipse(self, centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None:
        """Draw ellipse"""
        ...
    def draw_ellipse_lines(self, centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None:
        """Draw ellipse outline"""
        ...
    def draw_fps(self, posX: int, posY: int) -> None:
        """Draw current FPS"""
        ...
    def draw_grid(self, slices: int, spacing: float) -> None:
        """Draw a grid (centered at (0, 0, 0))"""
        ...
    def draw_line(self, startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None:
        """Draw a line"""
        ...
    def draw_line_3d(self, startPos: Vector3, endPos: Vector3, color: Color) -> None:
        """Draw a line in 3D world space"""
        ...
    def draw_line_bezier(self, startPos: Vector2, endPos: Vector2, thick: float, color: Color) -> None:
        """Draw a line using cubic-bezier curves in-out"""
        ...
    def draw_line_bezier_quad(self, startPos: Vector2, endPos: Vector2, controlPos: Vector2, thick: float, color: Color) -> None:
        """raw line using quadratic bezier curves with a control point"""
        ...
    def draw_line_ex(self, startPos: Vector2, endPos: Vector2, thick: float, color: Color) -> None:
        """Draw a line defining thickness"""
        ...
    def draw_line_strip(self, points: Any, pointsCount: int, color: Color) -> None:
        """Draw lines sequence"""
        ...
    def draw_line_v(self, startPos: Vector2, endPos: Vector2, color: Color) -> None:
        """Draw a line (Vector version)"""
        ...
    def draw_mesh(self, mesh: Mesh, material: Material, transform: Matrix) -> None:
        """Draw a 3d mesh with material and transform"""
        ...
    def draw_mesh_instanced(self, mesh: Mesh, material: Material, transforms: Any, instances: int) -> None:
        """Draw multiple mesh instances with material and different transforms"""
        ...
    def draw_model(self, model: Model, position: Vector3, scale: float, tint: Color) -> None:
        """Draw a model (with texture if set)"""
        ...
    def draw_model_ex(self, model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None:
        """Draw a model with extended parameters"""
        ...
    def draw_model_wires(self, model: Model, position: Vector3, scale: float, tint: Color) -> None:
        """Draw a model wires (with texture if set)"""
        ...
    def draw_model_wires_ex(self, model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None:
        """Draw a model wires (with texture if set) with extended parameters"""
        ...
    def draw_pixel(self, posX: int, posY: int, color: Color) -> None:
        """Draw a pixel"""
        ...
    def draw_pixel_v(self, position: Vector2, color: Color) -> None:
        """Draw a pixel (Vector version)"""
        ...
    def draw_plane(self, centerPos: Vector3, size: Vector2, color: Color) -> None:
        """Draw a plane XZ"""
        ...
    def draw_point_3d(self, position: Vector3, color: Color) -> None:
        """Draw a point in 3D space, actually a small line"""
        ...
    def draw_poly(self, center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None:
        """Draw a regular polygon (Vector version)"""
        ...
    def draw_poly_lines(self, center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None:
        """Draw a polygon outline of n sides"""
        ...
    def draw_ray(self, ray: Ray, color: Color) -> None:
        """Draw a ray line"""
        ...
    def draw_rectangle(self, posX: int, posY: int, width: int, height: int, color: Color) -> None:
        """Draw a color-filled rectangle"""
        ...
    def draw_rectangle_gradient_ex(self, rec: Rectangle, col1: Color, col2: Color, col3: Color, col4: Color) -> None:
        """Draw a gradient-filled rectangle with custom vertex colors"""
        ...
    def draw_rectangle_gradient_h(self, posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
        """Draw a horizontal-gradient-filled rectangle"""
        ...
    def draw_rectangle_gradient_v(self, posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
        """Draw a vertical-gradient-filled rectangle"""
        ...
    def draw_rectangle_lines(self, posX: int, posY: int, width: int, height: int, color: Color) -> None:
        """Draw rectangle outline"""
        ...
    def draw_rectangle_lines_ex(self, rec: Rectangle, lineThick: int, color: Color) -> None:
        """Draw rectangle outline with extended parameters"""
        ...
    def draw_rectangle_pro(self, rec: Rectangle, origin: Vector2, rotation: float, color: Color) -> None:
        """Draw a color-filled rectangle with pro parameters"""
        ...
    def draw_rectangle_rec(self, rec: Rectangle, color: Color) -> None:
        """Draw a color-filled rectangle"""
        ...
    def draw_rectangle_rounded(self, rec: Rectangle, roundness: float, segments: int, color: Color) -> None:
        """Draw rectangle with rounded edges"""
        ...
    def draw_rectangle_rounded_lines(self, rec: Rectangle, roundness: float, segments: int, lineThick: int, color: Color) -> None:
        """Draw rectangle with rounded edges outline"""
        ...
    def draw_rectangle_v(self, position: Vector2, size: Vector2, color: Color) -> None:
        """Draw a color-filled rectangle (Vector version)"""
        ...
    def draw_ring(self, center: Vector2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
        """Draw ring"""
        ...
    def draw_ring_lines(self, center: Vector2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
        """Draw ring outline"""
        ...
    def draw_sphere(self, centerPos: Vector3, radius: float, color: Color) -> None:
        """Draw sphere"""
        ...
    def draw_sphere_ex(self, centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None:
        """Draw sphere with extended parameters"""
        ...
    def draw_sphere_wires(self, centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None:
        """Draw sphere wires"""
        ...
    def draw_text(self, text: str, posX: int, posY: int, fontSize: int, color: Color) -> None:
        """Draw text (using default font)"""
        ...
    def draw_text_codepoint(self, font: Font, codepoint: int, position: Vector2, fontSize: float, tint: Color) -> None:
        """Draw one character (codepoint)"""
        ...
    def draw_text_ex(self, font: Font, text: str, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None:
        """Draw text using font and additional parameters"""
        ...
    def draw_text_rec(self, font: Font, text: str, rec: Rectangle, fontSize: float, spacing: float, wordWrap: bool, tint: Color) -> None:
        """Draw text using font inside rectangle limits"""
        ...
    def draw_text_rec_ex(self, font: Font, text: str, rec: Rectangle, fontSize: float, spacing: float, wordWrap: bool, tint: Color, selectStart: int, selectLength: int, selectTint: Color, selectBackTint: Color) -> None:
        """Draw text using font inside rectangle limits with support for text selection"""
        ...
    def draw_texture(self, texture: Texture, posX: int, posY: int, tint: Color) -> None:
        """Draw a Texture2D"""
        ...
    def draw_texture_ex(self, texture: Texture, position: Vector2, rotation: float, scale: float, tint: Color) -> None:
        """Draw a Texture2D with extended parameters"""
        ...
    def draw_texture_n_patch(self, texture: Texture, nPatchInfo: NPatchInfo, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None:
        """Draws a texture (or part of it) that stretches or shrinks nicely"""
        ...
    def draw_texture_poly(self, texture: Texture, center: Vector2, points: Any, texcoords: Any, pointsCount: int, tint: Color) -> None:
        """Draw a textured polygon"""
        ...
    def draw_texture_pro(self, texture: Texture, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None:
        """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
        ...
    def draw_texture_quad(self, texture: Texture, tiling: Vector2, offset: Vector2, quad: Rectangle, tint: Color) -> None:
        """Draw texture quad with tiling and offset parameters"""
        ...
    def draw_texture_rec(self, texture: Texture, source: Rectangle, position: Vector2, tint: Color) -> None:
        """Draw a part of a texture defined by a rectangle"""
        ...
    def draw_texture_tiled(self, texture: Texture, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, scale: float, tint: Color) -> None:
        """Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest."""
        ...
    def draw_texture_v(self, texture: Texture, position: Vector2, tint: Color) -> None:
        """Draw a Texture2D with position defined as Vector2"""
        ...
    def draw_triangle(self, v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
        """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
        ...
    def draw_triangle_3d(self, v1: Vector3, v2: Vector3, v3: Vector3, color: Color) -> None:
        """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
        ...
    def draw_triangle_fan(self, points: Any, pointsCount: int, color: Color) -> None:
        """Draw a triangle fan defined by points (first vertex is the center)"""
        ...
    def draw_triangle_lines(self, v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
        """Draw triangle outline (vertex in counter-clockwise order!)"""
        ...
    def draw_triangle_strip(self, points: Any, pointsCount: int, color: Color) -> None:
        """Draw a triangle strip defined by points"""
        ...
    def draw_triangle_strip_3d(self, points: Any, pointsCount: int, color: Color) -> None:
        """Draw a triangle strip defined by points"""
        ...
    def enable_cursor(self) -> None:
        """Enables cursor (unlock cursor)"""
        ...
    def end_blend_mode(self) -> None:
        """End blending mode (reset to default: alpha blending)"""
        ...
    def end_drawing(self) -> None:
        """End canvas drawing and swap buffers (double buffering)"""
        ...
    def end_mode_2d(self) -> None:
        """Ends 2D mode with custom camera"""
        ...
    def end_mode_3d(self) -> None:
        """Ends 3D mode and returns to default 2D orthographic mode"""
        ...
    def end_scissor_mode(self) -> None:
        """End scissor mode"""
        ...
    def end_shader_mode(self) -> None:
        """End custom shader drawing (use default shader)"""
        ...
    def end_texture_mode(self) -> None:
        """Ends drawing to render texture"""
        ...
    def end_vr_stereo_mode(self) -> None:
        """End stereo rendering (requires VR simulator)"""
        ...
    def export_image(self, image: Image, fileName: str) -> bool:
        """Export image data to file, returns true on success"""
        ...
    def export_image_as_code(self, image: Image, fileName: str) -> bool:
        """Export image as code file defining an array of bytes, returns true on success"""
        ...
    def export_mesh(self, mesh: Mesh, fileName: str) -> bool:
        """Export mesh data to file, returns true on success"""
        ...
    def export_wave(self, wave: Wave, fileName: str) -> bool:
        """Export wave data to file, returns true on success"""
        ...
    def export_wave_as_code(self, wave: Wave, fileName: str) -> bool:
        """Export wave sample data to code (.h), returns true on success"""
        ...
    FLAG_FULLSCREEN_MODE: int
    FLAG_INTERLACED_HINT: int
    FLAG_MSAA_4X_HINT: int
    FLAG_VSYNC_HINT: int
    FLAG_WINDOW_ALWAYS_RUN: int
    FLAG_WINDOW_HIDDEN: int
    FLAG_WINDOW_HIGHDPI: int
    FLAG_WINDOW_MAXIMIZED: int
    FLAG_WINDOW_MINIMIZED: int
    FLAG_WINDOW_RESIZABLE: int
    FLAG_WINDOW_TOPMOST: int
    FLAG_WINDOW_TRANSPARENT: int
    FLAG_WINDOW_UNDECORATED: int
    FLAG_WINDOW_UNFOCUSED: int
    FONT_BITMAP: int
    FONT_DEFAULT: int
    FONT_SDF: int
    def fade(self, color: Color, alpha: float) -> Color:
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        ...
    def file_exists(self, fileName: str) -> bool:
        """Check if file exists"""
        ...
    GAMEPAD_AXIS_LEFT_TRIGGER: int
    GAMEPAD_AXIS_LEFT_X: int
    GAMEPAD_AXIS_LEFT_Y: int
    GAMEPAD_AXIS_RIGHT_TRIGGER: int
    GAMEPAD_AXIS_RIGHT_X: int
    GAMEPAD_AXIS_RIGHT_Y: int
    GAMEPAD_BUTTON_LEFT_FACE_DOWN: int
    GAMEPAD_BUTTON_LEFT_FACE_LEFT: int
    GAMEPAD_BUTTON_LEFT_FACE_RIGHT: int
    GAMEPAD_BUTTON_LEFT_FACE_UP: int
    GAMEPAD_BUTTON_LEFT_THUMB: int
    GAMEPAD_BUTTON_LEFT_TRIGGER_1: int
    GAMEPAD_BUTTON_LEFT_TRIGGER_2: int
    GAMEPAD_BUTTON_MIDDLE: int
    GAMEPAD_BUTTON_MIDDLE_LEFT: int
    GAMEPAD_BUTTON_MIDDLE_RIGHT: int
    GAMEPAD_BUTTON_RIGHT_FACE_DOWN: int
    GAMEPAD_BUTTON_RIGHT_FACE_LEFT: int
    GAMEPAD_BUTTON_RIGHT_FACE_RIGHT: int
    GAMEPAD_BUTTON_RIGHT_FACE_UP: int
    GAMEPAD_BUTTON_RIGHT_THUMB: int
    GAMEPAD_BUTTON_RIGHT_TRIGGER_1: int
    GAMEPAD_BUTTON_RIGHT_TRIGGER_2: int
    GAMEPAD_BUTTON_UNKNOWN: int
    GESTURE_DOUBLETAP: int
    GESTURE_DRAG: int
    GESTURE_HOLD: int
    GESTURE_NONE: int
    GESTURE_PINCH_IN: int
    GESTURE_PINCH_OUT: int
    GESTURE_SWIPE_DOWN: int
    GESTURE_SWIPE_LEFT: int
    GESTURE_SWIPE_RIGHT: int
    GESTURE_SWIPE_UP: int
    GESTURE_TAP: int
    def gen_image_cellular(self, width: int, height: int, tileSize: int) -> Image:
        """Generate image: cellular algorithm. Bigger tileSize means bigger cells"""
        ...
    def gen_image_checked(self, width: int, height: int, checksX: int, checksY: int, col1: Color, col2: Color) -> Image:
        """Generate image: checked"""
        ...
    def gen_image_color(self, width: int, height: int, color: Color) -> Image:
        """Generate image: plain color"""
        ...
    def gen_image_font_atlas(self, chars: Any, recs: Any, charsCount: int, fontSize: int, padding: int, packMethod: int) -> Image:
        """Generate image font atlas using chars info"""
        ...
    def gen_image_gradient_h(self, width: int, height: int, left: Color, right: Color) -> Image:
        """Generate image: horizontal gradient"""
        ...
    def gen_image_gradient_radial(self, width: int, height: int, density: float, inner: Color, outer: Color) -> Image:
        """Generate image: radial gradient"""
        ...
    def gen_image_gradient_v(self, width: int, height: int, top: Color, bottom: Color) -> Image:
        """Generate image: vertical gradient"""
        ...
    def gen_image_perlin_noise(self, width: int, height: int, offsetX: int, offsetY: int, scale: float) -> Image:
        """Generate image: perlin noise"""
        ...
    def gen_image_white_noise(self, width: int, height: int, factor: float) -> Image:
        """Generate image: white noise"""
        ...
    def gen_mesh_cube(self, width: float, height: float, length: float) -> Mesh:
        """Generate cuboid mesh"""
        ...
    def gen_mesh_cubicmap(self, cubicmap: Image, cubeSize: Vector3) -> Mesh:
        """Generate cubes-based map mesh from image data"""
        ...
    def gen_mesh_cylinder(self, radius: float, height: float, slices: int) -> Mesh:
        """Generate cylinder mesh"""
        ...
    def gen_mesh_heightmap(self, heightmap: Image, size: Vector3) -> Mesh:
        """Generate heightmap mesh from image data"""
        ...
    def gen_mesh_hemi_sphere(self, radius: float, rings: int, slices: int) -> Mesh:
        """Generate half-sphere mesh (no bottom cap)"""
        ...
    def gen_mesh_knot(self, radius: float, size: float, radSeg: int, sides: int) -> Mesh:
        """Generate trefoil knot mesh"""
        ...
    def gen_mesh_plane(self, width: float, length: float, resX: int, resZ: int) -> Mesh:
        """Generate plane mesh (with subdivisions)"""
        ...
    def gen_mesh_poly(self, sides: int, radius: float) -> Mesh:
        """Generate polygonal mesh"""
        ...
    def gen_mesh_sphere(self, radius: float, rings: int, slices: int) -> Mesh:
        """Generate sphere mesh (standard sphere)"""
        ...
    def gen_mesh_torus(self, radius: float, size: float, radSeg: int, sides: int) -> Mesh:
        """Generate torus mesh"""
        ...
    def gen_texture_mipmaps(self, texture: Any) -> None:
        """Generate GPU mipmaps for a texture"""
        ...
    def get_camera_matrix(self, camera: Camera3D) -> Matrix:
        """Get camera transform matrix (view matrix)"""
        ...
    def get_camera_matrix_2d(self, camera: Camera2D) -> Matrix:
        """Get camera 2d transform matrix"""
        ...
    def get_char_pressed(self) -> int:
        """Get char pressed (unicode), call it multiple times for chars queued"""
        ...
    def get_clipboard_text(self) -> str:
        """Get clipboard text content"""
        ...
    def get_codepoints(self, text: str, count: Any) -> Any:
        """Get all codepoints in a string, codepoints count returned by parameters"""
        ...
    def get_codepoints_count(self, text: str) -> int:
        """Get total number of characters (codepoints) in a UTF8 encoded string"""
        ...
    def get_collision_ray_ground(self, Ray_0: Ray, float_1: float) -> RayHitInfo:
        """struct RayHitInfo GetCollisionRayGround(struct Ray, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_collision_ray_mesh(self, Ray_0: Ray, Mesh_1: Mesh, Matrix_2: Matrix) -> RayHitInfo:
        """struct RayHitInfo GetCollisionRayMesh(struct Ray, struct Mesh, struct Matrix);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_collision_ray_model(self, Ray_0: Ray, Model_1: Model) -> RayHitInfo:
        """struct RayHitInfo GetCollisionRayModel(struct Ray, struct Model);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_collision_ray_triangle(self, Ray_0: Ray, Vector3_1: Vector3, Vector3_2: Vector3, Vector3_3: Vector3) -> RayHitInfo:
        """struct RayHitInfo GetCollisionRayTriangle(struct Ray, struct Vector3, struct Vector3, struct Vector3);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_collision_rec(self, rec1: Rectangle, rec2: Rectangle) -> Rectangle:
        """Get collision rectangle for two rectangles collision"""
        ...
    def get_color(self, hexValue: int) -> Color:
        """Get Color structure from hexadecimal value"""
        ...
    def get_current_monitor(self) -> int:
        """Get current connected monitor"""
        ...
    def get_directory_files(self, dirPath: str, count: Any) -> str:
        """Get filenames in a directory path (memory should be freed)"""
        ...
    def get_directory_path(self, filePath: str) -> str:
        """Get full path for a given fileName with path (uses static string)"""
        ...
    def get_dropped_files(self, count: Any) -> str:
        """Get dropped files names (memory should be freed)"""
        ...
    def get_fps(self) -> int:
        """Get current FPS"""
        ...
    def get_file_extension(self, fileName: str) -> str:
        """Get pointer to extension for a filename string (includes dot: '.png')"""
        ...
    def get_file_mod_time(self, fileName: str) -> int:
        """Get file modification time (last write time)"""
        ...
    def get_file_name(self, filePath: str) -> str:
        """Get pointer to filename for a path string"""
        ...
    def get_file_name_without_ext(self, filePath: str) -> str:
        """Get filename string without extension (uses static string)"""
        ...
    def get_font_default(self) -> Font:
        """Get the default Font"""
        ...
    def get_frame_time(self) -> float:
        """Get time in seconds for last frame drawn (delta time)"""
        ...
    def get_gamepad_axis_count(self, gamepad: int) -> int:
        """Get gamepad axis count for a gamepad"""
        ...
    def get_gamepad_axis_movement(self, gamepad: int, axis: int) -> float:
        """Get axis movement value for a gamepad axis"""
        ...
    def get_gamepad_button_pressed(self) -> int:
        """Get the last gamepad button pressed"""
        ...
    def get_gamepad_name(self, gamepad: int) -> str:
        """Get gamepad internal name id"""
        ...
    def get_gesture_detected(self) -> int:
        """Get latest detected gesture"""
        ...
    def get_gesture_drag_angle(self) -> float:
        """Get gesture drag angle"""
        ...
    def get_gesture_drag_vector(self) -> Vector2:
        """Get gesture drag vector"""
        ...
    def get_gesture_hold_duration(self) -> float:
        """Get gesture hold time in milliseconds"""
        ...
    def get_gesture_pinch_angle(self) -> float:
        """Get gesture pinch angle"""
        ...
    def get_gesture_pinch_vector(self) -> Vector2:
        """Get gesture pinch delta"""
        ...
    def get_glyph_index(self, font: Font, codepoint: int) -> int:
        """Get index position for a unicode character on font"""
        ...
    def get_image_alpha_border(self, image: Image, threshold: float) -> Rectangle:
        """Get image alpha border rectangle"""
        ...
    def get_key_pressed(self) -> int:
        """Get key pressed (keycode), call it multiple times for keys queued"""
        ...
    def get_monitor_count(self) -> int:
        """Get number of connected monitors"""
        ...
    def get_monitor_height(self, monitor: int) -> int:
        """Get specified monitor height (max available by monitor)"""
        ...
    def get_monitor_name(self, monitor: int) -> str:
        """Get the human-readable, UTF-8 encoded name of the primary monitor"""
        ...
    def get_monitor_physical_height(self, monitor: int) -> int:
        """Get specified monitor physical height in millimetres"""
        ...
    def get_monitor_physical_width(self, monitor: int) -> int:
        """Get specified monitor physical width in millimetres"""
        ...
    def get_monitor_position(self, monitor: int) -> Vector2:
        """Get specified monitor position"""
        ...
    def get_monitor_refresh_rate(self, monitor: int) -> int:
        """Get specified monitor refresh rate"""
        ...
    def get_monitor_width(self, monitor: int) -> int:
        """Get specified monitor width (max available by monitor)"""
        ...
    def get_mouse_position(self) -> Vector2:
        """Get mouse position XY"""
        ...
    def get_mouse_ray(self, mousePosition: Vector2, camera: Camera3D) -> Ray:
        """Get a ray trace from mouse position"""
        ...
    def get_mouse_wheel_move(self) -> float:
        """Get mouse wheel movement Y"""
        ...
    def get_mouse_x(self) -> int:
        """Get mouse position X"""
        ...
    def get_mouse_y(self) -> int:
        """Get mouse position Y"""
        ...
    def get_music_time_length(self, music: Music) -> float:
        """Get music time length (in seconds)"""
        ...
    def get_music_time_played(self, music: Music) -> float:
        """Get current music time played (in seconds)"""
        ...
    def get_next_codepoint(self, text: str, bytesProcessed: Any) -> int:
        """Get next codepoint in a UTF8 encoded string; 0x3f('?') is returned on failure"""
        ...
    def get_pixel_color(self, srcPtr: Any, format: int) -> Color:
        """Get Color from a source pixel pointer of certain format"""
        ...
    def get_pixel_data_size(self, width: int, height: int, format: int) -> int:
        """Get pixel data size in bytes for certain format"""
        ...
    def get_prev_directory_path(self, dirPath: str) -> str:
        """Get previous directory path for a given path (uses static string)"""
        ...
    def get_random_value(self, min: int, max: int) -> int:
        """Get a random value between min and max (both included)"""
        ...
    def get_screen_data(self) -> Image:
        """Get pixel data from screen buffer and return an Image (screenshot)"""
        ...
    def get_screen_height(self) -> int:
        """Get current screen height"""
        ...
    def get_screen_to_world_2d(self, position: Vector2, camera: Camera2D) -> Vector2:
        """Get the world space position for a 2d camera screen space position"""
        ...
    def get_screen_width(self) -> int:
        """Get current screen width"""
        ...
    def get_shader_location(self, shader: Shader, uniformName: str) -> int:
        """Get shader uniform location"""
        ...
    def get_shader_location_attrib(self, shader: Shader, attribName: str) -> int:
        """Get shader attribute location"""
        ...
    def get_sounds_playing(self) -> int:
        """Get number of sounds playing in the multichannel"""
        ...
    def get_texture_data(self, texture: Texture) -> Image:
        """Get pixel data from GPU texture and return an Image"""
        ...
    def get_time(self) -> float:
        """Get elapsed time in seconds since InitWindow()"""
        ...
    def get_touch_points_count(self) -> int:
        """Get touch points count"""
        ...
    def get_touch_position(self, index: int) -> Vector2:
        """Get touch position XY for a touch point index (relative to screen size)"""
        ...
    def get_touch_x(self) -> int:
        """Get touch position X for touch point 0 (relative to screen size)"""
        ...
    def get_touch_y(self) -> int:
        """Get touch position Y for touch point 0 (relative to screen size)"""
        ...
    def get_window_handle(self) -> Any:
        """Get native window handle"""
        ...
    def get_window_position(self) -> Vector2:
        """Get window position XY on monitor"""
        ...
    def get_window_scale_dpi(self) -> Vector2:
        """Get window scale DPI factor"""
        ...
    def get_working_directory(self) -> str:
        """Get current working directory (uses static string)"""
        ...
    def get_world_to_screen(self, position: Vector3, camera: Camera3D) -> Vector2:
        """Get the screen space position for a 3d world space position"""
        ...
    def get_world_to_screen_2d(self, position: Vector2, camera: Camera2D) -> Vector2:
        """Get the screen space position for a 2d camera world space position"""
        ...
    def get_world_to_screen_ex(self, position: Vector3, camera: Camera3D, width: int, height: int) -> Vector2:
        """Get size position for a 3d world space position"""
        ...
    def hide_cursor(self) -> None:
        """Hides cursor"""
        ...
    def image_alpha_clear(self, image: Any, color: Color, threshold: float) -> None:
        """Clear alpha channel to desired color"""
        ...
    def image_alpha_crop(self, image: Any, threshold: float) -> None:
        """Crop image depending on alpha value"""
        ...
    def image_alpha_mask(self, image: Any, alphaMask: Image) -> None:
        """Apply alpha mask to image"""
        ...
    def image_alpha_premultiply(self, image: Any) -> None:
        """Premultiply alpha channel"""
        ...
    def image_clear_background(self, dst: Any, color: Color) -> None:
        """Clear image background with given color"""
        ...
    def image_color_brightness(self, image: Any, brightness: int) -> None:
        """Modify image color: brightness (-255 to 255)"""
        ...
    def image_color_contrast(self, image: Any, contrast: float) -> None:
        """Modify image color: contrast (-100 to 100)"""
        ...
    def image_color_grayscale(self, image: Any) -> None:
        """Modify image color: grayscale"""
        ...
    def image_color_invert(self, image: Any) -> None:
        """Modify image color: invert"""
        ...
    def image_color_replace(self, image: Any, color: Color, replace: Color) -> None:
        """Modify image color: replace color"""
        ...
    def image_color_tint(self, image: Any, color: Color) -> None:
        """Modify image color: tint"""
        ...
    def image_copy(self, image: Image) -> Image:
        """Create an image duplicate (useful for transformations)"""
        ...
    def image_crop(self, image: Any, crop: Rectangle) -> None:
        """Crop an image to a defined rectangle"""
        ...
    def image_dither(self, image: Any, rBpp: int, gBpp: int, bBpp: int, aBpp: int) -> None:
        """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
        ...
    def image_draw(self, dst: Any, src: Image, srcRec: Rectangle, dstRec: Rectangle, tint: Color) -> None:
        """Draw a source image within a destination image (tint applied to source)"""
        ...
    def image_draw_circle(self, dst: Any, centerX: int, centerY: int, radius: int, color: Color) -> None:
        """Draw circle within an image"""
        ...
    def image_draw_circle_v(self, dst: Any, center: Vector2, radius: int, color: Color) -> None:
        """Draw circle within an image (Vector version)"""
        ...
    def image_draw_line(self, dst: Any, startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None:
        """Draw line within an image"""
        ...
    def image_draw_line_v(self, dst: Any, start: Vector2, end: Vector2, color: Color) -> None:
        """Draw line within an image (Vector version)"""
        ...
    def image_draw_pixel(self, dst: Any, posX: int, posY: int, color: Color) -> None:
        """Draw pixel within an image"""
        ...
    def image_draw_pixel_v(self, dst: Any, position: Vector2, color: Color) -> None:
        """Draw pixel within an image (Vector version)"""
        ...
    def image_draw_rectangle(self, dst: Any, posX: int, posY: int, width: int, height: int, color: Color) -> None:
        """Draw rectangle within an image"""
        ...
    def image_draw_rectangle_lines(self, dst: Any, rec: Rectangle, thick: int, color: Color) -> None:
        """Draw rectangle lines within an image"""
        ...
    def image_draw_rectangle_rec(self, dst: Any, rec: Rectangle, color: Color) -> None:
        """Draw rectangle within an image"""
        ...
    def image_draw_rectangle_v(self, dst: Any, position: Vector2, size: Vector2, color: Color) -> None:
        """Draw rectangle within an image (Vector version)"""
        ...
    def image_draw_text(self, dst: Any, text: str, posX: int, posY: int, fontSize: int, color: Color) -> None:
        """Draw text (using default font) within an image (destination)"""
        ...
    def image_draw_text_ex(self, dst: Any, font: Font, text: str, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None:
        """Draw text (custom sprite font) within an image (destination)"""
        ...
    def image_flip_horizontal(self, image: Any) -> None:
        """Flip image horizontally"""
        ...
    def image_flip_vertical(self, image: Any) -> None:
        """Flip image vertically"""
        ...
    def image_format(self, image: Any, newFormat: int) -> None:
        """Convert image data to desired format"""
        ...
    def image_from_image(self, image: Image, rec: Rectangle) -> Image:
        """Create an image from another image piece"""
        ...
    def image_mipmaps(self, image: Any) -> None:
        """Compute all mipmap levels for a provided image"""
        ...
    def image_resize(self, image: Any, newWidth: int, newHeight: int) -> None:
        """Resize image (Bicubic scaling algorithm)"""
        ...
    def image_resize_canvas(self, image: Any, newWidth: int, newHeight: int, offsetX: int, offsetY: int, fill: Color) -> None:
        """Resize canvas and fill with color"""
        ...
    def image_resize_nn(self, image: Any, newWidth: int, newHeight: int) -> None:
        """Resize image (Nearest-Neighbor scaling algorithm)"""
        ...
    def image_rotate_ccw(self, image: Any) -> None:
        """Rotate image counter-clockwise 90deg"""
        ...
    def image_rotate_cw(self, image: Any) -> None:
        """Rotate image clockwise 90deg"""
        ...
    def image_text(self, text: str, fontSize: int, color: Color) -> Image:
        """Create an image from text (default font)"""
        ...
    def image_text_ex(self, font: Font, text: str, fontSize: float, spacing: float, tint: Color) -> Image:
        """Create an image from text (custom sprite font)"""
        ...
    def image_to_pot(self, image: Any, fill: Color) -> None:
        """Convert image to POT (power-of-two)"""
        ...
    def init_audio_device(self) -> None:
        """Initialize audio device and context"""
        ...
    def init_audio_stream(self, unsignedint_0: int, unsignedint_1: int, unsignedint_2: int) -> AudioStream:
        """struct AudioStream InitAudioStream(unsigned int, unsigned int, unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def init_window(self, width: int, height: int, title: str) -> None:
        """Initialize window and OpenGL context"""
        ...
    def is_audio_device_ready(self) -> bool:
        """Check if audio device has been initialized successfully"""
        ...
    def is_audio_stream_playing(self, stream: AudioStream) -> bool:
        """Check if audio stream is playing"""
        ...
    def is_audio_stream_processed(self, stream: AudioStream) -> bool:
        """Check if any audio stream buffers requires refill"""
        ...
    def is_cursor_hidden(self) -> bool:
        """Check if cursor is not visible"""
        ...
    def is_cursor_on_screen(self) -> bool:
        """Check if cursor is on the screen"""
        ...
    def is_file_dropped(self) -> bool:
        """Check if a file has been dropped into window"""
        ...
    def is_file_extension(self, fileName: str, ext: str) -> bool:
        """Check file extension (including point: .png, .wav)"""
        ...
    def is_gamepad_available(self, gamepad: int) -> bool:
        """Check if a gamepad is available"""
        ...
    def is_gamepad_button_down(self, gamepad: int, button: int) -> bool:
        """Check if a gamepad button is being pressed"""
        ...
    def is_gamepad_button_pressed(self, gamepad: int, button: int) -> bool:
        """Check if a gamepad button has been pressed once"""
        ...
    def is_gamepad_button_released(self, gamepad: int, button: int) -> bool:
        """Check if a gamepad button has been released once"""
        ...
    def is_gamepad_button_up(self, gamepad: int, button: int) -> bool:
        """Check if a gamepad button is NOT being pressed"""
        ...
    def is_gamepad_name(self, gamepad: int, name: str) -> bool:
        """Check gamepad name (if available)"""
        ...
    def is_gesture_detected(self, gesture: int) -> bool:
        """Check if a gesture have been detected"""
        ...
    def is_key_down(self, key: int) -> bool:
        """Check if a key is being pressed"""
        ...
    def is_key_pressed(self, key: int) -> bool:
        """Check if a key has been pressed once"""
        ...
    def is_key_released(self, key: int) -> bool:
        """Check if a key has been released once"""
        ...
    def is_key_up(self, key: int) -> bool:
        """Check if a key is NOT being pressed"""
        ...
    def is_model_animation_valid(self, model: Model, anim: ModelAnimation) -> bool:
        """Check model animation skeleton match"""
        ...
    def is_mouse_button_down(self, button: int) -> bool:
        """Check if a mouse button is being pressed"""
        ...
    def is_mouse_button_pressed(self, button: int) -> bool:
        """Check if a mouse button has been pressed once"""
        ...
    def is_mouse_button_released(self, button: int) -> bool:
        """Check if a mouse button has been released once"""
        ...
    def is_mouse_button_up(self, button: int) -> bool:
        """Check if a mouse button is NOT being pressed"""
        ...
    def is_music_playing(self, Music_0: Music) -> bool:
        """_Bool IsMusicPlaying(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_sound_playing(self, sound: Sound) -> bool:
        """Check if a sound is currently playing"""
        ...
    def is_window_focused(self) -> bool:
        """Check if window is currently focused (only PLATFORM_DESKTOP)"""
        ...
    def is_window_fullscreen(self) -> bool:
        """Check if window is currently fullscreen"""
        ...
    def is_window_hidden(self) -> bool:
        """Check if window is currently hidden (only PLATFORM_DESKTOP)"""
        ...
    def is_window_maximized(self) -> bool:
        """Check if window is currently maximized (only PLATFORM_DESKTOP)"""
        ...
    def is_window_minimized(self) -> bool:
        """Check if window is currently minimized (only PLATFORM_DESKTOP)"""
        ...
    def is_window_ready(self) -> bool:
        """Check if window has been initialized successfully"""
        ...
    def is_window_resized(self) -> bool:
        """Check if window has been resized last frame"""
        ...
    def is_window_state(self, flag: int) -> bool:
        """Check if one specific window flag is enabled"""
        ...
    KEY_A: int
    KEY_APOSTROPHE: int
    KEY_B: int
    KEY_BACK: int
    KEY_BACKSLASH: int
    KEY_BACKSPACE: int
    KEY_C: int
    KEY_CAPS_LOCK: int
    KEY_COMMA: int
    KEY_D: int
    KEY_DELETE: int
    KEY_DOWN: int
    KEY_E: int
    KEY_EIGHT: int
    KEY_END: int
    KEY_ENTER: int
    KEY_EQUAL: int
    KEY_ESCAPE: int
    KEY_F: int
    KEY_F1: int
    KEY_F10: int
    KEY_F11: int
    KEY_F12: int
    KEY_F2: int
    KEY_F3: int
    KEY_F4: int
    KEY_F5: int
    KEY_F6: int
    KEY_F7: int
    KEY_F8: int
    KEY_F9: int
    KEY_FIVE: int
    KEY_FOUR: int
    KEY_G: int
    KEY_GRAVE: int
    KEY_H: int
    KEY_HOME: int
    KEY_I: int
    KEY_INSERT: int
    KEY_J: int
    KEY_K: int
    KEY_KB_MENU: int
    KEY_KP_0: int
    KEY_KP_1: int
    KEY_KP_2: int
    KEY_KP_3: int
    KEY_KP_4: int
    KEY_KP_5: int
    KEY_KP_6: int
    KEY_KP_7: int
    KEY_KP_8: int
    KEY_KP_9: int
    KEY_KP_ADD: int
    KEY_KP_DECIMAL: int
    KEY_KP_DIVIDE: int
    KEY_KP_ENTER: int
    KEY_KP_EQUAL: int
    KEY_KP_MULTIPLY: int
    KEY_KP_SUBTRACT: int
    KEY_L: int
    KEY_LEFT: int
    KEY_LEFT_ALT: int
    KEY_LEFT_BRACKET: int
    KEY_LEFT_CONTROL: int
    KEY_LEFT_SHIFT: int
    KEY_LEFT_SUPER: int
    KEY_M: int
    KEY_MENU: int
    KEY_MINUS: int
    KEY_N: int
    KEY_NINE: int
    KEY_NULL: int
    KEY_NUM_LOCK: int
    KEY_O: int
    KEY_ONE: int
    KEY_P: int
    KEY_PAGE_DOWN: int
    KEY_PAGE_UP: int
    KEY_PAUSE: int
    KEY_PERIOD: int
    KEY_PRINT_SCREEN: int
    KEY_Q: int
    KEY_R: int
    KEY_RIGHT: int
    KEY_RIGHT_ALT: int
    KEY_RIGHT_BRACKET: int
    KEY_RIGHT_CONTROL: int
    KEY_RIGHT_SHIFT: int
    KEY_RIGHT_SUPER: int
    KEY_S: int
    KEY_SCROLL_LOCK: int
    KEY_SEMICOLON: int
    KEY_SEVEN: int
    KEY_SIX: int
    KEY_SLASH: int
    KEY_SPACE: int
    KEY_T: int
    KEY_TAB: int
    KEY_THREE: int
    KEY_TWO: int
    KEY_U: int
    KEY_UP: int
    KEY_V: int
    KEY_VOLUME_DOWN: int
    KEY_VOLUME_UP: int
    KEY_W: int
    KEY_X: int
    KEY_Y: int
    KEY_Z: int
    KEY_ZERO: int
    LOG_ALL: int
    LOG_DEBUG: int
    LOG_ERROR: int
    LOG_FATAL: int
    LOG_INFO: int
    LOG_NONE: int
    LOG_TRACE: int
    LOG_WARNING: int
    def load_file_data(self, fileName: str, bytesRead: Any) -> str:
        """Load file data as byte array (read)"""
        ...
    def load_file_text(self, fileName: str) -> str:
        """Load text data from file (read), returns a ' 0' terminated string"""
        ...
    def load_font(self, fileName: str) -> Font:
        """Load font from file into GPU memory (VRAM)"""
        ...
    def load_font_data(self, fileData: str, dataSize: int, fontSize: int, fontChars: Any, charsCount: int, type: int) -> Any:
        """Load font data for further use"""
        ...
    def load_font_ex(self, fileName: str, fontSize: int, fontChars: Any, charsCount: int) -> Font:
        """Load font from file with extended parameters"""
        ...
    def load_font_from_image(self, image: Image, key: Color, firstChar: int) -> Font:
        """Load font from Image (XNA style)"""
        ...
    def load_font_from_memory(self, fileType: str, fileData: str, dataSize: int, fontSize: int, fontChars: Any, charsCount: int) -> Font:
        """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
        ...
    def load_image(self, fileName: str) -> Image:
        """Load image from file into CPU memory (RAM)"""
        ...
    def load_image_anim(self, fileName: str, frames: Any) -> Image:
        """Load image sequence from file (frames appended to image.data)"""
        ...
    def load_image_colors(self, image: Image) -> Any:
        """Load color data from image as a Color array (RGBA - 32bit)"""
        ...
    def load_image_from_memory(self, fileType: str, fileData: str, dataSize: int) -> Image:
        """Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
        ...
    def load_image_palette(self, image: Image, maxPaletteSize: int, colorsCount: Any) -> Any:
        """Load colors palette from image as a Color array (RGBA - 32bit)"""
        ...
    def load_image_raw(self, fileName: str, width: int, height: int, format: int, headerSize: int) -> Image:
        """Load image from RAW file data"""
        ...
    def load_material_default(self) -> Material:
        """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
        ...
    def load_materials(self, fileName: str, materialCount: Any) -> Any:
        """Load materials from model file"""
        ...
    def load_model(self, fileName: str) -> Model:
        """Load model from files (meshes and materials)"""
        ...
    def load_model_animations(self, fileName: str, animsCount: Any) -> Any:
        """Load model animations from file"""
        ...
    def load_model_from_mesh(self, mesh: Mesh) -> Model:
        """Load model from generated mesh (default material)"""
        ...
    def load_music_stream(self, fileName: str) -> Music:
        """Load music stream from file"""
        ...
    def load_music_stream_from_memory(self, fileType: str, data: str, dataSize: int) -> Music:
        """Load music stream from data"""
        ...
    def load_render_texture(self, width: int, height: int) -> RenderTexture:
        """Load texture for rendering (framebuffer)"""
        ...
    def load_shader(self, vsFileName: str, fsFileName: str) -> Shader:
        """Load shader from files and bind default locations"""
        ...
    def load_shader_from_memory(self, vsCode: str, fsCode: str) -> Shader:
        """Load shader from code strings and bind default locations"""
        ...
    def load_sound(self, fileName: str) -> Sound:
        """Load sound from file"""
        ...
    def load_sound_from_wave(self, wave: Wave) -> Sound:
        """Load sound from wave data"""
        ...
    def load_storage_value(self, position: int) -> int:
        """Load integer value from storage file (from defined position)"""
        ...
    def load_texture(self, fileName: str) -> Texture:
        """Load texture from file into GPU memory (VRAM)"""
        ...
    def load_texture_cubemap(self, image: Image, layout: int) -> Texture:
        """Load cubemap from image, multiple image cubemap layouts supported"""
        ...
    def load_texture_from_image(self, image: Image) -> Texture:
        """Load texture from image data"""
        ...
    def load_vr_stereo_config(self, device: VrDeviceInfo) -> VrStereoConfig:
        """Load VR stereo config for VR simulator device parameters"""
        ...
    def load_wave(self, fileName: str) -> Wave:
        """Load wave data from file"""
        ...
    def load_wave_from_memory(self, fileType: str, fileData: str, dataSize: int) -> Wave:
        """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
        ...
    def load_wave_samples(self, wave: Wave) -> Any:
        """Load samples data from wave as a floats array"""
        ...
    MATERIAL_MAP_ALBEDO: int
    MATERIAL_MAP_BRDG: int
    MATERIAL_MAP_CUBEMAP: int
    MATERIAL_MAP_DIFFUSE: int
    MATERIAL_MAP_EMISSION: int
    MATERIAL_MAP_HEIGHT: int
    MATERIAL_MAP_IRRADIANCE: int
    MATERIAL_MAP_METALNESS: int
    MATERIAL_MAP_NORMAL: int
    MATERIAL_MAP_OCCLUSION: int
    MATERIAL_MAP_PREFILTER: int
    MATERIAL_MAP_ROUGHNESS: int
    MATERIAL_MAP_SPECULAR: int
    MOUSE_CURSOR_ARROW: int
    MOUSE_CURSOR_CROSSHAIR: int
    MOUSE_CURSOR_DEFAULT: int
    MOUSE_CURSOR_IBEAM: int
    MOUSE_CURSOR_NOT_ALLOWED: int
    MOUSE_CURSOR_POINTING_HAND: int
    MOUSE_CURSOR_RESIZE_ALL: int
    MOUSE_CURSOR_RESIZE_EW: int
    MOUSE_CURSOR_RESIZE_NESW: int
    MOUSE_CURSOR_RESIZE_NS: int
    MOUSE_CURSOR_RESIZE_NWSE: int
    MOUSE_LEFT_BUTTON: int
    MOUSE_MIDDLE_BUTTON: int
    MOUSE_RIGHT_BUTTON: int
    def maximize_window(self) -> None:
        """Set window state: maximized, if resizable (only PLATFORM_DESKTOP)"""
        ...
    def measure_text(self, text: str, fontSize: int) -> int:
        """Measure string width for default font"""
        ...
    def measure_text_ex(self, font: Font, text: str, fontSize: float, spacing: float) -> Vector2:
        """Measure string size for Font"""
        ...
    def mem_alloc(self, size: int) -> Any:
        """Internal memory allocator"""
        ...
    def mem_free(self, ptr: Any) -> None:
        """Internal memory free"""
        ...
    def mem_realloc(self, ptr: Any, size: int) -> Any:
        """Internal memory reallocator"""
        ...
    def mesh_binormals(self, mesh: Any) -> None:
        """Compute mesh binormals"""
        ...
    def mesh_bounding_box(self, Mesh_0: Mesh) -> BoundingBox:
        """struct BoundingBox MeshBoundingBox(struct Mesh);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mesh_tangents(self, mesh: Any) -> None:
        """Compute mesh tangents"""
        ...
    def minimize_window(self) -> None:
        """Set window state: minimized, if resizable (only PLATFORM_DESKTOP)"""
        ...
    NPATCH_NINE_PATCH: int
    NPATCH_THREE_PATCH_HORIZONTAL: int
    NPATCH_THREE_PATCH_VERTICAL: int
    def open_url(self, url: str) -> None:
        """Open URL with default system browser (if available)"""
        ...
    PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA: int
    PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA: int
    PIXELFORMAT_COMPRESSED_DXT1_RGB: int
    PIXELFORMAT_COMPRESSED_DXT1_RGBA: int
    PIXELFORMAT_COMPRESSED_DXT3_RGBA: int
    PIXELFORMAT_COMPRESSED_DXT5_RGBA: int
    PIXELFORMAT_COMPRESSED_ETC1_RGB: int
    PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA: int
    PIXELFORMAT_COMPRESSED_ETC2_RGB: int
    PIXELFORMAT_COMPRESSED_PVRT_RGB: int
    PIXELFORMAT_COMPRESSED_PVRT_RGBA: int
    PIXELFORMAT_UNCOMPRESSED_GRAYSCALE: int
    PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA: int
    PIXELFORMAT_UNCOMPRESSED_R32: int
    PIXELFORMAT_UNCOMPRESSED_R32G32B32: int
    PIXELFORMAT_UNCOMPRESSED_R32G32B32A32: int
    PIXELFORMAT_UNCOMPRESSED_R4G4B4A4: int
    PIXELFORMAT_UNCOMPRESSED_R5G5B5A1: int
    PIXELFORMAT_UNCOMPRESSED_R5G6B5: int
    PIXELFORMAT_UNCOMPRESSED_R8G8B8: int
    PIXELFORMAT_UNCOMPRESSED_R8G8B8A8: int
    def pause_audio_stream(self, stream: AudioStream) -> None:
        """Pause audio stream"""
        ...
    def pause_music_stream(self, music: Music) -> None:
        """Pause music playing"""
        ...
    def pause_sound(self, sound: Sound) -> None:
        """Pause a sound"""
        ...
    def play_audio_stream(self, stream: AudioStream) -> None:
        """Play audio stream"""
        ...
    def play_music_stream(self, music: Music) -> None:
        """Start music playing"""
        ...
    def play_sound(self, sound: Sound) -> None:
        """Play a sound"""
        ...
    def play_sound_multi(self, sound: Sound) -> None:
        """Play a sound (using multichannel buffer pool)"""
        ...
    def restore_window(self) -> None:
        """Set window state: not minimized/maximized (only PLATFORM_DESKTOP)"""
        ...
    def resume_audio_stream(self, stream: AudioStream) -> None:
        """Resume audio stream"""
        ...
    def resume_music_stream(self, music: Music) -> None:
        """Resume playing paused music"""
        ...
    def resume_sound(self, sound: Sound) -> None:
        """Resume a paused sound"""
        ...
    SHADER_LOC_COLOR_AMBIENT: int
    SHADER_LOC_COLOR_DIFFUSE: int
    SHADER_LOC_COLOR_SPECULAR: int
    SHADER_LOC_MAP_ALBEDO: int
    SHADER_LOC_MAP_BRDF: int
    SHADER_LOC_MAP_CUBEMAP: int
    SHADER_LOC_MAP_DIFFUSE: int
    SHADER_LOC_MAP_EMISSION: int
    SHADER_LOC_MAP_HEIGHT: int
    SHADER_LOC_MAP_IRRADIANCE: int
    SHADER_LOC_MAP_METALNESS: int
    SHADER_LOC_MAP_NORMAL: int
    SHADER_LOC_MAP_OCCLUSION: int
    SHADER_LOC_MAP_PREFILTER: int
    SHADER_LOC_MAP_ROUGHNESS: int
    SHADER_LOC_MAP_SPECULAR: int
    SHADER_LOC_MATRIX_MODEL: int
    SHADER_LOC_MATRIX_MVP: int
    SHADER_LOC_MATRIX_NORMAL: int
    SHADER_LOC_MATRIX_PROJECTION: int
    SHADER_LOC_MATRIX_VIEW: int
    SHADER_LOC_VECTOR_VIEW: int
    SHADER_LOC_VERTEX_COLOR: int
    SHADER_LOC_VERTEX_NORMAL: int
    SHADER_LOC_VERTEX_POSITION: int
    SHADER_LOC_VERTEX_TANGENT: int
    SHADER_LOC_VERTEX_TEXCOORD01: int
    SHADER_LOC_VERTEX_TEXCOORD02: int
    SHADER_UNIFORM_FLOAT: int
    SHADER_UNIFORM_INT: int
    SHADER_UNIFORM_IVEC2: int
    SHADER_UNIFORM_IVEC3: int
    SHADER_UNIFORM_IVEC4: int
    SHADER_UNIFORM_SAMPLER2D: int
    SHADER_UNIFORM_VEC2: int
    SHADER_UNIFORM_VEC3: int
    SHADER_UNIFORM_VEC4: int
    def save_file_data(self, fileName: str, data: Any, bytesToWrite: int) -> bool:
        """Save data to file from byte array (write), returns true on success"""
        ...
    def save_file_text(self, fileName: str, text: str) -> bool:
        """Save text data to file (write), string must be ' 0' terminated, returns true on success"""
        ...
    def save_storage_value(self, position: int, value: int) -> bool:
        """Save integer value to storage file (to defined position), returns true on success"""
        ...
    def set_audio_stream_buffer_size_default(self, size: int) -> None:
        """Default size for new audio streams"""
        ...
    def set_audio_stream_pitch(self, stream: AudioStream, pitch: float) -> None:
        """Set pitch for audio stream (1.0 is base level)"""
        ...
    def set_audio_stream_volume(self, stream: AudioStream, volume: float) -> None:
        """Set volume for audio stream (1.0 is max level)"""
        ...
    def set_camera_alt_control(self, keyAlt: int) -> None:
        """Set camera alt key to combine with mouse movement (free camera)"""
        ...
    def set_camera_mode(self, camera: Camera3D, mode: int) -> None:
        """Set camera mode (multiple camera modes available)"""
        ...
    def set_camera_move_controls(self, keyFront: int, keyBack: int, keyRight: int, keyLeft: int, keyUp: int, keyDown: int) -> None:
        """Set camera move controls (1st person and 3rd person cameras)"""
        ...
    def set_camera_pan_control(self, keyPan: int) -> None:
        """Set camera pan key to combine with mouse movement (free camera)"""
        ...
    def set_camera_smooth_zoom_control(self, keySmoothZoom: int) -> None:
        """Set camera smooth zoom key to combine with mouse (free camera)"""
        ...
    def set_clipboard_text(self, text: str) -> None:
        """Set clipboard text content"""
        ...
    def set_config_flags(self, flags: int) -> None:
        """Setup init configuration flags (view FLAGS)"""
        ...
    def set_exit_key(self, key: int) -> None:
        """Set a custom key to exit program (default is ESC)"""
        ...
    def set_gamepad_mappings(self, mappings: str) -> int:
        """Set internal gamepad mappings (SDL_GameControllerDB)"""
        ...
    def set_gestures_enabled(self, flags: int) -> None:
        """Enable a set of gestures using flags"""
        ...
    def set_master_volume(self, volume: float) -> None:
        """Set master volume (listener)"""
        ...
    def set_material_texture(self, material: Any, mapType: int, texture: Texture) -> None:
        """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
        ...
    def set_model_mesh_material(self, model: Any, meshId: int, materialId: int) -> None:
        """Set material for a mesh"""
        ...
    def set_mouse_cursor(self, cursor: int) -> None:
        """Set mouse cursor"""
        ...
    def set_mouse_offset(self, offsetX: int, offsetY: int) -> None:
        """Set mouse offset"""
        ...
    def set_mouse_position(self, x: int, y: int) -> None:
        """Set mouse position XY"""
        ...
    def set_mouse_scale(self, scaleX: float, scaleY: float) -> None:
        """Set mouse scaling"""
        ...
    def set_music_pitch(self, music: Music, pitch: float) -> None:
        """Set pitch for a music (1.0 is base level)"""
        ...
    def set_music_volume(self, music: Music, volume: float) -> None:
        """Set volume for music (1.0 is max level)"""
        ...
    def set_pixel_color(self, dstPtr: Any, color: Color, format: int) -> None:
        """Set color formatted into destination pixel pointer"""
        ...
    def set_shader_value(self, shader: Shader, locIndex: int, value: Any, uniformType: int) -> None:
        """Set shader uniform value"""
        ...
    def set_shader_value_matrix(self, shader: Shader, locIndex: int, mat: Matrix) -> None:
        """Set shader uniform value (matrix 4x4)"""
        ...
    def set_shader_value_texture(self, shader: Shader, locIndex: int, texture: Texture) -> None:
        """Set shader uniform value for texture (sampler2d)"""
        ...
    def set_shader_value_v(self, shader: Shader, locIndex: int, value: Any, uniformType: int, count: int) -> None:
        """Set shader uniform value vector"""
        ...
    def set_shapes_texture(self, texture: Texture, source: Rectangle) -> None:
        """Set texture and rectangle to be used on shapes drawing"""
        ...
    def set_sound_pitch(self, sound: Sound, pitch: float) -> None:
        """Set pitch for a sound (1.0 is base level)"""
        ...
    def set_sound_volume(self, sound: Sound, volume: float) -> None:
        """Set volume for a sound (1.0 is max level)"""
        ...
    def set_target_fps(self, fps: int) -> None:
        """Set target FPS (maximum)"""
        ...
    def set_texture_filter(self, texture: Texture, filter: int) -> None:
        """Set texture scaling filter mode"""
        ...
    def set_texture_wrap(self, texture: Texture, wrap: int) -> None:
        """Set texture wrapping mode"""
        ...
    def set_trace_log_level(self, logLevel: int) -> None:
        """Set the current threshold (minimum) log level"""
        ...
    def set_window_icon(self, image: Image) -> None:
        """Set icon for window (only PLATFORM_DESKTOP)"""
        ...
    def set_window_min_size(self, width: int, height: int) -> None:
        """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
        ...
    def set_window_monitor(self, monitor: int) -> None:
        """Set monitor for the current window (fullscreen mode)"""
        ...
    def set_window_position(self, x: int, y: int) -> None:
        """Set window position on screen (only PLATFORM_DESKTOP)"""
        ...
    def set_window_size(self, width: int, height: int) -> None:
        """Set window dimensions"""
        ...
    def set_window_state(self, flags: int) -> None:
        """Set window configuration state using flags"""
        ...
    def set_window_title(self, title: str) -> None:
        """Set title for window (only PLATFORM_DESKTOP)"""
        ...
    def show_cursor(self) -> None:
        """Shows cursor"""
        ...
    def stop_audio_stream(self, stream: AudioStream) -> None:
        """Stop audio stream"""
        ...
    def stop_music_stream(self, music: Music) -> None:
        """Stop music playing"""
        ...
    def stop_sound(self, sound: Sound) -> None:
        """Stop playing a sound"""
        ...
    def stop_sound_multi(self) -> None:
        """Stop any sound playing (using multichannel buffer pool)"""
        ...
    TEXTURE_FILTER_ANISOTROPIC_16X: int
    TEXTURE_FILTER_ANISOTROPIC_4X: int
    TEXTURE_FILTER_ANISOTROPIC_8X: int
    TEXTURE_FILTER_BILINEAR: int
    TEXTURE_FILTER_POINT: int
    TEXTURE_FILTER_TRILINEAR: int
    TEXTURE_WRAP_CLAMP: int
    TEXTURE_WRAP_MIRROR_CLAMP: int
    TEXTURE_WRAP_MIRROR_REPEAT: int
    TEXTURE_WRAP_REPEAT: int
    def take_screenshot(self, fileName: str) -> None:
        """Takes a screenshot of current screen (filename extension defines format)"""
        ...
    def text_append(self, text: str, append: str, position: Any) -> None:
        """Append text at specific position and move cursor!"""
        ...
    def text_copy(self, dst: str, src: str) -> int:
        """Copy one string to another, returns bytes copied"""
        ...
    def text_find_index(self, text: str, find: str) -> int:
        """Find first text occurrence within a string"""
        ...
    def text_format(self, *args) -> str:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
    def text_insert(self, text: str, insert: str, position: int) -> str:
        """Insert text in a position (memory must be freed!)"""
        ...
    def text_is_equal(self, text1: str, text2: str) -> bool:
        """Check if two text string are equal"""
        ...
    def text_join(self, textList: str, count: int, delimiter: str) -> str:
        """Join text strings with delimiter"""
        ...
    def text_length(self, text: str) -> int:
        """Get text length, checks for ' 0' ending"""
        ...
    def text_replace(self, text: str, replace: str, by: str) -> str:
        """Replace text string (memory must be freed!)"""
        ...
    def text_split(self, text: str, delimiter: str, count: Any) -> str:
        """Split text into multiple strings"""
        ...
    def text_subtext(self, text: str, position: int, length: int) -> str:
        """Get a piece of a text string"""
        ...
    def text_to_integer(self, text: str) -> int:
        """Get integer value from text (negative values not supported)"""
        ...
    def text_to_lower(self, text: str) -> str:
        """Get lower case version of provided string"""
        ...
    def text_to_pascal(self, text: str) -> str:
        """Get Pascal case notation version of provided string"""
        ...
    def text_to_upper(self, text: str) -> str:
        """Get upper case version of provided string"""
        ...
    def text_to_utf8(self, codepoints: Any, length: int) -> str:
        """Encode text codepoint into utf8 text (memory must be freed!)"""
        ...
    def toggle_fullscreen(self) -> None:
        """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
        ...
    def trace_log(self, *args) -> None:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
    def unload_file_data(self, data: str) -> None:
        """Unload file data allocated by LoadFileData()"""
        ...
    def unload_file_text(self, text: str) -> None:
        """Unload file text data allocated by LoadFileText()"""
        ...
    def unload_font(self, font: Font) -> None:
        """Unload Font from GPU memory (VRAM)"""
        ...
    def unload_font_data(self, chars: Any, charsCount: int) -> None:
        """Unload font chars info data (RAM)"""
        ...
    def unload_image(self, image: Image) -> None:
        """Unload image from CPU memory (RAM)"""
        ...
    def unload_image_colors(self, colors: Any) -> None:
        """Unload color data loaded with LoadImageColors()"""
        ...
    def unload_image_palette(self, colors: Any) -> None:
        """Unload colors palette loaded with LoadImagePalette()"""
        ...
    def unload_material(self, material: Material) -> None:
        """Unload material from GPU memory (VRAM)"""
        ...
    def unload_mesh(self, mesh: Mesh) -> None:
        """Unload mesh data from CPU and GPU"""
        ...
    def unload_model(self, model: Model) -> None:
        """Unload model (including meshes) from memory (RAM and/or VRAM)"""
        ...
    def unload_model_animation(self, anim: ModelAnimation) -> None:
        """Unload animation data"""
        ...
    def unload_model_animations(self, animations: Any, count: int) -> None:
        """Unload animation array data"""
        ...
    def unload_model_keep_meshes(self, model: Model) -> None:
        """Unload model (but not meshes) from memory (RAM and/or VRAM)"""
        ...
    def unload_music_stream(self, music: Music) -> None:
        """Unload music stream"""
        ...
    def unload_render_texture(self, target: RenderTexture) -> None:
        """Unload render texture from GPU memory (VRAM)"""
        ...
    def unload_shader(self, shader: Shader) -> None:
        """Unload shader from GPU memory (VRAM)"""
        ...
    def unload_sound(self, sound: Sound) -> None:
        """Unload sound"""
        ...
    def unload_texture(self, texture: Texture) -> None:
        """Unload texture from GPU memory (VRAM)"""
        ...
    def unload_vr_stereo_config(self, config: VrStereoConfig) -> None:
        """Unload VR stereo config"""
        ...
    def unload_wave(self, wave: Wave) -> None:
        """Unload wave data"""
        ...
    def unload_wave_samples(self, samples: Any) -> None:
        """Unload samples data loaded with LoadWaveSamples()"""
        ...
    def update_audio_stream(self, stream: AudioStream, data: Any, samplesCount: int) -> None:
        """Update audio stream buffers with data"""
        ...
    def update_camera(self, camera: Any) -> None:
        """Update camera position for selected mode"""
        ...
    def update_mesh_buffer(self, mesh: Mesh, index: int, data: Any, dataSize: int, offset: int) -> None:
        """Update mesh vertex data in GPU for a specific buffer index"""
        ...
    def update_model_animation(self, model: Model, anim: ModelAnimation, frame: int) -> None:
        """Update model animation pose"""
        ...
    def update_music_stream(self, music: Music) -> None:
        """Updates buffers for music streaming"""
        ...
    def update_sound(self, sound: Sound, data: Any, samplesCount: int) -> None:
        """Update sound buffer with new data"""
        ...
    def update_texture(self, texture: Texture, pixels: Any) -> None:
        """Update GPU texture with new data"""
        ...
    def update_texture_rec(self, texture: Texture, rec: Rectangle, pixels: Any) -> None:
        """Update GPU texture rectangle with new data"""
        ...
    def upload_mesh(self, mesh: Any, dynamic: bool) -> None:
        """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
        ...
    def wave_copy(self, wave: Wave) -> Wave:
        """Copy a wave to a new wave"""
        ...
    def wave_crop(self, wave: Any, initSample: int, finalSample: int) -> None:
        """Crop a wave to defined samples range"""
        ...
    def wave_format(self, wave: Any, sampleRate: int, sampleSize: int, channels: int) -> None:
        """Convert wave data to desired format"""
        ...
    def window_should_close(self) -> bool:
        """Check if KEY_ESCAPE pressed or Close icon pressed"""
        ...
    class AudioStream:
        """ comment """
        def __init__(self, buffer, sampleRate, sampleSize, channels):
            self.buffer=buffer
            self.sampleRate=sampleRate
            self.sampleSize=sampleSize
            self.channels=channels
    BlendMode: int
    class BoneInfo:
        """ comment """
        def __init__(self, name, parent):
            self.name=name
            self.parent=parent
    class BoundingBox:
        """ comment """
        def __init__(self, min, max):
            self.min=min
            self.max=max
    class Camera:
        """ comment """
        def __init__(self, position, target, up, fovy, projection):
            self.position=position
            self.target=target
            self.up=up
            self.fovy=fovy
            self.projection=projection
    class Camera2D:
        """ comment """
        def __init__(self, offset, target, rotation, zoom):
            self.offset=offset
            self.target=target
            self.rotation=rotation
            self.zoom=zoom
    class Camera3D:
        """ comment """
        def __init__(self, position, target, up, fovy, projection):
            self.position=position
            self.target=target
            self.up=up
            self.fovy=fovy
            self.projection=projection
    CameraMode: int
    CameraProjection: int
    class CharInfo:
        """ comment """
        def __init__(self, value, offsetX, offsetY, advanceX, image):
            self.value=value
            self.offsetX=offsetX
            self.offsetY=offsetY
            self.advanceX=advanceX
            self.image=image
    class Color:
        """ comment """
        def __init__(self, r, g, b, a):
            self.r=r
            self.g=g
            self.b=b
            self.a=a
    ConfigFlags: int
    CubemapLayout: int
    class Font:
        """ comment """
        def __init__(self, baseSize, charsCount, charsPadding, texture, recs, chars):
            self.baseSize=baseSize
            self.charsCount=charsCount
            self.charsPadding=charsPadding
            self.texture=texture
            self.recs=recs
            self.chars=chars
    FontType: int
    GamepadAxis: int
    GamepadButton: int
    Gestures: int
    class Image:
        """ comment """
        def __init__(self, data, width, height, mipmaps, format):
            self.data=data
            self.width=width
            self.height=height
            self.mipmaps=mipmaps
            self.format=format
    KeyboardKey: int
    class Material:
        """ comment """
        def __init__(self, shader, maps, params):
            self.shader=shader
            self.maps=maps
            self.params=params
    class MaterialMap:
        """ comment """
        def __init__(self, texture, color, value):
            self.texture=texture
            self.color=color
            self.value=value
    MaterialMapIndex: int
    class Matrix:
        """ comment """
        def __init__(self, m0, m4, m8, m12, m1, m5, m9, m13, m2, m6, m10, m14, m3, m7, m11, m15):
            self.m0=m0
            self.m4=m4
            self.m8=m8
            self.m12=m12
            self.m1=m1
            self.m5=m5
            self.m9=m9
            self.m13=m13
            self.m2=m2
            self.m6=m6
            self.m10=m10
            self.m14=m14
            self.m3=m3
            self.m7=m7
            self.m11=m11
            self.m15=m15
    class Mesh:
        """ comment """
        def __init__(self, vertexCount, triangleCount, vertices, texcoords, texcoords2, normals, tangents, colors, indices, animVertices, animNormals, boneIds, boneWeights, vaoId, vboId):
            self.vertexCount=vertexCount
            self.triangleCount=triangleCount
            self.vertices=vertices
            self.texcoords=texcoords
            self.texcoords2=texcoords2
            self.normals=normals
            self.tangents=tangents
            self.colors=colors
            self.indices=indices
            self.animVertices=animVertices
            self.animNormals=animNormals
            self.boneIds=boneIds
            self.boneWeights=boneWeights
            self.vaoId=vaoId
            self.vboId=vboId
    class Model:
        """ comment """
        def __init__(self, transform, meshCount, materialCount, meshes, materials, meshMaterial, boneCount, bones, bindPose):
            self.transform=transform
            self.meshCount=meshCount
            self.materialCount=materialCount
            self.meshes=meshes
            self.materials=materials
            self.meshMaterial=meshMaterial
            self.boneCount=boneCount
            self.bones=bones
            self.bindPose=bindPose
    class ModelAnimation:
        """ comment """
        def __init__(self, boneCount, frameCount, bones, framePoses):
            self.boneCount=boneCount
            self.frameCount=frameCount
            self.bones=bones
            self.framePoses=framePoses
    MouseButton: int
    MouseCursor: int
    class Music:
        """ comment """
        def __init__(self, stream, sampleCount, looping, ctxType, ctxData):
            self.stream=stream
            self.sampleCount=sampleCount
            self.looping=looping
            self.ctxType=ctxType
            self.ctxData=ctxData
    class NPatchInfo:
        """ comment """
        def __init__(self, source, left, top, right, bottom, layout):
            self.source=source
            self.left=left
            self.top=top
            self.right=right
            self.bottom=bottom
            self.layout=layout
    NPatchLayout: int
    PixelFormat: int
    class Quaternion:
        """ comment """
        def __init__(self, x, y, z, w):
            self.x=x
            self.y=y
            self.z=z
            self.w=w
    class Ray:
        """ comment """
        def __init__(self, position, direction):
            self.position=position
            self.direction=direction
    class RayHitInfo:
        """ comment """
        def __init__(self, hit, distance, position, normal):
            self.hit=hit
            self.distance=distance
            self.position=position
            self.normal=normal
    class Rectangle:
        """ comment """
        def __init__(self, x, y, width, height):
            self.x=x
            self.y=y
            self.width=width
            self.height=height
    class RenderTexture:
        """ comment """
        def __init__(self, id, texture, depth):
            self.id=id
            self.texture=texture
            self.depth=depth
    class RenderTexture2D:
        """ comment """
        def __init__(self, id, texture, depth):
            self.id=id
            self.texture=texture
            self.depth=depth
    class Shader:
        """ comment """
        def __init__(self, id, locs):
            self.id=id
            self.locs=locs
    ShaderLocationIndex: int
    ShaderUniformDataType: int
    class Sound:
        """ comment """
        def __init__(self, stream, sampleCount):
            self.stream=stream
            self.sampleCount=sampleCount
    class Texture:
        """ comment """
        def __init__(self, id, width, height, mipmaps, format):
            self.id=id
            self.width=width
            self.height=height
            self.mipmaps=mipmaps
            self.format=format
    class Texture2D:
        """ comment """
        def __init__(self, id, width, height, mipmaps, format):
            self.id=id
            self.width=width
            self.height=height
            self.mipmaps=mipmaps
            self.format=format
    class TextureCubemap:
        """ comment """
        def __init__(self, id, width, height, mipmaps, format):
            self.id=id
            self.width=width
            self.height=height
            self.mipmaps=mipmaps
            self.format=format
    TextureFilter: int
    TextureWrap: int
    TraceLogLevel: int
    class Transform:
        """ comment """
        def __init__(self, translation, rotation, scale):
            self.translation=translation
            self.rotation=rotation
            self.scale=scale
    class Vector2:
        """ comment """
        def __init__(self, x, y):
            self.x=x
            self.y=y
    class Vector3:
        """ comment """
        def __init__(self, x, y, z):
            self.x=x
            self.y=y
            self.z=z
    class Vector4:
        """ comment """
        def __init__(self, x, y, z, w):
            self.x=x
            self.y=y
            self.z=z
            self.w=w
    class VrDeviceInfo:
        """ comment """
        def __init__(self, hResolution, vResolution, hScreenSize, vScreenSize, vScreenCenter, eyeToScreenDistance, lensSeparationDistance, interpupillaryDistance, lensDistortionValues, chromaAbCorrection):
            self.hResolution=hResolution
            self.vResolution=vResolution
            self.hScreenSize=hScreenSize
            self.vScreenSize=vScreenSize
            self.vScreenCenter=vScreenCenter
            self.eyeToScreenDistance=eyeToScreenDistance
            self.lensSeparationDistance=lensSeparationDistance
            self.interpupillaryDistance=interpupillaryDistance
            self.lensDistortionValues=lensDistortionValues
            self.chromaAbCorrection=chromaAbCorrection
    class VrStereoConfig:
        """ comment """
        def __init__(self, projection, viewOffset, leftLensCenter, rightLensCenter, leftScreenCenter, rightScreenCenter, scale, scaleIn):
            self.projection=projection
            self.viewOffset=viewOffset
            self.leftLensCenter=leftLensCenter
            self.rightLensCenter=rightLensCenter
            self.leftScreenCenter=leftScreenCenter
            self.rightScreenCenter=rightScreenCenter
            self.scale=scale
            self.scaleIn=scaleIn
    class Wave:
        """ comment """
        def __init__(self, sampleCount, sampleRate, sampleSize, channels, data):
            self.sampleCount=sampleCount
            self.sampleRate=sampleRate
            self.sampleSize=sampleSize
            self.channels=channels
            self.data=data

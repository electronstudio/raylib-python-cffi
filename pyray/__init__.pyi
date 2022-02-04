from typing import Any


def pointer(struct):
    ...

ARROWS_SIZE: int
ARROWS_VISIBLE: int
ARROW_PADDING: int
BACKGROUND_COLOR: int
BASE_COLOR_DISABLED: int
BASE_COLOR_FOCUSED: int
BASE_COLOR_NORMAL: int
BASE_COLOR_PRESSED: int
BLEND_ADDITIVE: int
BLEND_ADD_COLORS: int
BLEND_ALPHA: int
BLEND_CUSTOM: int
BLEND_MULTIPLIED: int
BLEND_SUBTRACT_COLORS: int
BORDER_COLOR_DISABLED: int
BORDER_COLOR_FOCUSED: int
BORDER_COLOR_NORMAL: int
BORDER_COLOR_PRESSED: int
BORDER_WIDTH: int
BUTTON: int
def begin_blend_mode(mode: int,) -> None:
        """Begin blending mode (alpha, additive, multiplied, subtract, custom)"""
        ...
def begin_drawing() -> None:
        """Setup canvas (framebuffer) to start drawing"""
        ...
def begin_mode_2d(camera: Camera2D,) -> None:
        """Begin 2D mode with custom camera (2D)"""
        ...
def begin_mode_3d(camera: Camera3D,) -> None:
        """Begin 3D mode with custom camera (3D)"""
        ...
def begin_scissor_mode(x: int,y: int,width: int,height: int,) -> None:
        """Begin scissor mode (define screen area for following drawing)"""
        ...
def begin_shader_mode(shader: Shader,) -> None:
        """Begin custom shader drawing"""
        ...
def begin_texture_mode(target: RenderTexture,) -> None:
        """Begin drawing to render texture"""
        ...
def begin_vr_stereo_mode(config: VrStereoConfig,) -> None:
        """Begin stereo rendering (requires VR simulator)"""
        ...
CAMERA_CUSTOM: int
CAMERA_FIRST_PERSON: int
CAMERA_FREE: int
CAMERA_ORBITAL: int
CAMERA_ORTHOGRAPHIC: int
CAMERA_PERSPECTIVE: int
CAMERA_THIRD_PERSON: int
CHECKBOX: int
CHECK_PADDING: int
COLORPICKER: int
COLOR_SELECTED_BG: int
COLOR_SELECTED_FG: int
COLOR_SELECTOR_SIZE: int
COMBOBOX: int
COMBO_BUTTON_PADDING: int
COMBO_BUTTON_WIDTH: int
CUBEMAP_LAYOUT_AUTO_DETECT: int
CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE: int
CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR: int
CUBEMAP_LAYOUT_LINE_HORIZONTAL: int
CUBEMAP_LAYOUT_LINE_VERTICAL: int
CUBEMAP_LAYOUT_PANORAMA: int
def change_directory(dir: str,) -> bool:
        """Change working directory, return true on success"""
        ...
def check_collision_box_sphere(box: BoundingBox,center: Vector3,radius: float,) -> bool:
        """Check collision between box and sphere"""
        ...
def check_collision_boxes(box1: BoundingBox,box2: BoundingBox,) -> bool:
        """Check collision between two bounding boxes"""
        ...
def check_collision_circle_rec(center: Vector2,radius: float,rec: Rectangle,) -> bool:
        """Check collision between circle and rectangle"""
        ...
def check_collision_circles(center1: Vector2,radius1: float,center2: Vector2,radius2: float,) -> bool:
        """Check collision between two circles"""
        ...
def check_collision_lines(startPos1: Vector2,endPos1: Vector2,startPos2: Vector2,endPos2: Vector2,collisionPoint: Any,) -> bool:
        """Check the collision between two lines defined by two points each, returns collision point by reference"""
        ...
def check_collision_point_circle(point: Vector2,center: Vector2,radius: float,) -> bool:
        """Check if point is inside circle"""
        ...
def check_collision_point_line(point: Vector2,p1: Vector2,p2: Vector2,threshold: int,) -> bool:
        """Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]"""
        ...
def check_collision_point_rec(point: Vector2,rec: Rectangle,) -> bool:
        """Check if point is inside rectangle"""
        ...
def check_collision_point_triangle(point: Vector2,p1: Vector2,p2: Vector2,p3: Vector2,) -> bool:
        """Check if point is inside a triangle"""
        ...
def check_collision_recs(rec1: Rectangle,rec2: Rectangle,) -> bool:
        """Check collision between two rectangles"""
        ...
def check_collision_spheres(center1: Vector3,radius1: float,center2: Vector3,radius2: float,) -> bool:
        """Check collision between two spheres"""
        ...
def clear_background(color: Color,) -> None:
        """Set background color (framebuffer clear color)"""
        ...
def clear_directory_files() -> None:
        """Clear directory files paths buffers (free memory)"""
        ...
def clear_dropped_files() -> None:
        """Clear dropped files paths buffer (free memory)"""
        ...
def clear_window_state(flags: int,) -> None:
        """Clear window configuration state flags"""
        ...
def close_audio_device() -> None:
        """Close the audio device and context"""
        ...
def close_physics() -> None:
        """void ClosePhysics();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def close_window() -> None:
        """Close window and unload OpenGL context"""
        ...
def codepoint_to_utf8(codepoint: int,byteSize: Any,) -> str:
        """Encode one codepoint into UTF-8 byte array (array length returned as parameter)"""
        ...
def color_alpha(color: Color,alpha: float,) -> Color:
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        ...
def color_alpha_blend(dst: Color,src: Color,tint: Color,) -> Color:
        """Get src alpha-blended into dst color with tint"""
        ...
def color_from_hsv(hue: float,saturation: float,value: float,) -> Color:
        """Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
        ...
def color_from_normalized(normalized: Vector4,) -> Color:
        """Get Color from normalized values [0..1]"""
        ...
def color_normalize(color: Color,) -> Vector4:
        """Get Color normalized as float [0..1]"""
        ...
def color_to_hsv(color: Color,) -> Vector3:
        """Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
        ...
def color_to_int(color: Color,) -> int:
        """Get hexadecimal value for a Color"""
        ...
def compress_data(data: str,dataLength: int,compDataLength: Any,) -> str:
        """Compress data (DEFLATE algorithm)"""
        ...
def create_physics_body_circle(Vector2_0: Vector2,float_1: float,float_2: float,) -> Any:
        """struct PhysicsBodyData *CreatePhysicsBodyCircle(struct Vector2, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def create_physics_body_polygon(Vector2_0: Vector2,float_1: float,int_2: int,float_3: float,) -> Any:
        """struct PhysicsBodyData *CreatePhysicsBodyPolygon(struct Vector2, float, int, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def create_physics_body_rectangle(Vector2_0: Vector2,float_1: float,float_2: float,float_3: float,) -> Any:
        """struct PhysicsBodyData *CreatePhysicsBodyRectangle(struct Vector2, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
DEFAULT: int
DROPDOWNBOX: int
DROPDOWN_ITEMS_PADDING: int
def decode_data_base64(data: str,outputLength: Any,) -> str:
        """Decode Base64 string data"""
        ...
def decompress_data(compData: str,compDataLength: int,dataLength: Any,) -> str:
        """Decompress data (DEFLATE algorithm)"""
        ...
def destroy_physics_body(PhysicsBodyData_pointer_0: Any,) -> None:
        """void DestroyPhysicsBody(struct PhysicsBodyData *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def directory_exists(dirPath: str,) -> bool:
        """Check if a directory path exists"""
        ...
def disable_cursor() -> None:
        """Disables cursor (lock cursor)"""
        ...
def draw_billboard(camera: Camera3D,texture: Texture,position: Vector3,size: float,tint: Color,) -> None:
        """Draw a billboard texture"""
        ...
def draw_billboard_pro(camera: Camera3D,texture: Texture,source: Rectangle,position: Vector3,up: Vector3,size: Vector2,origin: Vector2,rotation: float,tint: Color,) -> None:
        """Draw a billboard texture defined by source and rotation"""
        ...
def draw_billboard_rec(camera: Camera3D,texture: Texture,source: Rectangle,position: Vector3,size: Vector2,tint: Color,) -> None:
        """Draw a billboard texture defined by source"""
        ...
def draw_bounding_box(box: BoundingBox,color: Color,) -> None:
        """Draw bounding box (wires)"""
        ...
def draw_circle(centerX: int,centerY: int,radius: float,color: Color,) -> None:
        """Draw a color-filled circle"""
        ...
def draw_circle_3d(center: Vector3,radius: float,rotationAxis: Vector3,rotationAngle: float,color: Color,) -> None:
        """Draw a circle in 3D world space"""
        ...
def draw_circle_gradient(centerX: int,centerY: int,radius: float,color1: Color,color2: Color,) -> None:
        """Draw a gradient-filled circle"""
        ...
def draw_circle_lines(centerX: int,centerY: int,radius: float,color: Color,) -> None:
        """Draw circle outline"""
        ...
def draw_circle_sector(center: Vector2,radius: float,startAngle: float,endAngle: float,segments: int,color: Color,) -> None:
        """Draw a piece of a circle"""
        ...
def draw_circle_sector_lines(center: Vector2,radius: float,startAngle: float,endAngle: float,segments: int,color: Color,) -> None:
        """Draw circle sector outline"""
        ...
def draw_circle_v(center: Vector2,radius: float,color: Color,) -> None:
        """Draw a color-filled circle (Vector version)"""
        ...
def draw_cube(position: Vector3,width: float,height: float,length: float,color: Color,) -> None:
        """Draw cube"""
        ...
def draw_cube_texture(texture: Texture,position: Vector3,width: float,height: float,length: float,color: Color,) -> None:
        """Draw cube textured"""
        ...
def draw_cube_texture_rec(texture: Texture,source: Rectangle,position: Vector3,width: float,height: float,length: float,color: Color,) -> None:
        """Draw cube with a region of a texture"""
        ...
def draw_cube_v(position: Vector3,size: Vector3,color: Color,) -> None:
        """Draw cube (Vector version)"""
        ...
def draw_cube_wires(position: Vector3,width: float,height: float,length: float,color: Color,) -> None:
        """Draw cube wires"""
        ...
def draw_cube_wires_v(position: Vector3,size: Vector3,color: Color,) -> None:
        """Draw cube wires (Vector version)"""
        ...
def draw_cylinder(position: Vector3,radiusTop: float,radiusBottom: float,height: float,slices: int,color: Color,) -> None:
        """Draw a cylinder/cone"""
        ...
def draw_cylinder_ex(startPos: Vector3,endPos: Vector3,startRadius: float,endRadius: float,sides: int,color: Color,) -> None:
        """Draw a cylinder with base at startPos and top at endPos"""
        ...
def draw_cylinder_wires(position: Vector3,radiusTop: float,radiusBottom: float,height: float,slices: int,color: Color,) -> None:
        """Draw a cylinder/cone wires"""
        ...
def draw_cylinder_wires_ex(startPos: Vector3,endPos: Vector3,startRadius: float,endRadius: float,sides: int,color: Color,) -> None:
        """Draw a cylinder wires with base at startPos and top at endPos"""
        ...
def draw_ellipse(centerX: int,centerY: int,radiusH: float,radiusV: float,color: Color,) -> None:
        """Draw ellipse"""
        ...
def draw_ellipse_lines(centerX: int,centerY: int,radiusH: float,radiusV: float,color: Color,) -> None:
        """Draw ellipse outline"""
        ...
def draw_fps(posX: int,posY: int,) -> None:
        """Draw current FPS"""
        ...
def draw_grid(slices: int,spacing: float,) -> None:
        """Draw a grid (centered at (0, 0, 0))"""
        ...
def draw_line(startPosX: int,startPosY: int,endPosX: int,endPosY: int,color: Color,) -> None:
        """Draw a line"""
        ...
def draw_line_3d(startPos: Vector3,endPos: Vector3,color: Color,) -> None:
        """Draw a line in 3D world space"""
        ...
def draw_line_bezier(startPos: Vector2,endPos: Vector2,thick: float,color: Color,) -> None:
        """Draw a line using cubic-bezier curves in-out"""
        ...
def draw_line_bezier_cubic(startPos: Vector2,endPos: Vector2,startControlPos: Vector2,endControlPos: Vector2,thick: float,color: Color,) -> None:
        """Draw line using cubic bezier curves with 2 control points"""
        ...
def draw_line_bezier_quad(startPos: Vector2,endPos: Vector2,controlPos: Vector2,thick: float,color: Color,) -> None:
        """Draw line using quadratic bezier curves with a control point"""
        ...
def draw_line_ex(startPos: Vector2,endPos: Vector2,thick: float,color: Color,) -> None:
        """Draw a line defining thickness"""
        ...
def draw_line_strip(points: Any,pointCount: int,color: Color,) -> None:
        """Draw lines sequence"""
        ...
def draw_line_v(startPos: Vector2,endPos: Vector2,color: Color,) -> None:
        """Draw a line (Vector version)"""
        ...
def draw_mesh(mesh: Mesh,material: Material,transform: Matrix,) -> None:
        """Draw a 3d mesh with material and transform"""
        ...
def draw_mesh_instanced(mesh: Mesh,material: Material,transforms: Any,instances: int,) -> None:
        """Draw multiple mesh instances with material and different transforms"""
        ...
def draw_model(model: Model,position: Vector3,scale: float,tint: Color,) -> None:
        """Draw a model (with texture if set)"""
        ...
def draw_model_ex(model: Model,position: Vector3,rotationAxis: Vector3,rotationAngle: float,scale: Vector3,tint: Color,) -> None:
        """Draw a model with extended parameters"""
        ...
def draw_model_wires(model: Model,position: Vector3,scale: float,tint: Color,) -> None:
        """Draw a model wires (with texture if set)"""
        ...
def draw_model_wires_ex(model: Model,position: Vector3,rotationAxis: Vector3,rotationAngle: float,scale: Vector3,tint: Color,) -> None:
        """Draw a model wires (with texture if set) with extended parameters"""
        ...
def draw_pixel(posX: int,posY: int,color: Color,) -> None:
        """Draw a pixel"""
        ...
def draw_pixel_v(position: Vector2,color: Color,) -> None:
        """Draw a pixel (Vector version)"""
        ...
def draw_plane(centerPos: Vector3,size: Vector2,color: Color,) -> None:
        """Draw a plane XZ"""
        ...
def draw_point_3d(position: Vector3,color: Color,) -> None:
        """Draw a point in 3D space, actually a small line"""
        ...
def draw_poly(center: Vector2,sides: int,radius: float,rotation: float,color: Color,) -> None:
        """Draw a regular polygon (Vector version)"""
        ...
def draw_poly_lines(center: Vector2,sides: int,radius: float,rotation: float,color: Color,) -> None:
        """Draw a polygon outline of n sides"""
        ...
def draw_poly_lines_ex(center: Vector2,sides: int,radius: float,rotation: float,lineThick: float,color: Color,) -> None:
        """Draw a polygon outline of n sides with extended parameters"""
        ...
def draw_ray(ray: Ray,color: Color,) -> None:
        """Draw a ray line"""
        ...
def draw_rectangle(posX: int,posY: int,width: int,height: int,color: Color,) -> None:
        """Draw a color-filled rectangle"""
        ...
def draw_rectangle_gradient_ex(rec: Rectangle,col1: Color,col2: Color,col3: Color,col4: Color,) -> None:
        """Draw a gradient-filled rectangle with custom vertex colors"""
        ...
def draw_rectangle_gradient_h(posX: int,posY: int,width: int,height: int,color1: Color,color2: Color,) -> None:
        """Draw a horizontal-gradient-filled rectangle"""
        ...
def draw_rectangle_gradient_v(posX: int,posY: int,width: int,height: int,color1: Color,color2: Color,) -> None:
        """Draw a vertical-gradient-filled rectangle"""
        ...
def draw_rectangle_lines(posX: int,posY: int,width: int,height: int,color: Color,) -> None:
        """Draw rectangle outline"""
        ...
def draw_rectangle_lines_ex(rec: Rectangle,lineThick: float,color: Color,) -> None:
        """Draw rectangle outline with extended parameters"""
        ...
def draw_rectangle_pro(rec: Rectangle,origin: Vector2,rotation: float,color: Color,) -> None:
        """Draw a color-filled rectangle with pro parameters"""
        ...
def draw_rectangle_rec(rec: Rectangle,color: Color,) -> None:
        """Draw a color-filled rectangle"""
        ...
def draw_rectangle_rounded(rec: Rectangle,roundness: float,segments: int,color: Color,) -> None:
        """Draw rectangle with rounded edges"""
        ...
def draw_rectangle_rounded_lines(rec: Rectangle,roundness: float,segments: int,lineThick: float,color: Color,) -> None:
        """Draw rectangle with rounded edges outline"""
        ...
def draw_rectangle_v(position: Vector2,size: Vector2,color: Color,) -> None:
        """Draw a color-filled rectangle (Vector version)"""
        ...
def draw_ring(center: Vector2,innerRadius: float,outerRadius: float,startAngle: float,endAngle: float,segments: int,color: Color,) -> None:
        """Draw ring"""
        ...
def draw_ring_lines(center: Vector2,innerRadius: float,outerRadius: float,startAngle: float,endAngle: float,segments: int,color: Color,) -> None:
        """Draw ring outline"""
        ...
def draw_sphere(centerPos: Vector3,radius: float,color: Color,) -> None:
        """Draw sphere"""
        ...
def draw_sphere_ex(centerPos: Vector3,radius: float,rings: int,slices: int,color: Color,) -> None:
        """Draw sphere with extended parameters"""
        ...
def draw_sphere_wires(centerPos: Vector3,radius: float,rings: int,slices: int,color: Color,) -> None:
        """Draw sphere wires"""
        ...
def draw_text(text: str,posX: int,posY: int,fontSize: int,color: Color,) -> None:
        """Draw text (using default font)"""
        ...
def draw_text_codepoint(font: Font,codepoint: int,position: Vector2,fontSize: float,tint: Color,) -> None:
        """Draw one character (codepoint)"""
        ...
def draw_text_ex(font: Font,text: str,position: Vector2,fontSize: float,spacing: float,tint: Color,) -> None:
        """Draw text using font and additional parameters"""
        ...
def draw_text_pro(font: Font,text: str,position: Vector2,origin: Vector2,rotation: float,fontSize: float,spacing: float,tint: Color,) -> None:
        """Draw text using Font and pro parameters (rotation)"""
        ...
def draw_texture(texture: Texture,posX: int,posY: int,tint: Color,) -> None:
        """Draw a Texture2D"""
        ...
def draw_texture_ex(texture: Texture,position: Vector2,rotation: float,scale: float,tint: Color,) -> None:
        """Draw a Texture2D with extended parameters"""
        ...
def draw_texture_n_patch(texture: Texture,nPatchInfo: NPatchInfo,dest: Rectangle,origin: Vector2,rotation: float,tint: Color,) -> None:
        """Draws a texture (or part of it) that stretches or shrinks nicely"""
        ...
def draw_texture_poly(texture: Texture,center: Vector2,points: Any,texcoords: Any,pointCount: int,tint: Color,) -> None:
        """Draw a textured polygon"""
        ...
def draw_texture_pro(texture: Texture,source: Rectangle,dest: Rectangle,origin: Vector2,rotation: float,tint: Color,) -> None:
        """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
        ...
def draw_texture_quad(texture: Texture,tiling: Vector2,offset: Vector2,quad: Rectangle,tint: Color,) -> None:
        """Draw texture quad with tiling and offset parameters"""
        ...
def draw_texture_rec(texture: Texture,source: Rectangle,position: Vector2,tint: Color,) -> None:
        """Draw a part of a texture defined by a rectangle"""
        ...
def draw_texture_tiled(texture: Texture,source: Rectangle,dest: Rectangle,origin: Vector2,rotation: float,scale: float,tint: Color,) -> None:
        """Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest."""
        ...
def draw_texture_v(texture: Texture,position: Vector2,tint: Color,) -> None:
        """Draw a Texture2D with position defined as Vector2"""
        ...
def draw_triangle(v1: Vector2,v2: Vector2,v3: Vector2,color: Color,) -> None:
        """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
        ...
def draw_triangle_3d(v1: Vector3,v2: Vector3,v3: Vector3,color: Color,) -> None:
        """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
        ...
def draw_triangle_fan(points: Any,pointCount: int,color: Color,) -> None:
        """Draw a triangle fan defined by points (first vertex is the center)"""
        ...
def draw_triangle_lines(v1: Vector2,v2: Vector2,v3: Vector2,color: Color,) -> None:
        """Draw triangle outline (vertex in counter-clockwise order!)"""
        ...
def draw_triangle_strip(points: Any,pointCount: int,color: Color,) -> None:
        """Draw a triangle strip defined by points"""
        ...
def draw_triangle_strip_3d(points: Any,pointCount: int,color: Color,) -> None:
        """Draw a triangle strip defined by points"""
        ...
def enable_cursor() -> None:
        """Enables cursor (unlock cursor)"""
        ...
def encode_data_base64(data: str,dataLength: int,outputLength: Any,) -> str:
        """Encode data to Base64 string"""
        ...
def end_blend_mode() -> None:
        """End blending mode (reset to default: alpha blending)"""
        ...
def end_drawing() -> None:
        """End canvas drawing and swap buffers (double buffering)"""
        ...
def end_mode_2d() -> None:
        """Ends 2D mode with custom camera"""
        ...
def end_mode_3d() -> None:
        """Ends 3D mode and returns to default 2D orthographic mode"""
        ...
def end_scissor_mode() -> None:
        """End scissor mode"""
        ...
def end_shader_mode() -> None:
        """End custom shader drawing (use default shader)"""
        ...
def end_texture_mode() -> None:
        """Ends drawing to render texture"""
        ...
def end_vr_stereo_mode() -> None:
        """End stereo rendering (requires VR simulator)"""
        ...
def export_image(image: Image,fileName: str,) -> bool:
        """Export image data to file, returns true on success"""
        ...
def export_image_as_code(image: Image,fileName: str,) -> bool:
        """Export image as code file defining an array of bytes, returns true on success"""
        ...
def export_mesh(mesh: Mesh,fileName: str,) -> bool:
        """Export mesh data to file, returns true on success"""
        ...
def export_wave(wave: Wave,fileName: str,) -> bool:
        """Export wave data to file, returns true on success"""
        ...
def export_wave_as_code(wave: Wave,fileName: str,) -> bool:
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
def fade(color: Color,alpha: float,) -> Color:
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        ...
def file_exists(fileName: str,) -> bool:
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
GROUP_PADDING: int
GUI_STATE_DISABLED: int
GUI_STATE_FOCUSED: int
GUI_STATE_NORMAL: int
GUI_STATE_PRESSED: int
GUI_TEXT_ALIGN_CENTER: int
GUI_TEXT_ALIGN_LEFT: int
GUI_TEXT_ALIGN_RIGHT: int
def gen_image_cellular(width: int,height: int,tileSize: int,) -> Image:
        """Generate image: cellular algorithm, bigger tileSize means bigger cells"""
        ...
def gen_image_checked(width: int,height: int,checksX: int,checksY: int,col1: Color,col2: Color,) -> Image:
        """Generate image: checked"""
        ...
def gen_image_color(width: int,height: int,color: Color,) -> Image:
        """Generate image: plain color"""
        ...
def gen_image_font_atlas(chars: Any,recs: Any,glyphCount: int,fontSize: int,padding: int,packMethod: int,) -> Image:
        """Generate image font atlas using chars info"""
        ...
def gen_image_gradient_h(width: int,height: int,left: Color,right: Color,) -> Image:
        """Generate image: horizontal gradient"""
        ...
def gen_image_gradient_radial(width: int,height: int,density: float,inner: Color,outer: Color,) -> Image:
        """Generate image: radial gradient"""
        ...
def gen_image_gradient_v(width: int,height: int,top: Color,bottom: Color,) -> Image:
        """Generate image: vertical gradient"""
        ...
def gen_image_white_noise(width: int,height: int,factor: float,) -> Image:
        """Generate image: white noise"""
        ...
def gen_mesh_binormals(mesh: Any,) -> None:
        """Compute mesh binormals"""
        ...
def gen_mesh_cone(radius: float,height: float,slices: int,) -> Mesh:
        """Generate cone/pyramid mesh"""
        ...
def gen_mesh_cube(width: float,height: float,length: float,) -> Mesh:
        """Generate cuboid mesh"""
        ...
def gen_mesh_cubicmap(cubicmap: Image,cubeSize: Vector3,) -> Mesh:
        """Generate cubes-based map mesh from image data"""
        ...
def gen_mesh_cylinder(radius: float,height: float,slices: int,) -> Mesh:
        """Generate cylinder mesh"""
        ...
def gen_mesh_heightmap(heightmap: Image,size: Vector3,) -> Mesh:
        """Generate heightmap mesh from image data"""
        ...
def gen_mesh_hemi_sphere(radius: float,rings: int,slices: int,) -> Mesh:
        """Generate half-sphere mesh (no bottom cap)"""
        ...
def gen_mesh_knot(radius: float,size: float,radSeg: int,sides: int,) -> Mesh:
        """Generate trefoil knot mesh"""
        ...
def gen_mesh_plane(width: float,length: float,resX: int,resZ: int,) -> Mesh:
        """Generate plane mesh (with subdivisions)"""
        ...
def gen_mesh_poly(sides: int,radius: float,) -> Mesh:
        """Generate polygonal mesh"""
        ...
def gen_mesh_sphere(radius: float,rings: int,slices: int,) -> Mesh:
        """Generate sphere mesh (standard sphere)"""
        ...
def gen_mesh_tangents(mesh: Any,) -> None:
        """Compute mesh tangents"""
        ...
def gen_mesh_torus(radius: float,size: float,radSeg: int,sides: int,) -> Mesh:
        """Generate torus mesh"""
        ...
def gen_texture_mipmaps(texture: Any,) -> None:
        """Generate GPU mipmaps for a texture"""
        ...
def get_camera_matrix(camera: Camera3D,) -> Matrix:
        """Get camera transform matrix (view matrix)"""
        ...
def get_camera_matrix_2d(camera: Camera2D,) -> Matrix:
        """Get camera 2d transform matrix"""
        ...
def get_char_pressed() -> int:
        """Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty"""
        ...
def get_clipboard_text() -> str:
        """Get clipboard text content"""
        ...
def get_codepoint(text: str,bytesProcessed: Any,) -> int:
        """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
        ...
def get_codepoint_count(text: str,) -> int:
        """Get total number of codepoints in a UTF-8 encoded string"""
        ...
def get_collision_rec(rec1: Rectangle,rec2: Rectangle,) -> Rectangle:
        """Get collision rectangle for two rectangles collision"""
        ...
def get_color(hexValue: int,) -> Color:
        """Get Color structure from hexadecimal value"""
        ...
def get_current_monitor() -> int:
        """Get current connected monitor"""
        ...
def get_directory_files(dirPath: str,count: Any,) -> str:
        """Get filenames in a directory path (memory should be freed)"""
        ...
def get_directory_path(filePath: str,) -> str:
        """Get full path for a given fileName with path (uses static string)"""
        ...
def get_dropped_files(count: Any,) -> str:
        """Get dropped files names (memory should be freed)"""
        ...
def get_fps() -> int:
        """Get current FPS"""
        ...
def get_file_extension(fileName: str,) -> str:
        """Get pointer to extension for a filename string (includes dot: '.png')"""
        ...
def get_file_mod_time(fileName: str,) -> int:
        """Get file modification time (last write time)"""
        ...
def get_file_name(filePath: str,) -> str:
        """Get pointer to filename for a path string"""
        ...
def get_file_name_without_ext(filePath: str,) -> str:
        """Get filename string without extension (uses static string)"""
        ...
def get_font_default() -> Font:
        """Get the default Font"""
        ...
def get_frame_time() -> float:
        """Get time in seconds for last frame drawn (delta time)"""
        ...
def get_gamepad_axis_count(gamepad: int,) -> int:
        """Get gamepad axis count for a gamepad"""
        ...
def get_gamepad_axis_movement(gamepad: int,axis: int,) -> float:
        """Get axis movement value for a gamepad axis"""
        ...
def get_gamepad_button_pressed() -> int:
        """Get the last gamepad button pressed"""
        ...
def get_gamepad_name(gamepad: int,) -> str:
        """Get gamepad internal name id"""
        ...
def get_gesture_detected() -> int:
        """Get latest detected gesture"""
        ...
def get_gesture_drag_angle() -> float:
        """Get gesture drag angle"""
        ...
def get_gesture_drag_vector() -> Vector2:
        """Get gesture drag vector"""
        ...
def get_gesture_hold_duration() -> float:
        """Get gesture hold time in milliseconds"""
        ...
def get_gesture_pinch_angle() -> float:
        """Get gesture pinch angle"""
        ...
def get_gesture_pinch_vector() -> Vector2:
        """Get gesture pinch delta"""
        ...
def get_glyph_atlas_rec(font: Font,codepoint: int,) -> Rectangle:
        """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
        ...
def get_glyph_index(font: Font,codepoint: int,) -> int:
        """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
        ...
def get_glyph_info(font: Font,codepoint: int,) -> GlyphInfo:
        """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
        ...
def get_image_alpha_border(image: Image,threshold: float,) -> Rectangle:
        """Get image alpha border rectangle"""
        ...
def get_image_color(image: Image,x: int,y: int,) -> Color:
        """Get image pixel color at (x, y) position"""
        ...
def get_key_pressed() -> int:
        """Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty"""
        ...
def get_mesh_bounding_box(mesh: Mesh,) -> BoundingBox:
        """Compute mesh bounding box limits"""
        ...
def get_model_bounding_box(model: Model,) -> BoundingBox:
        """Compute model bounding box limits (considers all meshes)"""
        ...
def get_monitor_count() -> int:
        """Get number of connected monitors"""
        ...
def get_monitor_height(monitor: int,) -> int:
        """Get specified monitor height (max available by monitor)"""
        ...
def get_monitor_name(monitor: int,) -> str:
        """Get the human-readable, UTF-8 encoded name of the primary monitor"""
        ...
def get_monitor_physical_height(monitor: int,) -> int:
        """Get specified monitor physical height in millimetres"""
        ...
def get_monitor_physical_width(monitor: int,) -> int:
        """Get specified monitor physical width in millimetres"""
        ...
def get_monitor_position(monitor: int,) -> Vector2:
        """Get specified monitor position"""
        ...
def get_monitor_refresh_rate(monitor: int,) -> int:
        """Get specified monitor refresh rate"""
        ...
def get_monitor_width(monitor: int,) -> int:
        """Get specified monitor width (max available by monitor)"""
        ...
def get_mouse_delta() -> Vector2:
        """Get mouse delta between frames"""
        ...
def get_mouse_position() -> Vector2:
        """Get mouse position XY"""
        ...
def get_mouse_ray(mousePosition: Vector2,camera: Camera3D,) -> Ray:
        """Get a ray trace from mouse position"""
        ...
def get_mouse_wheel_move() -> float:
        """Get mouse wheel movement Y"""
        ...
def get_mouse_x() -> int:
        """Get mouse position X"""
        ...
def get_mouse_y() -> int:
        """Get mouse position Y"""
        ...
def get_music_time_length(music: Music,) -> float:
        """Get music time length (in seconds)"""
        ...
def get_music_time_played(music: Music,) -> float:
        """Get current music time played (in seconds)"""
        ...
def get_physics_bodies_count() -> int:
        """int GetPhysicsBodiesCount();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def get_physics_body(int_0: int,) -> Any:
        """struct PhysicsBodyData *GetPhysicsBody(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def get_physics_shape_type(int_0: int,) -> int:
        """int GetPhysicsShapeType(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def get_physics_shape_vertex(PhysicsBodyData_pointer_0: Any,int_1: int,) -> Vector2:
        """struct Vector2 GetPhysicsShapeVertex(struct PhysicsBodyData *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def get_physics_shape_vertices_count(int_0: int,) -> int:
        """int GetPhysicsShapeVerticesCount(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def get_pixel_color(srcPtr: Any,format: int,) -> Color:
        """Get Color from a source pixel pointer of certain format"""
        ...
def get_pixel_data_size(width: int,height: int,format: int,) -> int:
        """Get pixel data size in bytes for certain format"""
        ...
def get_prev_directory_path(dirPath: str,) -> str:
        """Get previous directory path for a given path (uses static string)"""
        ...
def get_random_value(min: int,max: int,) -> int:
        """Get a random value between min and max (both included)"""
        ...
def get_ray_collision_box(ray: Ray,box: BoundingBox,) -> RayCollision:
        """Get collision info between ray and box"""
        ...
def get_ray_collision_mesh(ray: Ray,mesh: Mesh,transform: Matrix,) -> RayCollision:
        """Get collision info between ray and mesh"""
        ...
def get_ray_collision_model(ray: Ray,model: Model,) -> RayCollision:
        """Get collision info between ray and model"""
        ...
def get_ray_collision_quad(ray: Ray,p1: Vector3,p2: Vector3,p3: Vector3,p4: Vector3,) -> RayCollision:
        """Get collision info between ray and quad"""
        ...
def get_ray_collision_sphere(ray: Ray,center: Vector3,radius: float,) -> RayCollision:
        """Get collision info between ray and sphere"""
        ...
def get_ray_collision_triangle(ray: Ray,p1: Vector3,p2: Vector3,p3: Vector3,) -> RayCollision:
        """Get collision info between ray and triangle"""
        ...
def get_screen_height() -> int:
        """Get current screen height"""
        ...
def get_screen_to_world_2d(position: Vector2,camera: Camera2D,) -> Vector2:
        """Get the world space position for a 2d camera screen space position"""
        ...
def get_screen_width() -> int:
        """Get current screen width"""
        ...
def get_shader_location(shader: Shader,uniformName: str,) -> int:
        """Get shader uniform location"""
        ...
def get_shader_location_attrib(shader: Shader,attribName: str,) -> int:
        """Get shader attribute location"""
        ...
def get_sounds_playing() -> int:
        """Get number of sounds playing in the multichannel"""
        ...
def get_time() -> float:
        """Get elapsed time in seconds since InitWindow()"""
        ...
def get_touch_point_count() -> int:
        """Get number of touch points"""
        ...
def get_touch_point_id(index: int,) -> int:
        """Get touch point identifier for given index"""
        ...
def get_touch_position(index: int,) -> Vector2:
        """Get touch position XY for a touch point index (relative to screen size)"""
        ...
def get_touch_x() -> int:
        """Get touch position X for touch point 0 (relative to screen size)"""
        ...
def get_touch_y() -> int:
        """Get touch position Y for touch point 0 (relative to screen size)"""
        ...
def get_window_handle() -> Any:
        """Get native window handle"""
        ...
def get_window_position() -> Vector2:
        """Get window position XY on monitor"""
        ...
def get_window_scale_dpi() -> Vector2:
        """Get window scale DPI factor"""
        ...
def get_working_directory() -> str:
        """Get current working directory (uses static string)"""
        ...
def get_world_to_screen(position: Vector3,camera: Camera3D,) -> Vector2:
        """Get the screen space position for a 3d world space position"""
        ...
def get_world_to_screen_2d(position: Vector2,camera: Camera2D,) -> Vector2:
        """Get the screen space position for a 2d camera world space position"""
        ...
def get_world_to_screen_ex(position: Vector3,camera: Camera3D,width: int,height: int,) -> Vector2:
        """Get size position for a 3d world space position"""
        ...
def gui_button(Rectangle_0: Rectangle,str_1: str,) -> bool:
        """_Bool GuiButton(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_check_box(Rectangle_0: Rectangle,str_1: str,_Bool_2: bool,) -> bool:
        """_Bool GuiCheckBox(struct Rectangle, char *, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_check_icon_pixel(int_0: int,int_1: int,int_2: int,) -> bool:
        """_Bool GuiCheckIconPixel(int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_clear_icon_pixel(int_0: int,int_1: int,int_2: int,) -> None:
        """void GuiClearIconPixel(int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_color_bar_alpha(Rectangle_0: Rectangle,float_1: float,) -> float:
        """float GuiColorBarAlpha(struct Rectangle, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_color_bar_hue(Rectangle_0: Rectangle,float_1: float,) -> float:
        """float GuiColorBarHue(struct Rectangle, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_color_panel(Rectangle_0: Rectangle,Color_1: Color,) -> Color:
        """struct Color GuiColorPanel(struct Rectangle, struct Color);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_color_picker(Rectangle_0: Rectangle,Color_1: Color,) -> Color:
        """struct Color GuiColorPicker(struct Rectangle, struct Color);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_combo_box(Rectangle_0: Rectangle,str_1: str,int_2: int,) -> int:
        """int GuiComboBox(struct Rectangle, char *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_disable() -> None:
        """void GuiDisable();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_draw_icon(int_0: int,int_1: int,int_2: int,int_3: int,Color_4: Color,) -> None:
        """void GuiDrawIcon(int, int, int, int, struct Color);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_dropdown_box(Rectangle_0: Rectangle,str_1: str,int_pointer_2: Any,_Bool_3: bool,) -> bool:
        """_Bool GuiDropdownBox(struct Rectangle, char *, int *, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_dummy_rec(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiDummyRec(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_enable() -> None:
        """void GuiEnable();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_fade(float_0: float,) -> None:
        """void GuiFade(float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_get_font() -> Font:
        """struct Font GuiGetFont();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_get_icon_data(int_0: int,) -> Any:
        """unsigned int *GuiGetIconData(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_get_icons() -> Any:
        """unsigned int *GuiGetIcons();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_get_state() -> int:
        """int GuiGetState();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_get_style(int_0: int,int_1: int,) -> int:
        """int GuiGetStyle(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_grid(Rectangle_0: Rectangle,float_1: float,int_2: int,) -> Vector2:
        """struct Vector2 GuiGrid(struct Rectangle, float, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_group_box(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiGroupBox(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_icon_text(int_0: int,str_1: str,) -> str:
        """char *GuiIconText(int, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_is_locked() -> bool:
        """_Bool GuiIsLocked();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_label(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiLabel(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_label_button(Rectangle_0: Rectangle,str_1: str,) -> bool:
        """_Bool GuiLabelButton(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_line(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiLine(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_list_view(Rectangle_0: Rectangle,str_1: str,int_pointer_2: Any,int_3: int,) -> int:
        """int GuiListView(struct Rectangle, char *, int *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_list_view_ex(Rectangle_0: Rectangle,str_pointer_1: str,int_2: int,int_pointer_3: Any,int_pointer_4: Any,int_5: int,) -> int:
        """int GuiListViewEx(struct Rectangle, char * *, int, int *, int *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_load_style(str_0: str,) -> None:
        """void GuiLoadStyle(char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_load_style_default() -> None:
        """void GuiLoadStyleDefault();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_lock() -> None:
        """void GuiLock();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_message_box(Rectangle_0: Rectangle,str_1: str,str_2: str,str_3: str,) -> int:
        """int GuiMessageBox(struct Rectangle, char *, char *, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_panel(Rectangle_0: Rectangle,) -> None:
        """void GuiPanel(struct Rectangle);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_progress_bar(Rectangle_0: Rectangle,str_1: str,str_2: str,float_3: float,float_4: float,float_5: float,) -> float:
        """float GuiProgressBar(struct Rectangle, char *, char *, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_scroll_bar(Rectangle_0: Rectangle,int_1: int,int_2: int,int_3: int,) -> int:
        """int GuiScrollBar(struct Rectangle, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_scroll_panel(Rectangle_0: Rectangle,Rectangle_1: Rectangle,Vector2_pointer_2: Any,) -> Rectangle:
        """struct Rectangle GuiScrollPanel(struct Rectangle, struct Rectangle, struct Vector2 *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_set_font(Font_0: Font,) -> None:
        """void GuiSetFont(struct Font);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_set_icon_data(int_0: int,unsignedint_pointer_1: Any,) -> None:
        """void GuiSetIconData(int, unsigned int *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_set_icon_pixel(int_0: int,int_1: int,int_2: int,) -> None:
        """void GuiSetIconPixel(int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_set_state(int_0: int,) -> None:
        """void GuiSetState(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_set_style(int_0: int,int_1: int,int_2: int,) -> None:
        """void GuiSetStyle(int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_slider(Rectangle_0: Rectangle,str_1: str,str_2: str,float_3: float,float_4: float,float_5: float,) -> float:
        """float GuiSlider(struct Rectangle, char *, char *, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_slider_bar(Rectangle_0: Rectangle,str_1: str,str_2: str,float_3: float,float_4: float,float_5: float,) -> float:
        """float GuiSliderBar(struct Rectangle, char *, char *, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_spinner(Rectangle_0: Rectangle,str_1: str,int_pointer_2: Any,int_3: int,int_4: int,_Bool_5: bool,) -> bool:
        """_Bool GuiSpinner(struct Rectangle, char *, int *, int, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_status_bar(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiStatusBar(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_text_box(Rectangle_0: Rectangle,str_1: str,int_2: int,_Bool_3: bool,) -> bool:
        """_Bool GuiTextBox(struct Rectangle, char *, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_text_box_multi(Rectangle_0: Rectangle,str_1: str,int_2: int,_Bool_3: bool,) -> bool:
        """_Bool GuiTextBoxMulti(struct Rectangle, char *, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_text_input_box(Rectangle_0: Rectangle,str_1: str,str_2: str,str_3: str,str_4: str,) -> int:
        """int GuiTextInputBox(struct Rectangle, char *, char *, char *, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_toggle(Rectangle_0: Rectangle,str_1: str,_Bool_2: bool,) -> bool:
        """_Bool GuiToggle(struct Rectangle, char *, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_toggle_group(Rectangle_0: Rectangle,str_1: str,int_2: int,) -> int:
        """int GuiToggleGroup(struct Rectangle, char *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_unlock() -> None:
        """void GuiUnlock();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_value_box(Rectangle_0: Rectangle,str_1: str,int_pointer_2: Any,int_3: int,int_4: int,_Bool_5: bool,) -> bool:
        """_Bool GuiValueBox(struct Rectangle, char *, int *, int, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def gui_window_box(Rectangle_0: Rectangle,str_1: str,) -> bool:
        """_Bool GuiWindowBox(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
HUEBAR_PADDING: int
HUEBAR_SELECTOR_HEIGHT: int
HUEBAR_SELECTOR_OVERFLOW: int
HUEBAR_WIDTH: int
def hide_cursor() -> None:
        """Hides cursor"""
        ...
def image_alpha_clear(image: Any,color: Color,threshold: float,) -> None:
        """Clear alpha channel to desired color"""
        ...
def image_alpha_crop(image: Any,threshold: float,) -> None:
        """Crop image depending on alpha value"""
        ...
def image_alpha_mask(image: Any,alphaMask: Image,) -> None:
        """Apply alpha mask to image"""
        ...
def image_alpha_premultiply(image: Any,) -> None:
        """Premultiply alpha channel"""
        ...
def image_clear_background(dst: Any,color: Color,) -> None:
        """Clear image background with given color"""
        ...
def image_color_brightness(image: Any,brightness: int,) -> None:
        """Modify image color: brightness (-255 to 255)"""
        ...
def image_color_contrast(image: Any,contrast: float,) -> None:
        """Modify image color: contrast (-100 to 100)"""
        ...
def image_color_grayscale(image: Any,) -> None:
        """Modify image color: grayscale"""
        ...
def image_color_invert(image: Any,) -> None:
        """Modify image color: invert"""
        ...
def image_color_replace(image: Any,color: Color,replace: Color,) -> None:
        """Modify image color: replace color"""
        ...
def image_color_tint(image: Any,color: Color,) -> None:
        """Modify image color: tint"""
        ...
def image_copy(image: Image,) -> Image:
        """Create an image duplicate (useful for transformations)"""
        ...
def image_crop(image: Any,crop: Rectangle,) -> None:
        """Crop an image to a defined rectangle"""
        ...
def image_dither(image: Any,rBpp: int,gBpp: int,bBpp: int,aBpp: int,) -> None:
        """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
        ...
def image_draw(dst: Any,src: Image,srcRec: Rectangle,dstRec: Rectangle,tint: Color,) -> None:
        """Draw a source image within a destination image (tint applied to source)"""
        ...
def image_draw_circle(dst: Any,centerX: int,centerY: int,radius: int,color: Color,) -> None:
        """Draw circle within an image"""
        ...
def image_draw_circle_v(dst: Any,center: Vector2,radius: int,color: Color,) -> None:
        """Draw circle within an image (Vector version)"""
        ...
def image_draw_line(dst: Any,startPosX: int,startPosY: int,endPosX: int,endPosY: int,color: Color,) -> None:
        """Draw line within an image"""
        ...
def image_draw_line_v(dst: Any,start: Vector2,end: Vector2,color: Color,) -> None:
        """Draw line within an image (Vector version)"""
        ...
def image_draw_pixel(dst: Any,posX: int,posY: int,color: Color,) -> None:
        """Draw pixel within an image"""
        ...
def image_draw_pixel_v(dst: Any,position: Vector2,color: Color,) -> None:
        """Draw pixel within an image (Vector version)"""
        ...
def image_draw_rectangle(dst: Any,posX: int,posY: int,width: int,height: int,color: Color,) -> None:
        """Draw rectangle within an image"""
        ...
def image_draw_rectangle_lines(dst: Any,rec: Rectangle,thick: int,color: Color,) -> None:
        """Draw rectangle lines within an image"""
        ...
def image_draw_rectangle_rec(dst: Any,rec: Rectangle,color: Color,) -> None:
        """Draw rectangle within an image"""
        ...
def image_draw_rectangle_v(dst: Any,position: Vector2,size: Vector2,color: Color,) -> None:
        """Draw rectangle within an image (Vector version)"""
        ...
def image_draw_text(dst: Any,text: str,posX: int,posY: int,fontSize: int,color: Color,) -> None:
        """Draw text (using default font) within an image (destination)"""
        ...
def image_draw_text_ex(dst: Any,font: Font,text: str,position: Vector2,fontSize: float,spacing: float,tint: Color,) -> None:
        """Draw text (custom sprite font) within an image (destination)"""
        ...
def image_flip_horizontal(image: Any,) -> None:
        """Flip image horizontally"""
        ...
def image_flip_vertical(image: Any,) -> None:
        """Flip image vertically"""
        ...
def image_format(image: Any,newFormat: int,) -> None:
        """Convert image data to desired format"""
        ...
def image_from_image(image: Image,rec: Rectangle,) -> Image:
        """Create an image from another image piece"""
        ...
def image_mipmaps(image: Any,) -> None:
        """Compute all mipmap levels for a provided image"""
        ...
def image_resize(image: Any,newWidth: int,newHeight: int,) -> None:
        """Resize image (Bicubic scaling algorithm)"""
        ...
def image_resize_canvas(image: Any,newWidth: int,newHeight: int,offsetX: int,offsetY: int,fill: Color,) -> None:
        """Resize canvas and fill with color"""
        ...
def image_resize_nn(image: Any,newWidth: int,newHeight: int,) -> None:
        """Resize image (Nearest-Neighbor scaling algorithm)"""
        ...
def image_rotate_ccw(image: Any,) -> None:
        """Rotate image counter-clockwise 90deg"""
        ...
def image_rotate_cw(image: Any,) -> None:
        """Rotate image clockwise 90deg"""
        ...
def image_text(text: str,fontSize: int,color: Color,) -> Image:
        """Create an image from text (default font)"""
        ...
def image_text_ex(font: Font,text: str,fontSize: float,spacing: float,tint: Color,) -> Image:
        """Create an image from text (custom sprite font)"""
        ...
def image_to_pot(image: Any,fill: Color,) -> None:
        """Convert image to POT (power-of-two)"""
        ...
def init_audio_device() -> None:
        """Initialize audio device and context"""
        ...
def init_physics() -> None:
        """void InitPhysics();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def init_window(width: int,height: int,title: str,) -> None:
        """Initialize window and OpenGL context"""
        ...
def is_audio_device_ready() -> bool:
        """Check if audio device has been initialized successfully"""
        ...
def is_audio_stream_playing(stream: AudioStream,) -> bool:
        """Check if audio stream is playing"""
        ...
def is_audio_stream_processed(stream: AudioStream,) -> bool:
        """Check if any audio stream buffers requires refill"""
        ...
def is_cursor_hidden() -> bool:
        """Check if cursor is not visible"""
        ...
def is_cursor_on_screen() -> bool:
        """Check if cursor is on the screen"""
        ...
def is_file_dropped() -> bool:
        """Check if a file has been dropped into window"""
        ...
def is_file_extension(fileName: str,ext: str,) -> bool:
        """Check file extension (including point: .png, .wav)"""
        ...
def is_gamepad_available(gamepad: int,) -> bool:
        """Check if a gamepad is available"""
        ...
def is_gamepad_button_down(gamepad: int,button: int,) -> bool:
        """Check if a gamepad button is being pressed"""
        ...
def is_gamepad_button_pressed(gamepad: int,button: int,) -> bool:
        """Check if a gamepad button has been pressed once"""
        ...
def is_gamepad_button_released(gamepad: int,button: int,) -> bool:
        """Check if a gamepad button has been released once"""
        ...
def is_gamepad_button_up(gamepad: int,button: int,) -> bool:
        """Check if a gamepad button is NOT being pressed"""
        ...
def is_gesture_detected(gesture: int,) -> bool:
        """Check if a gesture have been detected"""
        ...
def is_key_down(key: int,) -> bool:
        """Check if a key is being pressed"""
        ...
def is_key_pressed(key: int,) -> bool:
        """Check if a key has been pressed once"""
        ...
def is_key_released(key: int,) -> bool:
        """Check if a key has been released once"""
        ...
def is_key_up(key: int,) -> bool:
        """Check if a key is NOT being pressed"""
        ...
def is_model_animation_valid(model: Model,anim: ModelAnimation,) -> bool:
        """Check model animation skeleton match"""
        ...
def is_mouse_button_down(button: int,) -> bool:
        """Check if a mouse button is being pressed"""
        ...
def is_mouse_button_pressed(button: int,) -> bool:
        """Check if a mouse button has been pressed once"""
        ...
def is_mouse_button_released(button: int,) -> bool:
        """Check if a mouse button has been released once"""
        ...
def is_mouse_button_up(button: int,) -> bool:
        """Check if a mouse button is NOT being pressed"""
        ...
def is_music_stream_playing(music: Music,) -> bool:
        """Check if music is playing"""
        ...
def is_sound_playing(sound: Sound,) -> bool:
        """Check if a sound is currently playing"""
        ...
def is_window_focused() -> bool:
        """Check if window is currently focused (only PLATFORM_DESKTOP)"""
        ...
def is_window_fullscreen() -> bool:
        """Check if window is currently fullscreen"""
        ...
def is_window_hidden() -> bool:
        """Check if window is currently hidden (only PLATFORM_DESKTOP)"""
        ...
def is_window_maximized() -> bool:
        """Check if window is currently maximized (only PLATFORM_DESKTOP)"""
        ...
def is_window_minimized() -> bool:
        """Check if window is currently minimized (only PLATFORM_DESKTOP)"""
        ...
def is_window_ready() -> bool:
        """Check if window has been initialized successfully"""
        ...
def is_window_resized() -> bool:
        """Check if window has been resized last frame"""
        ...
def is_window_state(flag: int,) -> bool:
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
LABEL: int
LINE_COLOR: int
LISTVIEW: int
LIST_ITEMS_HEIGHT: int
LIST_ITEMS_PADDING: int
LOG_ALL: int
LOG_DEBUG: int
LOG_ERROR: int
LOG_FATAL: int
LOG_INFO: int
LOG_NONE: int
LOG_TRACE: int
LOG_WARNING: int
def load_audio_stream(sampleRate: int,sampleSize: int,channels: int,) -> AudioStream:
        """Load audio stream (to stream raw audio pcm data)"""
        ...
def load_codepoints(text: str,count: Any,) -> Any:
        """Load all codepoints from a UTF-8 text string, codepoints count returned by parameter"""
        ...
def load_file_data(fileName: str,bytesRead: Any,) -> str:
        """Load file data as byte array (read)"""
        ...
def load_file_text(fileName: str,) -> str:
        """Load text data from file (read), returns a ' 0' terminated string"""
        ...
def load_font(fileName: str,) -> Font:
        """Load font from file into GPU memory (VRAM)"""
        ...
def load_font_data(fileData: str,dataSize: int,fontSize: int,fontChars: Any,glyphCount: int,type: int,) -> Any:
        """Load font data for further use"""
        ...
def load_font_ex(fileName: str,fontSize: int,fontChars: Any,glyphCount: int,) -> Font:
        """Load font from file with extended parameters"""
        ...
def load_font_from_image(image: Image,key: Color,firstChar: int,) -> Font:
        """Load font from Image (XNA style)"""
        ...
def load_font_from_memory(fileType: str,fileData: str,dataSize: int,fontSize: int,fontChars: Any,glyphCount: int,) -> Font:
        """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
        ...
def load_image(fileName: str,) -> Image:
        """Load image from file into CPU memory (RAM)"""
        ...
def load_image_anim(fileName: str,frames: Any,) -> Image:
        """Load image sequence from file (frames appended to image.data)"""
        ...
def load_image_colors(image: Image,) -> Any:
        """Load color data from image as a Color array (RGBA - 32bit)"""
        ...
def load_image_from_memory(fileType: str,fileData: str,dataSize: int,) -> Image:
        """Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
        ...
def load_image_from_screen() -> Image:
        """Load image from screen buffer and (screenshot)"""
        ...
def load_image_from_texture(texture: Texture,) -> Image:
        """Load image from GPU texture data"""
        ...
def load_image_palette(image: Image,maxPaletteSize: int,colorCount: Any,) -> Any:
        """Load colors palette from image as a Color array (RGBA - 32bit)"""
        ...
def load_image_raw(fileName: str,width: int,height: int,format: int,headerSize: int,) -> Image:
        """Load image from RAW file data"""
        ...
def load_material_default() -> Material:
        """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
        ...
def load_materials(fileName: str,materialCount: Any,) -> Any:
        """Load materials from model file"""
        ...
def load_model(fileName: str,) -> Model:
        """Load model from files (meshes and materials)"""
        ...
def load_model_animations(fileName: str,animCount: Any,) -> Any:
        """Load model animations from file"""
        ...
def load_model_from_mesh(mesh: Mesh,) -> Model:
        """Load model from generated mesh (default material)"""
        ...
def load_music_stream(fileName: str,) -> Music:
        """Load music stream from file"""
        ...
def load_music_stream_from_memory(fileType: str,data: str,dataSize: int,) -> Music:
        """Load music stream from data"""
        ...
def load_render_texture(width: int,height: int,) -> RenderTexture:
        """Load texture for rendering (framebuffer)"""
        ...
def load_shader(vsFileName: str,fsFileName: str,) -> Shader:
        """Load shader from files and bind default locations"""
        ...
def load_shader_from_memory(vsCode: str,fsCode: str,) -> Shader:
        """Load shader from code strings and bind default locations"""
        ...
def load_sound(fileName: str,) -> Sound:
        """Load sound from file"""
        ...
def load_sound_from_wave(wave: Wave,) -> Sound:
        """Load sound from wave data"""
        ...
def load_storage_value(position: int,) -> int:
        """Load integer value from storage file (from defined position)"""
        ...
def load_texture(fileName: str,) -> Texture:
        """Load texture from file into GPU memory (VRAM)"""
        ...
def load_texture_cubemap(image: Image,layout: int,) -> Texture:
        """Load cubemap from image, multiple image cubemap layouts supported"""
        ...
def load_texture_from_image(image: Image,) -> Texture:
        """Load texture from image data"""
        ...
def load_vr_stereo_config(device: VrDeviceInfo,) -> VrStereoConfig:
        """Load VR stereo config for VR simulator device parameters"""
        ...
def load_wave(fileName: str,) -> Wave:
        """Load wave data from file"""
        ...
def load_wave_from_memory(fileType: str,fileData: str,dataSize: int,) -> Wave:
        """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
        ...
def load_wave_samples(wave: Wave,) -> Any:
        """Load samples data from wave as a floats array"""
        ...
MATERIAL_MAP_ALBEDO: int
MATERIAL_MAP_BRDF: int
MATERIAL_MAP_CUBEMAP: int
MATERIAL_MAP_EMISSION: int
MATERIAL_MAP_HEIGHT: int
MATERIAL_MAP_IRRADIANCE: int
MATERIAL_MAP_METALNESS: int
MATERIAL_MAP_NORMAL: int
MATERIAL_MAP_OCCLUSION: int
MATERIAL_MAP_PREFILTER: int
MATERIAL_MAP_ROUGHNESS: int
MOUSE_BUTTON_BACK: int
MOUSE_BUTTON_EXTRA: int
MOUSE_BUTTON_FORWARD: int
MOUSE_BUTTON_LEFT: int
MOUSE_BUTTON_MIDDLE: int
MOUSE_BUTTON_RIGHT: int
MOUSE_BUTTON_SIDE: int
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
def maximize_window() -> None:
        """Set window state: maximized, if resizable (only PLATFORM_DESKTOP)"""
        ...
def measure_text(text: str,fontSize: int,) -> int:
        """Measure string width for default font"""
        ...
def measure_text_ex(font: Font,text: str,fontSize: float,spacing: float,) -> Vector2:
        """Measure string size for Font"""
        ...
def mem_alloc(size: int,) -> Any:
        """Internal memory allocator"""
        ...
def mem_free(ptr: Any,) -> None:
        """Internal memory free"""
        ...
def mem_realloc(ptr: Any,size: int,) -> Any:
        """Internal memory reallocator"""
        ...
def minimize_window() -> None:
        """Set window state: minimized, if resizable (only PLATFORM_DESKTOP)"""
        ...
NPATCH_NINE_PATCH: int
NPATCH_THREE_PATCH_HORIZONTAL: int
NPATCH_THREE_PATCH_VERTICAL: int
OPENGL_11: int
OPENGL_21: int
OPENGL_33: int
OPENGL_43: int
OPENGL_ES_20: int
def open_url(url: str,) -> None:
        """Open URL with default system browser (if available)"""
        ...
PHYSICS_CIRCLE: int
PHYSICS_POLYGON: int
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
PROGRESSBAR: int
PROGRESS_PADDING: int
def pause_audio_stream(stream: AudioStream,) -> None:
        """Pause audio stream"""
        ...
def pause_music_stream(music: Music,) -> None:
        """Pause music playing"""
        ...
def pause_sound(sound: Sound,) -> None:
        """Pause a sound"""
        ...
def physics_add_force(PhysicsBodyData_pointer_0: Any,Vector2_1: Vector2,) -> None:
        """void PhysicsAddForce(struct PhysicsBodyData *, struct Vector2);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def physics_add_torque(PhysicsBodyData_pointer_0: Any,float_1: float,) -> None:
        """void PhysicsAddTorque(struct PhysicsBodyData *, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def physics_shatter(PhysicsBodyData_pointer_0: Any,Vector2_1: Vector2,float_2: float,) -> None:
        """void PhysicsShatter(struct PhysicsBodyData *, struct Vector2, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def play_audio_stream(stream: AudioStream,) -> None:
        """Play audio stream"""
        ...
def play_music_stream(music: Music,) -> None:
        """Start music playing"""
        ...
def play_sound(sound: Sound,) -> None:
        """Play a sound"""
        ...
def play_sound_multi(sound: Sound,) -> None:
        """Play a sound (using multichannel buffer pool)"""
        ...
def poll_input_events() -> None:
        """Register all input events"""
        ...
RESERVED: int
RL_ATTACHMENT_COLOR_CHANNEL0: int
RL_ATTACHMENT_COLOR_CHANNEL1: int
RL_ATTACHMENT_COLOR_CHANNEL2: int
RL_ATTACHMENT_COLOR_CHANNEL3: int
RL_ATTACHMENT_COLOR_CHANNEL4: int
RL_ATTACHMENT_COLOR_CHANNEL5: int
RL_ATTACHMENT_COLOR_CHANNEL6: int
RL_ATTACHMENT_COLOR_CHANNEL7: int
RL_ATTACHMENT_CUBEMAP_NEGATIVE_X: int
RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y: int
RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z: int
RL_ATTACHMENT_CUBEMAP_POSITIVE_X: int
RL_ATTACHMENT_CUBEMAP_POSITIVE_Y: int
RL_ATTACHMENT_CUBEMAP_POSITIVE_Z: int
RL_ATTACHMENT_DEPTH: int
RL_ATTACHMENT_RENDERBUFFER: int
RL_ATTACHMENT_STENCIL: int
RL_ATTACHMENT_TEXTURE2D: int
RL_BLEND_ADDITIVE: int
RL_BLEND_ADD_COLORS: int
RL_BLEND_ALPHA: int
RL_BLEND_CUSTOM: int
RL_BLEND_MULTIPLIED: int
RL_BLEND_SUBTRACT_COLORS: int
RL_LOG_ALL: int
RL_LOG_DEBUG: int
RL_LOG_ERROR: int
RL_LOG_FATAL: int
RL_LOG_INFO: int
RL_LOG_NONE: int
RL_LOG_TRACE: int
RL_LOG_WARNING: int
RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA: int
RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA: int
RL_PIXELFORMAT_COMPRESSED_DXT1_RGB: int
RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA: int
RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA: int
RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA: int
RL_PIXELFORMAT_COMPRESSED_ETC1_RGB: int
RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA: int
RL_PIXELFORMAT_COMPRESSED_ETC2_RGB: int
RL_PIXELFORMAT_COMPRESSED_PVRT_RGB: int
RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA: int
RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE: int
RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA: int
RL_PIXELFORMAT_UNCOMPRESSED_R32: int
RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32: int
RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32: int
RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4: int
RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1: int
RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5: int
RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8: int
RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8: int
RL_SHADER_ATTRIB_FLOAT: int
RL_SHADER_ATTRIB_VEC2: int
RL_SHADER_ATTRIB_VEC3: int
RL_SHADER_ATTRIB_VEC4: int
RL_SHADER_LOC_COLOR_AMBIENT: int
RL_SHADER_LOC_COLOR_DIFFUSE: int
RL_SHADER_LOC_COLOR_SPECULAR: int
RL_SHADER_LOC_MAP_ALBEDO: int
RL_SHADER_LOC_MAP_BRDF: int
RL_SHADER_LOC_MAP_CUBEMAP: int
RL_SHADER_LOC_MAP_EMISSION: int
RL_SHADER_LOC_MAP_HEIGHT: int
RL_SHADER_LOC_MAP_IRRADIANCE: int
RL_SHADER_LOC_MAP_METALNESS: int
RL_SHADER_LOC_MAP_NORMAL: int
RL_SHADER_LOC_MAP_OCCLUSION: int
RL_SHADER_LOC_MAP_PREFILTER: int
RL_SHADER_LOC_MAP_ROUGHNESS: int
RL_SHADER_LOC_MATRIX_MODEL: int
RL_SHADER_LOC_MATRIX_MVP: int
RL_SHADER_LOC_MATRIX_NORMAL: int
RL_SHADER_LOC_MATRIX_PROJECTION: int
RL_SHADER_LOC_MATRIX_VIEW: int
RL_SHADER_LOC_VECTOR_VIEW: int
RL_SHADER_LOC_VERTEX_COLOR: int
RL_SHADER_LOC_VERTEX_NORMAL: int
RL_SHADER_LOC_VERTEX_POSITION: int
RL_SHADER_LOC_VERTEX_TANGENT: int
RL_SHADER_LOC_VERTEX_TEXCOORD01: int
RL_SHADER_LOC_VERTEX_TEXCOORD02: int
RL_SHADER_UNIFORM_FLOAT: int
RL_SHADER_UNIFORM_INT: int
RL_SHADER_UNIFORM_IVEC2: int
RL_SHADER_UNIFORM_IVEC3: int
RL_SHADER_UNIFORM_IVEC4: int
RL_SHADER_UNIFORM_SAMPLER2D: int
RL_SHADER_UNIFORM_VEC2: int
RL_SHADER_UNIFORM_VEC3: int
RL_SHADER_UNIFORM_VEC4: int
RL_TEXTURE_FILTER_ANISOTROPIC_16X: int
RL_TEXTURE_FILTER_ANISOTROPIC_4X: int
RL_TEXTURE_FILTER_ANISOTROPIC_8X: int
RL_TEXTURE_FILTER_BILINEAR: int
RL_TEXTURE_FILTER_POINT: int
RL_TEXTURE_FILTER_TRILINEAR: int
def reset_physics() -> None:
        """void ResetPhysics();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def restore_window() -> None:
        """Set window state: not minimized/maximized (only PLATFORM_DESKTOP)"""
        ...
def resume_audio_stream(stream: AudioStream,) -> None:
        """Resume audio stream"""
        ...
def resume_music_stream(music: Music,) -> None:
        """Resume playing paused music"""
        ...
def resume_sound(sound: Sound,) -> None:
        """Resume a paused sound"""
        ...
SCROLLBAR: int
SCROLLBAR_LEFT_SIDE: int
SCROLLBAR_RIGHT_SIDE: int
SCROLLBAR_SIDE: int
SCROLLBAR_WIDTH: int
SCROLL_PADDING: int
SCROLL_SLIDER_PADDING: int
SCROLL_SLIDER_SIZE: int
SCROLL_SPEED: int
SHADER_ATTRIB_FLOAT: int
SHADER_ATTRIB_VEC2: int
SHADER_ATTRIB_VEC3: int
SHADER_ATTRIB_VEC4: int
SHADER_LOC_COLOR_AMBIENT: int
SHADER_LOC_COLOR_DIFFUSE: int
SHADER_LOC_COLOR_SPECULAR: int
SHADER_LOC_MAP_ALBEDO: int
SHADER_LOC_MAP_BRDF: int
SHADER_LOC_MAP_CUBEMAP: int
SHADER_LOC_MAP_EMISSION: int
SHADER_LOC_MAP_HEIGHT: int
SHADER_LOC_MAP_IRRADIANCE: int
SHADER_LOC_MAP_METALNESS: int
SHADER_LOC_MAP_NORMAL: int
SHADER_LOC_MAP_OCCLUSION: int
SHADER_LOC_MAP_PREFILTER: int
SHADER_LOC_MAP_ROUGHNESS: int
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
SLIDER: int
SLIDER_PADDING: int
SLIDER_WIDTH: int
SPINNER: int
SPIN_BUTTON_PADDING: int
SPIN_BUTTON_WIDTH: int
STATUSBAR: int
def save_file_data(fileName: str,data: Any,bytesToWrite: int,) -> bool:
        """Save data to file from byte array (write), returns true on success"""
        ...
def save_file_text(fileName: str,text: str,) -> bool:
        """Save text data to file (write), string must be ' 0' terminated, returns true on success"""
        ...
def save_storage_value(position: int,value: int,) -> bool:
        """Save integer value to storage file (to defined position), returns true on success"""
        ...
def seek_music_stream(music: Music,position: float,) -> None:
        """Seek music to a position (in seconds)"""
        ...
def set_audio_stream_buffer_size_default(size: int,) -> None:
        """Default size for new audio streams"""
        ...
def set_audio_stream_pitch(stream: AudioStream,pitch: float,) -> None:
        """Set pitch for audio stream (1.0 is base level)"""
        ...
def set_audio_stream_volume(stream: AudioStream,volume: float,) -> None:
        """Set volume for audio stream (1.0 is max level)"""
        ...
def set_camera_alt_control(keyAlt: int,) -> None:
        """Set camera alt key to combine with mouse movement (free camera)"""
        ...
def set_camera_mode(camera: Camera3D,mode: int,) -> None:
        """Set camera mode (multiple camera modes available)"""
        ...
def set_camera_move_controls(keyFront: int,keyBack: int,keyRight: int,keyLeft: int,keyUp: int,keyDown: int,) -> None:
        """Set camera move controls (1st person and 3rd person cameras)"""
        ...
def set_camera_pan_control(keyPan: int,) -> None:
        """Set camera pan key to combine with mouse movement (free camera)"""
        ...
def set_camera_smooth_zoom_control(keySmoothZoom: int,) -> None:
        """Set camera smooth zoom key to combine with mouse (free camera)"""
        ...
def set_clipboard_text(text: str,) -> None:
        """Set clipboard text content"""
        ...
def set_config_flags(flags: int,) -> None:
        """Setup init configuration flags (view FLAGS)"""
        ...
def set_exit_key(key: int,) -> None:
        """Set a custom key to exit program (default is ESC)"""
        ...
def set_gamepad_mappings(mappings: str,) -> int:
        """Set internal gamepad mappings (SDL_GameControllerDB)"""
        ...
def set_gestures_enabled(flags: int,) -> None:
        """Enable a set of gestures using flags"""
        ...
def set_load_file_data_callback(callback: str,) -> None:
        """Set custom file binary data loader"""
        ...
def set_load_file_text_callback(callback: str,) -> None:
        """Set custom file text data loader"""
        ...
def set_master_volume(volume: float,) -> None:
        """Set master volume (listener)"""
        ...
def set_material_texture(material: Any,mapType: int,texture: Texture,) -> None:
        """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
        ...
def set_model_mesh_material(model: Any,meshId: int,materialId: int,) -> None:
        """Set material for a mesh"""
        ...
def set_mouse_cursor(cursor: int,) -> None:
        """Set mouse cursor"""
        ...
def set_mouse_offset(offsetX: int,offsetY: int,) -> None:
        """Set mouse offset"""
        ...
def set_mouse_position(x: int,y: int,) -> None:
        """Set mouse position XY"""
        ...
def set_mouse_scale(scaleX: float,scaleY: float,) -> None:
        """Set mouse scaling"""
        ...
def set_music_pitch(music: Music,pitch: float,) -> None:
        """Set pitch for a music (1.0 is base level)"""
        ...
def set_music_volume(music: Music,volume: float,) -> None:
        """Set volume for music (1.0 is max level)"""
        ...
def set_physics_body_rotation(PhysicsBodyData_pointer_0: Any,float_1: float,) -> None:
        """void SetPhysicsBodyRotation(struct PhysicsBodyData *, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def set_physics_gravity(float_0: float,float_1: float,) -> None:
        """void SetPhysicsGravity(float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def set_physics_time_step(double_0: float,) -> None:
        """void SetPhysicsTimeStep(double);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def set_pixel_color(dstPtr: Any,color: Color,format: int,) -> None:
        """Set color formatted into destination pixel pointer"""
        ...
def set_random_seed(seed: int,) -> None:
        """Set the seed for the random number generator"""
        ...
def set_save_file_data_callback(callback: str,) -> None:
        """Set custom file binary data saver"""
        ...
def set_save_file_text_callback(callback: str,) -> None:
        """Set custom file text data saver"""
        ...
def set_shader_value(shader: Shader,locIndex: int,value: Any,uniformType: int,) -> None:
        """Set shader uniform value"""
        ...
def set_shader_value_matrix(shader: Shader,locIndex: int,mat: Matrix,) -> None:
        """Set shader uniform value (matrix 4x4)"""
        ...
def set_shader_value_texture(shader: Shader,locIndex: int,texture: Texture,) -> None:
        """Set shader uniform value for texture (sampler2d)"""
        ...
def set_shader_value_v(shader: Shader,locIndex: int,value: Any,uniformType: int,count: int,) -> None:
        """Set shader uniform value vector"""
        ...
def set_shapes_texture(texture: Texture,source: Rectangle,) -> None:
        """Set texture and rectangle to be used on shapes drawing"""
        ...
def set_sound_pitch(sound: Sound,pitch: float,) -> None:
        """Set pitch for a sound (1.0 is base level)"""
        ...
def set_sound_volume(sound: Sound,volume: float,) -> None:
        """Set volume for a sound (1.0 is max level)"""
        ...
def set_target_fps(fps: int,) -> None:
        """Set target FPS (maximum)"""
        ...
def set_texture_filter(texture: Texture,filter: int,) -> None:
        """Set texture scaling filter mode"""
        ...
def set_texture_wrap(texture: Texture,wrap: int,) -> None:
        """Set texture wrapping mode"""
        ...
def set_trace_log_callback(callback: str,) -> None:
        """Set custom trace log"""
        ...
def set_trace_log_level(logLevel: int,) -> None:
        """Set the current threshold (minimum) log level"""
        ...
def set_window_icon(image: Image,) -> None:
        """Set icon for window (only PLATFORM_DESKTOP)"""
        ...
def set_window_min_size(width: int,height: int,) -> None:
        """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
        ...
def set_window_monitor(monitor: int,) -> None:
        """Set monitor for the current window (fullscreen mode)"""
        ...
def set_window_position(x: int,y: int,) -> None:
        """Set window position on screen (only PLATFORM_DESKTOP)"""
        ...
def set_window_size(width: int,height: int,) -> None:
        """Set window dimensions"""
        ...
def set_window_state(flags: int,) -> None:
        """Set window configuration state using flags"""
        ...
def set_window_title(title: str,) -> None:
        """Set title for window (only PLATFORM_DESKTOP)"""
        ...
def show_cursor() -> None:
        """Shows cursor"""
        ...
def stop_audio_stream(stream: AudioStream,) -> None:
        """Stop audio stream"""
        ...
def stop_music_stream(music: Music,) -> None:
        """Stop music playing"""
        ...
def stop_sound(sound: Sound,) -> None:
        """Stop playing a sound"""
        ...
def stop_sound_multi() -> None:
        """Stop any sound playing (using multichannel buffer pool)"""
        ...
def swap_screen_buffer() -> None:
        """Swap back buffer with front buffer (screen drawing)"""
        ...
TEXTBOX: int
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
TEXT_ALIGNMENT: int
TEXT_COLOR_DISABLED: int
TEXT_COLOR_FOCUSED: int
TEXT_COLOR_NORMAL: int
TEXT_COLOR_PRESSED: int
TEXT_INNER_PADDING: int
TEXT_LINES_PADDING: int
TEXT_PADDING: int
TEXT_SIZE: int
TEXT_SPACING: int
TOGGLE: int
def take_screenshot(fileName: str,) -> None:
        """Takes a screenshot of current screen (filename extension defines format)"""
        ...
def text_append(text: str,append: str,position: Any,) -> None:
        """Append text at specific position and move cursor!"""
        ...
def text_codepoints_to_utf8(codepoints: Any,length: int,) -> str:
        """Encode text as codepoints array into UTF-8 text string (WARNING: memory must be freed!)"""
        ...
def text_copy(dst: str,src: str,) -> int:
        """Copy one string to another, returns bytes copied"""
        ...
def text_find_index(text: str,find: str,) -> int:
        """Find first text occurrence within a string"""
        ...
def text_format(*args) -> str:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def text_insert(text: str,insert: str,position: int,) -> str:
        """Insert text in a position (WARNING: memory must be freed!)"""
        ...
def text_is_equal(text1: str,text2: str,) -> bool:
        """Check if two text string are equal"""
        ...
def text_join(textList: str,count: int,delimiter: str,) -> str:
        """Join text strings with delimiter"""
        ...
def text_length(text: str,) -> int:
        """Get text length, checks for ' 0' ending"""
        ...
def text_replace(text: str,replace: str,by: str,) -> str:
        """Replace text string (WARNING: memory must be freed!)"""
        ...
def text_split(text: str,delimiter: str,count: Any,) -> str:
        """Split text into multiple strings"""
        ...
def text_subtext(text: str,position: int,length: int,) -> str:
        """Get a piece of a text string"""
        ...
def text_to_integer(text: str,) -> int:
        """Get integer value from text (negative values not supported)"""
        ...
def text_to_lower(text: str,) -> str:
        """Get lower case version of provided string"""
        ...
def text_to_pascal(text: str,) -> str:
        """Get Pascal case notation version of provided string"""
        ...
def text_to_upper(text: str,) -> str:
        """Get upper case version of provided string"""
        ...
def toggle_fullscreen() -> None:
        """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
        ...
def trace_log(*args) -> None:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def unload_audio_stream(stream: AudioStream,) -> None:
        """Unload audio stream and free memory"""
        ...
def unload_codepoints(codepoints: Any,) -> None:
        """Unload codepoints data from memory"""
        ...
def unload_file_data(data: str,) -> None:
        """Unload file data allocated by LoadFileData()"""
        ...
def unload_file_text(text: str,) -> None:
        """Unload file text data allocated by LoadFileText()"""
        ...
def unload_font(font: Font,) -> None:
        """Unload Font from GPU memory (VRAM)"""
        ...
def unload_font_data(chars: Any,glyphCount: int,) -> None:
        """Unload font chars info data (RAM)"""
        ...
def unload_image(image: Image,) -> None:
        """Unload image from CPU memory (RAM)"""
        ...
def unload_image_colors(colors: Any,) -> None:
        """Unload color data loaded with LoadImageColors()"""
        ...
def unload_image_palette(colors: Any,) -> None:
        """Unload colors palette loaded with LoadImagePalette()"""
        ...
def unload_material(material: Material,) -> None:
        """Unload material from GPU memory (VRAM)"""
        ...
def unload_mesh(mesh: Mesh,) -> None:
        """Unload mesh data from CPU and GPU"""
        ...
def unload_model(model: Model,) -> None:
        """Unload model (including meshes) from memory (RAM and/or VRAM)"""
        ...
def unload_model_animation(anim: ModelAnimation,) -> None:
        """Unload animation data"""
        ...
def unload_model_animations(animations: Any,count: int,) -> None:
        """Unload animation array data"""
        ...
def unload_model_keep_meshes(model: Model,) -> None:
        """Unload model (but not meshes) from memory (RAM and/or VRAM)"""
        ...
def unload_music_stream(music: Music,) -> None:
        """Unload music stream"""
        ...
def unload_render_texture(target: RenderTexture,) -> None:
        """Unload render texture from GPU memory (VRAM)"""
        ...
def unload_shader(shader: Shader,) -> None:
        """Unload shader from GPU memory (VRAM)"""
        ...
def unload_sound(sound: Sound,) -> None:
        """Unload sound"""
        ...
def unload_texture(texture: Texture,) -> None:
        """Unload texture from GPU memory (VRAM)"""
        ...
def unload_vr_stereo_config(config: VrStereoConfig,) -> None:
        """Unload VR stereo config"""
        ...
def unload_wave(wave: Wave,) -> None:
        """Unload wave data"""
        ...
def unload_wave_samples(samples: Any,) -> None:
        """Unload samples data loaded with LoadWaveSamples()"""
        ...
def update_audio_stream(stream: AudioStream,data: Any,frameCount: int,) -> None:
        """Update audio stream buffers with data"""
        ...
def update_camera(camera: Any,) -> None:
        """Update camera position for selected mode"""
        ...
def update_mesh_buffer(mesh: Mesh,index: int,data: Any,dataSize: int,offset: int,) -> None:
        """Update mesh vertex data in GPU for a specific buffer index"""
        ...
def update_model_animation(model: Model,anim: ModelAnimation,frame: int,) -> None:
        """Update model animation pose"""
        ...
def update_music_stream(music: Music,) -> None:
        """Updates buffers for music streaming"""
        ...
def update_physics() -> None:
        """void UpdatePhysics();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def update_sound(sound: Sound,data: Any,sampleCount: int,) -> None:
        """Update sound buffer with new data"""
        ...
def update_texture(texture: Texture,pixels: Any,) -> None:
        """Update GPU texture with new data"""
        ...
def update_texture_rec(texture: Texture,rec: Rectangle,pixels: Any,) -> None:
        """Update GPU texture rectangle with new data"""
        ...
def upload_mesh(mesh: Any,dynamic: bool,) -> None:
        """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
        ...
VALUEBOX: int
def wait_time(ms: float,) -> None:
        """Wait for some milliseconds (halt program execution)"""
        ...
def wave_copy(wave: Wave,) -> Wave:
        """Copy a wave to a new wave"""
        ...
def wave_crop(wave: Any,initSample: int,finalSample: int,) -> None:
        """Crop a wave to defined samples range"""
        ...
def wave_format(wave: Any,sampleRate: int,sampleSize: int,channels: int,) -> None:
        """Convert wave data to desired format"""
        ...
def window_should_close() -> bool:
        """Check if KEY_ESCAPE pressed or Close icon pressed"""
        ...
def rl_active_draw_buffers(int_0: int,) -> None:
        """void rlActiveDrawBuffers(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_active_texture_slot(int_0: int,) -> None:
        """void rlActiveTextureSlot(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_begin(int_0: int,) -> None:
        """void rlBegin(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_bind_image_texture(unsignedint_0: int,unsignedint_1: int,unsignedint_2: int,int_3: int,) -> None:
        """void rlBindImageTexture(unsigned int, unsigned int, unsigned int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_bind_shader_buffer(unsignedint_0: int,unsignedint_1: int,) -> None:
        """void rlBindShaderBuffer(unsigned int, unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_check_errors() -> None:
        """void rlCheckErrors();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_check_render_batch_limit(int_0: int,) -> bool:
        """_Bool rlCheckRenderBatchLimit(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_clear_color(unsignedchar_0: str,unsignedchar_1: str,unsignedchar_2: str,unsignedchar_3: str,) -> None:
        """void rlClearColor(unsigned char, unsigned char, unsigned char, unsigned char);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_clear_screen_buffers() -> None:
        """void rlClearScreenBuffers();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_color3f(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlColor3f(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_color4f(float_0: float,float_1: float,float_2: float,float_3: float,) -> None:
        """void rlColor4f(float, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_color4ub(unsignedchar_0: str,unsignedchar_1: str,unsignedchar_2: str,unsignedchar_3: str,) -> None:
        """void rlColor4ub(unsigned char, unsigned char, unsigned char, unsigned char);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_compile_shader(str_0: str,int_1: int,) -> int:
        """unsigned int rlCompileShader(char *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_compute_shader_dispatch(unsignedint_0: int,unsignedint_1: int,unsignedint_2: int,) -> None:
        """void rlComputeShaderDispatch(unsigned int, unsigned int, unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_copy_buffers_elements(unsignedint_0: int,unsignedint_1: int,unsignedlonglong_2: int,unsignedlonglong_3: int,unsignedlonglong_4: int,) -> None:
        """void rlCopyBuffersElements(unsigned int, unsigned int, unsigned long long, unsigned long long, unsigned long long);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_backface_culling() -> None:
        """void rlDisableBackfaceCulling();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_color_blend() -> None:
        """void rlDisableColorBlend();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_depth_mask() -> None:
        """void rlDisableDepthMask();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_depth_test() -> None:
        """void rlDisableDepthTest();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_framebuffer() -> None:
        """void rlDisableFramebuffer();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_scissor_test() -> None:
        """void rlDisableScissorTest();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_shader() -> None:
        """void rlDisableShader();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_smooth_lines() -> None:
        """void rlDisableSmoothLines();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_stereo_render() -> None:
        """void rlDisableStereoRender();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_texture() -> None:
        """void rlDisableTexture();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_texture_cubemap() -> None:
        """void rlDisableTextureCubemap();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_vertex_array() -> None:
        """void rlDisableVertexArray();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_vertex_attribute(unsignedint_0: int,) -> None:
        """void rlDisableVertexAttribute(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_vertex_buffer() -> None:
        """void rlDisableVertexBuffer();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_vertex_buffer_element() -> None:
        """void rlDisableVertexBufferElement();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_disable_wire_mode() -> None:
        """void rlDisableWireMode();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_draw_render_batch(rlRenderBatch_pointer_0: Any,) -> None:
        """void rlDrawRenderBatch(struct rlRenderBatch *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_draw_render_batch_active() -> None:
        """void rlDrawRenderBatchActive();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_draw_vertex_array(int_0: int,int_1: int,) -> None:
        """void rlDrawVertexArray(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_draw_vertex_array_elements(int_0: int,int_1: int,void_pointer_2: Any,) -> None:
        """void rlDrawVertexArrayElements(int, int, void *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_draw_vertex_array_elements_instanced(int_0: int,int_1: int,void_pointer_2: Any,int_3: int,) -> None:
        """void rlDrawVertexArrayElementsInstanced(int, int, void *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_draw_vertex_array_instanced(int_0: int,int_1: int,int_2: int,) -> None:
        """void rlDrawVertexArrayInstanced(int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_backface_culling() -> None:
        """void rlEnableBackfaceCulling();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_color_blend() -> None:
        """void rlEnableColorBlend();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_depth_mask() -> None:
        """void rlEnableDepthMask();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_depth_test() -> None:
        """void rlEnableDepthTest();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_framebuffer(unsignedint_0: int,) -> None:
        """void rlEnableFramebuffer(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_scissor_test() -> None:
        """void rlEnableScissorTest();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_shader(unsignedint_0: int,) -> None:
        """void rlEnableShader(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_smooth_lines() -> None:
        """void rlEnableSmoothLines();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_stereo_render() -> None:
        """void rlEnableStereoRender();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_texture(unsignedint_0: int,) -> None:
        """void rlEnableTexture(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_texture_cubemap(unsignedint_0: int,) -> None:
        """void rlEnableTextureCubemap(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_vertex_array(unsignedint_0: int,) -> bool:
        """_Bool rlEnableVertexArray(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_vertex_attribute(unsignedint_0: int,) -> None:
        """void rlEnableVertexAttribute(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_vertex_buffer(unsignedint_0: int,) -> None:
        """void rlEnableVertexBuffer(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_vertex_buffer_element(unsignedint_0: int,) -> None:
        """void rlEnableVertexBufferElement(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_enable_wire_mode() -> None:
        """void rlEnableWireMode();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_end() -> None:
        """void rlEnd();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_framebuffer_attach(unsignedint_0: int,unsignedint_1: int,int_2: int,int_3: int,int_4: int,) -> None:
        """void rlFramebufferAttach(unsigned int, unsigned int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_framebuffer_complete(unsignedint_0: int,) -> bool:
        """_Bool rlFramebufferComplete(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_frustum(double_0: float,double_1: float,double_2: float,double_3: float,double_4: float,double_5: float,) -> None:
        """void rlFrustum(double, double, double, double, double, double);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_gen_texture_mipmaps(unsignedint_0: int,int_1: int,int_2: int,int_3: int,int_pointer_4: Any,) -> None:
        """void rlGenTextureMipmaps(unsigned int, int, int, int, int *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_framebuffer_height() -> int:
        """int rlGetFramebufferHeight();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_framebuffer_width() -> int:
        """int rlGetFramebufferWidth();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_gl_texture_formats(int_0: int,int_pointer_1: Any,int_pointer_2: Any,int_pointer_3: Any,) -> None:
        """void rlGetGlTextureFormats(int, int *, int *, int *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_line_width() -> float:
        """float rlGetLineWidth();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_location_attrib(unsignedint_0: int,str_1: str,) -> int:
        """int rlGetLocationAttrib(unsigned int, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_location_uniform(unsignedint_0: int,str_1: str,) -> int:
        """int rlGetLocationUniform(unsigned int, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_matrix_modelview() -> Matrix:
        """struct Matrix rlGetMatrixModelview();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_matrix_projection() -> Matrix:
        """struct Matrix rlGetMatrixProjection();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_matrix_projection_stereo(int_0: int,) -> Matrix:
        """struct Matrix rlGetMatrixProjectionStereo(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_matrix_transform() -> Matrix:
        """struct Matrix rlGetMatrixTransform();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_matrix_view_offset_stereo(int_0: int,) -> Matrix:
        """struct Matrix rlGetMatrixViewOffsetStereo(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_pixel_format_name(unsignedint_0: int,) -> str:
        """char *rlGetPixelFormatName(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_shader_buffer_size(unsignedint_0: int,) -> int:
        """unsigned long long rlGetShaderBufferSize(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_shader_id_default() -> int:
        """unsigned int rlGetShaderIdDefault();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_shader_locs_default() -> Any:
        """int *rlGetShaderLocsDefault();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_texture_id_default() -> int:
        """unsigned int rlGetTextureIdDefault();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_get_version() -> int:
        """int rlGetVersion();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_is_stereo_render_enabled() -> bool:
        """_Bool rlIsStereoRenderEnabled();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_compute_shader_program(unsignedint_0: int,) -> int:
        """unsigned int rlLoadComputeShaderProgram(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_draw_cube() -> None:
        """void rlLoadDrawCube();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_draw_quad() -> None:
        """void rlLoadDrawQuad();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_extensions(void_pointer_0: Any,) -> None:
        """void rlLoadExtensions(void *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_framebuffer(int_0: int,int_1: int,) -> int:
        """unsigned int rlLoadFramebuffer(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_identity() -> None:
        """void rlLoadIdentity();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_render_batch(int_0: int,int_1: int,) -> rlRenderBatch:
        """struct rlRenderBatch rlLoadRenderBatch(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_shader_buffer(unsignedlonglong_0: int,void_pointer_1: Any,int_2: int,) -> int:
        """unsigned int rlLoadShaderBuffer(unsigned long long, void *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_shader_code(str_0: str,str_1: str,) -> int:
        """unsigned int rlLoadShaderCode(char *, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_shader_program(unsignedint_0: int,unsignedint_1: int,) -> int:
        """unsigned int rlLoadShaderProgram(unsigned int, unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_texture(void_pointer_0: Any,int_1: int,int_2: int,int_3: int,int_4: int,) -> int:
        """unsigned int rlLoadTexture(void *, int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_texture_cubemap(void_pointer_0: Any,int_1: int,int_2: int,) -> int:
        """unsigned int rlLoadTextureCubemap(void *, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_texture_depth(int_0: int,int_1: int,_Bool_2: bool,) -> int:
        """unsigned int rlLoadTextureDepth(int, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_vertex_array() -> int:
        """unsigned int rlLoadVertexArray();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_vertex_buffer(void_pointer_0: Any,int_1: int,_Bool_2: bool,) -> int:
        """unsigned int rlLoadVertexBuffer(void *, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_load_vertex_buffer_element(void_pointer_0: Any,int_1: int,_Bool_2: bool,) -> int:
        """unsigned int rlLoadVertexBufferElement(void *, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_matrix_mode(int_0: int,) -> None:
        """void rlMatrixMode(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_mult_matrixf(float_pointer_0: Any,) -> None:
        """void rlMultMatrixf(float *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_normal3f(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlNormal3f(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_ortho(double_0: float,double_1: float,double_2: float,double_3: float,double_4: float,double_5: float,) -> None:
        """void rlOrtho(double, double, double, double, double, double);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_pop_matrix() -> None:
        """void rlPopMatrix();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_push_matrix() -> None:
        """void rlPushMatrix();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_read_screen_pixels(int_0: int,int_1: int,) -> str:
        """unsigned char *rlReadScreenPixels(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_read_shader_buffer_elements(unsignedint_0: int,void_pointer_1: Any,unsignedlonglong_2: int,unsignedlonglong_3: int,) -> None:
        """void rlReadShaderBufferElements(unsigned int, void *, unsigned long long, unsigned long long);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_read_texture_pixels(unsignedint_0: int,int_1: int,int_2: int,int_3: int,) -> Any:
        """void *rlReadTexturePixels(unsigned int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_rotatef(float_0: float,float_1: float,float_2: float,float_3: float,) -> None:
        """void rlRotatef(float, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_scalef(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlScalef(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_scissor(int_0: int,int_1: int,int_2: int,int_3: int,) -> None:
        """void rlScissor(int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_blend_factors(int_0: int,int_1: int,int_2: int,) -> None:
        """void rlSetBlendFactors(int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_blend_mode(int_0: int,) -> None:
        """void rlSetBlendMode(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_line_width(float_0: float,) -> None:
        """void rlSetLineWidth(float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_matrix_modelview(Matrix_0: Matrix,) -> None:
        """void rlSetMatrixModelview(struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_matrix_projection(Matrix_0: Matrix,) -> None:
        """void rlSetMatrixProjection(struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_matrix_projection_stereo(Matrix_0: Matrix,Matrix_1: Matrix,) -> None:
        """void rlSetMatrixProjectionStereo(struct Matrix, struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_matrix_view_offset_stereo(Matrix_0: Matrix,Matrix_1: Matrix,) -> None:
        """void rlSetMatrixViewOffsetStereo(struct Matrix, struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_render_batch_active(rlRenderBatch_pointer_0: Any,) -> None:
        """void rlSetRenderBatchActive(struct rlRenderBatch *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_shader(unsignedint_0: int,int_pointer_1: Any,) -> None:
        """void rlSetShader(unsigned int, int *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_texture(unsignedint_0: int,) -> None:
        """void rlSetTexture(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_uniform(int_0: int,void_pointer_1: Any,int_2: int,int_3: int,) -> None:
        """void rlSetUniform(int, void *, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_uniform_matrix(int_0: int,Matrix_1: Matrix,) -> None:
        """void rlSetUniformMatrix(int, struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_uniform_sampler(int_0: int,unsignedint_1: int,) -> None:
        """void rlSetUniformSampler(int, unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_vertex_attribute(unsignedint_0: int,int_1: int,int_2: int,_Bool_3: bool,int_4: int,void_pointer_5: Any,) -> None:
        """void rlSetVertexAttribute(unsigned int, int, int, _Bool, int, void *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_vertex_attribute_default(int_0: int,void_pointer_1: Any,int_2: int,int_3: int,) -> None:
        """void rlSetVertexAttributeDefault(int, void *, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_set_vertex_attribute_divisor(unsignedint_0: int,int_1: int,) -> None:
        """void rlSetVertexAttributeDivisor(unsigned int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_tex_coord2f(float_0: float,float_1: float,) -> None:
        """void rlTexCoord2f(float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_texture_parameters(unsignedint_0: int,int_1: int,int_2: int,) -> None:
        """void rlTextureParameters(unsigned int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_translatef(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlTranslatef(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_unload_framebuffer(unsignedint_0: int,) -> None:
        """void rlUnloadFramebuffer(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_unload_render_batch(rlRenderBatch_0: rlRenderBatch,) -> None:
        """void rlUnloadRenderBatch(struct rlRenderBatch);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_unload_shader_buffer(unsignedint_0: int,) -> None:
        """void rlUnloadShaderBuffer(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_unload_shader_program(unsignedint_0: int,) -> None:
        """void rlUnloadShaderProgram(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_unload_texture(unsignedint_0: int,) -> None:
        """void rlUnloadTexture(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_unload_vertex_array(unsignedint_0: int,) -> None:
        """void rlUnloadVertexArray(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_unload_vertex_buffer(unsignedint_0: int,) -> None:
        """void rlUnloadVertexBuffer(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_update_shader_buffer_elements(unsignedint_0: int,void_pointer_1: Any,unsignedlonglong_2: int,unsignedlonglong_3: int,) -> None:
        """void rlUpdateShaderBufferElements(unsigned int, void *, unsigned long long, unsigned long long);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_update_texture(unsignedint_0: int,int_1: int,int_2: int,int_3: int,int_4: int,int_5: int,void_pointer_6: Any,) -> None:
        """void rlUpdateTexture(unsigned int, int, int, int, int, int, void *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_update_vertex_buffer(unsignedint_0: int,void_pointer_1: Any,int_2: int,int_3: int,) -> None:
        """void rlUpdateVertexBuffer(unsigned int, void *, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_vertex2f(float_0: float,float_1: float,) -> None:
        """void rlVertex2f(float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_vertex2i(int_0: int,int_1: int,) -> None:
        """void rlVertex2i(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_vertex3f(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlVertex3f(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rl_viewport(int_0: int,int_1: int,int_2: int,int_3: int,) -> None:
        """void rlViewport(int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlgl_close() -> None:
        """void rlglClose();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlgl_init(int_0: int,int_1: int,) -> None:
        """void rlglInit(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
class AudioStream:
    """ struct """
    def __init__(self, buffer, sampleRate, sampleSize, channels):
        self.buffer=buffer
        self.sampleRate=sampleRate
        self.sampleSize=sampleSize
        self.channels=channels
BlendMode: int
class BoneInfo:
    """ struct """
    def __init__(self, name, parent):
        self.name=name
        self.parent=parent
class BoundingBox:
    """ struct """
    def __init__(self, min, max):
        self.min=min
        self.max=max
class Camera:
    """ struct """
    def __init__(self, position, target, up, fovy, projection):
        self.position=position
        self.target=target
        self.up=up
        self.fovy=fovy
        self.projection=projection
class Camera2D:
    """ struct """
    def __init__(self, offset, target, rotation, zoom):
        self.offset=offset
        self.target=target
        self.rotation=rotation
        self.zoom=zoom
class Camera3D:
    """ struct """
    def __init__(self, position, target, up, fovy, projection):
        self.position=position
        self.target=target
        self.up=up
        self.fovy=fovy
        self.projection=projection
CameraMode: int
CameraProjection: int
class Color:
    """ struct """
    def __init__(self, r, g, b, a):
        self.r=r
        self.g=g
        self.b=b
        self.a=a
ConfigFlags: int
CubemapLayout: int
class Font:
    """ struct """
    def __init__(self, baseSize, glyphCount, glyphPadding, texture, recs, glyphs):
        self.baseSize=baseSize
        self.glyphCount=glyphCount
        self.glyphPadding=glyphPadding
        self.texture=texture
        self.recs=recs
        self.glyphs=glyphs
FontType: int
GamepadAxis: int
GamepadButton: int
Gesture: int
class GlyphInfo:
    """ struct """
    def __init__(self, value, offsetX, offsetY, advanceX, image):
        self.value=value
        self.offsetX=offsetX
        self.offsetY=offsetY
        self.advanceX=advanceX
        self.image=image
GuiCheckBoxProperty: int
GuiColorPickerProperty: int
GuiComboBoxProperty: int
GuiControl: int
GuiControlProperty: int
GuiControlState: int
GuiDefaultProperty: int
GuiDropdownBoxProperty: int
GuiListViewProperty: int
GuiProgressBarProperty: int
GuiScrollBarProperty: int
GuiScrollBarSide: int
GuiSliderProperty: int
GuiSpinnerProperty: int
class GuiStyleProp:
    """ struct """
    def __init__(self, controlId, propertyId, propertyValue):
        self.controlId=controlId
        self.propertyId=propertyId
        self.propertyValue=propertyValue
GuiTextAlignment: int
GuiTextBoxProperty: int
GuiToggleProperty: int
class Image:
    """ struct """
    def __init__(self, data, width, height, mipmaps, format):
        self.data=data
        self.width=width
        self.height=height
        self.mipmaps=mipmaps
        self.format=format
KeyboardKey: int
class Material:
    """ struct """
    def __init__(self, shader, maps, params):
        self.shader=shader
        self.maps=maps
        self.params=params
class MaterialMap:
    """ struct """
    def __init__(self, texture, color, value):
        self.texture=texture
        self.color=color
        self.value=value
MaterialMapIndex: int
class Matrix:
    """ struct """
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
class Matrix2x2:
    """ struct """
    def __init__(self, m00, m01, m10, m11):
        self.m00=m00
        self.m01=m01
        self.m10=m10
        self.m11=m11
class Mesh:
    """ struct """
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
    """ struct """
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
    """ struct """
    def __init__(self, boneCount, frameCount, bones, framePoses):
        self.boneCount=boneCount
        self.frameCount=frameCount
        self.bones=bones
        self.framePoses=framePoses
MouseButton: int
MouseCursor: int
class Music:
    """ struct """
    def __init__(self, stream, frameCount, looping, ctxType, ctxData):
        self.stream=stream
        self.frameCount=frameCount
        self.looping=looping
        self.ctxType=ctxType
        self.ctxData=ctxData
class NPatchInfo:
    """ struct """
    def __init__(self, source, left, top, right, bottom, layout):
        self.source=source
        self.left=left
        self.top=top
        self.right=right
        self.bottom=bottom
        self.layout=layout
NPatchLayout: int
class PhysicsBodyData:
    """ struct """
    def __init__(self, id, enabled, position, velocity, force, angularVelocity, torque, orient, inertia, inverseInertia, mass, inverseMass, staticFriction, dynamicFriction, restitution, useGravity, isGrounded, freezeOrient, shape):
        self.id=id
        self.enabled=enabled
        self.position=position
        self.velocity=velocity
        self.force=force
        self.angularVelocity=angularVelocity
        self.torque=torque
        self.orient=orient
        self.inertia=inertia
        self.inverseInertia=inverseInertia
        self.mass=mass
        self.inverseMass=inverseMass
        self.staticFriction=staticFriction
        self.dynamicFriction=dynamicFriction
        self.restitution=restitution
        self.useGravity=useGravity
        self.isGrounded=isGrounded
        self.freezeOrient=freezeOrient
        self.shape=shape
class PhysicsManifoldData:
    """ struct """
    def __init__(self, id, bodyA, bodyB, penetration, normal, contacts, contactsCount, restitution, dynamicFriction, staticFriction):
        self.id=id
        self.bodyA=bodyA
        self.bodyB=bodyB
        self.penetration=penetration
        self.normal=normal
        self.contacts=contacts
        self.contactsCount=contactsCount
        self.restitution=restitution
        self.dynamicFriction=dynamicFriction
        self.staticFriction=staticFriction
class PhysicsShape:
    """ struct """
    def __init__(self, type, body, vertexData, radius, transform):
        self.type=type
        self.body=body
        self.vertexData=vertexData
        self.radius=radius
        self.transform=transform
PhysicsShapeType: int
class PhysicsVertexData:
    """ struct """
    def __init__(self, vertexCount, positions, normals):
        self.vertexCount=vertexCount
        self.positions=positions
        self.normals=normals
PixelFormat: int
class Quaternion:
    """ struct """
    def __init__(self, x, y, z, w):
        self.x=x
        self.y=y
        self.z=z
        self.w=w
class Ray:
    """ struct """
    def __init__(self, position, direction):
        self.position=position
        self.direction=direction
class RayCollision:
    """ struct """
    def __init__(self, hit, distance, point, normal):
        self.hit=hit
        self.distance=distance
        self.point=point
        self.normal=normal
class Rectangle:
    """ struct """
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
class RenderTexture:
    """ struct """
    def __init__(self, id, texture, depth):
        self.id=id
        self.texture=texture
        self.depth=depth
class RenderTexture2D:
    """ struct """
    def __init__(self, id, texture, depth):
        self.id=id
        self.texture=texture
        self.depth=depth
class Shader:
    """ struct """
    def __init__(self, id, locs):
        self.id=id
        self.locs=locs
ShaderAttributeDataType: int
ShaderLocationIndex: int
ShaderUniformDataType: int
class Sound:
    """ struct """
    def __init__(self, stream, frameCount):
        self.stream=stream
        self.frameCount=frameCount
class Texture:
    """ struct """
    def __init__(self, id, width, height, mipmaps, format):
        self.id=id
        self.width=width
        self.height=height
        self.mipmaps=mipmaps
        self.format=format
class Texture2D:
    """ struct """
    def __init__(self, id, width, height, mipmaps, format):
        self.id=id
        self.width=width
        self.height=height
        self.mipmaps=mipmaps
        self.format=format
class TextureCubemap:
    """ struct """
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
    """ struct """
    def __init__(self, translation, rotation, scale):
        self.translation=translation
        self.rotation=rotation
        self.scale=scale
class Vector2:
    """ struct """
    def __init__(self, x, y):
        self.x=x
        self.y=y
class Vector3:
    """ struct """
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
class Vector4:
    """ struct """
    def __init__(self, x, y, z, w):
        self.x=x
        self.y=y
        self.z=z
        self.w=w
class VrDeviceInfo:
    """ struct """
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
    """ struct """
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
    """ struct """
    def __init__(self, frameCount, sampleRate, sampleSize, channels, data):
        self.frameCount=frameCount
        self.sampleRate=sampleRate
        self.sampleSize=sampleSize
        self.channels=channels
        self.data=data

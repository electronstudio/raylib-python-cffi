from typing import Any

class struct: ...


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
def BeginBlendMode(mode: int,) -> None:
        """Begin blending mode (alpha, additive, multiplied, subtract, custom)"""
        ...
def BeginDrawing() -> None:
        """Setup canvas (framebuffer) to start drawing"""
        ...
def BeginMode2D(camera: Camera2D,) -> None:
        """Begin 2D mode with custom camera (2D)"""
        ...
def BeginMode3D(camera: Camera3D,) -> None:
        """Begin 3D mode with custom camera (3D)"""
        ...
def BeginScissorMode(x: int,y: int,width: int,height: int,) -> None:
        """Begin scissor mode (define screen area for following drawing)"""
        ...
def BeginShaderMode(shader: Shader,) -> None:
        """Begin custom shader drawing"""
        ...
def BeginTextureMode(target: RenderTexture,) -> None:
        """Begin drawing to render texture"""
        ...
def BeginVrStereoMode(config: VrStereoConfig,) -> None:
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
def ChangeDirectory(dir: str,) -> bool:
        """Change working directory, return true on success"""
        ...
def CheckCollisionBoxSphere(box: BoundingBox,center: Vector3,radius: float,) -> bool:
        """Check collision between box and sphere"""
        ...
def CheckCollisionBoxes(box1: BoundingBox,box2: BoundingBox,) -> bool:
        """Check collision between two bounding boxes"""
        ...
def CheckCollisionCircleRec(center: Vector2,radius: float,rec: Rectangle,) -> bool:
        """Check collision between circle and rectangle"""
        ...
def CheckCollisionCircles(center1: Vector2,radius1: float,center2: Vector2,radius2: float,) -> bool:
        """Check collision between two circles"""
        ...
def CheckCollisionLines(startPos1: Vector2,endPos1: Vector2,startPos2: Vector2,endPos2: Vector2,collisionPoint: Any,) -> bool:
        """Check the collision between two lines defined by two points each, returns collision point by reference"""
        ...
def CheckCollisionPointCircle(point: Vector2,center: Vector2,radius: float,) -> bool:
        """Check if point is inside circle"""
        ...
def CheckCollisionPointLine(point: Vector2,p1: Vector2,p2: Vector2,threshold: int,) -> bool:
        """Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]"""
        ...
def CheckCollisionPointRec(point: Vector2,rec: Rectangle,) -> bool:
        """Check if point is inside rectangle"""
        ...
def CheckCollisionPointTriangle(point: Vector2,p1: Vector2,p2: Vector2,p3: Vector2,) -> bool:
        """Check if point is inside a triangle"""
        ...
def CheckCollisionRecs(rec1: Rectangle,rec2: Rectangle,) -> bool:
        """Check collision between two rectangles"""
        ...
def CheckCollisionSpheres(center1: Vector3,radius1: float,center2: Vector3,radius2: float,) -> bool:
        """Check collision between two spheres"""
        ...
def ClearBackground(color: Color,) -> None:
        """Set background color (framebuffer clear color)"""
        ...
def ClearDirectoryFiles() -> None:
        """Clear directory files paths buffers (free memory)"""
        ...
def ClearDroppedFiles() -> None:
        """Clear dropped files paths buffer (free memory)"""
        ...
def ClearWindowState(flags: int,) -> None:
        """Clear window configuration state flags"""
        ...
def CloseAudioDevice() -> None:
        """Close the audio device and context"""
        ...
def ClosePhysics() -> None:
        """void ClosePhysics();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def CloseWindow() -> None:
        """Close window and unload OpenGL context"""
        ...
def CodepointToUTF8(codepoint: int,byteSize: Any,) -> str:
        """Encode one codepoint into UTF-8 byte array (array length returned as parameter)"""
        ...
def ColorAlpha(color: Color,alpha: float,) -> Color:
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        ...
def ColorAlphaBlend(dst: Color,src: Color,tint: Color,) -> Color:
        """Get src alpha-blended into dst color with tint"""
        ...
def ColorFromHSV(hue: float,saturation: float,value: float,) -> Color:
        """Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
        ...
def ColorFromNormalized(normalized: Vector4,) -> Color:
        """Get Color from normalized values [0..1]"""
        ...
def ColorNormalize(color: Color,) -> Vector4:
        """Get Color normalized as float [0..1]"""
        ...
def ColorToHSV(color: Color,) -> Vector3:
        """Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
        ...
def ColorToInt(color: Color,) -> int:
        """Get hexadecimal value for a Color"""
        ...
def CompressData(data: str,dataLength: int,compDataLength: Any,) -> str:
        """Compress data (DEFLATE algorithm)"""
        ...
def CreatePhysicsBodyCircle(Vector2_0: Vector2,float_1: float,float_2: float,) -> Any:
        """struct PhysicsBodyData *CreatePhysicsBodyCircle(struct Vector2, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def CreatePhysicsBodyPolygon(Vector2_0: Vector2,float_1: float,int_2: int,float_3: float,) -> Any:
        """struct PhysicsBodyData *CreatePhysicsBodyPolygon(struct Vector2, float, int, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def CreatePhysicsBodyRectangle(Vector2_0: Vector2,float_1: float,float_2: float,float_3: float,) -> Any:
        """struct PhysicsBodyData *CreatePhysicsBodyRectangle(struct Vector2, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
DEFAULT: int
DROPDOWNBOX: int
DROPDOWN_ITEMS_PADDING: int
def DecodeDataBase64(data: str,outputLength: Any,) -> str:
        """Decode Base64 string data"""
        ...
def DecompressData(compData: str,compDataLength: int,dataLength: Any,) -> str:
        """Decompress data (DEFLATE algorithm)"""
        ...
def DestroyPhysicsBody(PhysicsBodyData_pointer_0: Any,) -> None:
        """void DestroyPhysicsBody(struct PhysicsBodyData *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def DirectoryExists(dirPath: str,) -> bool:
        """Check if a directory path exists"""
        ...
def DisableCursor() -> None:
        """Disables cursor (lock cursor)"""
        ...
def DrawBillboard(camera: Camera3D,texture: Texture,position: Vector3,size: float,tint: Color,) -> None:
        """Draw a billboard texture"""
        ...
def DrawBillboardPro(camera: Camera3D,texture: Texture,source: Rectangle,position: Vector3,up: Vector3,size: Vector2,origin: Vector2,rotation: float,tint: Color,) -> None:
        """Draw a billboard texture defined by source and rotation"""
        ...
def DrawBillboardRec(camera: Camera3D,texture: Texture,source: Rectangle,position: Vector3,size: Vector2,tint: Color,) -> None:
        """Draw a billboard texture defined by source"""
        ...
def DrawBoundingBox(box: BoundingBox,color: Color,) -> None:
        """Draw bounding box (wires)"""
        ...
def DrawCircle(centerX: int,centerY: int,radius: float,color: Color,) -> None:
        """Draw a color-filled circle"""
        ...
def DrawCircle3D(center: Vector3,radius: float,rotationAxis: Vector3,rotationAngle: float,color: Color,) -> None:
        """Draw a circle in 3D world space"""
        ...
def DrawCircleGradient(centerX: int,centerY: int,radius: float,color1: Color,color2: Color,) -> None:
        """Draw a gradient-filled circle"""
        ...
def DrawCircleLines(centerX: int,centerY: int,radius: float,color: Color,) -> None:
        """Draw circle outline"""
        ...
def DrawCircleSector(center: Vector2,radius: float,startAngle: float,endAngle: float,segments: int,color: Color,) -> None:
        """Draw a piece of a circle"""
        ...
def DrawCircleSectorLines(center: Vector2,radius: float,startAngle: float,endAngle: float,segments: int,color: Color,) -> None:
        """Draw circle sector outline"""
        ...
def DrawCircleV(center: Vector2,radius: float,color: Color,) -> None:
        """Draw a color-filled circle (Vector version)"""
        ...
def DrawCube(position: Vector3,width: float,height: float,length: float,color: Color,) -> None:
        """Draw cube"""
        ...
def DrawCubeTexture(texture: Texture,position: Vector3,width: float,height: float,length: float,color: Color,) -> None:
        """Draw cube textured"""
        ...
def DrawCubeTextureRec(texture: Texture,source: Rectangle,position: Vector3,width: float,height: float,length: float,color: Color,) -> None:
        """Draw cube with a region of a texture"""
        ...
def DrawCubeV(position: Vector3,size: Vector3,color: Color,) -> None:
        """Draw cube (Vector version)"""
        ...
def DrawCubeWires(position: Vector3,width: float,height: float,length: float,color: Color,) -> None:
        """Draw cube wires"""
        ...
def DrawCubeWiresV(position: Vector3,size: Vector3,color: Color,) -> None:
        """Draw cube wires (Vector version)"""
        ...
def DrawCylinder(position: Vector3,radiusTop: float,radiusBottom: float,height: float,slices: int,color: Color,) -> None:
        """Draw a cylinder/cone"""
        ...
def DrawCylinderEx(startPos: Vector3,endPos: Vector3,startRadius: float,endRadius: float,sides: int,color: Color,) -> None:
        """Draw a cylinder with base at startPos and top at endPos"""
        ...
def DrawCylinderWires(position: Vector3,radiusTop: float,radiusBottom: float,height: float,slices: int,color: Color,) -> None:
        """Draw a cylinder/cone wires"""
        ...
def DrawCylinderWiresEx(startPos: Vector3,endPos: Vector3,startRadius: float,endRadius: float,sides: int,color: Color,) -> None:
        """Draw a cylinder wires with base at startPos and top at endPos"""
        ...
def DrawEllipse(centerX: int,centerY: int,radiusH: float,radiusV: float,color: Color,) -> None:
        """Draw ellipse"""
        ...
def DrawEllipseLines(centerX: int,centerY: int,radiusH: float,radiusV: float,color: Color,) -> None:
        """Draw ellipse outline"""
        ...
def DrawFPS(posX: int,posY: int,) -> None:
        """Draw current FPS"""
        ...
def DrawGrid(slices: int,spacing: float,) -> None:
        """Draw a grid (centered at (0, 0, 0))"""
        ...
def DrawLine(startPosX: int,startPosY: int,endPosX: int,endPosY: int,color: Color,) -> None:
        """Draw a line"""
        ...
def DrawLine3D(startPos: Vector3,endPos: Vector3,color: Color,) -> None:
        """Draw a line in 3D world space"""
        ...
def DrawLineBezier(startPos: Vector2,endPos: Vector2,thick: float,color: Color,) -> None:
        """Draw a line using cubic-bezier curves in-out"""
        ...
def DrawLineBezierCubic(startPos: Vector2,endPos: Vector2,startControlPos: Vector2,endControlPos: Vector2,thick: float,color: Color,) -> None:
        """Draw line using cubic bezier curves with 2 control points"""
        ...
def DrawLineBezierQuad(startPos: Vector2,endPos: Vector2,controlPos: Vector2,thick: float,color: Color,) -> None:
        """Draw line using quadratic bezier curves with a control point"""
        ...
def DrawLineEx(startPos: Vector2,endPos: Vector2,thick: float,color: Color,) -> None:
        """Draw a line defining thickness"""
        ...
def DrawLineStrip(points: Any,pointCount: int,color: Color,) -> None:
        """Draw lines sequence"""
        ...
def DrawLineV(startPos: Vector2,endPos: Vector2,color: Color,) -> None:
        """Draw a line (Vector version)"""
        ...
def DrawMesh(mesh: Mesh,material: Material,transform: Matrix,) -> None:
        """Draw a 3d mesh with material and transform"""
        ...
def DrawMeshInstanced(mesh: Mesh,material: Material,transforms: Any,instances: int,) -> None:
        """Draw multiple mesh instances with material and different transforms"""
        ...
def DrawModel(model: Model,position: Vector3,scale: float,tint: Color,) -> None:
        """Draw a model (with texture if set)"""
        ...
def DrawModelEx(model: Model,position: Vector3,rotationAxis: Vector3,rotationAngle: float,scale: Vector3,tint: Color,) -> None:
        """Draw a model with extended parameters"""
        ...
def DrawModelWires(model: Model,position: Vector3,scale: float,tint: Color,) -> None:
        """Draw a model wires (with texture if set)"""
        ...
def DrawModelWiresEx(model: Model,position: Vector3,rotationAxis: Vector3,rotationAngle: float,scale: Vector3,tint: Color,) -> None:
        """Draw a model wires (with texture if set) with extended parameters"""
        ...
def DrawPixel(posX: int,posY: int,color: Color,) -> None:
        """Draw a pixel"""
        ...
def DrawPixelV(position: Vector2,color: Color,) -> None:
        """Draw a pixel (Vector version)"""
        ...
def DrawPlane(centerPos: Vector3,size: Vector2,color: Color,) -> None:
        """Draw a plane XZ"""
        ...
def DrawPoint3D(position: Vector3,color: Color,) -> None:
        """Draw a point in 3D space, actually a small line"""
        ...
def DrawPoly(center: Vector2,sides: int,radius: float,rotation: float,color: Color,) -> None:
        """Draw a regular polygon (Vector version)"""
        ...
def DrawPolyLines(center: Vector2,sides: int,radius: float,rotation: float,color: Color,) -> None:
        """Draw a polygon outline of n sides"""
        ...
def DrawPolyLinesEx(center: Vector2,sides: int,radius: float,rotation: float,lineThick: float,color: Color,) -> None:
        """Draw a polygon outline of n sides with extended parameters"""
        ...
def DrawRay(ray: Ray,color: Color,) -> None:
        """Draw a ray line"""
        ...
def DrawRectangle(posX: int,posY: int,width: int,height: int,color: Color,) -> None:
        """Draw a color-filled rectangle"""
        ...
def DrawRectangleGradientEx(rec: Rectangle,col1: Color,col2: Color,col3: Color,col4: Color,) -> None:
        """Draw a gradient-filled rectangle with custom vertex colors"""
        ...
def DrawRectangleGradientH(posX: int,posY: int,width: int,height: int,color1: Color,color2: Color,) -> None:
        """Draw a horizontal-gradient-filled rectangle"""
        ...
def DrawRectangleGradientV(posX: int,posY: int,width: int,height: int,color1: Color,color2: Color,) -> None:
        """Draw a vertical-gradient-filled rectangle"""
        ...
def DrawRectangleLines(posX: int,posY: int,width: int,height: int,color: Color,) -> None:
        """Draw rectangle outline"""
        ...
def DrawRectangleLinesEx(rec: Rectangle,lineThick: float,color: Color,) -> None:
        """Draw rectangle outline with extended parameters"""
        ...
def DrawRectanglePro(rec: Rectangle,origin: Vector2,rotation: float,color: Color,) -> None:
        """Draw a color-filled rectangle with pro parameters"""
        ...
def DrawRectangleRec(rec: Rectangle,color: Color,) -> None:
        """Draw a color-filled rectangle"""
        ...
def DrawRectangleRounded(rec: Rectangle,roundness: float,segments: int,color: Color,) -> None:
        """Draw rectangle with rounded edges"""
        ...
def DrawRectangleRoundedLines(rec: Rectangle,roundness: float,segments: int,lineThick: float,color: Color,) -> None:
        """Draw rectangle with rounded edges outline"""
        ...
def DrawRectangleV(position: Vector2,size: Vector2,color: Color,) -> None:
        """Draw a color-filled rectangle (Vector version)"""
        ...
def DrawRing(center: Vector2,innerRadius: float,outerRadius: float,startAngle: float,endAngle: float,segments: int,color: Color,) -> None:
        """Draw ring"""
        ...
def DrawRingLines(center: Vector2,innerRadius: float,outerRadius: float,startAngle: float,endAngle: float,segments: int,color: Color,) -> None:
        """Draw ring outline"""
        ...
def DrawSphere(centerPos: Vector3,radius: float,color: Color,) -> None:
        """Draw sphere"""
        ...
def DrawSphereEx(centerPos: Vector3,radius: float,rings: int,slices: int,color: Color,) -> None:
        """Draw sphere with extended parameters"""
        ...
def DrawSphereWires(centerPos: Vector3,radius: float,rings: int,slices: int,color: Color,) -> None:
        """Draw sphere wires"""
        ...
def DrawText(text: str,posX: int,posY: int,fontSize: int,color: Color,) -> None:
        """Draw text (using default font)"""
        ...
def DrawTextCodepoint(font: Font,codepoint: int,position: Vector2,fontSize: float,tint: Color,) -> None:
        """Draw one character (codepoint)"""
        ...
def DrawTextEx(font: Font,text: str,position: Vector2,fontSize: float,spacing: float,tint: Color,) -> None:
        """Draw text using font and additional parameters"""
        ...
def DrawTextPro(font: Font,text: str,position: Vector2,origin: Vector2,rotation: float,fontSize: float,spacing: float,tint: Color,) -> None:
        """Draw text using Font and pro parameters (rotation)"""
        ...
def DrawTexture(texture: Texture,posX: int,posY: int,tint: Color,) -> None:
        """Draw a Texture2D"""
        ...
def DrawTextureEx(texture: Texture,position: Vector2,rotation: float,scale: float,tint: Color,) -> None:
        """Draw a Texture2D with extended parameters"""
        ...
def DrawTextureNPatch(texture: Texture,nPatchInfo: NPatchInfo,dest: Rectangle,origin: Vector2,rotation: float,tint: Color,) -> None:
        """Draws a texture (or part of it) that stretches or shrinks nicely"""
        ...
def DrawTexturePoly(texture: Texture,center: Vector2,points: Any,texcoords: Any,pointCount: int,tint: Color,) -> None:
        """Draw a textured polygon"""
        ...
def DrawTexturePro(texture: Texture,source: Rectangle,dest: Rectangle,origin: Vector2,rotation: float,tint: Color,) -> None:
        """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
        ...
def DrawTextureQuad(texture: Texture,tiling: Vector2,offset: Vector2,quad: Rectangle,tint: Color,) -> None:
        """Draw texture quad with tiling and offset parameters"""
        ...
def DrawTextureRec(texture: Texture,source: Rectangle,position: Vector2,tint: Color,) -> None:
        """Draw a part of a texture defined by a rectangle"""
        ...
def DrawTextureTiled(texture: Texture,source: Rectangle,dest: Rectangle,origin: Vector2,rotation: float,scale: float,tint: Color,) -> None:
        """Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest."""
        ...
def DrawTextureV(texture: Texture,position: Vector2,tint: Color,) -> None:
        """Draw a Texture2D with position defined as Vector2"""
        ...
def DrawTriangle(v1: Vector2,v2: Vector2,v3: Vector2,color: Color,) -> None:
        """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
        ...
def DrawTriangle3D(v1: Vector3,v2: Vector3,v3: Vector3,color: Color,) -> None:
        """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
        ...
def DrawTriangleFan(points: Any,pointCount: int,color: Color,) -> None:
        """Draw a triangle fan defined by points (first vertex is the center)"""
        ...
def DrawTriangleLines(v1: Vector2,v2: Vector2,v3: Vector2,color: Color,) -> None:
        """Draw triangle outline (vertex in counter-clockwise order!)"""
        ...
def DrawTriangleStrip(points: Any,pointCount: int,color: Color,) -> None:
        """Draw a triangle strip defined by points"""
        ...
def DrawTriangleStrip3D(points: Any,pointCount: int,color: Color,) -> None:
        """Draw a triangle strip defined by points"""
        ...
def EnableCursor() -> None:
        """Enables cursor (unlock cursor)"""
        ...
def EncodeDataBase64(data: str,dataLength: int,outputLength: Any,) -> str:
        """Encode data to Base64 string"""
        ...
def EndBlendMode() -> None:
        """End blending mode (reset to default: alpha blending)"""
        ...
def EndDrawing() -> None:
        """End canvas drawing and swap buffers (double buffering)"""
        ...
def EndMode2D() -> None:
        """Ends 2D mode with custom camera"""
        ...
def EndMode3D() -> None:
        """Ends 3D mode and returns to default 2D orthographic mode"""
        ...
def EndScissorMode() -> None:
        """End scissor mode"""
        ...
def EndShaderMode() -> None:
        """End custom shader drawing (use default shader)"""
        ...
def EndTextureMode() -> None:
        """Ends drawing to render texture"""
        ...
def EndVrStereoMode() -> None:
        """End stereo rendering (requires VR simulator)"""
        ...
def ExportImage(image: Image,fileName: str,) -> bool:
        """Export image data to file, returns true on success"""
        ...
def ExportImageAsCode(image: Image,fileName: str,) -> bool:
        """Export image as code file defining an array of bytes, returns true on success"""
        ...
def ExportMesh(mesh: Mesh,fileName: str,) -> bool:
        """Export mesh data to file, returns true on success"""
        ...
def ExportWave(wave: Wave,fileName: str,) -> bool:
        """Export wave data to file, returns true on success"""
        ...
def ExportWaveAsCode(wave: Wave,fileName: str,) -> bool:
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
def Fade(color: Color,alpha: float,) -> Color:
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        ...
def FileExists(fileName: str,) -> bool:
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
def GenImageCellular(width: int,height: int,tileSize: int,) -> Image:
        """Generate image: cellular algorithm, bigger tileSize means bigger cells"""
        ...
def GenImageChecked(width: int,height: int,checksX: int,checksY: int,col1: Color,col2: Color,) -> Image:
        """Generate image: checked"""
        ...
def GenImageColor(width: int,height: int,color: Color,) -> Image:
        """Generate image: plain color"""
        ...
def GenImageFontAtlas(chars: Any,recs: Any,glyphCount: int,fontSize: int,padding: int,packMethod: int,) -> Image:
        """Generate image font atlas using chars info"""
        ...
def GenImageGradientH(width: int,height: int,left: Color,right: Color,) -> Image:
        """Generate image: horizontal gradient"""
        ...
def GenImageGradientRadial(width: int,height: int,density: float,inner: Color,outer: Color,) -> Image:
        """Generate image: radial gradient"""
        ...
def GenImageGradientV(width: int,height: int,top: Color,bottom: Color,) -> Image:
        """Generate image: vertical gradient"""
        ...
def GenImageWhiteNoise(width: int,height: int,factor: float,) -> Image:
        """Generate image: white noise"""
        ...
def GenMeshBinormals(mesh: Any,) -> None:
        """Compute mesh binormals"""
        ...
def GenMeshCone(radius: float,height: float,slices: int,) -> Mesh:
        """Generate cone/pyramid mesh"""
        ...
def GenMeshCube(width: float,height: float,length: float,) -> Mesh:
        """Generate cuboid mesh"""
        ...
def GenMeshCubicmap(cubicmap: Image,cubeSize: Vector3,) -> Mesh:
        """Generate cubes-based map mesh from image data"""
        ...
def GenMeshCylinder(radius: float,height: float,slices: int,) -> Mesh:
        """Generate cylinder mesh"""
        ...
def GenMeshHeightmap(heightmap: Image,size: Vector3,) -> Mesh:
        """Generate heightmap mesh from image data"""
        ...
def GenMeshHemiSphere(radius: float,rings: int,slices: int,) -> Mesh:
        """Generate half-sphere mesh (no bottom cap)"""
        ...
def GenMeshKnot(radius: float,size: float,radSeg: int,sides: int,) -> Mesh:
        """Generate trefoil knot mesh"""
        ...
def GenMeshPlane(width: float,length: float,resX: int,resZ: int,) -> Mesh:
        """Generate plane mesh (with subdivisions)"""
        ...
def GenMeshPoly(sides: int,radius: float,) -> Mesh:
        """Generate polygonal mesh"""
        ...
def GenMeshSphere(radius: float,rings: int,slices: int,) -> Mesh:
        """Generate sphere mesh (standard sphere)"""
        ...
def GenMeshTangents(mesh: Any,) -> None:
        """Compute mesh tangents"""
        ...
def GenMeshTorus(radius: float,size: float,radSeg: int,sides: int,) -> Mesh:
        """Generate torus mesh"""
        ...
def GenTextureMipmaps(texture: Any,) -> None:
        """Generate GPU mipmaps for a texture"""
        ...
def GetCameraMatrix(camera: Camera3D,) -> Matrix:
        """Get camera transform matrix (view matrix)"""
        ...
def GetCameraMatrix2D(camera: Camera2D,) -> Matrix:
        """Get camera 2d transform matrix"""
        ...
def GetCharPressed() -> int:
        """Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty"""
        ...
def GetClipboardText() -> str:
        """Get clipboard text content"""
        ...
def GetCodepoint(text: str,bytesProcessed: Any,) -> int:
        """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
        ...
def GetCodepointCount(text: str,) -> int:
        """Get total number of codepoints in a UTF-8 encoded string"""
        ...
def GetCollisionRec(rec1: Rectangle,rec2: Rectangle,) -> Rectangle:
        """Get collision rectangle for two rectangles collision"""
        ...
def GetColor(hexValue: int,) -> Color:
        """Get Color structure from hexadecimal value"""
        ...
def GetCurrentMonitor() -> int:
        """Get current connected monitor"""
        ...
def GetDirectoryFiles(dirPath: str,count: Any,) -> str:
        """Get filenames in a directory path (memory should be freed)"""
        ...
def GetDirectoryPath(filePath: str,) -> str:
        """Get full path for a given fileName with path (uses static string)"""
        ...
def GetDroppedFiles(count: Any,) -> str:
        """Get dropped files names (memory should be freed)"""
        ...
def GetFPS() -> int:
        """Get current FPS"""
        ...
def GetFileExtension(fileName: str,) -> str:
        """Get pointer to extension for a filename string (includes dot: '.png')"""
        ...
def GetFileModTime(fileName: str,) -> int:
        """Get file modification time (last write time)"""
        ...
def GetFileName(filePath: str,) -> str:
        """Get pointer to filename for a path string"""
        ...
def GetFileNameWithoutExt(filePath: str,) -> str:
        """Get filename string without extension (uses static string)"""
        ...
def GetFontDefault() -> Font:
        """Get the default Font"""
        ...
def GetFrameTime() -> float:
        """Get time in seconds for last frame drawn (delta time)"""
        ...
def GetGamepadAxisCount(gamepad: int,) -> int:
        """Get gamepad axis count for a gamepad"""
        ...
def GetGamepadAxisMovement(gamepad: int,axis: int,) -> float:
        """Get axis movement value for a gamepad axis"""
        ...
def GetGamepadButtonPressed() -> int:
        """Get the last gamepad button pressed"""
        ...
def GetGamepadName(gamepad: int,) -> str:
        """Get gamepad internal name id"""
        ...
def GetGestureDetected() -> int:
        """Get latest detected gesture"""
        ...
def GetGestureDragAngle() -> float:
        """Get gesture drag angle"""
        ...
def GetGestureDragVector() -> Vector2:
        """Get gesture drag vector"""
        ...
def GetGestureHoldDuration() -> float:
        """Get gesture hold time in milliseconds"""
        ...
def GetGesturePinchAngle() -> float:
        """Get gesture pinch angle"""
        ...
def GetGesturePinchVector() -> Vector2:
        """Get gesture pinch delta"""
        ...
def GetGlyphAtlasRec(font: Font,codepoint: int,) -> Rectangle:
        """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
        ...
def GetGlyphIndex(font: Font,codepoint: int,) -> int:
        """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
        ...
def GetGlyphInfo(font: Font,codepoint: int,) -> GlyphInfo:
        """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
        ...
def GetImageAlphaBorder(image: Image,threshold: float,) -> Rectangle:
        """Get image alpha border rectangle"""
        ...
def GetImageColor(image: Image,x: int,y: int,) -> Color:
        """Get image pixel color at (x, y) position"""
        ...
def GetKeyPressed() -> int:
        """Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty"""
        ...
def GetMeshBoundingBox(mesh: Mesh,) -> BoundingBox:
        """Compute mesh bounding box limits"""
        ...
def GetModelBoundingBox(model: Model,) -> BoundingBox:
        """Compute model bounding box limits (considers all meshes)"""
        ...
def GetMonitorCount() -> int:
        """Get number of connected monitors"""
        ...
def GetMonitorHeight(monitor: int,) -> int:
        """Get specified monitor height (max available by monitor)"""
        ...
def GetMonitorName(monitor: int,) -> str:
        """Get the human-readable, UTF-8 encoded name of the primary monitor"""
        ...
def GetMonitorPhysicalHeight(monitor: int,) -> int:
        """Get specified monitor physical height in millimetres"""
        ...
def GetMonitorPhysicalWidth(monitor: int,) -> int:
        """Get specified monitor physical width in millimetres"""
        ...
def GetMonitorPosition(monitor: int,) -> Vector2:
        """Get specified monitor position"""
        ...
def GetMonitorRefreshRate(monitor: int,) -> int:
        """Get specified monitor refresh rate"""
        ...
def GetMonitorWidth(monitor: int,) -> int:
        """Get specified monitor width (max available by monitor)"""
        ...
def GetMouseDelta() -> Vector2:
        """Get mouse delta between frames"""
        ...
def GetMousePosition() -> Vector2:
        """Get mouse position XY"""
        ...
def GetMouseRay(mousePosition: Vector2,camera: Camera3D,) -> Ray:
        """Get a ray trace from mouse position"""
        ...
def GetMouseWheelMove() -> float:
        """Get mouse wheel movement Y"""
        ...
def GetMouseX() -> int:
        """Get mouse position X"""
        ...
def GetMouseY() -> int:
        """Get mouse position Y"""
        ...
def GetMusicTimeLength(music: Music,) -> float:
        """Get music time length (in seconds)"""
        ...
def GetMusicTimePlayed(music: Music,) -> float:
        """Get current music time played (in seconds)"""
        ...
def GetPhysicsBodiesCount() -> int:
        """int GetPhysicsBodiesCount();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GetPhysicsBody(int_0: int,) -> Any:
        """struct PhysicsBodyData *GetPhysicsBody(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GetPhysicsShapeType(int_0: int,) -> int:
        """int GetPhysicsShapeType(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GetPhysicsShapeVertex(PhysicsBodyData_pointer_0: Any,int_1: int,) -> Vector2:
        """struct Vector2 GetPhysicsShapeVertex(struct PhysicsBodyData *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GetPhysicsShapeVerticesCount(int_0: int,) -> int:
        """int GetPhysicsShapeVerticesCount(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GetPixelColor(srcPtr: Any,format: int,) -> Color:
        """Get Color from a source pixel pointer of certain format"""
        ...
def GetPixelDataSize(width: int,height: int,format: int,) -> int:
        """Get pixel data size in bytes for certain format"""
        ...
def GetPrevDirectoryPath(dirPath: str,) -> str:
        """Get previous directory path for a given path (uses static string)"""
        ...
def GetRandomValue(min: int,max: int,) -> int:
        """Get a random value between min and max (both included)"""
        ...
def GetRayCollisionBox(ray: Ray,box: BoundingBox,) -> RayCollision:
        """Get collision info between ray and box"""
        ...
def GetRayCollisionMesh(ray: Ray,mesh: Mesh,transform: Matrix,) -> RayCollision:
        """Get collision info between ray and mesh"""
        ...
def GetRayCollisionModel(ray: Ray,model: Model,) -> RayCollision:
        """Get collision info between ray and model"""
        ...
def GetRayCollisionQuad(ray: Ray,p1: Vector3,p2: Vector3,p3: Vector3,p4: Vector3,) -> RayCollision:
        """Get collision info between ray and quad"""
        ...
def GetRayCollisionSphere(ray: Ray,center: Vector3,radius: float,) -> RayCollision:
        """Get collision info between ray and sphere"""
        ...
def GetRayCollisionTriangle(ray: Ray,p1: Vector3,p2: Vector3,p3: Vector3,) -> RayCollision:
        """Get collision info between ray and triangle"""
        ...
def GetScreenHeight() -> int:
        """Get current screen height"""
        ...
def GetScreenToWorld2D(position: Vector2,camera: Camera2D,) -> Vector2:
        """Get the world space position for a 2d camera screen space position"""
        ...
def GetScreenWidth() -> int:
        """Get current screen width"""
        ...
def GetShaderLocation(shader: Shader,uniformName: str,) -> int:
        """Get shader uniform location"""
        ...
def GetShaderLocationAttrib(shader: Shader,attribName: str,) -> int:
        """Get shader attribute location"""
        ...
def GetSoundsPlaying() -> int:
        """Get number of sounds playing in the multichannel"""
        ...
def GetTime() -> float:
        """Get elapsed time in seconds since InitWindow()"""
        ...
def GetTouchPointCount() -> int:
        """Get number of touch points"""
        ...
def GetTouchPointId(index: int,) -> int:
        """Get touch point identifier for given index"""
        ...
def GetTouchPosition(index: int,) -> Vector2:
        """Get touch position XY for a touch point index (relative to screen size)"""
        ...
def GetTouchX() -> int:
        """Get touch position X for touch point 0 (relative to screen size)"""
        ...
def GetTouchY() -> int:
        """Get touch position Y for touch point 0 (relative to screen size)"""
        ...
def GetWindowHandle() -> Any:
        """Get native window handle"""
        ...
def GetWindowPosition() -> Vector2:
        """Get window position XY on monitor"""
        ...
def GetWindowScaleDPI() -> Vector2:
        """Get window scale DPI factor"""
        ...
def GetWorkingDirectory() -> str:
        """Get current working directory (uses static string)"""
        ...
def GetWorldToScreen(position: Vector3,camera: Camera3D,) -> Vector2:
        """Get the screen space position for a 3d world space position"""
        ...
def GetWorldToScreen2D(position: Vector2,camera: Camera2D,) -> Vector2:
        """Get the screen space position for a 2d camera world space position"""
        ...
def GetWorldToScreenEx(position: Vector3,camera: Camera3D,width: int,height: int,) -> Vector2:
        """Get size position for a 3d world space position"""
        ...
def GuiButton(Rectangle_0: Rectangle,str_1: str,) -> bool:
        """_Bool GuiButton(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiCheckBox(Rectangle_0: Rectangle,str_1: str,_Bool_2: bool,) -> bool:
        """_Bool GuiCheckBox(struct Rectangle, char *, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiColorBarAlpha(Rectangle_0: Rectangle,float_1: float,) -> float:
        """float GuiColorBarAlpha(struct Rectangle, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiColorBarHue(Rectangle_0: Rectangle,float_1: float,) -> float:
        """float GuiColorBarHue(struct Rectangle, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiColorPanel(Rectangle_0: Rectangle,Color_1: Color,) -> Color:
        """struct Color GuiColorPanel(struct Rectangle, struct Color);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiColorPicker(Rectangle_0: Rectangle,Color_1: Color,) -> Color:
        """struct Color GuiColorPicker(struct Rectangle, struct Color);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiComboBox(Rectangle_0: Rectangle,str_1: str,int_2: int,) -> int:
        """int GuiComboBox(struct Rectangle, char *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiDisable() -> None:
        """void GuiDisable();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiDropdownBox(Rectangle_0: Rectangle,str_1: str,int_pointer_2: Any,_Bool_3: bool,) -> bool:
        """_Bool GuiDropdownBox(struct Rectangle, char *, int *, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiDummyRec(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiDummyRec(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiEnable() -> None:
        """void GuiEnable();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiFade(float_0: float,) -> None:
        """void GuiFade(float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiGetFont() -> Font:
        """struct Font GuiGetFont();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiGetState() -> int:
        """int GuiGetState();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiGetStyle(int_0: int,int_1: int,) -> int:
        """int GuiGetStyle(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiGrid(Rectangle_0: Rectangle,float_1: float,int_2: int,) -> Vector2:
        """struct Vector2 GuiGrid(struct Rectangle, float, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiGroupBox(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiGroupBox(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiIconText(int_0: int,str_1: str,) -> str:
        """char *GuiIconText(int, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiImageButton(Rectangle_0: Rectangle,str_1: str,Texture_2: Texture,) -> bool:
        """_Bool GuiImageButton(struct Rectangle, char *, struct Texture);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiImageButtonEx(Rectangle_0: Rectangle,str_1: str,Texture_2: Texture,Rectangle_3: Rectangle,) -> bool:
        """_Bool GuiImageButtonEx(struct Rectangle, char *, struct Texture, struct Rectangle);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiLabel(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiLabel(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiLabelButton(Rectangle_0: Rectangle,str_1: str,) -> bool:
        """_Bool GuiLabelButton(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiLine(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiLine(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiListView(Rectangle_0: Rectangle,str_1: str,int_pointer_2: Any,int_3: int,) -> int:
        """int GuiListView(struct Rectangle, char *, int *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiListViewEx(Rectangle_0: Rectangle,str_pointer_1: str,int_2: int,int_pointer_3: Any,int_pointer_4: Any,int_5: int,) -> int:
        """int GuiListViewEx(struct Rectangle, char * *, int, int *, int *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiLoadStyle(str_0: str,) -> None:
        """void GuiLoadStyle(char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiLoadStyleDefault() -> None:
        """void GuiLoadStyleDefault();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiLock() -> None:
        """void GuiLock();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiMessageBox(Rectangle_0: Rectangle,str_1: str,str_2: str,str_3: str,) -> int:
        """int GuiMessageBox(struct Rectangle, char *, char *, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiPanel(Rectangle_0: Rectangle,) -> None:
        """void GuiPanel(struct Rectangle);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiProgressBar(Rectangle_0: Rectangle,str_1: str,str_2: str,float_3: float,float_4: float,float_5: float,) -> float:
        """float GuiProgressBar(struct Rectangle, char *, char *, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiScrollBar(Rectangle_0: Rectangle,int_1: int,int_2: int,int_3: int,) -> int:
        """int GuiScrollBar(struct Rectangle, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiScrollPanel(Rectangle_0: Rectangle,Rectangle_1: Rectangle,Vector2_pointer_2: Any,) -> Rectangle:
        """struct Rectangle GuiScrollPanel(struct Rectangle, struct Rectangle, struct Vector2 *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiSetFont(Font_0: Font,) -> None:
        """void GuiSetFont(struct Font);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiSetState(int_0: int,) -> None:
        """void GuiSetState(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiSetStyle(int_0: int,int_1: int,int_2: int,) -> None:
        """void GuiSetStyle(int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiSlider(Rectangle_0: Rectangle,str_1: str,str_2: str,float_3: float,float_4: float,float_5: float,) -> float:
        """float GuiSlider(struct Rectangle, char *, char *, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiSliderBar(Rectangle_0: Rectangle,str_1: str,str_2: str,float_3: float,float_4: float,float_5: float,) -> float:
        """float GuiSliderBar(struct Rectangle, char *, char *, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiSpinner(Rectangle_0: Rectangle,str_1: str,int_pointer_2: Any,int_3: int,int_4: int,_Bool_5: bool,) -> bool:
        """_Bool GuiSpinner(struct Rectangle, char *, int *, int, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiStatusBar(Rectangle_0: Rectangle,str_1: str,) -> None:
        """void GuiStatusBar(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiTextBox(Rectangle_0: Rectangle,str_1: str,int_2: int,_Bool_3: bool,) -> bool:
        """_Bool GuiTextBox(struct Rectangle, char *, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiTextBoxMulti(Rectangle_0: Rectangle,str_1: str,int_2: int,_Bool_3: bool,) -> bool:
        """_Bool GuiTextBoxMulti(struct Rectangle, char *, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiTextInputBox(Rectangle_0: Rectangle,str_1: str,str_2: str,str_3: str,str_4: str,) -> int:
        """int GuiTextInputBox(struct Rectangle, char *, char *, char *, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiToggle(Rectangle_0: Rectangle,str_1: str,_Bool_2: bool,) -> bool:
        """_Bool GuiToggle(struct Rectangle, char *, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiToggleGroup(Rectangle_0: Rectangle,str_1: str,int_2: int,) -> int:
        """int GuiToggleGroup(struct Rectangle, char *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiUnlock() -> None:
        """void GuiUnlock();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiValueBox(Rectangle_0: Rectangle,str_1: str,int_pointer_2: Any,int_3: int,int_4: int,_Bool_5: bool,) -> bool:
        """_Bool GuiValueBox(struct Rectangle, char *, int *, int, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def GuiWindowBox(Rectangle_0: Rectangle,str_1: str,) -> bool:
        """_Bool GuiWindowBox(struct Rectangle, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
HUEBAR_PADDING: int
HUEBAR_SELECTOR_HEIGHT: int
HUEBAR_SELECTOR_OVERFLOW: int
HUEBAR_WIDTH: int
def HideCursor() -> None:
        """Hides cursor"""
        ...
def ImageAlphaClear(image: Any,color: Color,threshold: float,) -> None:
        """Clear alpha channel to desired color"""
        ...
def ImageAlphaCrop(image: Any,threshold: float,) -> None:
        """Crop image depending on alpha value"""
        ...
def ImageAlphaMask(image: Any,alphaMask: Image,) -> None:
        """Apply alpha mask to image"""
        ...
def ImageAlphaPremultiply(image: Any,) -> None:
        """Premultiply alpha channel"""
        ...
def ImageClearBackground(dst: Any,color: Color,) -> None:
        """Clear image background with given color"""
        ...
def ImageColorBrightness(image: Any,brightness: int,) -> None:
        """Modify image color: brightness (-255 to 255)"""
        ...
def ImageColorContrast(image: Any,contrast: float,) -> None:
        """Modify image color: contrast (-100 to 100)"""
        ...
def ImageColorGrayscale(image: Any,) -> None:
        """Modify image color: grayscale"""
        ...
def ImageColorInvert(image: Any,) -> None:
        """Modify image color: invert"""
        ...
def ImageColorReplace(image: Any,color: Color,replace: Color,) -> None:
        """Modify image color: replace color"""
        ...
def ImageColorTint(image: Any,color: Color,) -> None:
        """Modify image color: tint"""
        ...
def ImageCopy(image: Image,) -> Image:
        """Create an image duplicate (useful for transformations)"""
        ...
def ImageCrop(image: Any,crop: Rectangle,) -> None:
        """Crop an image to a defined rectangle"""
        ...
def ImageDither(image: Any,rBpp: int,gBpp: int,bBpp: int,aBpp: int,) -> None:
        """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
        ...
def ImageDraw(dst: Any,src: Image,srcRec: Rectangle,dstRec: Rectangle,tint: Color,) -> None:
        """Draw a source image within a destination image (tint applied to source)"""
        ...
def ImageDrawCircle(dst: Any,centerX: int,centerY: int,radius: int,color: Color,) -> None:
        """Draw circle within an image"""
        ...
def ImageDrawCircleV(dst: Any,center: Vector2,radius: int,color: Color,) -> None:
        """Draw circle within an image (Vector version)"""
        ...
def ImageDrawLine(dst: Any,startPosX: int,startPosY: int,endPosX: int,endPosY: int,color: Color,) -> None:
        """Draw line within an image"""
        ...
def ImageDrawLineV(dst: Any,start: Vector2,end: Vector2,color: Color,) -> None:
        """Draw line within an image (Vector version)"""
        ...
def ImageDrawPixel(dst: Any,posX: int,posY: int,color: Color,) -> None:
        """Draw pixel within an image"""
        ...
def ImageDrawPixelV(dst: Any,position: Vector2,color: Color,) -> None:
        """Draw pixel within an image (Vector version)"""
        ...
def ImageDrawRectangle(dst: Any,posX: int,posY: int,width: int,height: int,color: Color,) -> None:
        """Draw rectangle within an image"""
        ...
def ImageDrawRectangleLines(dst: Any,rec: Rectangle,thick: int,color: Color,) -> None:
        """Draw rectangle lines within an image"""
        ...
def ImageDrawRectangleRec(dst: Any,rec: Rectangle,color: Color,) -> None:
        """Draw rectangle within an image"""
        ...
def ImageDrawRectangleV(dst: Any,position: Vector2,size: Vector2,color: Color,) -> None:
        """Draw rectangle within an image (Vector version)"""
        ...
def ImageDrawText(dst: Any,text: str,posX: int,posY: int,fontSize: int,color: Color,) -> None:
        """Draw text (using default font) within an image (destination)"""
        ...
def ImageDrawTextEx(dst: Any,font: Font,text: str,position: Vector2,fontSize: float,spacing: float,tint: Color,) -> None:
        """Draw text (custom sprite font) within an image (destination)"""
        ...
def ImageFlipHorizontal(image: Any,) -> None:
        """Flip image horizontally"""
        ...
def ImageFlipVertical(image: Any,) -> None:
        """Flip image vertically"""
        ...
def ImageFormat(image: Any,newFormat: int,) -> None:
        """Convert image data to desired format"""
        ...
def ImageFromImage(image: Image,rec: Rectangle,) -> Image:
        """Create an image from another image piece"""
        ...
def ImageMipmaps(image: Any,) -> None:
        """Compute all mipmap levels for a provided image"""
        ...
def ImageResize(image: Any,newWidth: int,newHeight: int,) -> None:
        """Resize image (Bicubic scaling algorithm)"""
        ...
def ImageResizeCanvas(image: Any,newWidth: int,newHeight: int,offsetX: int,offsetY: int,fill: Color,) -> None:
        """Resize canvas and fill with color"""
        ...
def ImageResizeNN(image: Any,newWidth: int,newHeight: int,) -> None:
        """Resize image (Nearest-Neighbor scaling algorithm)"""
        ...
def ImageRotateCCW(image: Any,) -> None:
        """Rotate image counter-clockwise 90deg"""
        ...
def ImageRotateCW(image: Any,) -> None:
        """Rotate image clockwise 90deg"""
        ...
def ImageText(text: str,fontSize: int,color: Color,) -> Image:
        """Create an image from text (default font)"""
        ...
def ImageTextEx(font: Font,text: str,fontSize: float,spacing: float,tint: Color,) -> Image:
        """Create an image from text (custom sprite font)"""
        ...
def ImageToPOT(image: Any,fill: Color,) -> None:
        """Convert image to POT (power-of-two)"""
        ...
def InitAudioDevice() -> None:
        """Initialize audio device and context"""
        ...
def InitPhysics() -> None:
        """void InitPhysics();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def InitWindow(width: int,height: int,title: str,) -> None:
        """Initialize window and OpenGL context"""
        ...
def IsAudioDeviceReady() -> bool:
        """Check if audio device has been initialized successfully"""
        ...
def IsAudioStreamPlaying(stream: AudioStream,) -> bool:
        """Check if audio stream is playing"""
        ...
def IsAudioStreamProcessed(stream: AudioStream,) -> bool:
        """Check if any audio stream buffers requires refill"""
        ...
def IsCursorHidden() -> bool:
        """Check if cursor is not visible"""
        ...
def IsCursorOnScreen() -> bool:
        """Check if cursor is on the screen"""
        ...
def IsFileDropped() -> bool:
        """Check if a file has been dropped into window"""
        ...
def IsFileExtension(fileName: str,ext: str,) -> bool:
        """Check file extension (including point: .png, .wav)"""
        ...
def IsGamepadAvailable(gamepad: int,) -> bool:
        """Check if a gamepad is available"""
        ...
def IsGamepadButtonDown(gamepad: int,button: int,) -> bool:
        """Check if a gamepad button is being pressed"""
        ...
def IsGamepadButtonPressed(gamepad: int,button: int,) -> bool:
        """Check if a gamepad button has been pressed once"""
        ...
def IsGamepadButtonReleased(gamepad: int,button: int,) -> bool:
        """Check if a gamepad button has been released once"""
        ...
def IsGamepadButtonUp(gamepad: int,button: int,) -> bool:
        """Check if a gamepad button is NOT being pressed"""
        ...
def IsGestureDetected(gesture: int,) -> bool:
        """Check if a gesture have been detected"""
        ...
def IsKeyDown(key: int,) -> bool:
        """Check if a key is being pressed"""
        ...
def IsKeyPressed(key: int,) -> bool:
        """Check if a key has been pressed once"""
        ...
def IsKeyReleased(key: int,) -> bool:
        """Check if a key has been released once"""
        ...
def IsKeyUp(key: int,) -> bool:
        """Check if a key is NOT being pressed"""
        ...
def IsModelAnimationValid(model: Model,anim: ModelAnimation,) -> bool:
        """Check model animation skeleton match"""
        ...
def IsMouseButtonDown(button: int,) -> bool:
        """Check if a mouse button is being pressed"""
        ...
def IsMouseButtonPressed(button: int,) -> bool:
        """Check if a mouse button has been pressed once"""
        ...
def IsMouseButtonReleased(button: int,) -> bool:
        """Check if a mouse button has been released once"""
        ...
def IsMouseButtonUp(button: int,) -> bool:
        """Check if a mouse button is NOT being pressed"""
        ...
def IsMusicStreamPlaying(music: Music,) -> bool:
        """Check if music is playing"""
        ...
def IsSoundPlaying(sound: Sound,) -> bool:
        """Check if a sound is currently playing"""
        ...
def IsWindowFocused() -> bool:
        """Check if window is currently focused (only PLATFORM_DESKTOP)"""
        ...
def IsWindowFullscreen() -> bool:
        """Check if window is currently fullscreen"""
        ...
def IsWindowHidden() -> bool:
        """Check if window is currently hidden (only PLATFORM_DESKTOP)"""
        ...
def IsWindowMaximized() -> bool:
        """Check if window is currently maximized (only PLATFORM_DESKTOP)"""
        ...
def IsWindowMinimized() -> bool:
        """Check if window is currently minimized (only PLATFORM_DESKTOP)"""
        ...
def IsWindowReady() -> bool:
        """Check if window has been initialized successfully"""
        ...
def IsWindowResized() -> bool:
        """Check if window has been resized last frame"""
        ...
def IsWindowState(flag: int,) -> bool:
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
def LoadAudioStream(sampleRate: int,sampleSize: int,channels: int,) -> AudioStream:
        """Load audio stream (to stream raw audio pcm data)"""
        ...
def LoadCodepoints(text: str,count: Any,) -> Any:
        """Load all codepoints from a UTF-8 text string, codepoints count returned by parameter"""
        ...
def LoadFileData(fileName: str,bytesRead: Any,) -> str:
        """Load file data as byte array (read)"""
        ...
def LoadFileText(fileName: str,) -> str:
        """Load text data from file (read), returns a ' 0' terminated string"""
        ...
def LoadFont(fileName: str,) -> Font:
        """Load font from file into GPU memory (VRAM)"""
        ...
def LoadFontData(fileData: str,dataSize: int,fontSize: int,fontChars: Any,glyphCount: int,type: int,) -> Any:
        """Load font data for further use"""
        ...
def LoadFontEx(fileName: str,fontSize: int,fontChars: Any,glyphCount: int,) -> Font:
        """Load font from file with extended parameters"""
        ...
def LoadFontFromImage(image: Image,key: Color,firstChar: int,) -> Font:
        """Load font from Image (XNA style)"""
        ...
def LoadFontFromMemory(fileType: str,fileData: str,dataSize: int,fontSize: int,fontChars: Any,glyphCount: int,) -> Font:
        """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
        ...
def LoadImage(fileName: str,) -> Image:
        """Load image from file into CPU memory (RAM)"""
        ...
def LoadImageAnim(fileName: str,frames: Any,) -> Image:
        """Load image sequence from file (frames appended to image.data)"""
        ...
def LoadImageColors(image: Image,) -> Any:
        """Load color data from image as a Color array (RGBA - 32bit)"""
        ...
def LoadImageFromMemory(fileType: str,fileData: str,dataSize: int,) -> Image:
        """Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
        ...
def LoadImageFromScreen() -> Image:
        """Load image from screen buffer and (screenshot)"""
        ...
def LoadImageFromTexture(texture: Texture,) -> Image:
        """Load image from GPU texture data"""
        ...
def LoadImagePalette(image: Image,maxPaletteSize: int,colorCount: Any,) -> Any:
        """Load colors palette from image as a Color array (RGBA - 32bit)"""
        ...
def LoadImageRaw(fileName: str,width: int,height: int,format: int,headerSize: int,) -> Image:
        """Load image from RAW file data"""
        ...
def LoadMaterialDefault() -> Material:
        """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
        ...
def LoadMaterials(fileName: str,materialCount: Any,) -> Any:
        """Load materials from model file"""
        ...
def LoadModel(fileName: str,) -> Model:
        """Load model from files (meshes and materials)"""
        ...
def LoadModelAnimations(fileName: str,animCount: Any,) -> Any:
        """Load model animations from file"""
        ...
def LoadModelFromMesh(mesh: Mesh,) -> Model:
        """Load model from generated mesh (default material)"""
        ...
def LoadMusicStream(fileName: str,) -> Music:
        """Load music stream from file"""
        ...
def LoadMusicStreamFromMemory(fileType: str,data: str,dataSize: int,) -> Music:
        """Load music stream from data"""
        ...
def LoadRenderTexture(width: int,height: int,) -> RenderTexture:
        """Load texture for rendering (framebuffer)"""
        ...
def LoadShader(vsFileName: str,fsFileName: str,) -> Shader:
        """Load shader from files and bind default locations"""
        ...
def LoadShaderFromMemory(vsCode: str,fsCode: str,) -> Shader:
        """Load shader from code strings and bind default locations"""
        ...
def LoadSound(fileName: str,) -> Sound:
        """Load sound from file"""
        ...
def LoadSoundFromWave(wave: Wave,) -> Sound:
        """Load sound from wave data"""
        ...
def LoadStorageValue(position: int,) -> int:
        """Load integer value from storage file (from defined position)"""
        ...
def LoadTexture(fileName: str,) -> Texture:
        """Load texture from file into GPU memory (VRAM)"""
        ...
def LoadTextureCubemap(image: Image,layout: int,) -> Texture:
        """Load cubemap from image, multiple image cubemap layouts supported"""
        ...
def LoadTextureFromImage(image: Image,) -> Texture:
        """Load texture from image data"""
        ...
def LoadVrStereoConfig(device: VrDeviceInfo,) -> VrStereoConfig:
        """Load VR stereo config for VR simulator device parameters"""
        ...
def LoadWave(fileName: str,) -> Wave:
        """Load wave data from file"""
        ...
def LoadWaveFromMemory(fileType: str,fileData: str,dataSize: int,) -> Wave:
        """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
        ...
def LoadWaveSamples(wave: Wave,) -> Any:
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
def MaximizeWindow() -> None:
        """Set window state: maximized, if resizable (only PLATFORM_DESKTOP)"""
        ...
def MeasureText(text: str,fontSize: int,) -> int:
        """Measure string width for default font"""
        ...
def MeasureTextEx(font: Font,text: str,fontSize: float,spacing: float,) -> Vector2:
        """Measure string size for Font"""
        ...
def MemAlloc(size: int,) -> Any:
        """Internal memory allocator"""
        ...
def MemFree(ptr: Any,) -> None:
        """Internal memory free"""
        ...
def MemRealloc(ptr: Any,size: int,) -> Any:
        """Internal memory reallocator"""
        ...
def MinimizeWindow() -> None:
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
def OpenURL(url: str,) -> None:
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
def PauseAudioStream(stream: AudioStream,) -> None:
        """Pause audio stream"""
        ...
def PauseMusicStream(music: Music,) -> None:
        """Pause music playing"""
        ...
def PauseSound(sound: Sound,) -> None:
        """Pause a sound"""
        ...
def PhysicsAddForce(PhysicsBodyData_pointer_0: Any,Vector2_1: Vector2,) -> None:
        """void PhysicsAddForce(struct PhysicsBodyData *, struct Vector2);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def PhysicsAddTorque(PhysicsBodyData_pointer_0: Any,float_1: float,) -> None:
        """void PhysicsAddTorque(struct PhysicsBodyData *, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def PhysicsShatter(PhysicsBodyData_pointer_0: Any,Vector2_1: Vector2,float_2: float,) -> None:
        """void PhysicsShatter(struct PhysicsBodyData *, struct Vector2, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def PlayAudioStream(stream: AudioStream,) -> None:
        """Play audio stream"""
        ...
def PlayMusicStream(music: Music,) -> None:
        """Start music playing"""
        ...
def PlaySound(sound: Sound,) -> None:
        """Play a sound"""
        ...
def PlaySoundMulti(sound: Sound,) -> None:
        """Play a sound (using multichannel buffer pool)"""
        ...
def PollInputEvents() -> None:
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
def ResetPhysics() -> None:
        """void ResetPhysics();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def RestoreWindow() -> None:
        """Set window state: not minimized/maximized (only PLATFORM_DESKTOP)"""
        ...
def ResumeAudioStream(stream: AudioStream,) -> None:
        """Resume audio stream"""
        ...
def ResumeMusicStream(music: Music,) -> None:
        """Resume playing paused music"""
        ...
def ResumeSound(sound: Sound,) -> None:
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
def SaveFileData(fileName: str,data: Any,bytesToWrite: int,) -> bool:
        """Save data to file from byte array (write), returns true on success"""
        ...
def SaveFileText(fileName: str,text: str,) -> bool:
        """Save text data to file (write), string must be ' 0' terminated, returns true on success"""
        ...
def SaveStorageValue(position: int,value: int,) -> bool:
        """Save integer value to storage file (to defined position), returns true on success"""
        ...
def SeekMusicStream(music: Music,position: float,) -> None:
        """Seek music to a position (in seconds)"""
        ...
def SetAudioStreamBufferSizeDefault(size: int,) -> None:
        """Default size for new audio streams"""
        ...
def SetAudioStreamPitch(stream: AudioStream,pitch: float,) -> None:
        """Set pitch for audio stream (1.0 is base level)"""
        ...
def SetAudioStreamVolume(stream: AudioStream,volume: float,) -> None:
        """Set volume for audio stream (1.0 is max level)"""
        ...
def SetCameraAltControl(keyAlt: int,) -> None:
        """Set camera alt key to combine with mouse movement (free camera)"""
        ...
def SetCameraMode(camera: Camera3D,mode: int,) -> None:
        """Set camera mode (multiple camera modes available)"""
        ...
def SetCameraMoveControls(keyFront: int,keyBack: int,keyRight: int,keyLeft: int,keyUp: int,keyDown: int,) -> None:
        """Set camera move controls (1st person and 3rd person cameras)"""
        ...
def SetCameraPanControl(keyPan: int,) -> None:
        """Set camera pan key to combine with mouse movement (free camera)"""
        ...
def SetCameraSmoothZoomControl(keySmoothZoom: int,) -> None:
        """Set camera smooth zoom key to combine with mouse (free camera)"""
        ...
def SetClipboardText(text: str,) -> None:
        """Set clipboard text content"""
        ...
def SetConfigFlags(flags: int,) -> None:
        """Setup init configuration flags (view FLAGS)"""
        ...
def SetExitKey(key: int,) -> None:
        """Set a custom key to exit program (default is ESC)"""
        ...
def SetGamepadMappings(mappings: str,) -> int:
        """Set internal gamepad mappings (SDL_GameControllerDB)"""
        ...
def SetGesturesEnabled(flags: int,) -> None:
        """Enable a set of gestures using flags"""
        ...
def SetLoadFileDataCallback(callback: str,) -> None:
        """Set custom file binary data loader"""
        ...
def SetLoadFileTextCallback(callback: str,) -> None:
        """Set custom file text data loader"""
        ...
def SetMasterVolume(volume: float,) -> None:
        """Set master volume (listener)"""
        ...
def SetMaterialTexture(material: Any,mapType: int,texture: Texture,) -> None:
        """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
        ...
def SetModelMeshMaterial(model: Any,meshId: int,materialId: int,) -> None:
        """Set material for a mesh"""
        ...
def SetMouseCursor(cursor: int,) -> None:
        """Set mouse cursor"""
        ...
def SetMouseOffset(offsetX: int,offsetY: int,) -> None:
        """Set mouse offset"""
        ...
def SetMousePosition(x: int,y: int,) -> None:
        """Set mouse position XY"""
        ...
def SetMouseScale(scaleX: float,scaleY: float,) -> None:
        """Set mouse scaling"""
        ...
def SetMusicPitch(music: Music,pitch: float,) -> None:
        """Set pitch for a music (1.0 is base level)"""
        ...
def SetMusicVolume(music: Music,volume: float,) -> None:
        """Set volume for music (1.0 is max level)"""
        ...
def SetPhysicsBodyRotation(PhysicsBodyData_pointer_0: Any,float_1: float,) -> None:
        """void SetPhysicsBodyRotation(struct PhysicsBodyData *, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def SetPhysicsGravity(float_0: float,float_1: float,) -> None:
        """void SetPhysicsGravity(float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def SetPhysicsTimeStep(double_0: float,) -> None:
        """void SetPhysicsTimeStep(double);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def SetPixelColor(dstPtr: Any,color: Color,format: int,) -> None:
        """Set color formatted into destination pixel pointer"""
        ...
def SetRandomSeed(seed: int,) -> None:
        """Set the seed for the random number generator"""
        ...
def SetSaveFileDataCallback(callback: str,) -> None:
        """Set custom file binary data saver"""
        ...
def SetSaveFileTextCallback(callback: str,) -> None:
        """Set custom file text data saver"""
        ...
def SetShaderValue(shader: Shader,locIndex: int,value: Any,uniformType: int,) -> None:
        """Set shader uniform value"""
        ...
def SetShaderValueMatrix(shader: Shader,locIndex: int,mat: Matrix,) -> None:
        """Set shader uniform value (matrix 4x4)"""
        ...
def SetShaderValueTexture(shader: Shader,locIndex: int,texture: Texture,) -> None:
        """Set shader uniform value for texture (sampler2d)"""
        ...
def SetShaderValueV(shader: Shader,locIndex: int,value: Any,uniformType: int,count: int,) -> None:
        """Set shader uniform value vector"""
        ...
def SetShapesTexture(texture: Texture,source: Rectangle,) -> None:
        """Set texture and rectangle to be used on shapes drawing"""
        ...
def SetSoundPitch(sound: Sound,pitch: float,) -> None:
        """Set pitch for a sound (1.0 is base level)"""
        ...
def SetSoundVolume(sound: Sound,volume: float,) -> None:
        """Set volume for a sound (1.0 is max level)"""
        ...
def SetTargetFPS(fps: int,) -> None:
        """Set target FPS (maximum)"""
        ...
def SetTextureFilter(texture: Texture,filter: int,) -> None:
        """Set texture scaling filter mode"""
        ...
def SetTextureWrap(texture: Texture,wrap: int,) -> None:
        """Set texture wrapping mode"""
        ...
def SetTraceLogCallback(callback: str,) -> None:
        """Set custom trace log"""
        ...
def SetTraceLogLevel(logLevel: int,) -> None:
        """Set the current threshold (minimum) log level"""
        ...
def SetWindowIcon(image: Image,) -> None:
        """Set icon for window (only PLATFORM_DESKTOP)"""
        ...
def SetWindowMinSize(width: int,height: int,) -> None:
        """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
        ...
def SetWindowMonitor(monitor: int,) -> None:
        """Set monitor for the current window (fullscreen mode)"""
        ...
def SetWindowPosition(x: int,y: int,) -> None:
        """Set window position on screen (only PLATFORM_DESKTOP)"""
        ...
def SetWindowSize(width: int,height: int,) -> None:
        """Set window dimensions"""
        ...
def SetWindowState(flags: int,) -> None:
        """Set window configuration state using flags"""
        ...
def SetWindowTitle(title: str,) -> None:
        """Set title for window (only PLATFORM_DESKTOP)"""
        ...
def ShowCursor() -> None:
        """Shows cursor"""
        ...
def StopAudioStream(stream: AudioStream,) -> None:
        """Stop audio stream"""
        ...
def StopMusicStream(music: Music,) -> None:
        """Stop music playing"""
        ...
def StopSound(sound: Sound,) -> None:
        """Stop playing a sound"""
        ...
def StopSoundMulti() -> None:
        """Stop any sound playing (using multichannel buffer pool)"""
        ...
def SwapScreenBuffer() -> None:
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
def TakeScreenshot(fileName: str,) -> None:
        """Takes a screenshot of current screen (filename extension defines format)"""
        ...
def TextAppend(text: str,append: str,position: Any,) -> None:
        """Append text at specific position and move cursor!"""
        ...
def TextCodepointsToUTF8(codepoints: Any,length: int,) -> str:
        """Encode text as codepoints array into UTF-8 text string (WARNING: memory must be freed!)"""
        ...
def TextCopy(dst: str,src: str,) -> int:
        """Copy one string to another, returns bytes copied"""
        ...
def TextFindIndex(text: str,find: str,) -> int:
        """Find first text occurrence within a string"""
        ...
def TextFormat(*args) -> str:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def TextInsert(text: str,insert: str,position: int,) -> str:
        """Insert text in a position (WARNING: memory must be freed!)"""
        ...
def TextIsEqual(text1: str,text2: str,) -> bool:
        """Check if two text string are equal"""
        ...
def TextJoin(textList: str,count: int,delimiter: str,) -> str:
        """Join text strings with delimiter"""
        ...
def TextLength(text: str,) -> int:
        """Get text length, checks for ' 0' ending"""
        ...
def TextReplace(text: str,replace: str,by: str,) -> str:
        """Replace text string (WARNING: memory must be freed!)"""
        ...
def TextSplit(text: str,delimiter: str,count: Any,) -> str:
        """Split text into multiple strings"""
        ...
def TextSubtext(text: str,position: int,length: int,) -> str:
        """Get a piece of a text string"""
        ...
def TextToInteger(text: str,) -> int:
        """Get integer value from text (negative values not supported)"""
        ...
def TextToLower(text: str,) -> str:
        """Get lower case version of provided string"""
        ...
def TextToPascal(text: str,) -> str:
        """Get Pascal case notation version of provided string"""
        ...
def TextToUpper(text: str,) -> str:
        """Get upper case version of provided string"""
        ...
def ToggleFullscreen() -> None:
        """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
        ...
def TraceLog(*args) -> None:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def UnloadAudioStream(stream: AudioStream,) -> None:
        """Unload audio stream and free memory"""
        ...
def UnloadCodepoints(codepoints: Any,) -> None:
        """Unload codepoints data from memory"""
        ...
def UnloadFileData(data: str,) -> None:
        """Unload file data allocated by LoadFileData()"""
        ...
def UnloadFileText(text: str,) -> None:
        """Unload file text data allocated by LoadFileText()"""
        ...
def UnloadFont(font: Font,) -> None:
        """Unload Font from GPU memory (VRAM)"""
        ...
def UnloadFontData(chars: Any,glyphCount: int,) -> None:
        """Unload font chars info data (RAM)"""
        ...
def UnloadImage(image: Image,) -> None:
        """Unload image from CPU memory (RAM)"""
        ...
def UnloadImageColors(colors: Any,) -> None:
        """Unload color data loaded with LoadImageColors()"""
        ...
def UnloadImagePalette(colors: Any,) -> None:
        """Unload colors palette loaded with LoadImagePalette()"""
        ...
def UnloadMaterial(material: Material,) -> None:
        """Unload material from GPU memory (VRAM)"""
        ...
def UnloadMesh(mesh: Mesh,) -> None:
        """Unload mesh data from CPU and GPU"""
        ...
def UnloadModel(model: Model,) -> None:
        """Unload model (including meshes) from memory (RAM and/or VRAM)"""
        ...
def UnloadModelAnimation(anim: ModelAnimation,) -> None:
        """Unload animation data"""
        ...
def UnloadModelAnimations(animations: Any,count: int,) -> None:
        """Unload animation array data"""
        ...
def UnloadModelKeepMeshes(model: Model,) -> None:
        """Unload model (but not meshes) from memory (RAM and/or VRAM)"""
        ...
def UnloadMusicStream(music: Music,) -> None:
        """Unload music stream"""
        ...
def UnloadRenderTexture(target: RenderTexture,) -> None:
        """Unload render texture from GPU memory (VRAM)"""
        ...
def UnloadShader(shader: Shader,) -> None:
        """Unload shader from GPU memory (VRAM)"""
        ...
def UnloadSound(sound: Sound,) -> None:
        """Unload sound"""
        ...
def UnloadTexture(texture: Texture,) -> None:
        """Unload texture from GPU memory (VRAM)"""
        ...
def UnloadVrStereoConfig(config: VrStereoConfig,) -> None:
        """Unload VR stereo config"""
        ...
def UnloadWave(wave: Wave,) -> None:
        """Unload wave data"""
        ...
def UnloadWaveSamples(samples: Any,) -> None:
        """Unload samples data loaded with LoadWaveSamples()"""
        ...
def UpdateAudioStream(stream: AudioStream,data: Any,frameCount: int,) -> None:
        """Update audio stream buffers with data"""
        ...
def UpdateCamera(camera: Any,) -> None:
        """Update camera position for selected mode"""
        ...
def UpdateMeshBuffer(mesh: Mesh,index: int,data: Any,dataSize: int,offset: int,) -> None:
        """Update mesh vertex data in GPU for a specific buffer index"""
        ...
def UpdateModelAnimation(model: Model,anim: ModelAnimation,frame: int,) -> None:
        """Update model animation pose"""
        ...
def UpdateMusicStream(music: Music,) -> None:
        """Updates buffers for music streaming"""
        ...
def UpdatePhysics() -> None:
        """void UpdatePhysics();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def UpdateSound(sound: Sound,data: Any,sampleCount: int,) -> None:
        """Update sound buffer with new data"""
        ...
def UpdateTexture(texture: Texture,pixels: Any,) -> None:
        """Update GPU texture with new data"""
        ...
def UpdateTextureRec(texture: Texture,rec: Rectangle,pixels: Any,) -> None:
        """Update GPU texture rectangle with new data"""
        ...
def UploadMesh(mesh: Any,dynamic: bool,) -> None:
        """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
        ...
VALUEBOX: int
def WaitTime(ms: float,) -> None:
        """Wait for some milliseconds (halt program execution)"""
        ...
def WaveCopy(wave: Wave,) -> Wave:
        """Copy a wave to a new wave"""
        ...
def WaveCrop(wave: Any,initSample: int,finalSample: int,) -> None:
        """Crop a wave to defined samples range"""
        ...
def WaveFormat(wave: Any,sampleRate: int,sampleSize: int,channels: int,) -> None:
        """Convert wave data to desired format"""
        ...
def WindowShouldClose() -> bool:
        """Check if KEY_ESCAPE pressed or Close icon pressed"""
        ...
def rlActiveDrawBuffers(int_0: int,) -> None:
        """void rlActiveDrawBuffers(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlActiveTextureSlot(int_0: int,) -> None:
        """void rlActiveTextureSlot(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlBegin(int_0: int,) -> None:
        """void rlBegin(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlCheckErrors() -> None:
        """void rlCheckErrors();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlCheckRenderBatchLimit(int_0: int,) -> bool:
        """_Bool rlCheckRenderBatchLimit(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlClearColor(unsignedchar_0: str,unsignedchar_1: str,unsignedchar_2: str,unsignedchar_3: str,) -> None:
        """void rlClearColor(unsigned char, unsigned char, unsigned char, unsigned char);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlClearScreenBuffers() -> None:
        """void rlClearScreenBuffers();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlColor3f(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlColor3f(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlColor4f(float_0: float,float_1: float,float_2: float,float_3: float,) -> None:
        """void rlColor4f(float, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlColor4ub(unsignedchar_0: str,unsignedchar_1: str,unsignedchar_2: str,unsignedchar_3: str,) -> None:
        """void rlColor4ub(unsigned char, unsigned char, unsigned char, unsigned char);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlCompileShader(str_0: str,int_1: int,) -> int:
        """unsigned int rlCompileShader(char *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableBackfaceCulling() -> None:
        """void rlDisableBackfaceCulling();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableColorBlend() -> None:
        """void rlDisableColorBlend();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableDepthMask() -> None:
        """void rlDisableDepthMask();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableDepthTest() -> None:
        """void rlDisableDepthTest();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableFramebuffer() -> None:
        """void rlDisableFramebuffer();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableScissorTest() -> None:
        """void rlDisableScissorTest();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableShader() -> None:
        """void rlDisableShader();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableSmoothLines() -> None:
        """void rlDisableSmoothLines();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableStereoRender() -> None:
        """void rlDisableStereoRender();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableTexture() -> None:
        """void rlDisableTexture();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableTextureCubemap() -> None:
        """void rlDisableTextureCubemap();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableVertexArray() -> None:
        """void rlDisableVertexArray();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableVertexAttribute(unsignedint_0: int,) -> None:
        """void rlDisableVertexAttribute(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableVertexBuffer() -> None:
        """void rlDisableVertexBuffer();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableVertexBufferElement() -> None:
        """void rlDisableVertexBufferElement();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDisableWireMode() -> None:
        """void rlDisableWireMode();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDrawRenderBatch(rlRenderBatch_pointer_0: Any,) -> None:
        """void rlDrawRenderBatch(struct rlRenderBatch *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDrawRenderBatchActive() -> None:
        """void rlDrawRenderBatchActive();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDrawVertexArray(int_0: int,int_1: int,) -> None:
        """void rlDrawVertexArray(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDrawVertexArrayElements(int_0: int,int_1: int,void_pointer_2: Any,) -> None:
        """void rlDrawVertexArrayElements(int, int, void *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDrawVertexArrayElementsInstanced(int_0: int,int_1: int,void_pointer_2: Any,int_3: int,) -> None:
        """void rlDrawVertexArrayElementsInstanced(int, int, void *, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlDrawVertexArrayInstanced(int_0: int,int_1: int,int_2: int,) -> None:
        """void rlDrawVertexArrayInstanced(int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableBackfaceCulling() -> None:
        """void rlEnableBackfaceCulling();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableColorBlend() -> None:
        """void rlEnableColorBlend();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableDepthMask() -> None:
        """void rlEnableDepthMask();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableDepthTest() -> None:
        """void rlEnableDepthTest();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableFramebuffer(unsignedint_0: int,) -> None:
        """void rlEnableFramebuffer(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableScissorTest() -> None:
        """void rlEnableScissorTest();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableShader(unsignedint_0: int,) -> None:
        """void rlEnableShader(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableSmoothLines() -> None:
        """void rlEnableSmoothLines();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableStereoRender() -> None:
        """void rlEnableStereoRender();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableTexture(unsignedint_0: int,) -> None:
        """void rlEnableTexture(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableTextureCubemap(unsignedint_0: int,) -> None:
        """void rlEnableTextureCubemap(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableVertexArray(unsignedint_0: int,) -> bool:
        """_Bool rlEnableVertexArray(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableVertexAttribute(unsignedint_0: int,) -> None:
        """void rlEnableVertexAttribute(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableVertexBuffer(unsignedint_0: int,) -> None:
        """void rlEnableVertexBuffer(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableVertexBufferElement(unsignedint_0: int,) -> None:
        """void rlEnableVertexBufferElement(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnableWireMode() -> None:
        """void rlEnableWireMode();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlEnd() -> None:
        """void rlEnd();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlFramebufferAttach(unsignedint_0: int,unsignedint_1: int,int_2: int,int_3: int,int_4: int,) -> None:
        """void rlFramebufferAttach(unsigned int, unsigned int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlFramebufferComplete(unsignedint_0: int,) -> bool:
        """_Bool rlFramebufferComplete(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlFrustum(double_0: float,double_1: float,double_2: float,double_3: float,double_4: float,double_5: float,) -> None:
        """void rlFrustum(double, double, double, double, double, double);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGenTextureMipmaps(unsignedint_0: int,int_1: int,int_2: int,int_3: int,int_pointer_4: Any,) -> None:
        """void rlGenTextureMipmaps(unsigned int, int, int, int, int *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetFramebufferHeight() -> int:
        """int rlGetFramebufferHeight();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetFramebufferWidth() -> int:
        """int rlGetFramebufferWidth();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetGlTextureFormats(int_0: int,int_pointer_1: Any,int_pointer_2: Any,int_pointer_3: Any,) -> None:
        """void rlGetGlTextureFormats(int, int *, int *, int *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetLineWidth() -> float:
        """float rlGetLineWidth();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetLocationAttrib(unsignedint_0: int,str_1: str,) -> int:
        """int rlGetLocationAttrib(unsigned int, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetLocationUniform(unsignedint_0: int,str_1: str,) -> int:
        """int rlGetLocationUniform(unsigned int, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetMatrixModelview() -> Matrix:
        """struct Matrix rlGetMatrixModelview();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetMatrixProjection() -> Matrix:
        """struct Matrix rlGetMatrixProjection();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetMatrixProjectionStereo(int_0: int,) -> Matrix:
        """struct Matrix rlGetMatrixProjectionStereo(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetMatrixTransform() -> Matrix:
        """struct Matrix rlGetMatrixTransform();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetMatrixViewOffsetStereo(int_0: int,) -> Matrix:
        """struct Matrix rlGetMatrixViewOffsetStereo(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetPixelFormatName(unsignedint_0: int,) -> str:
        """char *rlGetPixelFormatName(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetShaderIdDefault() -> int:
        """unsigned int rlGetShaderIdDefault();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetShaderLocsDefault() -> Any:
        """int *rlGetShaderLocsDefault();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetTextureIdDefault() -> int:
        """unsigned int rlGetTextureIdDefault();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlGetVersion() -> int:
        """int rlGetVersion();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlIsStereoRenderEnabled() -> bool:
        """_Bool rlIsStereoRenderEnabled();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadDrawCube() -> None:
        """void rlLoadDrawCube();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadDrawQuad() -> None:
        """void rlLoadDrawQuad();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadExtensions(void_pointer_0: Any,) -> None:
        """void rlLoadExtensions(void *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadFramebuffer(int_0: int,int_1: int,) -> int:
        """unsigned int rlLoadFramebuffer(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadIdentity() -> None:
        """void rlLoadIdentity();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadRenderBatch(int_0: int,int_1: int,) -> rlRenderBatch:
        """struct rlRenderBatch rlLoadRenderBatch(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadShaderCode(str_0: str,str_1: str,) -> int:
        """unsigned int rlLoadShaderCode(char *, char *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadShaderProgram(unsignedint_0: int,unsignedint_1: int,) -> int:
        """unsigned int rlLoadShaderProgram(unsigned int, unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadTexture(void_pointer_0: Any,int_1: int,int_2: int,int_3: int,int_4: int,) -> int:
        """unsigned int rlLoadTexture(void *, int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadTextureCubemap(void_pointer_0: Any,int_1: int,int_2: int,) -> int:
        """unsigned int rlLoadTextureCubemap(void *, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadTextureDepth(int_0: int,int_1: int,_Bool_2: bool,) -> int:
        """unsigned int rlLoadTextureDepth(int, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadVertexArray() -> int:
        """unsigned int rlLoadVertexArray();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadVertexBuffer(void_pointer_0: Any,int_1: int,_Bool_2: bool,) -> int:
        """unsigned int rlLoadVertexBuffer(void *, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlLoadVertexBufferElement(void_pointer_0: Any,int_1: int,_Bool_2: bool,) -> int:
        """unsigned int rlLoadVertexBufferElement(void *, int, _Bool);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlMatrixMode(int_0: int,) -> None:
        """void rlMatrixMode(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlMultMatrixf(float_pointer_0: Any,) -> None:
        """void rlMultMatrixf(float *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlNormal3f(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlNormal3f(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlOrtho(double_0: float,double_1: float,double_2: float,double_3: float,double_4: float,double_5: float,) -> None:
        """void rlOrtho(double, double, double, double, double, double);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlPopMatrix() -> None:
        """void rlPopMatrix();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlPushMatrix() -> None:
        """void rlPushMatrix();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlReadScreenPixels(int_0: int,int_1: int,) -> str:
        """unsigned char *rlReadScreenPixels(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlReadTexturePixels(unsignedint_0: int,int_1: int,int_2: int,int_3: int,) -> Any:
        """void *rlReadTexturePixels(unsigned int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlRotatef(float_0: float,float_1: float,float_2: float,float_3: float,) -> None:
        """void rlRotatef(float, float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlScalef(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlScalef(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlScissor(int_0: int,int_1: int,int_2: int,int_3: int,) -> None:
        """void rlScissor(int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetBlendFactors(int_0: int,int_1: int,int_2: int,) -> None:
        """void rlSetBlendFactors(int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetBlendMode(int_0: int,) -> None:
        """void rlSetBlendMode(int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetLineWidth(float_0: float,) -> None:
        """void rlSetLineWidth(float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetMatrixModelview(Matrix_0: Matrix,) -> None:
        """void rlSetMatrixModelview(struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetMatrixProjection(Matrix_0: Matrix,) -> None:
        """void rlSetMatrixProjection(struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetMatrixProjectionStereo(Matrix_0: Matrix,Matrix_1: Matrix,) -> None:
        """void rlSetMatrixProjectionStereo(struct Matrix, struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetMatrixViewOffsetStereo(Matrix_0: Matrix,Matrix_1: Matrix,) -> None:
        """void rlSetMatrixViewOffsetStereo(struct Matrix, struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetRenderBatchActive(rlRenderBatch_pointer_0: Any,) -> None:
        """void rlSetRenderBatchActive(struct rlRenderBatch *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetShader(unsignedint_0: int,int_pointer_1: Any,) -> None:
        """void rlSetShader(unsigned int, int *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetTexture(unsignedint_0: int,) -> None:
        """void rlSetTexture(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetUniform(int_0: int,void_pointer_1: Any,int_2: int,int_3: int,) -> None:
        """void rlSetUniform(int, void *, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetUniformMatrix(int_0: int,Matrix_1: Matrix,) -> None:
        """void rlSetUniformMatrix(int, struct Matrix);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetUniformSampler(int_0: int,unsignedint_1: int,) -> None:
        """void rlSetUniformSampler(int, unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetVertexAttribute(unsignedint_0: int,int_1: int,int_2: int,_Bool_3: bool,int_4: int,void_pointer_5: Any,) -> None:
        """void rlSetVertexAttribute(unsigned int, int, int, _Bool, int, void *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetVertexAttributeDefault(int_0: int,void_pointer_1: Any,int_2: int,int_3: int,) -> None:
        """void rlSetVertexAttributeDefault(int, void *, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlSetVertexAttributeDivisor(unsignedint_0: int,int_1: int,) -> None:
        """void rlSetVertexAttributeDivisor(unsigned int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlTexCoord2f(float_0: float,float_1: float,) -> None:
        """void rlTexCoord2f(float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlTextureParameters(unsignedint_0: int,int_1: int,int_2: int,) -> None:
        """void rlTextureParameters(unsigned int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlTranslatef(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlTranslatef(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlUnloadFramebuffer(unsignedint_0: int,) -> None:
        """void rlUnloadFramebuffer(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlUnloadRenderBatch(rlRenderBatch_0: rlRenderBatch,) -> None:
        """void rlUnloadRenderBatch(struct rlRenderBatch);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlUnloadShaderProgram(unsignedint_0: int,) -> None:
        """void rlUnloadShaderProgram(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlUnloadTexture(unsignedint_0: int,) -> None:
        """void rlUnloadTexture(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlUnloadVertexArray(unsignedint_0: int,) -> None:
        """void rlUnloadVertexArray(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlUnloadVertexBuffer(unsignedint_0: int,) -> None:
        """void rlUnloadVertexBuffer(unsigned int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlUpdateTexture(unsignedint_0: int,int_1: int,int_2: int,int_3: int,int_4: int,int_5: int,void_pointer_6: Any,) -> None:
        """void rlUpdateTexture(unsigned int, int, int, int, int, int, void *);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlUpdateVertexBuffer(unsignedint_0: int,void_pointer_1: Any,int_2: int,int_3: int,) -> None:
        """void rlUpdateVertexBuffer(unsigned int, void *, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlVertex2f(float_0: float,float_1: float,) -> None:
        """void rlVertex2f(float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlVertex2i(int_0: int,int_1: int,) -> None:
        """void rlVertex2i(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlVertex3f(float_0: float,float_1: float,float_2: float,) -> None:
        """void rlVertex3f(float, float, float);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlViewport(int_0: int,int_1: int,int_2: int,int_3: int,) -> None:
        """void rlViewport(int, int, int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlglClose() -> None:
        """void rlglClose();

CFFI C function from raylib._raylib_cffi.lib"""
        ...
def rlglInit(int_0: int,int_1: int,) -> None:
        """void rlglInit(int, int);

CFFI C function from raylib._raylib_cffi.lib"""
        ...
AudioStream: struct
BlendMode: int
BoneInfo: struct
BoundingBox: struct
Camera: struct
Camera2D: struct
Camera3D: struct
CameraMode: int
CameraProjection: int
Color: struct
ConfigFlags: int
CubemapLayout: int
Font: struct
FontType: int
GamepadAxis: int
GamepadButton: int
Gesture: int
GlyphInfo: struct
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
GuiStyleProp: struct
GuiTextAlignment: int
GuiTextBoxProperty: int
GuiToggleProperty: int
Image: struct
KeyboardKey: int
Material: struct
MaterialMap: struct
MaterialMapIndex: int
Matrix: struct
Matrix2x2: struct
Mesh: struct
Model: struct
ModelAnimation: struct
MouseButton: int
MouseCursor: int
Music: struct
NPatchInfo: struct
NPatchLayout: int
PhysicsBodyData: struct
PhysicsManifoldData: struct
PhysicsShape: struct
PhysicsShapeType: int
PhysicsVertexData: struct
PixelFormat: int
Quaternion: struct
Ray: struct
RayCollision: struct
Rectangle: struct
RenderTexture: struct
RenderTexture2D: struct
Shader: struct
ShaderAttributeDataType: int
ShaderLocationIndex: int
ShaderUniformDataType: int
Sound: struct
Texture: struct
Texture2D: struct
TextureCubemap: struct
TextureFilter: int
TextureWrap: int
TraceLogLevel: int
Transform: struct
Vector2: struct
Vector3: struct
Vector4: struct
VrDeviceInfo: struct
VrStereoConfig: struct
Wave: struct
rAudioBuffer: struct
rlBlendMode: int
rlDrawCall: struct
rlFramebufferAttachTextureType: int
rlFramebufferAttachType: int
rlGlVersion: int
rlPixelFormat: int
rlRenderBatch: struct
rlShaderAttributeDataType: int
rlShaderLocationIndex: int
rlShaderUniformDataType: int
rlTextureFilter: int
rlTraceLogLevel: int
rlVertexBuffer: struct

LIGHTGRAY  =( 200, 200, 200, 255 )
GRAY       =( 130, 130, 130, 255 )
DARKGRAY   =( 80, 80, 80, 255 )
YELLOW     =( 253, 249, 0, 255 )
GOLD       =( 255, 203, 0, 255 )
ORANGE     =( 255, 161, 0, 255 )
PINK       =( 255, 109, 194, 255 )
RED        =( 230, 41, 55, 255 )
MAROON     =( 190, 33, 55, 255 )
GREEN      =( 0, 228, 48, 255 )
LIME       =( 0, 158, 47, 255 )
DARKGREEN  =( 0, 117, 44, 255 )
SKYBLUE    =( 102, 191, 255, 255 )
BLUE       =( 0, 121, 241, 255 )
DARKBLUE   =( 0, 82, 172, 255 )
PURPLE     =( 200, 122, 255, 255 )
VIOLET     =( 135, 60, 190, 255 )
DARKPURPLE =( 112, 31, 126, 255 )
BEIGE      =( 211, 176, 131, 255 )
BROWN      =( 127, 106, 79, 255 )
DARKBROWN  =( 76, 63, 47, 255 )
WHITE      =( 255, 255, 255, 255 )
BLACK      =( 0, 0, 0, 255 )
BLANK      =( 0, 0, 0, 0 )
MAGENTA    =( 255, 0, 255, 255 )
RAYWHITE   =( 245, 245, 245, 255 )
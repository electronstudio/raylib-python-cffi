from typing import Any

import _cffi_backend

ffi: _cffi_backend.FFI
rl: _cffi_backend.Lib

class struct: ...


ARROWS_SIZE: int
ARROWS_VISIBLE: int
ARROW_PADDING: int
def AttachAudioMixedProcessor(processor: Any,) -> None:
        """Attach audio stream processor to the entire audio pipeline, receives the samples as <float>s"""
        ...
def AttachAudioStreamProcessor(stream: AudioStream,processor: Any,) -> None:
        """Attach audio stream processor to stream, receives the samples as <float>s"""
        ...
BACKGROUND_COLOR: int
BASE_COLOR_DISABLED: int
BASE_COLOR_FOCUSED: int
BASE_COLOR_NORMAL: int
BASE_COLOR_PRESSED: int
BLEND_ADDITIVE: int
BLEND_ADD_COLORS: int
BLEND_ALPHA: int
BLEND_ALPHA_PREMULTIPLY: int
BLEND_CUSTOM: int
BLEND_CUSTOM_SEPARATE: int
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
COLOR_SELECTOR_SIZE: int
COMBOBOX: int
COMBO_BUTTON_SPACING: int
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
def CheckCollisionPointPoly(point: Vector2,points: Any,pointCount: int,) -> bool:
        """Check if point is within a polygon described by array of vertices"""
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
def Clamp(value: float,min_1: float,max_2: float,) -> float:
        """"""
        ...
def ClearBackground(color: Color,) -> None:
        """Set background color (framebuffer clear color)"""
        ...
def ClearWindowState(flags: int,) -> None:
        """Clear window configuration state flags"""
        ...
def CloseAudioDevice() -> None:
        """Close the audio device and context"""
        ...
def ClosePhysics() -> None:
        """Close physics system and unload used memory"""
        ...
def CloseWindow() -> None:
        """Close window and unload OpenGL context"""
        ...
def CodepointToUTF8(codepoint: int,utf8Size: Any,) -> str:
        """Encode one codepoint into UTF-8 byte array (array length returned as parameter)"""
        ...
def ColorAlpha(color: Color,alpha: float,) -> Color:
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        ...
def ColorAlphaBlend(dst: Color,src: Color,tint: Color,) -> Color:
        """Get src alpha-blended into dst color with tint"""
        ...
def ColorBrightness(color: Color,factor: float,) -> Color:
        """Get color with brightness correction, brightness factor goes from -1.0f to 1.0f"""
        ...
def ColorContrast(color: Color,contrast: float,) -> Color:
        """Get color with contrast correction, contrast values between -1.0f and 1.0f"""
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
def ColorTint(color: Color,tint: Color,) -> Color:
        """Get color multiplied with another color"""
        ...
def ColorToHSV(color: Color,) -> Vector3:
        """Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
        ...
def ColorToInt(color: Color,) -> int:
        """Get hexadecimal value for a Color"""
        ...
def CompressData(data: str,dataSize: int,compDataSize: Any,) -> str:
        """Compress data (DEFLATE algorithm), memory must be MemFree()"""
        ...
def CreatePhysicsBodyCircle(pos: Vector2,radius: float,density: float,) -> Any:
        """Creates a new circle physics body with generic parameters"""
        ...
def CreatePhysicsBodyPolygon(pos: Vector2,radius: float,sides: int,density: float,) -> Any:
        """Creates a new polygon physics body with generic parameters"""
        ...
def CreatePhysicsBodyRectangle(pos: Vector2,width: float,height: float,density: float,) -> Any:
        """Creates a new rectangle physics body with generic parameters"""
        ...
DEFAULT: int
DROPDOWNBOX: int
DROPDOWN_ITEMS_SPACING: int
def DecodeDataBase64(data: str,outputSize: Any,) -> str:
        """Decode Base64 string data, memory must be MemFree()"""
        ...
def DecompressData(compData: str,compDataSize: int,dataSize: Any,) -> str:
        """Decompress data (DEFLATE algorithm), memory must be MemFree()"""
        ...
def DestroyPhysicsBody(body: Any,) -> None:
        """Destroy a physics body"""
        ...
def DetachAudioMixedProcessor(processor: Any,) -> None:
        """Detach audio stream processor from the entire audio pipeline"""
        ...
def DetachAudioStreamProcessor(stream: AudioStream,processor: Any,) -> None:
        """Detach audio stream processor from stream"""
        ...
def DirectoryExists(dirPath: str,) -> bool:
        """Check if a directory path exists"""
        ...
def DisableCursor() -> None:
        """Disables cursor (lock cursor)"""
        ...
def DisableEventWaiting() -> None:
        """Disable waiting for events on EndDrawing(), automatic events polling"""
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
def DrawCapsule(startPos: Vector3,endPos: Vector3,radius: float,slices: int,rings: int,color: Color,) -> None:
        """Draw a capsule with the center of its sphere caps at startPos and endPos"""
        ...
def DrawCapsuleWires(startPos: Vector3,endPos: Vector3,radius: float,slices: int,rings: int,color: Color,) -> None:
        """Draw capsule wireframe with the center of its sphere caps at startPos and endPos"""
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
def DrawCircleLinesV(center: Vector2,radius: float,color: Color,) -> None:
        """Draw circle outline (Vector version)"""
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
        """Draw line segment cubic-bezier in-out interpolation"""
        ...
def DrawLineEx(startPos: Vector2,endPos: Vector2,thick: float,color: Color,) -> None:
        """Draw a line (using triangles/quads)"""
        ...
def DrawLineStrip(points: Any,pointCount: int,color: Color,) -> None:
        """Draw lines sequence (using gl lines)"""
        ...
def DrawLineV(startPos: Vector2,endPos: Vector2,color: Color,) -> None:
        """Draw a line (using gl lines)"""
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
def DrawSplineBasis(points: Any,pointCount: int,thick: float,color: Color,) -> None:
        """Draw spline: B-Spline, minimum 4 points"""
        ...
def DrawSplineBezierCubic(points: Any,pointCount: int,thick: float,color: Color,) -> None:
        """Draw spline: Cubic Bezier, minimum 4 points (2 control points): [p1, c2, c3, p4, c5, c6...]"""
        ...
def DrawSplineBezierQuadratic(points: Any,pointCount: int,thick: float,color: Color,) -> None:
        """Draw spline: Quadratic Bezier, minimum 3 points (1 control point): [p1, c2, p3, c4...]"""
        ...
def DrawSplineCatmullRom(points: Any,pointCount: int,thick: float,color: Color,) -> None:
        """Draw spline: Catmull-Rom, minimum 4 points"""
        ...
def DrawSplineLinear(points: Any,pointCount: int,thick: float,color: Color,) -> None:
        """Draw spline: Linear, minimum 2 points"""
        ...
def DrawSplineSegmentBasis(p1: Vector2,p2: Vector2,p3: Vector2,p4: Vector2,thick: float,color: Color,) -> None:
        """Draw spline segment: B-Spline, 4 points"""
        ...
def DrawSplineSegmentBezierCubic(p1: Vector2,c2: Vector2,c3: Vector2,p4: Vector2,thick: float,color: Color,) -> None:
        """Draw spline segment: Cubic Bezier, 2 points, 2 control points"""
        ...
def DrawSplineSegmentBezierQuadratic(p1: Vector2,c2: Vector2,p3: Vector2,thick: float,color: Color,) -> None:
        """Draw spline segment: Quadratic Bezier, 2 points, 1 control point"""
        ...
def DrawSplineSegmentCatmullRom(p1: Vector2,p2: Vector2,p3: Vector2,p4: Vector2,thick: float,color: Color,) -> None:
        """Draw spline segment: Catmull-Rom, 4 points"""
        ...
def DrawSplineSegmentLinear(p1: Vector2,p2: Vector2,thick: float,color: Color,) -> None:
        """Draw spline segment: Linear, 2 points"""
        ...
def DrawText(text: str,posX: int,posY: int,fontSize: int,color: Color,) -> None:
        """Draw text (using default font)"""
        ...
def DrawTextCodepoint(font: Font,codepoint: int,position: Vector2,fontSize: float,tint: Color,) -> None:
        """Draw one character (codepoint)"""
        ...
def DrawTextCodepoints(font: Font,codepoints: Any,codepointCount: int,position: Vector2,fontSize: float,spacing: float,tint: Color,) -> None:
        """Draw multiple character (codepoint)"""
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
def DrawTexturePro(texture: Texture,source: Rectangle,dest: Rectangle,origin: Vector2,rotation: float,tint: Color,) -> None:
        """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
        ...
def DrawTextureRec(texture: Texture,source: Rectangle,position: Vector2,tint: Color,) -> None:
        """Draw a part of a texture defined by a rectangle"""
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
def EnableEventWaiting() -> None:
        """Enable waiting for events on EndDrawing(), no automatic event polling"""
        ...
def EncodeDataBase64(data: str,dataSize: int,outputSize: Any,) -> str:
        """Encode data to Base64 string, memory must be MemFree()"""
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
def ExportAutomationEventList(list_0: AutomationEventList,fileName: str,) -> bool:
        """Export automation events list as text file"""
        ...
def ExportDataAsCode(data: str,dataSize: int,fileName: str,) -> bool:
        """Export data to code (.h), returns true on success"""
        ...
def ExportFontAsCode(font: Font,fileName: str,) -> bool:
        """Export font as code file, returns true on success"""
        ...
def ExportImage(image: Image,fileName: str,) -> bool:
        """Export image data to file, returns true on success"""
        ...
def ExportImageAsCode(image: Image,fileName: str,) -> bool:
        """Export image as code file defining an array of bytes, returns true on success"""
        ...
def ExportImageToMemory(image: Image,fileType: str,fileSize: Any,) -> str:
        """Export image to memory buffer"""
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
FLAG_BORDERLESS_WINDOWED_MODE: int
FLAG_FULLSCREEN_MODE: int
FLAG_INTERLACED_HINT: int
FLAG_MSAA_4X_HINT: int
FLAG_VSYNC_HINT: int
FLAG_WINDOW_ALWAYS_RUN: int
FLAG_WINDOW_HIDDEN: int
FLAG_WINDOW_HIGHDPI: int
FLAG_WINDOW_MAXIMIZED: int
FLAG_WINDOW_MINIMIZED: int
FLAG_WINDOW_MOUSE_PASSTHROUGH: int
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
def FloatEquals(x: float,y: float,) -> int:
        """"""
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
def GenImageCellular(width: int,height: int,tileSize: int,) -> Image:
        """Generate image: cellular algorithm, bigger tileSize means bigger cells"""
        ...
def GenImageChecked(width: int,height: int,checksX: int,checksY: int,col1: Color,col2: Color,) -> Image:
        """Generate image: checked"""
        ...
def GenImageColor(width: int,height: int,color: Color,) -> Image:
        """Generate image: plain color"""
        ...
def GenImageFontAtlas(glyphs: Any,glyphRecs: Any,glyphCount: int,fontSize: int,padding: int,packMethod: int,) -> Image:
        """Generate image font atlas using chars info"""
        ...
def GenImageGradientLinear(width: int,height: int,direction: int,start: Color,end: Color,) -> Image:
        """Generate image: linear gradient, direction in degrees [0..360], 0=Vertical gradient"""
        ...
def GenImageGradientRadial(width: int,height: int,density: float,inner: Color,outer: Color,) -> Image:
        """Generate image: radial gradient"""
        ...
def GenImageGradientSquare(width: int,height: int,density: float,inner: Color,outer: Color,) -> Image:
        """Generate image: square gradient"""
        ...
def GenImagePerlinNoise(width: int,height: int,offsetX: int,offsetY: int,scale: float,) -> Image:
        """Generate image: perlin noise"""
        ...
def GenImageText(width: int,height: int,text: str,) -> Image:
        """Generate image: grayscale image from text data"""
        ...
def GenImageWhiteNoise(width: int,height: int,factor: float,) -> Image:
        """Generate image: white noise"""
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
def GetApplicationDirectory() -> str:
        """Get the directory of the running application (uses static string)"""
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
def GetCodepoint(text: str,codepointSize: Any,) -> int:
        """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
        ...
def GetCodepointCount(text: str,) -> int:
        """Get total number of codepoints in a UTF-8 encoded string"""
        ...
def GetCodepointNext(text: str,codepointSize: Any,) -> int:
        """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
        ...
def GetCodepointPrevious(text: str,codepointSize: Any,) -> int:
        """Get previous codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
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
def GetDirectoryPath(filePath: str,) -> str:
        """Get full path for a given fileName with path (uses static string)"""
        ...
def GetFPS() -> int:
        """Get current FPS"""
        ...
def GetFileExtension(fileName: str,) -> str:
        """Get pointer to extension for a filename string (includes dot: '.png')"""
        ...
def GetFileLength(fileName: str,) -> int:
        """Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)"""
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
def GetMasterVolume() -> float:
        """Get master volume (listener)"""
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
        """Get specified monitor height (current video mode used by monitor)"""
        ...
def GetMonitorName(monitor: int,) -> str:
        """Get the human-readable, UTF-8 encoded name of the specified monitor"""
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
        """Get specified monitor width (current video mode used by monitor)"""
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
        """Get mouse wheel movement for X or Y, whichever is larger"""
        ...
def GetMouseWheelMoveV() -> Vector2:
        """Get mouse wheel movement for both X and Y"""
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
        """Returns the current amount of created physics bodies"""
        ...
def GetPhysicsBody(index: int,) -> Any:
        """Returns a physics body of the bodies pool at a specific index"""
        ...
def GetPhysicsShapeType(index: int,) -> int:
        """Returns the physics body shape type (PHYSICS_CIRCLE or PHYSICS_POLYGON)"""
        ...
def GetPhysicsShapeVertex(body: Any,vertex: int,) -> Vector2:
        """Returns transformed position of a body shape (body position + vertex transformed position)"""
        ...
def GetPhysicsShapeVerticesCount(index: int,) -> int:
        """Returns the amount of vertices of a physics body shape"""
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
def GetRandomValue(min_0: int,max_1: int,) -> int:
        """Get a random value between min and max (both included)"""
        ...
def GetRayCollisionBox(ray: Ray,box: BoundingBox,) -> RayCollision:
        """Get collision info between ray and box"""
        ...
def GetRayCollisionMesh(ray: Ray,mesh: Mesh,transform: Matrix,) -> RayCollision:
        """Get collision info between ray and mesh"""
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
def GetRenderHeight() -> int:
        """Get current render height (it considers HiDPI)"""
        ...
def GetRenderWidth() -> int:
        """Get current render width (it considers HiDPI)"""
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
def GetSplinePointBasis(p1: Vector2,p2: Vector2,p3: Vector2,p4: Vector2,t: float,) -> Vector2:
        """Get (evaluate) spline point: B-Spline"""
        ...
def GetSplinePointBezierCubic(p1: Vector2,c2: Vector2,c3: Vector2,p4: Vector2,t: float,) -> Vector2:
        """Get (evaluate) spline point: Cubic Bezier"""
        ...
def GetSplinePointBezierQuad(p1: Vector2,c2: Vector2,p3: Vector2,t: float,) -> Vector2:
        """Get (evaluate) spline point: Quadratic Bezier"""
        ...
def GetSplinePointCatmullRom(p1: Vector2,p2: Vector2,p3: Vector2,p4: Vector2,t: float,) -> Vector2:
        """Get (evaluate) spline point: Catmull-Rom"""
        ...
def GetSplinePointLinear(startPos: Vector2,endPos: Vector2,t: float,) -> Vector2:
        """Get (evaluate) spline point: Linear"""
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
def GuiButton(bounds: Rectangle,text: str,) -> int:
        """Button control, returns true when clicked"""
        ...
def GuiCheckBox(bounds: Rectangle,text: str,checked: Any,) -> int:
        """Check Box control, returns true when active"""
        ...
def GuiColorBarAlpha(bounds: Rectangle,text: str,alpha: Any,) -> int:
        """Color Bar Alpha control"""
        ...
def GuiColorBarHue(bounds: Rectangle,text: str,value: Any,) -> int:
        """Color Bar Hue control"""
        ...
def GuiColorPanel(bounds: Rectangle,text: str,color: Any,) -> int:
        """Color Panel control"""
        ...
def GuiColorPanelHSV(bounds: Rectangle,text: str,colorHsv: Any,) -> int:
        """Color Panel control that returns HSV color value, used by GuiColorPickerHSV()"""
        ...
def GuiColorPicker(bounds: Rectangle,text: str,color: Any,) -> int:
        """Color Picker control (multiple color controls)"""
        ...
def GuiColorPickerHSV(bounds: Rectangle,text: str,colorHsv: Any,) -> int:
        """Color Picker control that avoids conversion to RGB on each call (multiple color controls)"""
        ...
def GuiComboBox(bounds: Rectangle,text: str,active: Any,) -> int:
        """Combo Box control, returns selected item index"""
        ...
def GuiDisable() -> None:
        """Disable gui controls (global state)"""
        ...
def GuiDisableTooltip() -> None:
        """Disable gui tooltips (global state)"""
        ...
def GuiDrawIcon(iconId: int,posX: int,posY: int,pixelSize: int,color: Color,) -> None:
        """Draw icon using pixel size at specified position"""
        ...
def GuiDropdownBox(bounds: Rectangle,text: str,active: Any,editMode: bool,) -> int:
        """Dropdown Box control, returns selected item"""
        ...
def GuiDummyRec(bounds: Rectangle,text: str,) -> int:
        """Dummy control for placeholders"""
        ...
def GuiEnable() -> None:
        """Enable gui controls (global state)"""
        ...
def GuiEnableTooltip() -> None:
        """Enable gui tooltips (global state)"""
        ...
def GuiGetFont() -> Font:
        """Get gui custom font (global state)"""
        ...
def GuiGetIcons() -> Any:
        """Get raygui icons data pointer"""
        ...
def GuiGetState() -> int:
        """Get gui state (global state)"""
        ...
def GuiGetStyle(control: int,property: int,) -> int:
        """Get one style property"""
        ...
def GuiGrid(bounds: Rectangle,text: str,spacing: float,subdivs: int,mouseCell: Any,) -> int:
        """Grid control, returns mouse cell position"""
        ...
def GuiGroupBox(bounds: Rectangle,text: str,) -> int:
        """Group Box control with text name"""
        ...
def GuiIconText(iconId: int,text: str,) -> str:
        """Get text with icon id prepended (if supported)"""
        ...
def GuiIsLocked() -> bool:
        """Check if gui is locked (global state)"""
        ...
def GuiLabel(bounds: Rectangle,text: str,) -> int:
        """Label control, shows text"""
        ...
def GuiLabelButton(bounds: Rectangle,text: str,) -> int:
        """Label button control, show true when clicked"""
        ...
def GuiLine(bounds: Rectangle,text: str,) -> int:
        """Line separator control, could contain text"""
        ...
def GuiListView(bounds: Rectangle,text: str,scrollIndex: Any,active: Any,) -> int:
        """List View control, returns selected list item index"""
        ...
def GuiListViewEx(bounds: Rectangle,text: str,count: int,scrollIndex: Any,active: Any,focus: Any,) -> int:
        """List View with extended parameters"""
        ...
def GuiLoadIcons(fileName: str,loadIconsName: bool,) -> str:
        """Load raygui icons file (.rgi) into internal icons data"""
        ...
def GuiLoadStyle(fileName: str,) -> None:
        """Load style file over global style variable (.rgs)"""
        ...
def GuiLoadStyleDefault() -> None:
        """Load style default over global style"""
        ...
def GuiLock() -> None:
        """Lock gui controls (global state)"""
        ...
def GuiMessageBox(bounds: Rectangle,title: str,message: str,buttons: str,) -> int:
        """Message Box control, displays a message"""
        ...
def GuiPanel(bounds: Rectangle,text: str,) -> int:
        """Panel control, useful to group controls"""
        ...
def GuiProgressBar(bounds: Rectangle,textLeft: str,textRight: str,value: Any,minValue: float,maxValue: float,) -> int:
        """Progress Bar control, shows current progress value"""
        ...
def GuiScrollPanel(bounds: Rectangle,text: str,content: Rectangle,scroll: Any,view: Any,) -> int:
        """Scroll Panel control"""
        ...
def GuiSetAlpha(alpha: float,) -> None:
        """Set gui controls alpha (global state), alpha goes from 0.0f to 1.0f"""
        ...
def GuiSetFont(font: Font,) -> None:
        """Set gui custom font (global state)"""
        ...
def GuiSetIconScale(scale: int,) -> None:
        """Set default icon drawing size"""
        ...
def GuiSetState(state: int,) -> None:
        """Set gui state (global state)"""
        ...
def GuiSetStyle(control: int,property: int,value: int,) -> None:
        """Set one style property"""
        ...
def GuiSetTooltip(tooltip: str,) -> None:
        """Set tooltip string"""
        ...
def GuiSlider(bounds: Rectangle,textLeft: str,textRight: str,value: Any,minValue: float,maxValue: float,) -> int:
        """Slider control, returns selected value"""
        ...
def GuiSliderBar(bounds: Rectangle,textLeft: str,textRight: str,value: Any,minValue: float,maxValue: float,) -> int:
        """Slider Bar control, returns selected value"""
        ...
def GuiSpinner(bounds: Rectangle,text: str,value: Any,minValue: int,maxValue: int,editMode: bool,) -> int:
        """Spinner control, returns selected value"""
        ...
def GuiStatusBar(bounds: Rectangle,text: str,) -> int:
        """Status Bar control, shows info text"""
        ...
def GuiTabBar(bounds: Rectangle,text: str,count: int,active: Any,) -> int:
        """Tab Bar control, returns TAB to be closed or -1"""
        ...
def GuiTextBox(bounds: Rectangle,text: str,textSize: int,editMode: bool,) -> int:
        """Text Box control, updates input text"""
        ...
def GuiTextInputBox(bounds: Rectangle,title: str,message: str,buttons: str,text: str,textMaxSize: int,secretViewActive: Any,) -> int:
        """Text Input Box control, ask for text, supports secret"""
        ...
def GuiToggle(bounds: Rectangle,text: str,active: Any,) -> int:
        """Toggle Button control, returns true when active"""
        ...
def GuiToggleGroup(bounds: Rectangle,text: str,active: Any,) -> int:
        """Toggle Group control, returns active toggle index"""
        ...
def GuiToggleSlider(bounds: Rectangle,text: str,active: Any,) -> int:
        """Toggle Slider control, returns true when clicked"""
        ...
def GuiUnlock() -> None:
        """Unlock gui controls (global state)"""
        ...
def GuiValueBox(bounds: Rectangle,text: str,value: Any,minValue: int,maxValue: int,editMode: bool,) -> int:
        """Value Box control, updates input text with numbers"""
        ...
def GuiWindowBox(bounds: Rectangle,title: str,) -> int:
        """Window Box control, shows a window that can be closed"""
        ...
HUEBAR_PADDING: int
HUEBAR_SELECTOR_HEIGHT: int
HUEBAR_SELECTOR_OVERFLOW: int
HUEBAR_WIDTH: int
def HideCursor() -> None:
        """Hides cursor"""
        ...
ICON_1UP: int
ICON_220: int
ICON_221: int
ICON_222: int
ICON_223: int
ICON_224: int
ICON_225: int
ICON_226: int
ICON_227: int
ICON_228: int
ICON_229: int
ICON_230: int
ICON_231: int
ICON_232: int
ICON_233: int
ICON_234: int
ICON_235: int
ICON_236: int
ICON_237: int
ICON_238: int
ICON_239: int
ICON_240: int
ICON_241: int
ICON_242: int
ICON_243: int
ICON_244: int
ICON_245: int
ICON_246: int
ICON_247: int
ICON_248: int
ICON_249: int
ICON_250: int
ICON_251: int
ICON_252: int
ICON_253: int
ICON_254: int
ICON_255: int
ICON_ALARM: int
ICON_ALPHA_CLEAR: int
ICON_ALPHA_MULTIPLY: int
ICON_ARROW_DOWN: int
ICON_ARROW_DOWN_FILL: int
ICON_ARROW_LEFT: int
ICON_ARROW_LEFT_FILL: int
ICON_ARROW_RIGHT: int
ICON_ARROW_RIGHT_FILL: int
ICON_ARROW_UP: int
ICON_ARROW_UP_FILL: int
ICON_AUDIO: int
ICON_BIN: int
ICON_BOX: int
ICON_BOX_BOTTOM: int
ICON_BOX_BOTTOM_LEFT: int
ICON_BOX_BOTTOM_RIGHT: int
ICON_BOX_CENTER: int
ICON_BOX_CIRCLE_MASK: int
ICON_BOX_CONCENTRIC: int
ICON_BOX_CORNERS_BIG: int
ICON_BOX_CORNERS_SMALL: int
ICON_BOX_DOTS_BIG: int
ICON_BOX_DOTS_SMALL: int
ICON_BOX_GRID: int
ICON_BOX_GRID_BIG: int
ICON_BOX_LEFT: int
ICON_BOX_MULTISIZE: int
ICON_BOX_RIGHT: int
ICON_BOX_TOP: int
ICON_BOX_TOP_LEFT: int
ICON_BOX_TOP_RIGHT: int
ICON_BREAKPOINT_OFF: int
ICON_BREAKPOINT_ON: int
ICON_BRUSH_CLASSIC: int
ICON_BRUSH_PAINTER: int
ICON_BURGER_MENU: int
ICON_CAMERA: int
ICON_CASE_SENSITIVE: int
ICON_CLOCK: int
ICON_COIN: int
ICON_COLOR_BUCKET: int
ICON_COLOR_PICKER: int
ICON_CORNER: int
ICON_CPU: int
ICON_CRACK: int
ICON_CRACK_POINTS: int
ICON_CROP: int
ICON_CROP_ALPHA: int
ICON_CROSS: int
ICON_CROSSLINE: int
ICON_CROSS_SMALL: int
ICON_CUBE: int
ICON_CUBE_FACE_BACK: int
ICON_CUBE_FACE_BOTTOM: int
ICON_CUBE_FACE_FRONT: int
ICON_CUBE_FACE_LEFT: int
ICON_CUBE_FACE_RIGHT: int
ICON_CUBE_FACE_TOP: int
ICON_CURSOR_CLASSIC: int
ICON_CURSOR_HAND: int
ICON_CURSOR_MOVE: int
ICON_CURSOR_MOVE_FILL: int
ICON_CURSOR_POINTER: int
ICON_CURSOR_SCALE: int
ICON_CURSOR_SCALE_FILL: int
ICON_CURSOR_SCALE_LEFT: int
ICON_CURSOR_SCALE_LEFT_FILL: int
ICON_CURSOR_SCALE_RIGHT: int
ICON_CURSOR_SCALE_RIGHT_FILL: int
ICON_DEMON: int
ICON_DITHERING: int
ICON_DOOR: int
ICON_EMPTYBOX: int
ICON_EMPTYBOX_SMALL: int
ICON_EXIT: int
ICON_EXPLOSION: int
ICON_EYE_OFF: int
ICON_EYE_ON: int
ICON_FILE: int
ICON_FILETYPE_ALPHA: int
ICON_FILETYPE_AUDIO: int
ICON_FILETYPE_BINARY: int
ICON_FILETYPE_HOME: int
ICON_FILETYPE_IMAGE: int
ICON_FILETYPE_INFO: int
ICON_FILETYPE_PLAY: int
ICON_FILETYPE_TEXT: int
ICON_FILETYPE_VIDEO: int
ICON_FILE_ADD: int
ICON_FILE_COPY: int
ICON_FILE_CUT: int
ICON_FILE_DELETE: int
ICON_FILE_EXPORT: int
ICON_FILE_NEW: int
ICON_FILE_OPEN: int
ICON_FILE_PASTE: int
ICON_FILE_SAVE: int
ICON_FILE_SAVE_CLASSIC: int
ICON_FILTER: int
ICON_FILTER_BILINEAR: int
ICON_FILTER_POINT: int
ICON_FILTER_TOP: int
ICON_FOLDER: int
ICON_FOLDER_ADD: int
ICON_FOLDER_FILE_OPEN: int
ICON_FOLDER_OPEN: int
ICON_FOLDER_SAVE: int
ICON_FOUR_BOXES: int
ICON_FX: int
ICON_GEAR: int
ICON_GEAR_BIG: int
ICON_GEAR_EX: int
ICON_GRID: int
ICON_GRID_FILL: int
ICON_HAND_POINTER: int
ICON_HEART: int
ICON_HELP: int
ICON_HEX: int
ICON_HIDPI: int
ICON_HOUSE: int
ICON_INFO: int
ICON_KEY: int
ICON_LASER: int
ICON_LAYERS: int
ICON_LAYERS_VISIBLE: int
ICON_LENS: int
ICON_LENS_BIG: int
ICON_LIFE_BARS: int
ICON_LINK: int
ICON_LINK_BOXES: int
ICON_LINK_BROKE: int
ICON_LINK_MULTI: int
ICON_LINK_NET: int
ICON_LOCK_CLOSE: int
ICON_LOCK_OPEN: int
ICON_MAGNET: int
ICON_MAILBOX: int
ICON_MIPMAPS: int
ICON_MODE_2D: int
ICON_MODE_3D: int
ICON_MONITOR: int
ICON_MUTATE: int
ICON_MUTATE_FILL: int
ICON_NONE: int
ICON_NOTEBOOK: int
ICON_OK_TICK: int
ICON_PENCIL: int
ICON_PENCIL_BIG: int
ICON_PHOTO_CAMERA: int
ICON_PHOTO_CAMERA_FLASH: int
ICON_PLAYER: int
ICON_PLAYER_JUMP: int
ICON_PLAYER_NEXT: int
ICON_PLAYER_PAUSE: int
ICON_PLAYER_PLAY: int
ICON_PLAYER_PLAY_BACK: int
ICON_PLAYER_PREVIOUS: int
ICON_PLAYER_RECORD: int
ICON_PLAYER_STOP: int
ICON_POT: int
ICON_PRINTER: int
ICON_REDO: int
ICON_REDO_FILL: int
ICON_REG_EXP: int
ICON_REPEAT: int
ICON_REPEAT_FILL: int
ICON_REREDO: int
ICON_REREDO_FILL: int
ICON_RESIZE: int
ICON_RESTART: int
ICON_ROM: int
ICON_ROTATE: int
ICON_ROTATE_FILL: int
ICON_RUBBER: int
ICON_SAND_TIMER: int
ICON_SCALE: int
ICON_SHIELD: int
ICON_SHUFFLE: int
ICON_SHUFFLE_FILL: int
ICON_SPECIAL: int
ICON_SQUARE_TOGGLE: int
ICON_STAR: int
ICON_STEP_INTO: int
ICON_STEP_OUT: int
ICON_STEP_OVER: int
ICON_SUITCASE: int
ICON_SUITCASE_ZIP: int
ICON_SYMMETRY: int
ICON_SYMMETRY_HORIZONTAL: int
ICON_SYMMETRY_VERTICAL: int
ICON_TARGET: int
ICON_TARGET_BIG: int
ICON_TARGET_BIG_FILL: int
ICON_TARGET_MOVE: int
ICON_TARGET_MOVE_FILL: int
ICON_TARGET_POINT: int
ICON_TARGET_SMALL: int
ICON_TARGET_SMALL_FILL: int
ICON_TEXT_A: int
ICON_TEXT_NOTES: int
ICON_TEXT_POPUP: int
ICON_TEXT_T: int
ICON_TOOLS: int
ICON_UNDO: int
ICON_UNDO_FILL: int
ICON_VERTICAL_BARS: int
ICON_VERTICAL_BARS_FILL: int
ICON_WATER_DROP: int
ICON_WAVE: int
ICON_WAVE_SINUS: int
ICON_WAVE_SQUARE: int
ICON_WAVE_TRIANGULAR: int
ICON_WINDOW: int
ICON_ZOOM_ALL: int
ICON_ZOOM_BIG: int
ICON_ZOOM_CENTER: int
ICON_ZOOM_MEDIUM: int
ICON_ZOOM_SMALL: int
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
def ImageBlurGaussian(image: Any,blurSize: int,) -> None:
        """Apply Gaussian blur using a box blur approximation"""
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
        """Draw a filled circle within an image"""
        ...
def ImageDrawCircleLines(dst: Any,centerX: int,centerY: int,radius: int,color: Color,) -> None:
        """Draw circle outline within an image"""
        ...
def ImageDrawCircleLinesV(dst: Any,center: Vector2,radius: int,color: Color,) -> None:
        """Draw circle outline within an image (Vector version)"""
        ...
def ImageDrawCircleV(dst: Any,center: Vector2,radius: int,color: Color,) -> None:
        """Draw a filled circle within an image (Vector version)"""
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
def ImageRotate(image: Any,degrees: int,) -> None:
        """Rotate image by input angle in degrees (-359 to 359)"""
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
        """Initializes physics system"""
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
def IsAudioStreamReady(stream: AudioStream,) -> bool:
        """Checks if an audio stream is ready"""
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
def IsFontReady(font: Font,) -> bool:
        """Check if a font is ready"""
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
def IsImageReady(image: Image,) -> bool:
        """Check if an image is ready"""
        ...
def IsKeyDown(key: int,) -> bool:
        """Check if a key is being pressed"""
        ...
def IsKeyPressed(key: int,) -> bool:
        """Check if a key has been pressed once"""
        ...
def IsKeyPressedRepeat(key: int,) -> bool:
        """Check if a key has been pressed again (Only PLATFORM_DESKTOP)"""
        ...
def IsKeyReleased(key: int,) -> bool:
        """Check if a key has been released once"""
        ...
def IsKeyUp(key: int,) -> bool:
        """Check if a key is NOT being pressed"""
        ...
def IsMaterialReady(material: Material,) -> bool:
        """Check if a material is ready"""
        ...
def IsModelAnimationValid(model: Model,anim: ModelAnimation,) -> bool:
        """Check model animation skeleton match"""
        ...
def IsModelReady(model: Model,) -> bool:
        """Check if a model is ready"""
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
def IsMusicReady(music: Music,) -> bool:
        """Checks if a music stream is ready"""
        ...
def IsMusicStreamPlaying(music: Music,) -> bool:
        """Check if music is playing"""
        ...
def IsPathFile(path: str,) -> bool:
        """Check if a given path is a file or a directory"""
        ...
def IsRenderTextureReady(target: RenderTexture,) -> bool:
        """Check if a render texture is ready"""
        ...
def IsShaderReady(shader: Shader,) -> bool:
        """Check if a shader is ready"""
        ...
def IsSoundPlaying(sound: Sound,) -> bool:
        """Check if a sound is currently playing"""
        ...
def IsSoundReady(sound: Sound,) -> bool:
        """Checks if a sound is ready"""
        ...
def IsTextureReady(texture: Texture,) -> bool:
        """Check if a texture is ready"""
        ...
def IsWaveReady(wave: Wave,) -> bool:
        """Checks if wave data is ready"""
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
LIST_ITEMS_SPACING: int
LOG_ALL: int
LOG_DEBUG: int
LOG_ERROR: int
LOG_FATAL: int
LOG_INFO: int
LOG_NONE: int
LOG_TRACE: int
LOG_WARNING: int
def Lerp(start: float,end: float,amount: float,) -> float:
        """"""
        ...
def LoadAudioStream(sampleRate: int,sampleSize: int,channels: int,) -> AudioStream:
        """Load audio stream (to stream raw audio pcm data)"""
        ...
def LoadAutomationEventList(fileName: str,) -> AutomationEventList:
        """Load automation events list from file, NULL for empty list, capacity = MAX_AUTOMATION_EVENTS"""
        ...
def LoadCodepoints(text: str,count: Any,) -> Any:
        """Load all codepoints from a UTF-8 text string, codepoints count returned by parameter"""
        ...
def LoadDirectoryFiles(dirPath: str,) -> FilePathList:
        """Load directory filepaths"""
        ...
def LoadDirectoryFilesEx(basePath: str,filter: str,scanSubdirs: bool,) -> FilePathList:
        """Load directory filepaths with extension filtering and recursive directory scan"""
        ...
def LoadDroppedFiles() -> FilePathList:
        """Load dropped filepaths"""
        ...
def LoadFileData(fileName: str,dataSize: Any,) -> str:
        """Load file data as byte array (read)"""
        ...
def LoadFileText(fileName: str,) -> str:
        """Load text data from file (read), returns a '\0' terminated string"""
        ...
def LoadFont(fileName: str,) -> Font:
        """Load font from file into GPU memory (VRAM)"""
        ...
def LoadFontData(fileData: str,dataSize: int,fontSize: int,codepoints: Any,codepointCount: int,type: int,) -> Any:
        """Load font data for further use"""
        ...
def LoadFontEx(fileName: str,fontSize: int,codepoints: Any,codepointCount: int,) -> Font:
        """Load font from file with extended parameters, use NULL for codepoints and 0 for codepointCount to load the default character setFont"""
        ...
def LoadFontFromImage(image: Image,key: Color,firstChar: int,) -> Font:
        """Load font from Image (XNA style)"""
        ...
def LoadFontFromMemory(fileType: str,fileData: str,dataSize: int,fontSize: int,codepoints: Any,codepointCount: int,) -> Font:
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
def LoadImageSvg(fileNameOrString: str,width: int,height: int,) -> Image:
        """Load image from SVG file data or string with specified size"""
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
def LoadRandomSequence(count: int,min_1: int,max_2: int,) -> Any:
        """Load random values sequence, no values repeated"""
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
def LoadSoundAlias(source: Sound,) -> Sound:
        """Create a new sound that shares the same sample data as the source sound, does not own the sound data"""
        ...
def LoadSoundFromWave(wave: Wave,) -> Sound:
        """Load sound from wave data"""
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
def LoadUTF8(codepoints: Any,length: int,) -> str:
        """Load UTF-8 text encoded from codepoints array"""
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
        """Load samples data from wave as a 32bit float data array"""
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
def MatrixAdd(left: Matrix,right: Matrix,) -> Matrix:
        """"""
        ...
def MatrixDeterminant(mat: Matrix,) -> float:
        """"""
        ...
def MatrixFrustum(left: float,right: float,bottom: float,top: float,near: float,far: float,) -> Matrix:
        """"""
        ...
def MatrixIdentity() -> Matrix:
        """"""
        ...
def MatrixInvert(mat: Matrix,) -> Matrix:
        """"""
        ...
def MatrixLookAt(eye: Vector3,target: Vector3,up: Vector3,) -> Matrix:
        """"""
        ...
def MatrixMultiply(left: Matrix,right: Matrix,) -> Matrix:
        """"""
        ...
def MatrixOrtho(left: float,right: float,bottom: float,top: float,nearPlane: float,farPlane: float,) -> Matrix:
        """"""
        ...
def MatrixPerspective(fovY: float,aspect: float,nearPlane: float,farPlane: float,) -> Matrix:
        """"""
        ...
def MatrixRotate(axis: Vector3,angle: float,) -> Matrix:
        """"""
        ...
def MatrixRotateX(angle: float,) -> Matrix:
        """"""
        ...
def MatrixRotateXYZ(angle: Vector3,) -> Matrix:
        """"""
        ...
def MatrixRotateY(angle: float,) -> Matrix:
        """"""
        ...
def MatrixRotateZ(angle: float,) -> Matrix:
        """"""
        ...
def MatrixRotateZYX(angle: Vector3,) -> Matrix:
        """"""
        ...
def MatrixScale(x: float,y: float,z: float,) -> Matrix:
        """"""
        ...
def MatrixSubtract(left: Matrix,right: Matrix,) -> Matrix:
        """"""
        ...
def MatrixToFloatV(mat: Matrix,) -> float16:
        """"""
        ...
def MatrixTrace(mat: Matrix,) -> float:
        """"""
        ...
def MatrixTranslate(x: float,y: float,z: float,) -> Matrix:
        """"""
        ...
def MatrixTranspose(mat: Matrix,) -> Matrix:
        """"""
        ...
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
def Normalize(value: float,start: float,end: float,) -> float:
        """"""
        ...
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
PIXELFORMAT_UNCOMPRESSED_R16: int
PIXELFORMAT_UNCOMPRESSED_R16G16B16: int
PIXELFORMAT_UNCOMPRESSED_R16G16B16A16: int
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
def PhysicsAddForce(body: Any,force: Vector2,) -> None:
        """Adds a force to a physics body"""
        ...
def PhysicsAddTorque(body: Any,amount: float,) -> None:
        """Adds an angular force to a physics body"""
        ...
def PhysicsShatter(body: Any,position: Vector2,force: float,) -> None:
        """Shatters a polygon shape physics body to little physics bodies with explosion force"""
        ...
def PlayAudioStream(stream: AudioStream,) -> None:
        """Play audio stream"""
        ...
def PlayAutomationEvent(event: AutomationEvent,) -> None:
        """Play a recorded automation event"""
        ...
def PlayMusicStream(music: Music,) -> None:
        """Start music playing"""
        ...
def PlaySound(sound: Sound,) -> None:
        """Play a sound"""
        ...
def PollInputEvents() -> None:
        """Register all input events"""
        ...
def QuaternionAdd(q1: Vector4,q2: Vector4,) -> Vector4:
        """"""
        ...
def QuaternionAddValue(q: Vector4,add: float,) -> Vector4:
        """"""
        ...
def QuaternionDivide(q1: Vector4,q2: Vector4,) -> Vector4:
        """"""
        ...
def QuaternionEquals(p: Vector4,q: Vector4,) -> int:
        """"""
        ...
def QuaternionFromAxisAngle(axis: Vector3,angle: float,) -> Vector4:
        """"""
        ...
def QuaternionFromEuler(pitch: float,yaw: float,roll: float,) -> Vector4:
        """"""
        ...
def QuaternionFromMatrix(mat: Matrix,) -> Vector4:
        """"""
        ...
def QuaternionFromVector3ToVector3(from_0: Vector3,to: Vector3,) -> Vector4:
        """"""
        ...
def QuaternionIdentity() -> Vector4:
        """"""
        ...
def QuaternionInvert(q: Vector4,) -> Vector4:
        """"""
        ...
def QuaternionLength(q: Vector4,) -> float:
        """"""
        ...
def QuaternionLerp(q1: Vector4,q2: Vector4,amount: float,) -> Vector4:
        """"""
        ...
def QuaternionMultiply(q1: Vector4,q2: Vector4,) -> Vector4:
        """"""
        ...
def QuaternionNlerp(q1: Vector4,q2: Vector4,amount: float,) -> Vector4:
        """"""
        ...
def QuaternionNormalize(q: Vector4,) -> Vector4:
        """"""
        ...
def QuaternionScale(q: Vector4,mul: float,) -> Vector4:
        """"""
        ...
def QuaternionSlerp(q1: Vector4,q2: Vector4,amount: float,) -> Vector4:
        """"""
        ...
def QuaternionSubtract(q1: Vector4,q2: Vector4,) -> Vector4:
        """"""
        ...
def QuaternionSubtractValue(q: Vector4,sub: float,) -> Vector4:
        """"""
        ...
def QuaternionToAxisAngle(q: Vector4,outAxis: Any,outAngle: Any,) -> None:
        """"""
        ...
def QuaternionToEuler(q: Vector4,) -> Vector3:
        """"""
        ...
def QuaternionToMatrix(q: Vector4,) -> Matrix:
        """"""
        ...
def QuaternionTransform(q: Vector4,mat: Matrix,) -> Vector4:
        """"""
        ...
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
RL_BLEND_ALPHA_PREMULTIPLY: int
RL_BLEND_CUSTOM: int
RL_BLEND_CUSTOM_SEPARATE: int
RL_BLEND_MULTIPLIED: int
RL_BLEND_SUBTRACT_COLORS: int
RL_CULL_FACE_BACK: int
RL_CULL_FACE_FRONT: int
RL_LOG_ALL: int
RL_LOG_DEBUG: int
RL_LOG_ERROR: int
RL_LOG_FATAL: int
RL_LOG_INFO: int
RL_LOG_NONE: int
RL_LOG_TRACE: int
RL_LOG_WARNING: int
RL_OPENGL_11: int
RL_OPENGL_21: int
RL_OPENGL_33: int
RL_OPENGL_43: int
RL_OPENGL_ES_20: int
RL_OPENGL_ES_30: int
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
RL_PIXELFORMAT_UNCOMPRESSED_R16: int
RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16: int
RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16A16: int
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
def Remap(value: float,inputStart: float,inputEnd: float,outputStart: float,outputEnd: float,) -> float:
        """"""
        ...
def ResetPhysics() -> None:
        """Reset physics system (global variables)"""
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
SPIN_BUTTON_SPACING: int
SPIN_BUTTON_WIDTH: int
STATE_DISABLED: int
STATE_FOCUSED: int
STATE_NORMAL: int
STATE_PRESSED: int
STATUSBAR: int
def SaveFileData(fileName: str,data: Any,dataSize: int,) -> bool:
        """Save data to file from byte array (write), returns true on success"""
        ...
def SaveFileText(fileName: str,text: str,) -> bool:
        """Save text data to file (write), string must be '\0' terminated, returns true on success"""
        ...
def SeekMusicStream(music: Music,position: float,) -> None:
        """Seek music to a position (in seconds)"""
        ...
def SetAudioStreamBufferSizeDefault(size: int,) -> None:
        """Default size for new audio streams"""
        ...
def SetAudioStreamCallback(stream: AudioStream,callback: Any,) -> None:
        """Audio thread callback to request new data"""
        ...
def SetAudioStreamPan(stream: AudioStream,pan: float,) -> None:
        """Set pan for audio stream (0.5 is centered)"""
        ...
def SetAudioStreamPitch(stream: AudioStream,pitch: float,) -> None:
        """Set pitch for audio stream (1.0 is base level)"""
        ...
def SetAudioStreamVolume(stream: AudioStream,volume: float,) -> None:
        """Set volume for audio stream (1.0 is max level)"""
        ...
def SetAutomationEventBaseFrame(frame: int,) -> None:
        """Set automation event internal base frame to start recording"""
        ...
def SetAutomationEventList(list_0: Any,) -> None:
        """Set automation event list to record to"""
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
def SetMusicPan(music: Music,pan: float,) -> None:
        """Set pan for a music (0.5 is center)"""
        ...
def SetMusicPitch(music: Music,pitch: float,) -> None:
        """Set pitch for a music (1.0 is base level)"""
        ...
def SetMusicVolume(music: Music,volume: float,) -> None:
        """Set volume for music (1.0 is max level)"""
        ...
def SetPhysicsBodyRotation(body: Any,radians: float,) -> None:
        """Sets physics body shape transform based on radians parameter"""
        ...
def SetPhysicsGravity(x: float,y: float,) -> None:
        """Sets physics global gravity force"""
        ...
def SetPhysicsTimeStep(delta: float,) -> None:
        """Sets physics fixed time step in milliseconds. 1.666666 by default"""
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
def SetSoundPan(sound: Sound,pan: float,) -> None:
        """Set pan for a sound (0.5 is center)"""
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
def SetTextLineSpacing(spacing: int,) -> None:
        """Set vertical line spacing when drawing with line-breaks"""
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
def SetWindowFocused() -> None:
        """Set window focused (only PLATFORM_DESKTOP)"""
        ...
def SetWindowIcon(image: Image,) -> None:
        """Set icon for window (single image, RGBA 32bit, only PLATFORM_DESKTOP)"""
        ...
def SetWindowIcons(images: Any,count: int,) -> None:
        """Set icon for window (multiple images, RGBA 32bit, only PLATFORM_DESKTOP)"""
        ...
def SetWindowMaxSize(width: int,height: int,) -> None:
        """Set window maximum dimensions (for FLAG_WINDOW_RESIZABLE)"""
        ...
def SetWindowMinSize(width: int,height: int,) -> None:
        """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
        ...
def SetWindowMonitor(monitor: int,) -> None:
        """Set monitor for the current window"""
        ...
def SetWindowOpacity(opacity: float,) -> None:
        """Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)"""
        ...
def SetWindowPosition(x: int,y: int,) -> None:
        """Set window position on screen (only PLATFORM_DESKTOP)"""
        ...
def SetWindowSize(width: int,height: int,) -> None:
        """Set window dimensions"""
        ...
def SetWindowState(flags: int,) -> None:
        """Set window configuration state using flags (only PLATFORM_DESKTOP)"""
        ...
def SetWindowTitle(title: str,) -> None:
        """Set title for window (only PLATFORM_DESKTOP and PLATFORM_WEB)"""
        ...
def ShowCursor() -> None:
        """Shows cursor"""
        ...
def StartAutomationEventRecording() -> None:
        """Start recording automation events (AutomationEventList must be set)"""
        ...
def StopAudioStream(stream: AudioStream,) -> None:
        """Stop audio stream"""
        ...
def StopAutomationEventRecording() -> None:
        """Stop recording automation events"""
        ...
def StopMusicStream(music: Music,) -> None:
        """Stop music playing"""
        ...
def StopSound(sound: Sound,) -> None:
        """Stop playing a sound"""
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
TEXT_ALIGNMENT_VERTICAL: int
TEXT_ALIGN_BOTTOM: int
TEXT_ALIGN_CENTER: int
TEXT_ALIGN_LEFT: int
TEXT_ALIGN_MIDDLE: int
TEXT_ALIGN_RIGHT: int
TEXT_ALIGN_TOP: int
TEXT_COLOR_DISABLED: int
TEXT_COLOR_FOCUSED: int
TEXT_COLOR_NORMAL: int
TEXT_COLOR_PRESSED: int
TEXT_LINE_SPACING: int
TEXT_PADDING: int
TEXT_READONLY: int
TEXT_SIZE: int
TEXT_SPACING: int
TEXT_WRAP_CHAR: int
TEXT_WRAP_MODE: int
TEXT_WRAP_NONE: int
TEXT_WRAP_WORD: int
TOGGLE: int
def TakeScreenshot(fileName: str,) -> None:
        """Takes a screenshot of current screen (filename extension defines format)"""
        ...
def TextAppend(text: str,append: str,position: Any,) -> None:
        """Append text at specific position and move cursor!"""
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
        """Get text length, checks for '\0' ending"""
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
def ToggleBorderlessWindowed() -> None:
        """Toggle window state: borderless windowed (only PLATFORM_DESKTOP)"""
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
def UnloadAutomationEventList(list_0: Any,) -> None:
        """Unload automation events list from file"""
        ...
def UnloadCodepoints(codepoints: Any,) -> None:
        """Unload codepoints data from memory"""
        ...
def UnloadDirectoryFiles(files: FilePathList,) -> None:
        """Unload filepaths"""
        ...
def UnloadDroppedFiles(files: FilePathList,) -> None:
        """Unload dropped filepaths"""
        ...
def UnloadFileData(data: str,) -> None:
        """Unload file data allocated by LoadFileData()"""
        ...
def UnloadFileText(text: str,) -> None:
        """Unload file text data allocated by LoadFileText()"""
        ...
def UnloadFont(font: Font,) -> None:
        """Unload font from GPU memory (VRAM)"""
        ...
def UnloadFontData(glyphs: Any,glyphCount: int,) -> None:
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
def UnloadModelAnimations(animations: Any,animCount: int,) -> None:
        """Unload animation array data"""
        ...
def UnloadMusicStream(music: Music,) -> None:
        """Unload music stream"""
        ...
def UnloadRandomSequence(sequence: Any,) -> None:
        """Unload random values sequence"""
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
def UnloadSoundAlias(alias: Sound,) -> None:
        """Unload a sound alias (does not deallocate sample data)"""
        ...
def UnloadTexture(texture: Texture,) -> None:
        """Unload texture from GPU memory (VRAM)"""
        ...
def UnloadUTF8(text: str,) -> None:
        """Unload UTF-8 text encoded from codepoints array"""
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
def UpdateCamera(camera: Any,mode: int,) -> None:
        """Update camera position for selected mode"""
        ...
def UpdateCameraPro(camera: Any,movement: Vector3,rotation: Vector3,zoom: float,) -> None:
        """Update camera movement/rotation"""
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
        """Update physics system"""
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
def Vector2Add(v1: Vector2,v2: Vector2,) -> Vector2:
        """"""
        ...
def Vector2AddValue(v: Vector2,add: float,) -> Vector2:
        """"""
        ...
def Vector2Angle(v1: Vector2,v2: Vector2,) -> float:
        """"""
        ...
def Vector2Clamp(v: Vector2,min_1: Vector2,max_2: Vector2,) -> Vector2:
        """"""
        ...
def Vector2ClampValue(v: Vector2,min_1: float,max_2: float,) -> Vector2:
        """"""
        ...
def Vector2Distance(v1: Vector2,v2: Vector2,) -> float:
        """"""
        ...
def Vector2DistanceSqr(v1: Vector2,v2: Vector2,) -> float:
        """"""
        ...
def Vector2Divide(v1: Vector2,v2: Vector2,) -> Vector2:
        """"""
        ...
def Vector2DotProduct(v1: Vector2,v2: Vector2,) -> float:
        """"""
        ...
def Vector2Equals(p: Vector2,q: Vector2,) -> int:
        """"""
        ...
def Vector2Invert(v: Vector2,) -> Vector2:
        """"""
        ...
def Vector2Length(v: Vector2,) -> float:
        """"""
        ...
def Vector2LengthSqr(v: Vector2,) -> float:
        """"""
        ...
def Vector2Lerp(v1: Vector2,v2: Vector2,amount: float,) -> Vector2:
        """"""
        ...
def Vector2LineAngle(start: Vector2,end: Vector2,) -> float:
        """"""
        ...
def Vector2MoveTowards(v: Vector2,target: Vector2,maxDistance: float,) -> Vector2:
        """"""
        ...
def Vector2Multiply(v1: Vector2,v2: Vector2,) -> Vector2:
        """"""
        ...
def Vector2Negate(v: Vector2,) -> Vector2:
        """"""
        ...
def Vector2Normalize(v: Vector2,) -> Vector2:
        """"""
        ...
def Vector2One() -> Vector2:
        """"""
        ...
def Vector2Reflect(v: Vector2,normal: Vector2,) -> Vector2:
        """"""
        ...
def Vector2Rotate(v: Vector2,angle: float,) -> Vector2:
        """"""
        ...
def Vector2Scale(v: Vector2,scale: float,) -> Vector2:
        """"""
        ...
def Vector2Subtract(v1: Vector2,v2: Vector2,) -> Vector2:
        """"""
        ...
def Vector2SubtractValue(v: Vector2,sub: float,) -> Vector2:
        """"""
        ...
def Vector2Transform(v: Vector2,mat: Matrix,) -> Vector2:
        """"""
        ...
def Vector2Zero() -> Vector2:
        """"""
        ...
def Vector3Add(v1: Vector3,v2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3AddValue(v: Vector3,add: float,) -> Vector3:
        """"""
        ...
def Vector3Angle(v1: Vector3,v2: Vector3,) -> float:
        """"""
        ...
def Vector3Barycenter(p: Vector3,a: Vector3,b: Vector3,c: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Clamp(v: Vector3,min_1: Vector3,max_2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3ClampValue(v: Vector3,min_1: float,max_2: float,) -> Vector3:
        """"""
        ...
def Vector3CrossProduct(v1: Vector3,v2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Distance(v1: Vector3,v2: Vector3,) -> float:
        """"""
        ...
def Vector3DistanceSqr(v1: Vector3,v2: Vector3,) -> float:
        """"""
        ...
def Vector3Divide(v1: Vector3,v2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3DotProduct(v1: Vector3,v2: Vector3,) -> float:
        """"""
        ...
def Vector3Equals(p: Vector3,q: Vector3,) -> int:
        """"""
        ...
def Vector3Invert(v: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Length(v: Vector3,) -> float:
        """"""
        ...
def Vector3LengthSqr(v: Vector3,) -> float:
        """"""
        ...
def Vector3Lerp(v1: Vector3,v2: Vector3,amount: float,) -> Vector3:
        """"""
        ...
def Vector3Max(v1: Vector3,v2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Min(v1: Vector3,v2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Multiply(v1: Vector3,v2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Negate(v: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Normalize(v: Vector3,) -> Vector3:
        """"""
        ...
def Vector3One() -> Vector3:
        """"""
        ...
def Vector3OrthoNormalize(v1: Any,v2: Any,) -> None:
        """"""
        ...
def Vector3Perpendicular(v: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Project(v1: Vector3,v2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Reflect(v: Vector3,normal: Vector3,) -> Vector3:
        """"""
        ...
def Vector3Refract(v: Vector3,n: Vector3,r: float,) -> Vector3:
        """"""
        ...
def Vector3Reject(v1: Vector3,v2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3RotateByAxisAngle(v: Vector3,axis: Vector3,angle: float,) -> Vector3:
        """"""
        ...
def Vector3RotateByQuaternion(v: Vector3,q: Vector4,) -> Vector3:
        """"""
        ...
def Vector3Scale(v: Vector3,scalar: float,) -> Vector3:
        """"""
        ...
def Vector3Subtract(v1: Vector3,v2: Vector3,) -> Vector3:
        """"""
        ...
def Vector3SubtractValue(v: Vector3,sub: float,) -> Vector3:
        """"""
        ...
def Vector3ToFloatV(v: Vector3,) -> float3:
        """"""
        ...
def Vector3Transform(v: Vector3,mat: Matrix,) -> Vector3:
        """"""
        ...
def Vector3Unproject(source: Vector3,projection: Matrix,view: Matrix,) -> Vector3:
        """"""
        ...
def Vector3Zero() -> Vector3:
        """"""
        ...
def WaitTime(seconds: float,) -> None:
        """Wait for some time (halt program execution)"""
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
        """Check if application should close (KEY_ESCAPE pressed or windows close icon clicked)"""
        ...
def Wrap(value: float,min_1: float,max_2: float,) -> float:
        """"""
        ...
def glfwCreateCursor(image: Any,xhot: int,yhot: int,) -> Any:
        """"""
        ...
def glfwCreateStandardCursor(shape: int,) -> Any:
        """"""
        ...
def glfwCreateWindow(width: int,height: int,title: str,monitor: Any,share: Any,) -> Any:
        """"""
        ...
def glfwDefaultWindowHints() -> None:
        """"""
        ...
def glfwDestroyCursor(cursor: Any,) -> None:
        """"""
        ...
def glfwDestroyWindow(window: Any,) -> None:
        """"""
        ...
def glfwExtensionSupported(extension: str,) -> int:
        """"""
        ...
def glfwFocusWindow(window: Any,) -> None:
        """"""
        ...
def glfwGetClipboardString(window: Any,) -> str:
        """"""
        ...
def glfwGetCurrentContext() -> Any:
        """"""
        ...
def glfwGetCursorPos(window: Any,xpos: Any,ypos: Any,) -> None:
        """"""
        ...
def glfwGetError(description: str,) -> int:
        """"""
        ...
def glfwGetFramebufferSize(window: Any,width: Any,height: Any,) -> None:
        """"""
        ...
def glfwGetGamepadName(jid: int,) -> str:
        """"""
        ...
def glfwGetGamepadState(jid: int,state: Any,) -> int:
        """"""
        ...
def glfwGetGammaRamp(monitor: Any,) -> Any:
        """"""
        ...
def glfwGetInputMode(window: Any,mode: int,) -> int:
        """"""
        ...
def glfwGetJoystickAxes(jid: int,count: Any,) -> Any:
        """"""
        ...
def glfwGetJoystickButtons(jid: int,count: Any,) -> str:
        """"""
        ...
def glfwGetJoystickGUID(jid: int,) -> str:
        """"""
        ...
def glfwGetJoystickHats(jid: int,count: Any,) -> str:
        """"""
        ...
def glfwGetJoystickName(jid: int,) -> str:
        """"""
        ...
def glfwGetJoystickUserPointer(jid: int,) -> Any:
        """"""
        ...
def glfwGetKey(window: Any,key: int,) -> int:
        """"""
        ...
def glfwGetKeyName(key: int,scancode: int,) -> str:
        """"""
        ...
def glfwGetKeyScancode(key: int,) -> int:
        """"""
        ...
def glfwGetMonitorContentScale(monitor: Any,xscale: Any,yscale: Any,) -> None:
        """"""
        ...
def glfwGetMonitorName(monitor: Any,) -> str:
        """"""
        ...
def glfwGetMonitorPhysicalSize(monitor: Any,widthMM: Any,heightMM: Any,) -> None:
        """"""
        ...
def glfwGetMonitorPos(monitor: Any,xpos: Any,ypos: Any,) -> None:
        """"""
        ...
def glfwGetMonitorUserPointer(monitor: Any,) -> Any:
        """"""
        ...
def glfwGetMonitorWorkarea(monitor: Any,xpos: Any,ypos: Any,width: Any,height: Any,) -> None:
        """"""
        ...
def glfwGetMonitors(count: Any,) -> Any:
        """"""
        ...
def glfwGetMouseButton(window: Any,button: int,) -> int:
        """"""
        ...
def glfwGetPlatform() -> int:
        """"""
        ...
def glfwGetPrimaryMonitor() -> Any:
        """"""
        ...
def glfwGetProcAddress(procname: str,) -> Any:
        """"""
        ...
def glfwGetRequiredInstanceExtensions(count: Any,) -> str:
        """"""
        ...
def glfwGetTime() -> float:
        """"""
        ...
def glfwGetTimerFrequency() -> uint64_t:
        """"""
        ...
def glfwGetTimerValue() -> uint64_t:
        """"""
        ...
def glfwGetVersion(major: Any,minor: Any,rev: Any,) -> None:
        """"""
        ...
def glfwGetVersionString() -> str:
        """"""
        ...
def glfwGetVideoMode(monitor: Any,) -> Any:
        """"""
        ...
def glfwGetVideoModes(monitor: Any,count: Any,) -> Any:
        """"""
        ...
def glfwGetWindowAttrib(window: Any,attrib: int,) -> int:
        """"""
        ...
def glfwGetWindowContentScale(window: Any,xscale: Any,yscale: Any,) -> None:
        """"""
        ...
def glfwGetWindowFrameSize(window: Any,left: Any,top: Any,right: Any,bottom: Any,) -> None:
        """"""
        ...
def glfwGetWindowMonitor(window: Any,) -> Any:
        """"""
        ...
def glfwGetWindowOpacity(window: Any,) -> float:
        """"""
        ...
def glfwGetWindowPos(window: Any,xpos: Any,ypos: Any,) -> None:
        """"""
        ...
def glfwGetWindowSize(window: Any,width: Any,height: Any,) -> None:
        """"""
        ...
def glfwGetWindowUserPointer(window: Any,) -> Any:
        """"""
        ...
def glfwHideWindow(window: Any,) -> None:
        """"""
        ...
def glfwIconifyWindow(window: Any,) -> None:
        """"""
        ...
def glfwInit() -> int:
        """"""
        ...
def glfwInitAllocator(allocator: Any,) -> None:
        """"""
        ...
def glfwInitHint(hint: int,value: int,) -> None:
        """"""
        ...
def glfwJoystickIsGamepad(jid: int,) -> int:
        """"""
        ...
def glfwJoystickPresent(jid: int,) -> int:
        """"""
        ...
def glfwMakeContextCurrent(window: Any,) -> None:
        """"""
        ...
def glfwMaximizeWindow(window: Any,) -> None:
        """"""
        ...
def glfwPlatformSupported(platform: int,) -> int:
        """"""
        ...
def glfwPollEvents() -> None:
        """"""
        ...
def glfwPostEmptyEvent() -> None:
        """"""
        ...
def glfwRawMouseMotionSupported() -> int:
        """"""
        ...
def glfwRequestWindowAttention(window: Any,) -> None:
        """"""
        ...
def glfwRestoreWindow(window: Any,) -> None:
        """"""
        ...
def glfwSetCharCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetCharModsCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetClipboardString(window: Any,string: str,) -> None:
        """"""
        ...
def glfwSetCursor(window: Any,cursor: Any,) -> None:
        """"""
        ...
def glfwSetCursorEnterCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetCursorPos(window: Any,xpos: float,ypos: float,) -> None:
        """"""
        ...
def glfwSetCursorPosCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetDropCallback(window: Any,callback: str,) -> str:
        """"""
        ...
def glfwSetErrorCallback(callback: str,) -> str:
        """"""
        ...
def glfwSetFramebufferSizeCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetGamma(monitor: Any,gamma: float,) -> None:
        """"""
        ...
def glfwSetGammaRamp(monitor: Any,ramp: Any,) -> None:
        """"""
        ...
def glfwSetInputMode(window: Any,mode: int,value: int,) -> None:
        """"""
        ...
def glfwSetJoystickCallback(callback: Any,) -> Any:
        """"""
        ...
def glfwSetJoystickUserPointer(jid: int,pointer: Any,) -> None:
        """"""
        ...
def glfwSetKeyCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetMonitorCallback(callback: Any,) -> Any:
        """"""
        ...
def glfwSetMonitorUserPointer(monitor: Any,pointer: Any,) -> None:
        """"""
        ...
def glfwSetMouseButtonCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetScrollCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetTime(time: float,) -> None:
        """"""
        ...
def glfwSetWindowAspectRatio(window: Any,numer: int,denom: int,) -> None:
        """"""
        ...
def glfwSetWindowAttrib(window: Any,attrib: int,value: int,) -> None:
        """"""
        ...
def glfwSetWindowCloseCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetWindowContentScaleCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetWindowFocusCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetWindowIcon(window: Any,count: int,images: Any,) -> None:
        """"""
        ...
def glfwSetWindowIconifyCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetWindowMaximizeCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetWindowMonitor(window: Any,monitor: Any,xpos: int,ypos: int,width: int,height: int,refreshRate: int,) -> None:
        """"""
        ...
def glfwSetWindowOpacity(window: Any,opacity: float,) -> None:
        """"""
        ...
def glfwSetWindowPos(window: Any,xpos: int,ypos: int,) -> None:
        """"""
        ...
def glfwSetWindowPosCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetWindowRefreshCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetWindowShouldClose(window: Any,value: int,) -> None:
        """"""
        ...
def glfwSetWindowSize(window: Any,width: int,height: int,) -> None:
        """"""
        ...
def glfwSetWindowSizeCallback(window: Any,callback: Any,) -> Any:
        """"""
        ...
def glfwSetWindowSizeLimits(window: Any,minwidth: int,minheight: int,maxwidth: int,maxheight: int,) -> None:
        """"""
        ...
def glfwSetWindowTitle(window: Any,title: str,) -> None:
        """"""
        ...
def glfwSetWindowUserPointer(window: Any,pointer: Any,) -> None:
        """"""
        ...
def glfwShowWindow(window: Any,) -> None:
        """"""
        ...
def glfwSwapBuffers(window: Any,) -> None:
        """"""
        ...
def glfwSwapInterval(interval: int,) -> None:
        """"""
        ...
def glfwTerminate() -> None:
        """"""
        ...
def glfwUpdateGamepadMappings(string: str,) -> int:
        """"""
        ...
def glfwVulkanSupported() -> int:
        """"""
        ...
def glfwWaitEvents() -> None:
        """"""
        ...
def glfwWaitEventsTimeout(timeout: float,) -> None:
        """"""
        ...
def glfwWindowHint(hint: int,value: int,) -> None:
        """"""
        ...
def glfwWindowHintString(hint: int,value: str,) -> None:
        """"""
        ...
def glfwWindowShouldClose(window: Any,) -> int:
        """"""
        ...
def rlActiveDrawBuffers(count: int,) -> None:
        """Activate multiple draw color buffers"""
        ...
def rlActiveTextureSlot(slot: int,) -> None:
        """Select and active a texture slot"""
        ...
def rlBegin(mode: int,) -> None:
        """Initialize drawing mode (how to organize vertex)"""
        ...
def rlBindImageTexture(id: int,index: int,format: int,readonly: bool,) -> None:
        """Bind image texture"""
        ...
def rlBindShaderBuffer(id: int,index: int,) -> None:
        """Bind SSBO buffer"""
        ...
def rlBlitFramebuffer(srcX: int,srcY: int,srcWidth: int,srcHeight: int,dstX: int,dstY: int,dstWidth: int,dstHeight: int,bufferMask: int,) -> None:
        """Blit active framebuffer to main framebuffer"""
        ...
def rlCheckErrors() -> None:
        """Check and log OpenGL error codes"""
        ...
def rlCheckRenderBatchLimit(vCount: int,) -> bool:
        """Check internal buffer overflow for a given number of vertex"""
        ...
def rlClearColor(r: str,g: str,b: str,a: str,) -> None:
        """Clear color buffer with color"""
        ...
def rlClearScreenBuffers() -> None:
        """Clear used screen buffers (color and depth)"""
        ...
def rlColor3f(x: float,y: float,z: float,) -> None:
        """Define one vertex (color) - 3 float"""
        ...
def rlColor4f(x: float,y: float,z: float,w: float,) -> None:
        """Define one vertex (color) - 4 float"""
        ...
def rlColor4ub(r: str,g: str,b: str,a: str,) -> None:
        """Define one vertex (color) - 4 byte"""
        ...
def rlCompileShader(shaderCode: str,type: int,) -> int:
        """Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)"""
        ...
def rlComputeShaderDispatch(groupX: int,groupY: int,groupZ: int,) -> None:
        """Dispatch compute shader (equivalent to *draw* for graphics pipeline)"""
        ...
def rlCopyShaderBuffer(destId: int,srcId: int,destOffset: int,srcOffset: int,count: int,) -> None:
        """Copy SSBO data between buffers"""
        ...
def rlCubemapParameters(id: int,param: int,value: int,) -> None:
        """Set cubemap parameters (filter, wrap)"""
        ...
def rlDisableBackfaceCulling() -> None:
        """Disable backface culling"""
        ...
def rlDisableColorBlend() -> None:
        """Disable color blending"""
        ...
def rlDisableDepthMask() -> None:
        """Disable depth write"""
        ...
def rlDisableDepthTest() -> None:
        """Disable depth test"""
        ...
def rlDisableFramebuffer() -> None:
        """Disable render texture (fbo), return to default framebuffer"""
        ...
def rlDisableScissorTest() -> None:
        """Disable scissor test"""
        ...
def rlDisableShader() -> None:
        """Disable shader program"""
        ...
def rlDisableSmoothLines() -> None:
        """Disable line aliasing"""
        ...
def rlDisableStereoRender() -> None:
        """Disable stereo rendering"""
        ...
def rlDisableTexture() -> None:
        """Disable texture"""
        ...
def rlDisableTextureCubemap() -> None:
        """Disable texture cubemap"""
        ...
def rlDisableVertexArray() -> None:
        """Disable vertex array (VAO, if supported)"""
        ...
def rlDisableVertexAttribute(index: int,) -> None:
        """Disable vertex attribute index"""
        ...
def rlDisableVertexBuffer() -> None:
        """Disable vertex buffer (VBO)"""
        ...
def rlDisableVertexBufferElement() -> None:
        """Disable vertex buffer element (VBO element)"""
        ...
def rlDisableWireMode() -> None:
        """Disable wire mode ( and point ) maybe rename"""
        ...
def rlDrawRenderBatch(batch: Any,) -> None:
        """Draw render batch data (Update->Draw->Reset)"""
        ...
def rlDrawRenderBatchActive() -> None:
        """Update and draw internal render batch"""
        ...
def rlDrawVertexArray(offset: int,count: int,) -> None:
        """"""
        ...
def rlDrawVertexArrayElements(offset: int,count: int,buffer: Any,) -> None:
        """"""
        ...
def rlDrawVertexArrayElementsInstanced(offset: int,count: int,buffer: Any,instances: int,) -> None:
        """"""
        ...
def rlDrawVertexArrayInstanced(offset: int,count: int,instances: int,) -> None:
        """"""
        ...
def rlEnableBackfaceCulling() -> None:
        """Enable backface culling"""
        ...
def rlEnableColorBlend() -> None:
        """Enable color blending"""
        ...
def rlEnableDepthMask() -> None:
        """Enable depth write"""
        ...
def rlEnableDepthTest() -> None:
        """Enable depth test"""
        ...
def rlEnableFramebuffer(id: int,) -> None:
        """Enable render texture (fbo)"""
        ...
def rlEnablePointMode() -> None:
        """Enable point mode"""
        ...
def rlEnableScissorTest() -> None:
        """Enable scissor test"""
        ...
def rlEnableShader(id: int,) -> None:
        """Enable shader program"""
        ...
def rlEnableSmoothLines() -> None:
        """Enable line aliasing"""
        ...
def rlEnableStereoRender() -> None:
        """Enable stereo rendering"""
        ...
def rlEnableTexture(id: int,) -> None:
        """Enable texture"""
        ...
def rlEnableTextureCubemap(id: int,) -> None:
        """Enable texture cubemap"""
        ...
def rlEnableVertexArray(vaoId: int,) -> bool:
        """Enable vertex array (VAO, if supported)"""
        ...
def rlEnableVertexAttribute(index: int,) -> None:
        """Enable vertex attribute index"""
        ...
def rlEnableVertexBuffer(id: int,) -> None:
        """Enable vertex buffer (VBO)"""
        ...
def rlEnableVertexBufferElement(id: int,) -> None:
        """Enable vertex buffer element (VBO element)"""
        ...
def rlEnableWireMode() -> None:
        """Enable wire mode"""
        ...
def rlEnd() -> None:
        """Finish vertex providing"""
        ...
def rlFramebufferAttach(fboId: int,texId: int,attachType: int,texType: int,mipLevel: int,) -> None:
        """Attach texture/renderbuffer to a framebuffer"""
        ...
def rlFramebufferComplete(id: int,) -> bool:
        """Verify framebuffer is complete"""
        ...
def rlFrustum(left: float,right: float,bottom: float,top: float,znear: float,zfar: float,) -> None:
        """"""
        ...
def rlGenTextureMipmaps(id: int,width: int,height: int,format: int,mipmaps: Any,) -> None:
        """Generate mipmap data for selected texture"""
        ...
def rlGetFramebufferHeight() -> int:
        """Get default framebuffer height"""
        ...
def rlGetFramebufferWidth() -> int:
        """Get default framebuffer width"""
        ...
def rlGetGlTextureFormats(format: int,glInternalFormat: Any,glFormat: Any,glType: Any,) -> None:
        """Get OpenGL internal formats"""
        ...
def rlGetLineWidth() -> float:
        """Get the line drawing width"""
        ...
def rlGetLocationAttrib(shaderId: int,attribName: str,) -> int:
        """Get shader location attribute"""
        ...
def rlGetLocationUniform(shaderId: int,uniformName: str,) -> int:
        """Get shader location uniform"""
        ...
def rlGetMatrixModelview() -> Matrix:
        """Get internal modelview matrix"""
        ...
def rlGetMatrixProjection() -> Matrix:
        """Get internal projection matrix"""
        ...
def rlGetMatrixProjectionStereo(eye: int,) -> Matrix:
        """Get internal projection matrix for stereo render (selected eye)"""
        ...
def rlGetMatrixTransform() -> Matrix:
        """Get internal accumulated transform matrix"""
        ...
def rlGetMatrixViewOffsetStereo(eye: int,) -> Matrix:
        """Get internal view offset matrix for stereo render (selected eye)"""
        ...
def rlGetPixelFormatName(format: int,) -> str:
        """Get name string for pixel format"""
        ...
def rlGetShaderBufferSize(id: int,) -> int:
        """Get SSBO buffer size"""
        ...
def rlGetShaderIdDefault() -> int:
        """Get default shader id"""
        ...
def rlGetShaderLocsDefault() -> Any:
        """Get default shader locations"""
        ...
def rlGetTextureIdDefault() -> int:
        """Get default texture id"""
        ...
def rlGetVersion() -> int:
        """Get current OpenGL version"""
        ...
def rlIsStereoRenderEnabled() -> bool:
        """Check if stereo render is enabled"""
        ...
def rlLoadComputeShaderProgram(shaderId: int,) -> int:
        """Load compute shader program"""
        ...
def rlLoadDrawCube() -> None:
        """Load and draw a cube"""
        ...
def rlLoadDrawQuad() -> None:
        """Load and draw a quad"""
        ...
def rlLoadExtensions(loader: Any,) -> None:
        """Load OpenGL extensions (loader function required)"""
        ...
def rlLoadFramebuffer(width: int,height: int,) -> int:
        """Load an empty framebuffer"""
        ...
def rlLoadIdentity() -> None:
        """Reset current matrix to identity matrix"""
        ...
def rlLoadRenderBatch(numBuffers: int,bufferElements: int,) -> rlRenderBatch:
        """Load a render batch system"""
        ...
def rlLoadShaderBuffer(size: int,data: Any,usageHint: int,) -> int:
        """Load shader storage buffer object (SSBO)"""
        ...
def rlLoadShaderCode(vsCode: str,fsCode: str,) -> int:
        """Load shader from code strings"""
        ...
def rlLoadShaderProgram(vShaderId: int,fShaderId: int,) -> int:
        """Load custom shader program"""
        ...
def rlLoadTexture(data: Any,width: int,height: int,format: int,mipmapCount: int,) -> int:
        """Load texture in GPU"""
        ...
def rlLoadTextureCubemap(data: Any,size: int,format: int,) -> int:
        """Load texture cubemap"""
        ...
def rlLoadTextureDepth(width: int,height: int,useRenderBuffer: bool,) -> int:
        """Load depth texture/renderbuffer (to be attached to fbo)"""
        ...
def rlLoadVertexArray() -> int:
        """Load vertex array (vao) if supported"""
        ...
def rlLoadVertexBuffer(buffer: Any,size: int,dynamic: bool,) -> int:
        """Load a vertex buffer attribute"""
        ...
def rlLoadVertexBufferElement(buffer: Any,size: int,dynamic: bool,) -> int:
        """Load a new attributes element buffer"""
        ...
def rlMatrixMode(mode: int,) -> None:
        """Choose the current matrix to be transformed"""
        ...
def rlMultMatrixf(matf: Any,) -> None:
        """Multiply the current matrix by another matrix"""
        ...
def rlNormal3f(x: float,y: float,z: float,) -> None:
        """Define one vertex (normal) - 3 float"""
        ...
def rlOrtho(left: float,right: float,bottom: float,top: float,znear: float,zfar: float,) -> None:
        """"""
        ...
def rlPopMatrix() -> None:
        """Pop latest inserted matrix from stack"""
        ...
def rlPushMatrix() -> None:
        """Push the current matrix to stack"""
        ...
def rlReadScreenPixels(width: int,height: int,) -> str:
        """Read screen pixel data (color buffer)"""
        ...
def rlReadShaderBuffer(id: int,dest: Any,count: int,offset: int,) -> None:
        """Read SSBO buffer data (GPU->CPU)"""
        ...
def rlReadTexturePixels(id: int,width: int,height: int,format: int,) -> Any:
        """Read texture pixel data"""
        ...
def rlRotatef(angle: float,x: float,y: float,z: float,) -> None:
        """Multiply the current matrix by a rotation matrix"""
        ...
def rlScalef(x: float,y: float,z: float,) -> None:
        """Multiply the current matrix by a scaling matrix"""
        ...
def rlScissor(x: int,y: int,width: int,height: int,) -> None:
        """Scissor test"""
        ...
def rlSetBlendFactors(glSrcFactor: int,glDstFactor: int,glEquation: int,) -> None:
        """Set blending mode factor and equation (using OpenGL factors)"""
        ...
def rlSetBlendFactorsSeparate(glSrcRGB: int,glDstRGB: int,glSrcAlpha: int,glDstAlpha: int,glEqRGB: int,glEqAlpha: int,) -> None:
        """Set blending mode factors and equations separately (using OpenGL factors)"""
        ...
def rlSetBlendMode(mode: int,) -> None:
        """Set blending mode"""
        ...
def rlSetCullFace(mode: int,) -> None:
        """Set face culling mode"""
        ...
def rlSetFramebufferHeight(height: int,) -> None:
        """Set current framebuffer height"""
        ...
def rlSetFramebufferWidth(width: int,) -> None:
        """Set current framebuffer width"""
        ...
def rlSetLineWidth(width: float,) -> None:
        """Set the line drawing width"""
        ...
def rlSetMatrixModelview(view: Matrix,) -> None:
        """Set a custom modelview matrix (replaces internal modelview matrix)"""
        ...
def rlSetMatrixProjection(proj: Matrix,) -> None:
        """Set a custom projection matrix (replaces internal projection matrix)"""
        ...
def rlSetMatrixProjectionStereo(right: Matrix,left: Matrix,) -> None:
        """Set eyes projection matrices for stereo rendering"""
        ...
def rlSetMatrixViewOffsetStereo(right: Matrix,left: Matrix,) -> None:
        """Set eyes view offsets matrices for stereo rendering"""
        ...
def rlSetRenderBatchActive(batch: Any,) -> None:
        """Set the active render batch for rlgl (NULL for default internal)"""
        ...
def rlSetShader(id: int,locs: Any,) -> None:
        """Set shader currently active (id and locations)"""
        ...
def rlSetTexture(id: int,) -> None:
        """Set current texture for render batch and check buffers limits"""
        ...
def rlSetUniform(locIndex: int,value: Any,uniformType: int,count: int,) -> None:
        """Set shader value uniform"""
        ...
def rlSetUniformMatrix(locIndex: int,mat: Matrix,) -> None:
        """Set shader value matrix"""
        ...
def rlSetUniformSampler(locIndex: int,textureId: int,) -> None:
        """Set shader value sampler"""
        ...
def rlSetVertexAttribute(index: int,compSize: int,type: int,normalized: bool,stride: int,pointer: Any,) -> None:
        """"""
        ...
def rlSetVertexAttributeDefault(locIndex: int,value: Any,attribType: int,count: int,) -> None:
        """Set vertex attribute default value"""
        ...
def rlSetVertexAttributeDivisor(index: int,divisor: int,) -> None:
        """"""
        ...
def rlTexCoord2f(x: float,y: float,) -> None:
        """Define one vertex (texture coordinate) - 2 float"""
        ...
def rlTextureParameters(id: int,param: int,value: int,) -> None:
        """Set texture parameters (filter, wrap)"""
        ...
def rlTranslatef(x: float,y: float,z: float,) -> None:
        """Multiply the current matrix by a translation matrix"""
        ...
def rlUnloadFramebuffer(id: int,) -> None:
        """Delete framebuffer from GPU"""
        ...
def rlUnloadRenderBatch(batch: rlRenderBatch,) -> None:
        """Unload render batch system"""
        ...
def rlUnloadShaderBuffer(ssboId: int,) -> None:
        """Unload shader storage buffer object (SSBO)"""
        ...
def rlUnloadShaderProgram(id: int,) -> None:
        """Unload shader program"""
        ...
def rlUnloadTexture(id: int,) -> None:
        """Unload texture from GPU memory"""
        ...
def rlUnloadVertexArray(vaoId: int,) -> None:
        """"""
        ...
def rlUnloadVertexBuffer(vboId: int,) -> None:
        """"""
        ...
def rlUpdateShaderBuffer(id: int,data: Any,dataSize: int,offset: int,) -> None:
        """Update SSBO buffer data"""
        ...
def rlUpdateTexture(id: int,offsetX: int,offsetY: int,width: int,height: int,format: int,data: Any,) -> None:
        """Update GPU texture with new data"""
        ...
def rlUpdateVertexBuffer(bufferId: int,data: Any,dataSize: int,offset: int,) -> None:
        """Update GPU buffer with new data"""
        ...
def rlUpdateVertexBufferElements(id: int,data: Any,dataSize: int,offset: int,) -> None:
        """Update vertex buffer elements with new data"""
        ...
def rlVertex2f(x: float,y: float,) -> None:
        """Define one vertex (position) - 2 float"""
        ...
def rlVertex2i(x: int,y: int,) -> None:
        """Define one vertex (position) - 2 int"""
        ...
def rlVertex3f(x: float,y: float,z: float,) -> None:
        """Define one vertex (position) - 3 float"""
        ...
def rlViewport(x: int,y: int,width: int,height: int,) -> None:
        """Set the viewport area"""
        ...
def rlglClose() -> None:
        """De-initialize rlgl (buffers, shaders, textures)"""
        ...
def rlglInit(width: int,height: int,) -> None:
        """Initialize rlgl (buffers, shaders, textures, states)"""
        ...
AudioStream: struct
AutomationEvent: struct
AutomationEventList: struct
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
FilePathList: struct
Font: struct
FontType: int
GLFWallocator: struct
GLFWcursor: struct
GLFWgamepadstate: struct
GLFWgammaramp: struct
GLFWimage: struct
GLFWmonitor: struct
GLFWvidmode: struct
GLFWwindow: struct
GamepadAxis: int
GamepadButton: int
Gesture: int
GlyphInfo: struct
GuiCheckBoxProperty: int
GuiColorPickerProperty: int
GuiComboBoxProperty: int
GuiControl: int
GuiControlProperty: int
GuiDefaultProperty: int
GuiDropdownBoxProperty: int
GuiIconName: int
GuiListViewProperty: int
GuiProgressBarProperty: int
GuiScrollBarProperty: int
GuiSliderProperty: int
GuiSpinnerProperty: int
GuiState: int
GuiStyleProp: struct
GuiTextAlignment: int
GuiTextAlignmentVertical: int
GuiTextBoxProperty: int
GuiTextWrapMode: int
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
float16: struct
float3: struct
rAudioBuffer: struct
rAudioProcessor: struct
rlBlendMode: int
rlCullMode: int
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
#  Copyright (c) 2021 Richard Smith and others
#
#  This program and the accompanying materials are made available under the
#  terms of the Eclipse Public License 2.0 which is available at
#  http://www.eclipse.org/legal/epl-2.0.
#
#  This Source Code may also be made available under the following Secondary
#  licenses when the conditions for such availability set forth in the Eclipse
#  Public License, v. 2.0 are satisfied: GNU General Public License, version 2
#  with the GNU Classpath Exception which is
#  available at https://www.gnu.org/software/classpath/license.html.
#
#  SPDX-License-Identifier: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0

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


from typing import Any
from warnings import deprecated
import _cffi_backend # type: ignore

ffi: _cffi_backend.FFI
rl: _cffi_backend.Lib
PhysicsShapeType = int

class struct: ...


ARROWS_SIZE: int
ARROWS_VISIBLE: int
ARROW_PADDING: int
def AttachAudioMixedProcessor(processor: Any,) -> None:
    """Attach audio stream processor to the entire audio pipeline, receives the samples as 'float'."""
    ...
def AttachAudioStreamProcessor(stream: AudioStream|list|tuple,processor: Any,) -> None:
    """Attach audio stream processor to stream, receives the samples as 'float'."""
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
    """Begin blending mode (alpha, additive, multiplied, subtract, custom)."""
    ...
def BeginDrawing() -> None:
    """Setup canvas (framebuffer) to start drawing."""
    ...
def BeginMode2D(camera: Camera2D|list|tuple,) -> None:
    """Begin 2D mode with custom camera (2D)."""
    ...
def BeginMode3D(camera: Camera3D|list|tuple,) -> None:
    """Begin 3D mode with custom camera (3D)."""
    ...
def BeginScissorMode(x: int,y: int,width: int,height: int,) -> None:
    """Begin scissor mode (define screen area for following drawing)."""
    ...
def BeginShaderMode(shader: Shader|list|tuple,) -> None:
    """Begin custom shader drawing."""
    ...
def BeginTextureMode(target: RenderTexture|list|tuple,) -> None:
    """Begin drawing to render texture."""
    ...
def BeginVrStereoMode(config: VrStereoConfig|list|tuple,) -> None:
    """Begin stereo rendering (requires VR simulator)."""
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
def ChangeDirectory(dir: bytes,) -> bool:
    """Change working directory, return true on success."""
    ...
def CheckCollisionBoxSphere(box: BoundingBox|list|tuple,center: Vector3|list|tuple,radius: float,) -> bool:
    """Check collision between box and sphere."""
    ...
def CheckCollisionBoxes(box1: BoundingBox|list|tuple,box2: BoundingBox|list|tuple,) -> bool:
    """Check collision between two bounding boxes."""
    ...
def CheckCollisionCircleLine(center: Vector2|list|tuple,radius: float,p1: Vector2|list|tuple,p2: Vector2|list|tuple,) -> bool:
    """Check if circle collides with a line created betweeen two points [p1] and [p2]."""
    ...
def CheckCollisionCircleRec(center: Vector2|list|tuple,radius: float,rec: Rectangle|list|tuple,) -> bool:
    """Check collision between circle and rectangle."""
    ...
def CheckCollisionCircles(center1: Vector2|list|tuple,radius1: float,center2: Vector2|list|tuple,radius2: float,) -> bool:
    """Check collision between two circles."""
    ...
def CheckCollisionLines(startPos1: Vector2|list|tuple,endPos1: Vector2|list|tuple,startPos2: Vector2|list|tuple,endPos2: Vector2|list|tuple,collisionPoint: Any|list|tuple,) -> bool:
    """Check the collision between two lines defined by two points each, returns collision point by reference."""
    ...
def CheckCollisionPointCircle(point: Vector2|list|tuple,center: Vector2|list|tuple,radius: float,) -> bool:
    """Check if point is inside circle."""
    ...
def CheckCollisionPointLine(point: Vector2|list|tuple,p1: Vector2|list|tuple,p2: Vector2|list|tuple,threshold: int,) -> bool:
    """Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]."""
    ...
def CheckCollisionPointPoly(point: Vector2|list|tuple,points: Any|list|tuple,pointCount: int,) -> bool:
    """Check if point is within a polygon described by array of vertices."""
    ...
def CheckCollisionPointRec(point: Vector2|list|tuple,rec: Rectangle|list|tuple,) -> bool:
    """Check if point is inside rectangle."""
    ...
def CheckCollisionPointTriangle(point: Vector2|list|tuple,p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,) -> bool:
    """Check if point is inside a triangle."""
    ...
def CheckCollisionRecs(rec1: Rectangle|list|tuple,rec2: Rectangle|list|tuple,) -> bool:
    """Check collision between two rectangles."""
    ...
def CheckCollisionSpheres(center1: Vector3|list|tuple,radius1: float,center2: Vector3|list|tuple,radius2: float,) -> bool:
    """Check collision between two spheres."""
    ...
def Clamp(value: float,min_1: float,max_2: float,) -> float:
    """."""
    ...
def ClearBackground(color: Color|list|tuple,) -> None:
    """Set background color (framebuffer clear color)."""
    ...
def ClearWindowState(flags: int,) -> None:
    """Clear window configuration state flags."""
    ...
def CloseAudioDevice() -> None:
    """Close the audio device and context."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def ClosePhysics() -> None:
    """Unitializes physics pointers and closes physics loop thread."""
    ...
def CloseWindow() -> None:
    """Close window and unload OpenGL context."""
    ...
def CodepointToUTF8(codepoint: int,utf8Size: Any,) -> bytes:
    """Encode one codepoint into UTF-8 byte array (array length returned as parameter)."""
    ...
def ColorAlpha(color: Color|list|tuple,alpha: float,) -> Color:
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f."""
    ...
def ColorAlphaBlend(dst: Color|list|tuple,src: Color|list|tuple,tint: Color|list|tuple,) -> Color:
    """Get src alpha-blended into dst color with tint."""
    ...
def ColorBrightness(color: Color|list|tuple,factor: float,) -> Color:
    """Get color with brightness correction, brightness factor goes from -1.0f to 1.0f."""
    ...
def ColorContrast(color: Color|list|tuple,contrast: float,) -> Color:
    """Get color with contrast correction, contrast values between -1.0f and 1.0f."""
    ...
def ColorFromHSV(hue: float,saturation: float,value: float,) -> Color:
    """Get a Color from HSV values, hue [0..360], saturation/value [0..1]."""
    ...
def ColorFromNormalized(normalized: Vector4|list|tuple,) -> Color:
    """Get Color from normalized values [0..1]."""
    ...
def ColorIsEqual(col1: Color|list|tuple,col2: Color|list|tuple,) -> bool:
    """Check if two colors are equal."""
    ...
def ColorLerp(color1: Color|list|tuple,color2: Color|list|tuple,factor: float,) -> Color:
    """Get color lerp interpolation between two colors, factor [0.0f..1.0f]."""
    ...
def ColorNormalize(color: Color|list|tuple,) -> Vector4:
    """Get Color normalized as float [0..1]."""
    ...
def ColorTint(color: Color|list|tuple,tint: Color|list|tuple,) -> Color:
    """Get color multiplied with another color."""
    ...
def ColorToHSV(color: Color|list|tuple,) -> Vector3:
    """Get HSV values for a Color, hue [0..360], saturation/value [0..1]."""
    ...
def ColorToInt(color: Color|list|tuple,) -> int:
    """Get hexadecimal value for a Color (0xRRGGBBAA)."""
    ...
def CompressData(data: bytes,dataSize: int,compDataSize: Any,) -> bytes:
    """Compress data (DEFLATE algorithm), memory must be MemFree()."""
    ...
def ComputeCRC32(data: bytes,dataSize: int,) -> int:
    """Compute CRC32 hash code."""
    ...
def ComputeMD5(data: bytes,dataSize: int,) -> Any:
    """Compute MD5 hash code, returns static int[4] (16 bytes)."""
    ...
def ComputeSHA1(data: bytes,dataSize: int,) -> Any:
    """Compute SHA1 hash code, returns static int[5] (20 bytes)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def CreatePhysicsBodyCircle(pos: Vector2|list|tuple,radius: float,density: float,) -> Any:
    """Creates a new circle physics body with generic parameters."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def CreatePhysicsBodyPolygon(pos: Vector2|list|tuple,radius: float,sides: int,density: float,) -> Any:
    """Creates a new polygon physics body with generic parameters."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def CreatePhysicsBodyRectangle(pos: Vector2|list|tuple,width: float,height: float,density: float,) -> Any:
    """Creates a new rectangle physics body with generic parameters."""
    ...
DEFAULT: int
DROPDOWNBOX: int
DROPDOWN_ARROW_HIDDEN: int
DROPDOWN_ITEMS_SPACING: int
DROPDOWN_ROLL_UP: int
def DecodeDataBase64(data: bytes,outputSize: Any,) -> bytes:
    """Decode Base64 string data, memory must be MemFree()."""
    ...
def DecompressData(compData: bytes,compDataSize: int,dataSize: Any,) -> bytes:
    """Decompress data (DEFLATE algorithm), memory must be MemFree()."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def DestroyPhysicsBody(body: Any|list|tuple,) -> None:
    """Unitializes and destroy a physics body."""
    ...
def DetachAudioMixedProcessor(processor: Any,) -> None:
    """Detach audio stream processor from the entire audio pipeline."""
    ...
def DetachAudioStreamProcessor(stream: AudioStream|list|tuple,processor: Any,) -> None:
    """Detach audio stream processor from stream."""
    ...
def DirectoryExists(dirPath: bytes,) -> bool:
    """Check if a directory path exists."""
    ...
def DisableCursor() -> None:
    """Disables cursor (lock cursor)."""
    ...
def DisableEventWaiting() -> None:
    """Disable waiting for events on EndDrawing(), automatic events polling."""
    ...
def DrawBillboard(camera: Camera3D|list|tuple,texture: Texture|list|tuple,position: Vector3|list|tuple,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a billboard texture."""
    ...
def DrawBillboardPro(camera: Camera3D|list|tuple,texture: Texture|list|tuple,source: Rectangle|list|tuple,position: Vector3|list|tuple,up: Vector3|list|tuple,size: Vector2|list|tuple,origin: Vector2|list|tuple,rotation: float,tint: Color|list|tuple,) -> None:
    """Draw a billboard texture defined by source and rotation."""
    ...
def DrawBillboardRec(camera: Camera3D|list|tuple,texture: Texture|list|tuple,source: Rectangle|list|tuple,position: Vector3|list|tuple,size: Vector2|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a billboard texture defined by source."""
    ...
def DrawBoundingBox(box: BoundingBox|list|tuple,color: Color|list|tuple,) -> None:
    """Draw bounding box (wires)."""
    ...
def DrawCapsule(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,radius: float,slices: int,rings: int,color: Color|list|tuple,) -> None:
    """Draw a capsule with the center of its sphere caps at startPos and endPos."""
    ...
def DrawCapsuleWires(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,radius: float,slices: int,rings: int,color: Color|list|tuple,) -> None:
    """Draw capsule wireframe with the center of its sphere caps at startPos and endPos."""
    ...
def DrawCircle(centerX: int,centerY: int,radius: float,color: Color|list|tuple,) -> None:
    """Draw a color-filled circle."""
    ...
def DrawCircle3D(center: Vector3|list|tuple,radius: float,rotationAxis: Vector3|list|tuple,rotationAngle: float,color: Color|list|tuple,) -> None:
    """Draw a circle in 3D world space."""
    ...
def DrawCircleGradient(centerX: int,centerY: int,radius: float,inner: Color|list|tuple,outer: Color|list|tuple,) -> None:
    """Draw a gradient-filled circle."""
    ...
def DrawCircleLines(centerX: int,centerY: int,radius: float,color: Color|list|tuple,) -> None:
    """Draw circle outline."""
    ...
def DrawCircleLinesV(center: Vector2|list|tuple,radius: float,color: Color|list|tuple,) -> None:
    """Draw circle outline (Vector version)."""
    ...
def DrawCircleSector(center: Vector2|list|tuple,radius: float,startAngle: float,endAngle: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw a piece of a circle."""
    ...
def DrawCircleSectorLines(center: Vector2|list|tuple,radius: float,startAngle: float,endAngle: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw circle sector outline."""
    ...
def DrawCircleV(center: Vector2|list|tuple,radius: float,color: Color|list|tuple,) -> None:
    """Draw a color-filled circle (Vector version)."""
    ...
def DrawCube(position: Vector3|list|tuple,width: float,height: float,length: float,color: Color|list|tuple,) -> None:
    """Draw cube."""
    ...
def DrawCubeV(position: Vector3|list|tuple,size: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw cube (Vector version)."""
    ...
def DrawCubeWires(position: Vector3|list|tuple,width: float,height: float,length: float,color: Color|list|tuple,) -> None:
    """Draw cube wires."""
    ...
def DrawCubeWiresV(position: Vector3|list|tuple,size: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw cube wires (Vector version)."""
    ...
def DrawCylinder(position: Vector3|list|tuple,radiusTop: float,radiusBottom: float,height: float,slices: int,color: Color|list|tuple,) -> None:
    """Draw a cylinder/cone."""
    ...
def DrawCylinderEx(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,startRadius: float,endRadius: float,sides: int,color: Color|list|tuple,) -> None:
    """Draw a cylinder with base at startPos and top at endPos."""
    ...
def DrawCylinderWires(position: Vector3|list|tuple,radiusTop: float,radiusBottom: float,height: float,slices: int,color: Color|list|tuple,) -> None:
    """Draw a cylinder/cone wires."""
    ...
def DrawCylinderWiresEx(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,startRadius: float,endRadius: float,sides: int,color: Color|list|tuple,) -> None:
    """Draw a cylinder wires with base at startPos and top at endPos."""
    ...
def DrawEllipse(centerX: int,centerY: int,radiusH: float,radiusV: float,color: Color|list|tuple,) -> None:
    """Draw ellipse."""
    ...
def DrawEllipseLines(centerX: int,centerY: int,radiusH: float,radiusV: float,color: Color|list|tuple,) -> None:
    """Draw ellipse outline."""
    ...
def DrawFPS(posX: int,posY: int,) -> None:
    """Draw current FPS."""
    ...
def DrawGrid(slices: int,spacing: float,) -> None:
    """Draw a grid (centered at (0, 0, 0))."""
    ...
def DrawLine(startPosX: int,startPosY: int,endPosX: int,endPosY: int,color: Color|list|tuple,) -> None:
    """Draw a line."""
    ...
def DrawLine3D(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a line in 3D world space."""
    ...
def DrawLineBezier(startPos: Vector2|list|tuple,endPos: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw line segment cubic-bezier in-out interpolation."""
    ...
def DrawLineEx(startPos: Vector2|list|tuple,endPos: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw a line (using triangles/quads)."""
    ...
def DrawLineStrip(points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw lines sequence (using gl lines)."""
    ...
def DrawLineV(startPos: Vector2|list|tuple,endPos: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a line (using gl lines)."""
    ...
def DrawMesh(mesh: Mesh|list|tuple,material: Material|list|tuple,transform: Matrix|list|tuple,) -> None:
    """Draw a 3d mesh with material and transform."""
    ...
def DrawMeshInstanced(mesh: Mesh|list|tuple,material: Material|list|tuple,transforms: Any|list|tuple,instances: int,) -> None:
    """Draw multiple mesh instances with material and different transforms."""
    ...
def DrawModel(model: Model|list|tuple,position: Vector3|list|tuple,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a model (with texture if set)."""
    ...
def DrawModelEx(model: Model|list|tuple,position: Vector3|list|tuple,rotationAxis: Vector3|list|tuple,rotationAngle: float,scale: Vector3|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a model with extended parameters."""
    ...
def DrawModelPoints(model: Model|list|tuple,position: Vector3|list|tuple,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a model as points."""
    ...
def DrawModelPointsEx(model: Model|list|tuple,position: Vector3|list|tuple,rotationAxis: Vector3|list|tuple,rotationAngle: float,scale: Vector3|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a model as points with extended parameters."""
    ...
def DrawModelWires(model: Model|list|tuple,position: Vector3|list|tuple,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a model wires (with texture if set)."""
    ...
def DrawModelWiresEx(model: Model|list|tuple,position: Vector3|list|tuple,rotationAxis: Vector3|list|tuple,rotationAngle: float,scale: Vector3|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a model wires (with texture if set) with extended parameters."""
    ...
def DrawPixel(posX: int,posY: int,color: Color|list|tuple,) -> None:
    """Draw a pixel using geometry [Can be slow, use with care]."""
    ...
def DrawPixelV(position: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a pixel using geometry (Vector version) [Can be slow, use with care]."""
    ...
def DrawPlane(centerPos: Vector3|list|tuple,size: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a plane XZ."""
    ...
def DrawPoint3D(position: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a point in 3D space, actually a small line."""
    ...
def DrawPoly(center: Vector2|list|tuple,sides: int,radius: float,rotation: float,color: Color|list|tuple,) -> None:
    """Draw a regular polygon (Vector version)."""
    ...
def DrawPolyLines(center: Vector2|list|tuple,sides: int,radius: float,rotation: float,color: Color|list|tuple,) -> None:
    """Draw a polygon outline of n sides."""
    ...
def DrawPolyLinesEx(center: Vector2|list|tuple,sides: int,radius: float,rotation: float,lineThick: float,color: Color|list|tuple,) -> None:
    """Draw a polygon outline of n sides with extended parameters."""
    ...
def DrawRay(ray: Ray|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a ray line."""
    ...
def DrawRectangle(posX: int,posY: int,width: int,height: int,color: Color|list|tuple,) -> None:
    """Draw a color-filled rectangle."""
    ...
def DrawRectangleGradientEx(rec: Rectangle|list|tuple,topLeft: Color|list|tuple,bottomLeft: Color|list|tuple,topRight: Color|list|tuple,bottomRight: Color|list|tuple,) -> None:
    """Draw a gradient-filled rectangle with custom vertex colors."""
    ...
def DrawRectangleGradientH(posX: int,posY: int,width: int,height: int,left: Color|list|tuple,right: Color|list|tuple,) -> None:
    """Draw a horizontal-gradient-filled rectangle."""
    ...
def DrawRectangleGradientV(posX: int,posY: int,width: int,height: int,top: Color|list|tuple,bottom: Color|list|tuple,) -> None:
    """Draw a vertical-gradient-filled rectangle."""
    ...
def DrawRectangleLines(posX: int,posY: int,width: int,height: int,color: Color|list|tuple,) -> None:
    """Draw rectangle outline."""
    ...
def DrawRectangleLinesEx(rec: Rectangle|list|tuple,lineThick: float,color: Color|list|tuple,) -> None:
    """Draw rectangle outline with extended parameters."""
    ...
def DrawRectanglePro(rec: Rectangle|list|tuple,origin: Vector2|list|tuple,rotation: float,color: Color|list|tuple,) -> None:
    """Draw a color-filled rectangle with pro parameters."""
    ...
def DrawRectangleRec(rec: Rectangle|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a color-filled rectangle."""
    ...
def DrawRectangleRounded(rec: Rectangle|list|tuple,roundness: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw rectangle with rounded edges."""
    ...
def DrawRectangleRoundedLines(rec: Rectangle|list|tuple,roundness: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw rectangle lines with rounded edges."""
    ...
def DrawRectangleRoundedLinesEx(rec: Rectangle|list|tuple,roundness: float,segments: int,lineThick: float,color: Color|list|tuple,) -> None:
    """Draw rectangle with rounded edges outline."""
    ...
def DrawRectangleV(position: Vector2|list|tuple,size: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a color-filled rectangle (Vector version)."""
    ...
def DrawRing(center: Vector2|list|tuple,innerRadius: float,outerRadius: float,startAngle: float,endAngle: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw ring."""
    ...
def DrawRingLines(center: Vector2|list|tuple,innerRadius: float,outerRadius: float,startAngle: float,endAngle: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw ring outline."""
    ...
def DrawSphere(centerPos: Vector3|list|tuple,radius: float,color: Color|list|tuple,) -> None:
    """Draw sphere."""
    ...
def DrawSphereEx(centerPos: Vector3|list|tuple,radius: float,rings: int,slices: int,color: Color|list|tuple,) -> None:
    """Draw sphere with extended parameters."""
    ...
def DrawSphereWires(centerPos: Vector3|list|tuple,radius: float,rings: int,slices: int,color: Color|list|tuple,) -> None:
    """Draw sphere wires."""
    ...
def DrawSplineBasis(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: B-Spline, minimum 4 points."""
    ...
def DrawSplineBezierCubic(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: Cubic Bezier, minimum 4 points (2 control points): [p1, c2, c3, p4, c5, c6...]."""
    ...
def DrawSplineBezierQuadratic(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: Quadratic Bezier, minimum 3 points (1 control point): [p1, c2, p3, c4...]."""
    ...
def DrawSplineCatmullRom(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: Catmull-Rom, minimum 4 points."""
    ...
def DrawSplineLinear(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: Linear, minimum 2 points."""
    ...
def DrawSplineSegmentBasis(p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,p4: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: B-Spline, 4 points."""
    ...
def DrawSplineSegmentBezierCubic(p1: Vector2|list|tuple,c2: Vector2|list|tuple,c3: Vector2|list|tuple,p4: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: Cubic Bezier, 2 points, 2 control points."""
    ...
def DrawSplineSegmentBezierQuadratic(p1: Vector2|list|tuple,c2: Vector2|list|tuple,p3: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: Quadratic Bezier, 2 points, 1 control point."""
    ...
def DrawSplineSegmentCatmullRom(p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,p4: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: Catmull-Rom, 4 points."""
    ...
def DrawSplineSegmentLinear(p1: Vector2|list|tuple,p2: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: Linear, 2 points."""
    ...
def DrawText(text: bytes,posX: int,posY: int,fontSize: int,color: Color|list|tuple,) -> None:
    """Draw text (using default font)."""
    ...
def DrawTextCodepoint(font: Font|list|tuple,codepoint: int,position: Vector2|list|tuple,fontSize: float,tint: Color|list|tuple,) -> None:
    """Draw one character (codepoint)."""
    ...
def DrawTextCodepoints(font: Font|list|tuple,codepoints: Any,codepointCount: int,position: Vector2|list|tuple,fontSize: float,spacing: float,tint: Color|list|tuple,) -> None:
    """Draw multiple character (codepoint)."""
    ...
def DrawTextEx(font: Font|list|tuple,text: bytes,position: Vector2|list|tuple,fontSize: float,spacing: float,tint: Color|list|tuple,) -> None:
    """Draw text using font and additional parameters."""
    ...
def DrawTextPro(font: Font|list|tuple,text: bytes,position: Vector2|list|tuple,origin: Vector2|list|tuple,rotation: float,fontSize: float,spacing: float,tint: Color|list|tuple,) -> None:
    """Draw text using Font and pro parameters (rotation)."""
    ...
def DrawTexture(texture: Texture|list|tuple,posX: int,posY: int,tint: Color|list|tuple,) -> None:
    """Draw a Texture2D."""
    ...
def DrawTextureEx(texture: Texture|list|tuple,position: Vector2|list|tuple,rotation: float,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a Texture2D with extended parameters."""
    ...
def DrawTextureNPatch(texture: Texture|list|tuple,nPatchInfo: NPatchInfo|list|tuple,dest: Rectangle|list|tuple,origin: Vector2|list|tuple,rotation: float,tint: Color|list|tuple,) -> None:
    """Draws a texture (or part of it) that stretches or shrinks nicely."""
    ...
def DrawTexturePro(texture: Texture|list|tuple,source: Rectangle|list|tuple,dest: Rectangle|list|tuple,origin: Vector2|list|tuple,rotation: float,tint: Color|list|tuple,) -> None:
    """Draw a part of a texture defined by a rectangle with 'pro' parameters."""
    ...
def DrawTextureRec(texture: Texture|list|tuple,source: Rectangle|list|tuple,position: Vector2|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a part of a texture defined by a rectangle."""
    ...
def DrawTextureV(texture: Texture|list|tuple,position: Vector2|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a Texture2D with position defined as Vector2."""
    ...
def DrawTriangle(v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a color-filled triangle (vertex in counter-clockwise order!)."""
    ...
def DrawTriangle3D(v1: Vector3|list|tuple,v2: Vector3|list|tuple,v3: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a color-filled triangle (vertex in counter-clockwise order!)."""
    ...
def DrawTriangleFan(points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle fan defined by points (first vertex is the center)."""
    ...
def DrawTriangleLines(v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw triangle outline (vertex in counter-clockwise order!)."""
    ...
def DrawTriangleStrip(points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle strip defined by points."""
    ...
def DrawTriangleStrip3D(points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle strip defined by points."""
    ...
def EnableCursor() -> None:
    """Enables cursor (unlock cursor)."""
    ...
def EnableEventWaiting() -> None:
    """Enable waiting for events on EndDrawing(), no automatic event polling."""
    ...
def EncodeDataBase64(data: bytes,dataSize: int,outputSize: Any,) -> bytes:
    """Encode data to Base64 string, memory must be MemFree()."""
    ...
def EndBlendMode() -> None:
    """End blending mode (reset to default: alpha blending)."""
    ...
def EndDrawing() -> None:
    """End canvas drawing and swap buffers (double buffering)."""
    ...
def EndMode2D() -> None:
    """Ends 2D mode with custom camera."""
    ...
def EndMode3D() -> None:
    """Ends 3D mode and returns to default 2D orthographic mode."""
    ...
def EndScissorMode() -> None:
    """End scissor mode."""
    ...
def EndShaderMode() -> None:
    """End custom shader drawing (use default shader)."""
    ...
def EndTextureMode() -> None:
    """Ends drawing to render texture."""
    ...
def EndVrStereoMode() -> None:
    """End stereo rendering (requires VR simulator)."""
    ...
def ExportAutomationEventList(list_0: AutomationEventList|list|tuple,fileName: bytes,) -> bool:
    """Export automation events list as text file."""
    ...
def ExportDataAsCode(data: bytes,dataSize: int,fileName: bytes,) -> bool:
    """Export data to code (.h), returns true on success."""
    ...
def ExportFontAsCode(font: Font|list|tuple,fileName: bytes,) -> bool:
    """Export font as code file, returns true on success."""
    ...
def ExportImage(image: Image|list|tuple,fileName: bytes,) -> bool:
    """Export image data to file, returns true on success."""
    ...
def ExportImageAsCode(image: Image|list|tuple,fileName: bytes,) -> bool:
    """Export image as code file defining an array of bytes, returns true on success."""
    ...
def ExportImageToMemory(image: Image|list|tuple,fileType: bytes,fileSize: Any,) -> bytes:
    """Export image to memory buffer."""
    ...
def ExportMesh(mesh: Mesh|list|tuple,fileName: bytes,) -> bool:
    """Export mesh data to file, returns true on success."""
    ...
def ExportMeshAsCode(mesh: Mesh|list|tuple,fileName: bytes,) -> bool:
    """Export mesh as code file (.h) defining multiple arrays of vertex attributes."""
    ...
def ExportWave(wave: Wave|list|tuple,fileName: bytes,) -> bool:
    """Export wave data to file, returns true on success."""
    ...
def ExportWaveAsCode(wave: Wave|list|tuple,fileName: bytes,) -> bool:
    """Export wave sample data to code (.h), returns true on success."""
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
def Fade(color: Color|list|tuple,alpha: float,) -> Color:
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f."""
    ...
def FileExists(fileName: bytes,) -> bool:
    """Check if file exists."""
    ...
def FloatEquals(x: float,y: float,) -> int:
    """."""
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
    """Generate image: cellular algorithm, bigger tileSize means bigger cells."""
    ...
def GenImageChecked(width: int,height: int,checksX: int,checksY: int,col1: Color|list|tuple,col2: Color|list|tuple,) -> Image:
    """Generate image: checked."""
    ...
def GenImageColor(width: int,height: int,color: Color|list|tuple,) -> Image:
    """Generate image: plain color."""
    ...
def GenImageFontAtlas(glyphs: Any|list|tuple,glyphRecs: Any|list|tuple,glyphCount: int,fontSize: int,padding: int,packMethod: int,) -> Image:
    """Generate image font atlas using chars info."""
    ...
def GenImageGradientLinear(width: int,height: int,direction: int,start: Color|list|tuple,end: Color|list|tuple,) -> Image:
    """Generate image: linear gradient, direction in degrees [0..360], 0=Vertical gradient."""
    ...
def GenImageGradientRadial(width: int,height: int,density: float,inner: Color|list|tuple,outer: Color|list|tuple,) -> Image:
    """Generate image: radial gradient."""
    ...
def GenImageGradientSquare(width: int,height: int,density: float,inner: Color|list|tuple,outer: Color|list|tuple,) -> Image:
    """Generate image: square gradient."""
    ...
def GenImagePerlinNoise(width: int,height: int,offsetX: int,offsetY: int,scale: float,) -> Image:
    """Generate image: perlin noise."""
    ...
def GenImageText(width: int,height: int,text: bytes,) -> Image:
    """Generate image: grayscale image from text data."""
    ...
def GenImageWhiteNoise(width: int,height: int,factor: float,) -> Image:
    """Generate image: white noise."""
    ...
def GenMeshCone(radius: float,height: float,slices: int,) -> Mesh:
    """Generate cone/pyramid mesh."""
    ...
def GenMeshCube(width: float,height: float,length: float,) -> Mesh:
    """Generate cuboid mesh."""
    ...
def GenMeshCubicmap(cubicmap: Image|list|tuple,cubeSize: Vector3|list|tuple,) -> Mesh:
    """Generate cubes-based map mesh from image data."""
    ...
def GenMeshCylinder(radius: float,height: float,slices: int,) -> Mesh:
    """Generate cylinder mesh."""
    ...
def GenMeshHeightmap(heightmap: Image|list|tuple,size: Vector3|list|tuple,) -> Mesh:
    """Generate heightmap mesh from image data."""
    ...
def GenMeshHemiSphere(radius: float,rings: int,slices: int,) -> Mesh:
    """Generate half-sphere mesh (no bottom cap)."""
    ...
def GenMeshKnot(radius: float,size: float,radSeg: int,sides: int,) -> Mesh:
    """Generate trefoil knot mesh."""
    ...
def GenMeshPlane(width: float,length: float,resX: int,resZ: int,) -> Mesh:
    """Generate plane mesh (with subdivisions)."""
    ...
def GenMeshPoly(sides: int,radius: float,) -> Mesh:
    """Generate polygonal mesh."""
    ...
def GenMeshSphere(radius: float,rings: int,slices: int,) -> Mesh:
    """Generate sphere mesh (standard sphere)."""
    ...
def GenMeshTangents(mesh: Any|list|tuple,) -> None:
    """Compute mesh tangents."""
    ...
def GenMeshTorus(radius: float,size: float,radSeg: int,sides: int,) -> Mesh:
    """Generate torus mesh."""
    ...
def GenTextureMipmaps(texture: Any|list|tuple,) -> None:
    """Generate GPU mipmaps for a texture."""
    ...
def GetApplicationDirectory() -> bytes:
    """Get the directory of the running application (uses static string)."""
    ...
def GetCameraMatrix(camera: Camera3D|list|tuple,) -> Matrix:
    """Get camera transform matrix (view matrix)."""
    ...
def GetCameraMatrix2D(camera: Camera2D|list|tuple,) -> Matrix:
    """Get camera 2d transform matrix."""
    ...
def GetCharPressed() -> int:
    """Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty."""
    ...
def GetClipboardImage() -> Image:
    """Get clipboard image content."""
    ...
def GetClipboardText() -> bytes:
    """Get clipboard text content."""
    ...
def GetCodepoint(text: bytes,codepointSize: Any,) -> int:
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure."""
    ...
def GetCodepointCount(text: bytes,) -> int:
    """Get total number of codepoints in a UTF-8 encoded string."""
    ...
def GetCodepointNext(text: bytes,codepointSize: Any,) -> int:
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure."""
    ...
def GetCodepointPrevious(text: bytes,codepointSize: Any,) -> int:
    """Get previous codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure."""
    ...
def GetCollisionRec(rec1: Rectangle|list|tuple,rec2: Rectangle|list|tuple,) -> Rectangle:
    """Get collision rectangle for two rectangles collision."""
    ...
def GetColor(hexValue: int,) -> Color:
    """Get Color structure from hexadecimal value."""
    ...
def GetCurrentMonitor() -> int:
    """Get current monitor where window is placed."""
    ...
def GetDirectoryPath(filePath: bytes,) -> bytes:
    """Get full path for a given fileName with path (uses static string)."""
    ...
def GetFPS() -> int:
    """Get current FPS."""
    ...
def GetFileExtension(fileName: bytes,) -> bytes:
    """Get pointer to extension for a filename string (includes dot: '.png')."""
    ...
def GetFileLength(fileName: bytes,) -> int:
    """Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)."""
    ...
def GetFileModTime(fileName: bytes,) -> int:
    """Get file modification time (last write time)."""
    ...
def GetFileName(filePath: bytes,) -> bytes:
    """Get pointer to filename for a path string."""
    ...
def GetFileNameWithoutExt(filePath: bytes,) -> bytes:
    """Get filename string without extension (uses static string)."""
    ...
def GetFontDefault() -> Font:
    """Get the default Font."""
    ...
def GetFrameTime() -> float:
    """Get time in seconds for last frame drawn (delta time)."""
    ...
def GetGamepadAxisCount(gamepad: int,) -> int:
    """Get gamepad axis count for a gamepad."""
    ...
def GetGamepadAxisMovement(gamepad: int,axis: int,) -> float:
    """Get axis movement value for a gamepad axis."""
    ...
def GetGamepadButtonPressed() -> int:
    """Get the last gamepad button pressed."""
    ...
def GetGamepadName(gamepad: int,) -> bytes:
    """Get gamepad internal name id."""
    ...
def GetGestureDetected() -> int:
    """Get latest detected gesture."""
    ...
def GetGestureDragAngle() -> float:
    """Get gesture drag angle."""
    ...
def GetGestureDragVector() -> Vector2:
    """Get gesture drag vector."""
    ...
def GetGestureHoldDuration() -> float:
    """Get gesture hold time in seconds."""
    ...
def GetGesturePinchAngle() -> float:
    """Get gesture pinch angle."""
    ...
def GetGesturePinchVector() -> Vector2:
    """Get gesture pinch delta."""
    ...
def GetGlyphAtlasRec(font: Font|list|tuple,codepoint: int,) -> Rectangle:
    """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found."""
    ...
def GetGlyphIndex(font: Font|list|tuple,codepoint: int,) -> int:
    """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found."""
    ...
def GetGlyphInfo(font: Font|list|tuple,codepoint: int,) -> GlyphInfo:
    """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found."""
    ...
def GetImageAlphaBorder(image: Image|list|tuple,threshold: float,) -> Rectangle:
    """Get image alpha border rectangle."""
    ...
def GetImageColor(image: Image|list|tuple,x: int,y: int,) -> Color:
    """Get image pixel color at (x, y) position."""
    ...
def GetKeyPressed() -> int:
    """Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty."""
    ...
def GetMasterVolume() -> float:
    """Get master volume (listener)."""
    ...
def GetMeshBoundingBox(mesh: Mesh|list|tuple,) -> BoundingBox:
    """Compute mesh bounding box limits."""
    ...
def GetModelBoundingBox(model: Model|list|tuple,) -> BoundingBox:
    """Compute model bounding box limits (considers all meshes)."""
    ...
def GetMonitorCount() -> int:
    """Get number of connected monitors."""
    ...
def GetMonitorHeight(monitor: int,) -> int:
    """Get specified monitor height (current video mode used by monitor)."""
    ...
def GetMonitorName(monitor: int,) -> bytes:
    """Get the human-readable, UTF-8 encoded name of the specified monitor."""
    ...
def GetMonitorPhysicalHeight(monitor: int,) -> int:
    """Get specified monitor physical height in millimetres."""
    ...
def GetMonitorPhysicalWidth(monitor: int,) -> int:
    """Get specified monitor physical width in millimetres."""
    ...
def GetMonitorPosition(monitor: int,) -> Vector2:
    """Get specified monitor position."""
    ...
def GetMonitorRefreshRate(monitor: int,) -> int:
    """Get specified monitor refresh rate."""
    ...
def GetMonitorWidth(monitor: int,) -> int:
    """Get specified monitor width (current video mode used by monitor)."""
    ...
def GetMouseDelta() -> Vector2:
    """Get mouse delta between frames."""
    ...
def GetMousePosition() -> Vector2:
    """Get mouse position XY."""
    ...
def GetMouseWheelMove() -> float:
    """Get mouse wheel movement for X or Y, whichever is larger."""
    ...
def GetMouseWheelMoveV() -> Vector2:
    """Get mouse wheel movement for both X and Y."""
    ...
def GetMouseX() -> int:
    """Get mouse position X."""
    ...
def GetMouseY() -> int:
    """Get mouse position Y."""
    ...
def GetMusicTimeLength(music: Music|list|tuple,) -> float:
    """Get music time length (in seconds)."""
    ...
def GetMusicTimePlayed(music: Music|list|tuple,) -> float:
    """Get current music time played (in seconds)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def GetPhysicsBodiesCount() -> int:
    """Returns the current amount of created physics bodies."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def GetPhysicsBody(index: int,) -> Any:
    """Returns a physics body of the bodies pool at a specific index."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def GetPhysicsShapeType(index: int,) -> int:
    """Returns the physics body shape type (PHYSICS_CIRCLE or PHYSICS_POLYGON)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def GetPhysicsShapeVertex(body: Any|list|tuple,vertex: int,) -> Vector2:
    """Returns transformed position of a body shape (body position + vertex transformed position)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def GetPhysicsShapeVerticesCount(index: int,) -> int:
    """Returns the amount of vertices of a physics body shape."""
    ...
def GetPixelColor(srcPtr: Any,format: int,) -> Color:
    """Get Color from a source pixel pointer of certain format."""
    ...
def GetPixelDataSize(width: int,height: int,format: int,) -> int:
    """Get pixel data size in bytes for certain format."""
    ...
def GetPrevDirectoryPath(dirPath: bytes,) -> bytes:
    """Get previous directory path for a given path (uses static string)."""
    ...
def GetRandomValue(min_0: int,max_1: int,) -> int:
    """Get a random value between min and max (both included)."""
    ...
def GetRayCollisionBox(ray: Ray|list|tuple,box: BoundingBox|list|tuple,) -> RayCollision:
    """Get collision info between ray and box."""
    ...
def GetRayCollisionMesh(ray: Ray|list|tuple,mesh: Mesh|list|tuple,transform: Matrix|list|tuple,) -> RayCollision:
    """Get collision info between ray and mesh."""
    ...
def GetRayCollisionQuad(ray: Ray|list|tuple,p1: Vector3|list|tuple,p2: Vector3|list|tuple,p3: Vector3|list|tuple,p4: Vector3|list|tuple,) -> RayCollision:
    """Get collision info between ray and quad."""
    ...
def GetRayCollisionSphere(ray: Ray|list|tuple,center: Vector3|list|tuple,radius: float,) -> RayCollision:
    """Get collision info between ray and sphere."""
    ...
def GetRayCollisionTriangle(ray: Ray|list|tuple,p1: Vector3|list|tuple,p2: Vector3|list|tuple,p3: Vector3|list|tuple,) -> RayCollision:
    """Get collision info between ray and triangle."""
    ...
def GetRenderHeight() -> int:
    """Get current render height (it considers HiDPI)."""
    ...
def GetRenderWidth() -> int:
    """Get current render width (it considers HiDPI)."""
    ...
def GetScreenHeight() -> int:
    """Get current screen height."""
    ...
def GetScreenToWorld2D(position: Vector2|list|tuple,camera: Camera2D|list|tuple,) -> Vector2:
    """Get the world space position for a 2d camera screen space position."""
    ...
def GetScreenToWorldRay(position: Vector2|list|tuple,camera: Camera3D|list|tuple,) -> Ray:
    """Get a ray trace from screen position (i.e mouse)."""
    ...
def GetScreenToWorldRayEx(position: Vector2|list|tuple,camera: Camera3D|list|tuple,width: int,height: int,) -> Ray:
    """Get a ray trace from screen position (i.e mouse) in a viewport."""
    ...
def GetScreenWidth() -> int:
    """Get current screen width."""
    ...
def GetShaderLocation(shader: Shader|list|tuple,uniformName: bytes,) -> int:
    """Get shader uniform location."""
    ...
def GetShaderLocationAttrib(shader: Shader|list|tuple,attribName: bytes,) -> int:
    """Get shader attribute location."""
    ...
def GetShapesTexture() -> Texture:
    """Get texture that is used for shapes drawing."""
    ...
def GetShapesTextureRectangle() -> Rectangle:
    """Get texture source rectangle that is used for shapes drawing."""
    ...
def GetSplinePointBasis(p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,p4: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: B-Spline."""
    ...
def GetSplinePointBezierCubic(p1: Vector2|list|tuple,c2: Vector2|list|tuple,c3: Vector2|list|tuple,p4: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: Cubic Bezier."""
    ...
def GetSplinePointBezierQuad(p1: Vector2|list|tuple,c2: Vector2|list|tuple,p3: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: Quadratic Bezier."""
    ...
def GetSplinePointCatmullRom(p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,p4: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: Catmull-Rom."""
    ...
def GetSplinePointLinear(startPos: Vector2|list|tuple,endPos: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: Linear."""
    ...
def GetTime() -> float:
    """Get elapsed time in seconds since InitWindow()."""
    ...
def GetTouchPointCount() -> int:
    """Get number of touch points."""
    ...
def GetTouchPointId(index: int,) -> int:
    """Get touch point identifier for given index."""
    ...
def GetTouchPosition(index: int,) -> Vector2:
    """Get touch position XY for a touch point index (relative to screen size)."""
    ...
def GetTouchX() -> int:
    """Get touch position X for touch point 0 (relative to screen size)."""
    ...
def GetTouchY() -> int:
    """Get touch position Y for touch point 0 (relative to screen size)."""
    ...
def GetWindowHandle() -> Any:
    """Get native window handle."""
    ...
def GetWindowPosition() -> Vector2:
    """Get window position XY on monitor."""
    ...
def GetWindowScaleDPI() -> Vector2:
    """Get window scale DPI factor."""
    ...
def GetWorkingDirectory() -> bytes:
    """Get current working directory (uses static string)."""
    ...
def GetWorldToScreen(position: Vector3|list|tuple,camera: Camera3D|list|tuple,) -> Vector2:
    """Get the screen space position for a 3d world space position."""
    ...
def GetWorldToScreen2D(position: Vector2|list|tuple,camera: Camera2D|list|tuple,) -> Vector2:
    """Get the screen space position for a 2d camera world space position."""
    ...
def GetWorldToScreenEx(position: Vector3|list|tuple,camera: Camera3D|list|tuple,width: int,height: int,) -> Vector2:
    """Get size position for a 3d world space position."""
    ...
def GuiButton(bounds: Rectangle|list|tuple,text: bytes,) -> int:
    """Button control, returns true when clicked."""
    ...
def GuiCheckBox(bounds: Rectangle|list|tuple,text: bytes,checked: Any,) -> int:
    """Check Box control, returns true when active."""
    ...
def GuiColorBarAlpha(bounds: Rectangle|list|tuple,text: bytes,alpha: Any,) -> int:
    """Color Bar Alpha control."""
    ...
def GuiColorBarHue(bounds: Rectangle|list|tuple,text: bytes,value: Any,) -> int:
    """Color Bar Hue control."""
    ...
def GuiColorPanel(bounds: Rectangle|list|tuple,text: bytes,color: Any|list|tuple,) -> int:
    """Color Panel control."""
    ...
def GuiColorPanelHSV(bounds: Rectangle|list|tuple,text: bytes,colorHsv: Any|list|tuple,) -> int:
    """Color Panel control that updates Hue-Saturation-Value color value, used by GuiColorPickerHSV()."""
    ...
def GuiColorPicker(bounds: Rectangle|list|tuple,text: bytes,color: Any|list|tuple,) -> int:
    """Color Picker control (multiple color controls)."""
    ...
def GuiColorPickerHSV(bounds: Rectangle|list|tuple,text: bytes,colorHsv: Any|list|tuple,) -> int:
    """Color Picker control that avoids conversion to RGB on each call (multiple color controls)."""
    ...
def GuiComboBox(bounds: Rectangle|list|tuple,text: bytes,active: Any,) -> int:
    """Combo Box control."""
    ...
def GuiDisable() -> None:
    """Disable gui controls (global state)."""
    ...
def GuiDisableTooltip() -> None:
    """Disable gui tooltips (global state)."""
    ...
def GuiDrawIcon(iconId: int,posX: int,posY: int,pixelSize: int,color: Color|list|tuple,) -> None:
    """Draw icon using pixel size at specified position."""
    ...
def GuiDropdownBox(bounds: Rectangle|list|tuple,text: bytes,active: Any,editMode: bool,) -> int:
    """Dropdown Box control."""
    ...
def GuiDummyRec(bounds: Rectangle|list|tuple,text: bytes,) -> int:
    """Dummy control for placeholders."""
    ...
def GuiEnable() -> None:
    """Enable gui controls (global state)."""
    ...
def GuiEnableTooltip() -> None:
    """Enable gui tooltips (global state)."""
    ...
def GuiGetFont() -> Font:
    """Get gui custom font (global state)."""
    ...
def GuiGetIcons() -> Any:
    """Get raygui icons data pointer."""
    ...
def GuiGetState() -> int:
    """Get gui state (global state)."""
    ...
def GuiGetStyle(control: int,property: int,) -> int:
    """Get one style property."""
    ...
def GuiGrid(bounds: Rectangle|list|tuple,text: bytes,spacing: float,subdivs: int,mouseCell: Any|list|tuple,) -> int:
    """Grid control."""
    ...
def GuiGroupBox(bounds: Rectangle|list|tuple,text: bytes,) -> int:
    """Group Box control with text name."""
    ...
def GuiIconText(iconId: int,text: bytes,) -> bytes:
    """Get text with icon id prepended (if supported)."""
    ...
def GuiIsLocked() -> bool:
    """Check if gui is locked (global state)."""
    ...
def GuiLabel(bounds: Rectangle|list|tuple,text: bytes,) -> int:
    """Label control."""
    ...
def GuiLabelButton(bounds: Rectangle|list|tuple,text: bytes,) -> int:
    """Label button control, returns true when clicked."""
    ...
def GuiLine(bounds: Rectangle|list|tuple,text: bytes,) -> int:
    """Line separator control, could contain text."""
    ...
def GuiListView(bounds: Rectangle|list|tuple,text: bytes,scrollIndex: Any,active: Any,) -> int:
    """List View control."""
    ...
def GuiListViewEx(bounds: Rectangle|list|tuple,text: list[bytes],count: int,scrollIndex: Any,active: Any,focus: Any,) -> int:
    """List View with extended parameters."""
    ...
def GuiLoadIcons(fileName: bytes,loadIconsName: bool,) -> list[bytes]:
    """Load raygui icons file (.rgi) into internal icons data."""
    ...
def GuiLoadStyle(fileName: bytes,) -> None:
    """Load style file over global style variable (.rgs)."""
    ...
def GuiLoadStyleDefault() -> None:
    """Load style default over global style."""
    ...
def GuiLock() -> None:
    """Lock gui controls (global state)."""
    ...
def GuiMessageBox(bounds: Rectangle|list|tuple,title: bytes,message: bytes,buttons: bytes,) -> int:
    """Message Box control, displays a message."""
    ...
def GuiPanel(bounds: Rectangle|list|tuple,text: bytes,) -> int:
    """Panel control, useful to group controls."""
    ...
def GuiProgressBar(bounds: Rectangle|list|tuple,textLeft: bytes,textRight: bytes,value: Any,minValue: float,maxValue: float,) -> int:
    """Progress Bar control."""
    ...
def GuiScrollPanel(bounds: Rectangle|list|tuple,text: bytes,content: Rectangle|list|tuple,scroll: Any|list|tuple,view: Any|list|tuple,) -> int:
    """Scroll Panel control."""
    ...
def GuiSetAlpha(alpha: float,) -> None:
    """Set gui controls alpha (global state), alpha goes from 0.0f to 1.0f."""
    ...
def GuiSetFont(font: Font|list|tuple,) -> None:
    """Set gui custom font (global state)."""
    ...
def GuiSetIconScale(scale: int,) -> None:
    """Set default icon drawing size."""
    ...
def GuiSetState(state: int,) -> None:
    """Set gui state (global state)."""
    ...
def GuiSetStyle(control: int,property: int,value: int,) -> None:
    """Set one style property."""
    ...
def GuiSetTooltip(tooltip: bytes,) -> None:
    """Set tooltip string."""
    ...
def GuiSlider(bounds: Rectangle|list|tuple,textLeft: bytes,textRight: bytes,value: Any,minValue: float,maxValue: float,) -> int:
    """Slider control."""
    ...
def GuiSliderBar(bounds: Rectangle|list|tuple,textLeft: bytes,textRight: bytes,value: Any,minValue: float,maxValue: float,) -> int:
    """Slider Bar control."""
    ...
def GuiSpinner(bounds: Rectangle|list|tuple,text: bytes,value: Any,minValue: int,maxValue: int,editMode: bool,) -> int:
    """Spinner control."""
    ...
def GuiStatusBar(bounds: Rectangle|list|tuple,text: bytes,) -> int:
    """Status Bar control, shows info text."""
    ...
def GuiTabBar(bounds: Rectangle|list|tuple,text: list[bytes],count: int,active: Any,) -> int:
    """Tab Bar control, returns TAB to be closed or -1."""
    ...
def GuiTextBox(bounds: Rectangle|list|tuple,text: bytes,textSize: int,editMode: bool,) -> int:
    """Text Box control, updates input text."""
    ...
def GuiTextInputBox(bounds: Rectangle|list|tuple,title: bytes,message: bytes,buttons: bytes,text: bytes,textMaxSize: int,secretViewActive: Any,) -> int:
    """Text Input Box control, ask for text, supports secret."""
    ...
def GuiToggle(bounds: Rectangle|list|tuple,text: bytes,active: Any,) -> int:
    """Toggle Button control."""
    ...
def GuiToggleGroup(bounds: Rectangle|list|tuple,text: bytes,active: Any,) -> int:
    """Toggle Group control."""
    ...
def GuiToggleSlider(bounds: Rectangle|list|tuple,text: bytes,active: Any,) -> int:
    """Toggle Slider control."""
    ...
def GuiUnlock() -> None:
    """Unlock gui controls (global state)."""
    ...
def GuiValueBox(bounds: Rectangle|list|tuple,text: bytes,value: Any,minValue: int,maxValue: int,editMode: bool,) -> int:
    """Value Box control, updates input text with numbers."""
    ...
def GuiValueBoxFloat(bounds: Rectangle|list|tuple,text: bytes,textValue: bytes,value: Any,editMode: bool,) -> int:
    """Value box control for float values."""
    ...
def GuiWindowBox(bounds: Rectangle|list|tuple,title: bytes,) -> int:
    """Window Box control, shows a window that can be closed."""
    ...
HUEBAR_PADDING: int
HUEBAR_SELECTOR_HEIGHT: int
HUEBAR_SELECTOR_OVERFLOW: int
HUEBAR_WIDTH: int
def HideCursor() -> None:
    """Hides cursor."""
    ...
ICON_1UP: int
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
ICON_HELP_BOX: int
ICON_HEX: int
ICON_HIDPI: int
ICON_HOT: int
ICON_HOUSE: int
ICON_INFO: int
ICON_INFO_BOX: int
ICON_KEY: int
ICON_LASER: int
ICON_LAYERS: int
ICON_LAYERS2: int
ICON_LAYERS_ISO: int
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
ICON_MAPS: int
ICON_MIPMAPS: int
ICON_MLAYERS: int
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
ICON_PRIORITY: int
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
ICON_WARNING: int
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
def ImageAlphaClear(image: Any|list|tuple,color: Color|list|tuple,threshold: float,) -> None:
    """Clear alpha channel to desired color."""
    ...
def ImageAlphaCrop(image: Any|list|tuple,threshold: float,) -> None:
    """Crop image depending on alpha value."""
    ...
def ImageAlphaMask(image: Any|list|tuple,alphaMask: Image|list|tuple,) -> None:
    """Apply alpha mask to image."""
    ...
def ImageAlphaPremultiply(image: Any|list|tuple,) -> None:
    """Premultiply alpha channel."""
    ...
def ImageBlurGaussian(image: Any|list|tuple,blurSize: int,) -> None:
    """Apply Gaussian blur using a box blur approximation."""
    ...
def ImageClearBackground(dst: Any|list|tuple,color: Color|list|tuple,) -> None:
    """Clear image background with given color."""
    ...
def ImageColorBrightness(image: Any|list|tuple,brightness: int,) -> None:
    """Modify image color: brightness (-255 to 255)."""
    ...
def ImageColorContrast(image: Any|list|tuple,contrast: float,) -> None:
    """Modify image color: contrast (-100 to 100)."""
    ...
def ImageColorGrayscale(image: Any|list|tuple,) -> None:
    """Modify image color: grayscale."""
    ...
def ImageColorInvert(image: Any|list|tuple,) -> None:
    """Modify image color: invert."""
    ...
def ImageColorReplace(image: Any|list|tuple,color: Color|list|tuple,replace: Color|list|tuple,) -> None:
    """Modify image color: replace color."""
    ...
def ImageColorTint(image: Any|list|tuple,color: Color|list|tuple,) -> None:
    """Modify image color: tint."""
    ...
def ImageCopy(image: Image|list|tuple,) -> Image:
    """Create an image duplicate (useful for transformations)."""
    ...
def ImageCrop(image: Any|list|tuple,crop: Rectangle|list|tuple,) -> None:
    """Crop an image to a defined rectangle."""
    ...
def ImageDither(image: Any|list|tuple,rBpp: int,gBpp: int,bBpp: int,aBpp: int,) -> None:
    """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)."""
    ...
def ImageDraw(dst: Any|list|tuple,src: Image|list|tuple,srcRec: Rectangle|list|tuple,dstRec: Rectangle|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a source image within a destination image (tint applied to source)."""
    ...
def ImageDrawCircle(dst: Any|list|tuple,centerX: int,centerY: int,radius: int,color: Color|list|tuple,) -> None:
    """Draw a filled circle within an image."""
    ...
def ImageDrawCircleLines(dst: Any|list|tuple,centerX: int,centerY: int,radius: int,color: Color|list|tuple,) -> None:
    """Draw circle outline within an image."""
    ...
def ImageDrawCircleLinesV(dst: Any|list|tuple,center: Vector2|list|tuple,radius: int,color: Color|list|tuple,) -> None:
    """Draw circle outline within an image (Vector version)."""
    ...
def ImageDrawCircleV(dst: Any|list|tuple,center: Vector2|list|tuple,radius: int,color: Color|list|tuple,) -> None:
    """Draw a filled circle within an image (Vector version)."""
    ...
def ImageDrawLine(dst: Any|list|tuple,startPosX: int,startPosY: int,endPosX: int,endPosY: int,color: Color|list|tuple,) -> None:
    """Draw line within an image."""
    ...
def ImageDrawLineEx(dst: Any|list|tuple,start: Vector2|list|tuple,end: Vector2|list|tuple,thick: int,color: Color|list|tuple,) -> None:
    """Draw a line defining thickness within an image."""
    ...
def ImageDrawLineV(dst: Any|list|tuple,start: Vector2|list|tuple,end: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw line within an image (Vector version)."""
    ...
def ImageDrawPixel(dst: Any|list|tuple,posX: int,posY: int,color: Color|list|tuple,) -> None:
    """Draw pixel within an image."""
    ...
def ImageDrawPixelV(dst: Any|list|tuple,position: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw pixel within an image (Vector version)."""
    ...
def ImageDrawRectangle(dst: Any|list|tuple,posX: int,posY: int,width: int,height: int,color: Color|list|tuple,) -> None:
    """Draw rectangle within an image."""
    ...
def ImageDrawRectangleLines(dst: Any|list|tuple,rec: Rectangle|list|tuple,thick: int,color: Color|list|tuple,) -> None:
    """Draw rectangle lines within an image."""
    ...
def ImageDrawRectangleRec(dst: Any|list|tuple,rec: Rectangle|list|tuple,color: Color|list|tuple,) -> None:
    """Draw rectangle within an image."""
    ...
def ImageDrawRectangleV(dst: Any|list|tuple,position: Vector2|list|tuple,size: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw rectangle within an image (Vector version)."""
    ...
def ImageDrawText(dst: Any|list|tuple,text: bytes,posX: int,posY: int,fontSize: int,color: Color|list|tuple,) -> None:
    """Draw text (using default font) within an image (destination)."""
    ...
def ImageDrawTextEx(dst: Any|list|tuple,font: Font|list|tuple,text: bytes,position: Vector2|list|tuple,fontSize: float,spacing: float,tint: Color|list|tuple,) -> None:
    """Draw text (custom sprite font) within an image (destination)."""
    ...
def ImageDrawTriangle(dst: Any|list|tuple,v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw triangle within an image."""
    ...
def ImageDrawTriangleEx(dst: Any|list|tuple,v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,c1: Color|list|tuple,c2: Color|list|tuple,c3: Color|list|tuple,) -> None:
    """Draw triangle with interpolated colors within an image."""
    ...
def ImageDrawTriangleFan(dst: Any|list|tuple,points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle fan defined by points within an image (first vertex is the center)."""
    ...
def ImageDrawTriangleLines(dst: Any|list|tuple,v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw triangle outline within an image."""
    ...
def ImageDrawTriangleStrip(dst: Any|list|tuple,points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle strip defined by points within an image."""
    ...
def ImageFlipHorizontal(image: Any|list|tuple,) -> None:
    """Flip image horizontally."""
    ...
def ImageFlipVertical(image: Any|list|tuple,) -> None:
    """Flip image vertically."""
    ...
def ImageFormat(image: Any|list|tuple,newFormat: int,) -> None:
    """Convert image data to desired format."""
    ...
def ImageFromChannel(image: Image|list|tuple,selectedChannel: int,) -> Image:
    """Create an image from a selected channel of another image (GRAYSCALE)."""
    ...
def ImageFromImage(image: Image|list|tuple,rec: Rectangle|list|tuple,) -> Image:
    """Create an image from another image piece."""
    ...
def ImageKernelConvolution(image: Any|list|tuple,kernel: Any,kernelSize: int,) -> None:
    """Apply custom square convolution kernel to image."""
    ...
def ImageMipmaps(image: Any|list|tuple,) -> None:
    """Compute all mipmap levels for a provided image."""
    ...
def ImageResize(image: Any|list|tuple,newWidth: int,newHeight: int,) -> None:
    """Resize image (Bicubic scaling algorithm)."""
    ...
def ImageResizeCanvas(image: Any|list|tuple,newWidth: int,newHeight: int,offsetX: int,offsetY: int,fill: Color|list|tuple,) -> None:
    """Resize canvas and fill with color."""
    ...
def ImageResizeNN(image: Any|list|tuple,newWidth: int,newHeight: int,) -> None:
    """Resize image (Nearest-Neighbor scaling algorithm)."""
    ...
def ImageRotate(image: Any|list|tuple,degrees: int,) -> None:
    """Rotate image by input angle in degrees (-359 to 359)."""
    ...
def ImageRotateCCW(image: Any|list|tuple,) -> None:
    """Rotate image counter-clockwise 90deg."""
    ...
def ImageRotateCW(image: Any|list|tuple,) -> None:
    """Rotate image clockwise 90deg."""
    ...
def ImageText(text: bytes,fontSize: int,color: Color|list|tuple,) -> Image:
    """Create an image from text (default font)."""
    ...
def ImageTextEx(font: Font|list|tuple,text: bytes,fontSize: float,spacing: float,tint: Color|list|tuple,) -> Image:
    """Create an image from text (custom sprite font)."""
    ...
def ImageToPOT(image: Any|list|tuple,fill: Color|list|tuple,) -> None:
    """Convert image to POT (power-of-two)."""
    ...
def InitAudioDevice() -> None:
    """Initialize audio device and context."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def InitPhysics() -> None:
    """Initializes physics values, pointers and creates physics loop thread."""
    ...
def InitWindow(width: int,height: int,title: bytes,) -> None:
    """Initialize window and OpenGL context."""
    ...
def IsAudioDeviceReady() -> bool:
    """Check if audio device has been initialized successfully."""
    ...
def IsAudioStreamPlaying(stream: AudioStream|list|tuple,) -> bool:
    """Check if audio stream is playing."""
    ...
def IsAudioStreamProcessed(stream: AudioStream|list|tuple,) -> bool:
    """Check if any audio stream buffers requires refill."""
    ...
def IsAudioStreamValid(stream: AudioStream|list|tuple,) -> bool:
    """Checks if an audio stream is valid (buffers initialized)."""
    ...
def IsCursorHidden() -> bool:
    """Check if cursor is not visible."""
    ...
def IsCursorOnScreen() -> bool:
    """Check if cursor is on the screen."""
    ...
def IsFileDropped() -> bool:
    """Check if a file has been dropped into window."""
    ...
def IsFileExtension(fileName: bytes,ext: bytes,) -> bool:
    """Check file extension (including point: .png, .wav)."""
    ...
def IsFileNameValid(fileName: bytes,) -> bool:
    """Check if fileName is valid for the platform/OS."""
    ...
def IsFontValid(font: Font|list|tuple,) -> bool:
    """Check if a font is valid (font data loaded, WARNING: GPU texture not checked)."""
    ...
def IsGamepadAvailable(gamepad: int,) -> bool:
    """Check if a gamepad is available."""
    ...
def IsGamepadButtonDown(gamepad: int,button: int,) -> bool:
    """Check if a gamepad button is being pressed."""
    ...
def IsGamepadButtonPressed(gamepad: int,button: int,) -> bool:
    """Check if a gamepad button has been pressed once."""
    ...
def IsGamepadButtonReleased(gamepad: int,button: int,) -> bool:
    """Check if a gamepad button has been released once."""
    ...
def IsGamepadButtonUp(gamepad: int,button: int,) -> bool:
    """Check if a gamepad button is NOT being pressed."""
    ...
def IsGestureDetected(gesture: int,) -> bool:
    """Check if a gesture have been detected."""
    ...
def IsImageValid(image: Image|list|tuple,) -> bool:
    """Check if an image is valid (data and parameters)."""
    ...
def IsKeyDown(key: int,) -> bool:
    """Check if a key is being pressed."""
    ...
def IsKeyPressed(key: int,) -> bool:
    """Check if a key has been pressed once."""
    ...
def IsKeyPressedRepeat(key: int,) -> bool:
    """Check if a key has been pressed again."""
    ...
def IsKeyReleased(key: int,) -> bool:
    """Check if a key has been released once."""
    ...
def IsKeyUp(key: int,) -> bool:
    """Check if a key is NOT being pressed."""
    ...
def IsMaterialValid(material: Material|list|tuple,) -> bool:
    """Check if a material is valid (shader assigned, map textures loaded in GPU)."""
    ...
def IsModelAnimationValid(model: Model|list|tuple,anim: ModelAnimation|list|tuple,) -> bool:
    """Check model animation skeleton match."""
    ...
def IsModelValid(model: Model|list|tuple,) -> bool:
    """Check if a model is valid (loaded in GPU, VAO/VBOs)."""
    ...
def IsMouseButtonDown(button: int,) -> bool:
    """Check if a mouse button is being pressed."""
    ...
def IsMouseButtonPressed(button: int,) -> bool:
    """Check if a mouse button has been pressed once."""
    ...
def IsMouseButtonReleased(button: int,) -> bool:
    """Check if a mouse button has been released once."""
    ...
def IsMouseButtonUp(button: int,) -> bool:
    """Check if a mouse button is NOT being pressed."""
    ...
def IsMusicStreamPlaying(music: Music|list|tuple,) -> bool:
    """Check if music is playing."""
    ...
def IsMusicValid(music: Music|list|tuple,) -> bool:
    """Checks if a music stream is valid (context and buffers initialized)."""
    ...
def IsPathFile(path: bytes,) -> bool:
    """Check if a given path is a file or a directory."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def IsPhysicsEnabled() -> bool:
    """Returns true if physics thread is currently enabled."""
    ...
def IsRenderTextureValid(target: RenderTexture|list|tuple,) -> bool:
    """Check if a render texture is valid (loaded in GPU)."""
    ...
def IsShaderValid(shader: Shader|list|tuple,) -> bool:
    """Check if a shader is valid (loaded on GPU)."""
    ...
def IsSoundPlaying(sound: Sound|list|tuple,) -> bool:
    """Check if a sound is currently playing."""
    ...
def IsSoundValid(sound: Sound|list|tuple,) -> bool:
    """Checks if a sound is valid (data loaded and buffers initialized)."""
    ...
def IsTextureValid(texture: Texture|list|tuple,) -> bool:
    """Check if a texture is valid (loaded in GPU)."""
    ...
def IsWaveValid(wave: Wave|list|tuple,) -> bool:
    """Checks if wave data is valid (data loaded and parameters)."""
    ...
def IsWindowFocused() -> bool:
    """Check if window is currently focused."""
    ...
def IsWindowFullscreen() -> bool:
    """Check if window is currently fullscreen."""
    ...
def IsWindowHidden() -> bool:
    """Check if window is currently hidden."""
    ...
def IsWindowMaximized() -> bool:
    """Check if window is currently maximized."""
    ...
def IsWindowMinimized() -> bool:
    """Check if window is currently minimized."""
    ...
def IsWindowReady() -> bool:
    """Check if window has been initialized successfully."""
    ...
def IsWindowResized() -> bool:
    """Check if window has been resized last frame."""
    ...
def IsWindowState(flag: int,) -> bool:
    """Check if one specific window flag is enabled."""
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
LIST_ITEMS_BORDER_WIDTH: int
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
    """."""
    ...
def LoadAudioStream(sampleRate: int,sampleSize: int,channels: int,) -> AudioStream:
    """Load audio stream (to stream raw audio pcm data)."""
    ...
def LoadAutomationEventList(fileName: bytes,) -> AutomationEventList:
    """Load automation events list from file, NULL for empty list, capacity = MAX_AUTOMATION_EVENTS."""
    ...
def LoadCodepoints(text: bytes,count: Any,) -> Any:
    """Load all codepoints from a UTF-8 text string, codepoints count returned by parameter."""
    ...
def LoadDirectoryFiles(dirPath: bytes,) -> FilePathList:
    """Load directory filepaths."""
    ...
def LoadDirectoryFilesEx(basePath: bytes,filter: bytes,scanSubdirs: bool,) -> FilePathList:
    """Load directory filepaths with extension filtering and recursive directory scan. Use 'DIR' in the filter string to include directories in the result."""
    ...
def LoadDroppedFiles() -> FilePathList:
    """Load dropped filepaths."""
    ...
def LoadFileData(fileName: bytes,dataSize: Any,) -> bytes:
    """Load file data as byte array (read)."""
    ...
def LoadFileText(fileName: bytes,) -> bytes:
    """Load text data from file (read), returns a '\0' terminated string."""
    ...
def LoadFont(fileName: bytes,) -> Font:
    """Load font from file into GPU memory (VRAM)."""
    ...
def LoadFontData(fileData: bytes,dataSize: int,fontSize: int,codepoints: Any,codepointCount: int,type: int,) -> Any:
    """Load font data for further use."""
    ...
def LoadFontEx(fileName: bytes,fontSize: int,codepoints: Any,codepointCount: int,) -> Font:
    """Load font from file with extended parameters, use NULL for codepoints and 0 for codepointCount to load the default character set, font size is provided in pixels height."""
    ...
def LoadFontFromImage(image: Image|list|tuple,key: Color|list|tuple,firstChar: int,) -> Font:
    """Load font from Image (XNA style)."""
    ...
def LoadFontFromMemory(fileType: bytes,fileData: bytes,dataSize: int,fontSize: int,codepoints: Any,codepointCount: int,) -> Font:
    """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'."""
    ...
def LoadImage(fileName: bytes,) -> Image:
    """Load image from file into CPU memory (RAM)."""
    ...
def LoadImageAnim(fileName: bytes,frames: Any,) -> Image:
    """Load image sequence from file (frames appended to image.data)."""
    ...
def LoadImageAnimFromMemory(fileType: bytes,fileData: bytes,dataSize: int,frames: Any,) -> Image:
    """Load image sequence from memory buffer."""
    ...
def LoadImageColors(image: Image|list|tuple,) -> Any:
    """Load color data from image as a Color array (RGBA - 32bit)."""
    ...
def LoadImageFromMemory(fileType: bytes,fileData: bytes,dataSize: int,) -> Image:
    """Load image from memory buffer, fileType refers to extension: i.e. '.png'."""
    ...
def LoadImageFromScreen() -> Image:
    """Load image from screen buffer and (screenshot)."""
    ...
def LoadImageFromTexture(texture: Texture|list|tuple,) -> Image:
    """Load image from GPU texture data."""
    ...
def LoadImagePalette(image: Image|list|tuple,maxPaletteSize: int,colorCount: Any,) -> Any:
    """Load colors palette from image as a Color array (RGBA - 32bit)."""
    ...
def LoadImageRaw(fileName: bytes,width: int,height: int,format: int,headerSize: int,) -> Image:
    """Load image from RAW file data."""
    ...
def LoadMaterialDefault() -> Material:
    """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)."""
    ...
def LoadMaterials(fileName: bytes,materialCount: Any,) -> Any:
    """Load materials from model file."""
    ...
def LoadModel(fileName: bytes,) -> Model:
    """Load model from files (meshes and materials)."""
    ...
def LoadModelAnimations(fileName: bytes,animCount: Any,) -> Any:
    """Load model animations from file."""
    ...
def LoadModelFromMesh(mesh: Mesh|list|tuple,) -> Model:
    """Load model from generated mesh (default material)."""
    ...
def LoadMusicStream(fileName: bytes,) -> Music:
    """Load music stream from file."""
    ...
def LoadMusicStreamFromMemory(fileType: bytes,data: bytes,dataSize: int,) -> Music:
    """Load music stream from data."""
    ...
def LoadRandomSequence(count: int,min_1: int,max_2: int,) -> Any:
    """Load random values sequence, no values repeated."""
    ...
def LoadRenderTexture(width: int,height: int,) -> RenderTexture:
    """Load texture for rendering (framebuffer)."""
    ...
def LoadShader(vsFileName: bytes,fsFileName: bytes,) -> Shader:
    """Load shader from files and bind default locations."""
    ...
def LoadShaderFromMemory(vsCode: bytes,fsCode: bytes,) -> Shader:
    """Load shader from code strings and bind default locations."""
    ...
def LoadSound(fileName: bytes,) -> Sound:
    """Load sound from file."""
    ...
def LoadSoundAlias(source: Sound|list|tuple,) -> Sound:
    """Create a new sound that shares the same sample data as the source sound, does not own the sound data."""
    ...
def LoadSoundFromWave(wave: Wave|list|tuple,) -> Sound:
    """Load sound from wave data."""
    ...
def LoadTexture(fileName: bytes,) -> Texture:
    """Load texture from file into GPU memory (VRAM)."""
    ...
def LoadTextureCubemap(image: Image|list|tuple,layout: int,) -> Texture:
    """Load cubemap from image, multiple image cubemap layouts supported."""
    ...
def LoadTextureFromImage(image: Image|list|tuple,) -> Texture:
    """Load texture from image data."""
    ...
def LoadUTF8(codepoints: Any,length: int,) -> bytes:
    """Load UTF-8 text encoded from codepoints array."""
    ...
def LoadVrStereoConfig(device: VrDeviceInfo|list|tuple,) -> VrStereoConfig:
    """Load VR stereo config for VR simulator device parameters."""
    ...
def LoadWave(fileName: bytes,) -> Wave:
    """Load wave data from file."""
    ...
def LoadWaveFromMemory(fileType: bytes,fileData: bytes,dataSize: int,) -> Wave:
    """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'."""
    ...
def LoadWaveSamples(wave: Wave|list|tuple,) -> Any:
    """Load samples data from wave as a 32bit float data array."""
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
def MakeDirectory(dirPath: bytes,) -> int:
    """Create directories (including full path requested), returns 0 on success."""
    ...
def MatrixAdd(left: Matrix|list|tuple,right: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def MatrixDecompose(mat: Matrix|list|tuple,translation: Any|list|tuple,rotation: Any|list|tuple,scale: Any|list|tuple,) -> None:
    """."""
    ...
def MatrixDeterminant(mat: Matrix|list|tuple,) -> float:
    """."""
    ...
def MatrixFrustum(left: float,right: float,bottom: float,top: float,nearPlane: float,farPlane: float,) -> Matrix:
    """."""
    ...
def MatrixIdentity() -> Matrix:
    """."""
    ...
def MatrixInvert(mat: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def MatrixLookAt(eye: Vector3|list|tuple,target: Vector3|list|tuple,up: Vector3|list|tuple,) -> Matrix:
    """."""
    ...
def MatrixMultiply(left: Matrix|list|tuple,right: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def MatrixOrtho(left: float,right: float,bottom: float,top: float,nearPlane: float,farPlane: float,) -> Matrix:
    """."""
    ...
def MatrixPerspective(fovY: float,aspect: float,nearPlane: float,farPlane: float,) -> Matrix:
    """."""
    ...
def MatrixRotate(axis: Vector3|list|tuple,angle: float,) -> Matrix:
    """."""
    ...
def MatrixRotateX(angle: float,) -> Matrix:
    """."""
    ...
def MatrixRotateXYZ(angle: Vector3|list|tuple,) -> Matrix:
    """."""
    ...
def MatrixRotateY(angle: float,) -> Matrix:
    """."""
    ...
def MatrixRotateZ(angle: float,) -> Matrix:
    """."""
    ...
def MatrixRotateZYX(angle: Vector3|list|tuple,) -> Matrix:
    """."""
    ...
def MatrixScale(x: float,y: float,z: float,) -> Matrix:
    """."""
    ...
def MatrixSubtract(left: Matrix|list|tuple,right: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def MatrixToFloatV(mat: Matrix|list|tuple,) -> float16:
    """."""
    ...
def MatrixTrace(mat: Matrix|list|tuple,) -> float:
    """."""
    ...
def MatrixTranslate(x: float,y: float,z: float,) -> Matrix:
    """."""
    ...
def MatrixTranspose(mat: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def MaximizeWindow() -> None:
    """Set window state: maximized, if resizable."""
    ...
def MeasureText(text: bytes,fontSize: int,) -> int:
    """Measure string width for default font."""
    ...
def MeasureTextEx(font: Font|list|tuple,text: bytes,fontSize: float,spacing: float,) -> Vector2:
    """Measure string size for Font."""
    ...
def MemAlloc(size: int,) -> Any:
    """Internal memory allocator."""
    ...
def MemFree(ptr: Any,) -> None:
    """Internal memory free."""
    ...
def MemRealloc(ptr: Any,size: int,) -> Any:
    """Internal memory reallocator."""
    ...
def MinimizeWindow() -> None:
    """Set window state: minimized, if resizable."""
    ...
NPATCH_NINE_PATCH: int
NPATCH_THREE_PATCH_HORIZONTAL: int
NPATCH_THREE_PATCH_VERTICAL: int
def Normalize(value: float,start: float,end: float,) -> float:
    """."""
    ...
def OpenURL(url: bytes,) -> None:
    """Open URL with default system browser (if available)."""
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
def PauseAudioStream(stream: AudioStream|list|tuple,) -> None:
    """Pause audio stream."""
    ...
def PauseMusicStream(music: Music|list|tuple,) -> None:
    """Pause music playing."""
    ...
def PauseSound(sound: Sound|list|tuple,) -> None:
    """Pause a sound."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def PhysicsAddForce(body: Any|list|tuple,force: Vector2|list|tuple,) -> None:
    """Adds a force to a physics body."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def PhysicsAddTorque(body: Any|list|tuple,amount: float,) -> None:
    """Adds an angular force to a physics body."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def PhysicsShatter(body: Any|list|tuple,position: Vector2|list|tuple,force: float,) -> None:
    """Shatters a polygon shape physics body to little physics bodies with explosion force."""
    ...
def PlayAudioStream(stream: AudioStream|list|tuple,) -> None:
    """Play audio stream."""
    ...
def PlayAutomationEvent(event: AutomationEvent|list|tuple,) -> None:
    """Play a recorded automation event."""
    ...
def PlayMusicStream(music: Music|list|tuple,) -> None:
    """Start music playing."""
    ...
def PlaySound(sound: Sound|list|tuple,) -> None:
    """Play a sound."""
    ...
def PollInputEvents() -> None:
    """Register all input events."""
    ...
def QuaternionAdd(q1: Vector4|list|tuple,q2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def QuaternionAddValue(q: Vector4|list|tuple,add: float,) -> Vector4:
    """."""
    ...
def QuaternionCubicHermiteSpline(q1: Vector4|list|tuple,outTangent1: Vector4|list|tuple,q2: Vector4|list|tuple,inTangent2: Vector4|list|tuple,t: float,) -> Vector4:
    """."""
    ...
def QuaternionDivide(q1: Vector4|list|tuple,q2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def QuaternionEquals(p: Vector4|list|tuple,q: Vector4|list|tuple,) -> int:
    """."""
    ...
def QuaternionFromAxisAngle(axis: Vector3|list|tuple,angle: float,) -> Vector4:
    """."""
    ...
def QuaternionFromEuler(pitch: float,yaw: float,roll: float,) -> Vector4:
    """."""
    ...
def QuaternionFromMatrix(mat: Matrix|list|tuple,) -> Vector4:
    """."""
    ...
def QuaternionFromVector3ToVector3(from_0: Vector3|list|tuple,to: Vector3|list|tuple,) -> Vector4:
    """."""
    ...
def QuaternionIdentity() -> Vector4:
    """."""
    ...
def QuaternionInvert(q: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def QuaternionLength(q: Vector4|list|tuple,) -> float:
    """."""
    ...
def QuaternionLerp(q1: Vector4|list|tuple,q2: Vector4|list|tuple,amount: float,) -> Vector4:
    """."""
    ...
def QuaternionMultiply(q1: Vector4|list|tuple,q2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def QuaternionNlerp(q1: Vector4|list|tuple,q2: Vector4|list|tuple,amount: float,) -> Vector4:
    """."""
    ...
def QuaternionNormalize(q: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def QuaternionScale(q: Vector4|list|tuple,mul: float,) -> Vector4:
    """."""
    ...
def QuaternionSlerp(q1: Vector4|list|tuple,q2: Vector4|list|tuple,amount: float,) -> Vector4:
    """."""
    ...
def QuaternionSubtract(q1: Vector4|list|tuple,q2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def QuaternionSubtractValue(q: Vector4|list|tuple,sub: float,) -> Vector4:
    """."""
    ...
def QuaternionToAxisAngle(q: Vector4|list|tuple,outAxis: Any|list|tuple,outAngle: Any,) -> None:
    """."""
    ...
def QuaternionToEuler(q: Vector4|list|tuple,) -> Vector3:
    """."""
    ...
def QuaternionToMatrix(q: Vector4|list|tuple,) -> Matrix:
    """."""
    ...
def QuaternionTransform(q: Vector4|list|tuple,mat: Matrix|list|tuple,) -> Vector4:
    """."""
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
RL_SHADER_UNIFORM_UINT: int
RL_SHADER_UNIFORM_UIVEC2: int
RL_SHADER_UNIFORM_UIVEC3: int
RL_SHADER_UNIFORM_UIVEC4: int
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
    """."""
    ...
def RestoreWindow() -> None:
    """Set window state: not minimized/maximized."""
    ...
def ResumeAudioStream(stream: AudioStream|list|tuple,) -> None:
    """Resume audio stream."""
    ...
def ResumeMusicStream(music: Music|list|tuple,) -> None:
    """Resume playing paused music."""
    ...
def ResumeSound(sound: Sound|list|tuple,) -> None:
    """Resume a paused sound."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def RunPhysicsStep() -> None:
    """Run physics step, to be used if PHYSICS_NO_THREADS is set in your main loop."""
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
SHADER_LOC_BONE_MATRICES: int
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
SHADER_LOC_VERTEX_BONEIDS: int
SHADER_LOC_VERTEX_BONEWEIGHTS: int
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
def SaveFileData(fileName: bytes,data: Any,dataSize: int,) -> bool:
    """Save data to file from byte array (write), returns true on success."""
    ...
def SaveFileText(fileName: bytes,text: bytes,) -> bool:
    """Save text data to file (write), string must be '\0' terminated, returns true on success."""
    ...
def SeekMusicStream(music: Music|list|tuple,position: float,) -> None:
    """Seek music to a position (in seconds)."""
    ...
def SetAudioStreamBufferSizeDefault(size: int,) -> None:
    """Default size for new audio streams."""
    ...
def SetAudioStreamCallback(stream: AudioStream|list|tuple,callback: Any,) -> None:
    """Audio thread callback to request new data."""
    ...
def SetAudioStreamPan(stream: AudioStream|list|tuple,pan: float,) -> None:
    """Set pan for audio stream (0.5 is centered)."""
    ...
def SetAudioStreamPitch(stream: AudioStream|list|tuple,pitch: float,) -> None:
    """Set pitch for audio stream (1.0 is base level)."""
    ...
def SetAudioStreamVolume(stream: AudioStream|list|tuple,volume: float,) -> None:
    """Set volume for audio stream (1.0 is max level)."""
    ...
def SetAutomationEventBaseFrame(frame: int,) -> None:
    """Set automation event internal base frame to start recording."""
    ...
def SetAutomationEventList(list_0: Any|list|tuple,) -> None:
    """Set automation event list to record to."""
    ...
def SetClipboardText(text: bytes,) -> None:
    """Set clipboard text content."""
    ...
def SetConfigFlags(flags: int,) -> None:
    """Setup init configuration flags (view FLAGS)."""
    ...
def SetExitKey(key: int,) -> None:
    """Set a custom key to exit program (default is ESC)."""
    ...
def SetGamepadMappings(mappings: bytes,) -> int:
    """Set internal gamepad mappings (SDL_GameControllerDB)."""
    ...
def SetGamepadVibration(gamepad: int,leftMotor: float,rightMotor: float,duration: float,) -> None:
    """Set gamepad vibration for both motors (duration in seconds)."""
    ...
def SetGesturesEnabled(flags: int,) -> None:
    """Enable a set of gestures using flags."""
    ...
def SetLoadFileDataCallback(callback: bytes,) -> None:
    """Set custom file binary data loader."""
    ...
def SetLoadFileTextCallback(callback: bytes,) -> None:
    """Set custom file text data loader."""
    ...
def SetMasterVolume(volume: float,) -> None:
    """Set master volume (listener)."""
    ...
def SetMaterialTexture(material: Any|list|tuple,mapType: int,texture: Texture|list|tuple,) -> None:
    """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)."""
    ...
def SetModelMeshMaterial(model: Any|list|tuple,meshId: int,materialId: int,) -> None:
    """Set material for a mesh."""
    ...
def SetMouseCursor(cursor: int,) -> None:
    """Set mouse cursor."""
    ...
def SetMouseOffset(offsetX: int,offsetY: int,) -> None:
    """Set mouse offset."""
    ...
def SetMousePosition(x: int,y: int,) -> None:
    """Set mouse position XY."""
    ...
def SetMouseScale(scaleX: float,scaleY: float,) -> None:
    """Set mouse scaling."""
    ...
def SetMusicPan(music: Music|list|tuple,pan: float,) -> None:
    """Set pan for a music (0.5 is center)."""
    ...
def SetMusicPitch(music: Music|list|tuple,pitch: float,) -> None:
    """Set pitch for a music (1.0 is base level)."""
    ...
def SetMusicVolume(music: Music|list|tuple,volume: float,) -> None:
    """Set volume for music (1.0 is max level)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def SetPhysicsBodyRotation(body: Any|list|tuple,radians: float,) -> None:
    """Sets physics body shape transform based on radians parameter."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def SetPhysicsGravity(x: float,y: float,) -> None:
    """Sets physics global gravity force."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def SetPhysicsTimeStep(delta: float,) -> None:
    """Sets physics fixed time step in milliseconds. 1.666666 by default."""
    ...
def SetPixelColor(dstPtr: Any,color: Color|list|tuple,format: int,) -> None:
    """Set color formatted into destination pixel pointer."""
    ...
def SetRandomSeed(seed: int,) -> None:
    """Set the seed for the random number generator."""
    ...
def SetSaveFileDataCallback(callback: bytes,) -> None:
    """Set custom file binary data saver."""
    ...
def SetSaveFileTextCallback(callback: bytes,) -> None:
    """Set custom file text data saver."""
    ...
def SetShaderValue(shader: Shader|list|tuple,locIndex: int,value: Any,uniformType: int,) -> None:
    """Set shader uniform value."""
    ...
def SetShaderValueMatrix(shader: Shader|list|tuple,locIndex: int,mat: Matrix|list|tuple,) -> None:
    """Set shader uniform value (matrix 4x4)."""
    ...
def SetShaderValueTexture(shader: Shader|list|tuple,locIndex: int,texture: Texture|list|tuple,) -> None:
    """Set shader uniform value for texture (sampler2d)."""
    ...
def SetShaderValueV(shader: Shader|list|tuple,locIndex: int,value: Any,uniformType: int,count: int,) -> None:
    """Set shader uniform value vector."""
    ...
def SetShapesTexture(texture: Texture|list|tuple,source: Rectangle|list|tuple,) -> None:
    """Set texture and rectangle to be used on shapes drawing."""
    ...
def SetSoundPan(sound: Sound|list|tuple,pan: float,) -> None:
    """Set pan for a sound (0.5 is center)."""
    ...
def SetSoundPitch(sound: Sound|list|tuple,pitch: float,) -> None:
    """Set pitch for a sound (1.0 is base level)."""
    ...
def SetSoundVolume(sound: Sound|list|tuple,volume: float,) -> None:
    """Set volume for a sound (1.0 is max level)."""
    ...
def SetTargetFPS(fps: int,) -> None:
    """Set target FPS (maximum)."""
    ...
def SetTextLineSpacing(spacing: int,) -> None:
    """Set vertical line spacing when drawing with line-breaks."""
    ...
def SetTextureFilter(texture: Texture|list|tuple,filter: int,) -> None:
    """Set texture scaling filter mode."""
    ...
def SetTextureWrap(texture: Texture|list|tuple,wrap: int,) -> None:
    """Set texture wrapping mode."""
    ...
def SetTraceLogCallback(callback: bytes,) -> None:
    """Set custom trace log."""
    ...
def SetTraceLogLevel(logLevel: int,) -> None:
    """Set the current threshold (minimum) log level."""
    ...
def SetWindowFocused() -> None:
    """Set window focused."""
    ...
def SetWindowIcon(image: Image|list|tuple,) -> None:
    """Set icon for window (single image, RGBA 32bit)."""
    ...
def SetWindowIcons(images: Any|list|tuple,count: int,) -> None:
    """Set icon for window (multiple images, RGBA 32bit)."""
    ...
def SetWindowMaxSize(width: int,height: int,) -> None:
    """Set window maximum dimensions (for FLAG_WINDOW_RESIZABLE)."""
    ...
def SetWindowMinSize(width: int,height: int,) -> None:
    """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)."""
    ...
def SetWindowMonitor(monitor: int,) -> None:
    """Set monitor for the current window."""
    ...
def SetWindowOpacity(opacity: float,) -> None:
    """Set window opacity [0.0f..1.0f]."""
    ...
def SetWindowPosition(x: int,y: int,) -> None:
    """Set window position on screen."""
    ...
def SetWindowSize(width: int,height: int,) -> None:
    """Set window dimensions."""
    ...
def SetWindowState(flags: int,) -> None:
    """Set window configuration state using flags."""
    ...
def SetWindowTitle(title: bytes,) -> None:
    """Set title for window."""
    ...
def ShowCursor() -> None:
    """Shows cursor."""
    ...
def StartAutomationEventRecording() -> None:
    """Start recording automation events (AutomationEventList must be set)."""
    ...
def StopAudioStream(stream: AudioStream|list|tuple,) -> None:
    """Stop audio stream."""
    ...
def StopAutomationEventRecording() -> None:
    """Stop recording automation events."""
    ...
def StopMusicStream(music: Music|list|tuple,) -> None:
    """Stop music playing."""
    ...
def StopSound(sound: Sound|list|tuple,) -> None:
    """Stop playing a sound."""
    ...
def SwapScreenBuffer() -> None:
    """Swap back buffer with front buffer (screen drawing)."""
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
def TakeScreenshot(fileName: bytes,) -> None:
    """Takes a screenshot of current screen (filename extension defines format)."""
    ...
def TextAppend(text: bytes,append: bytes,position: Any,) -> None:
    """Append text at specific position and move cursor!."""
    ...
def TextCopy(dst: bytes,src: bytes,) -> int:
    """Copy one string to another, returns bytes copied."""
    ...
def TextFindIndex(text: bytes,find: bytes,) -> int:
    """Find first text occurrence within a string."""
    ...
def TextFormat(*args) -> bytes:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def TextInsert(text: bytes,insert: bytes,position: int,) -> bytes:
    """Insert text in a position (WARNING: memory must be freed!)."""
    ...
def TextIsEqual(text1: bytes,text2: bytes,) -> bool:
    """Check if two text string are equal."""
    ...
def TextJoin(textList: list[bytes],count: int,delimiter: bytes,) -> bytes:
    """Join text strings with delimiter."""
    ...
def TextLength(text: bytes,) -> int:
    """Get text length, checks for '\0' ending."""
    ...
def TextReplace(text: bytes,replace: bytes,by: bytes,) -> bytes:
    """Replace text string (WARNING: memory must be freed!)."""
    ...
def TextSplit(text: bytes,delimiter: bytes,count: Any,) -> list[bytes]:
    """Split text into multiple strings."""
    ...
def TextSubtext(text: bytes,position: int,length: int,) -> bytes:
    """Get a piece of a text string."""
    ...
def TextToCamel(text: bytes,) -> bytes:
    """Get Camel case notation version of provided string."""
    ...
def TextToFloat(text: bytes,) -> float:
    """Get float value from text (negative values not supported)."""
    ...
def TextToInteger(text: bytes,) -> int:
    """Get integer value from text (negative values not supported)."""
    ...
def TextToLower(text: bytes,) -> bytes:
    """Get lower case version of provided string."""
    ...
def TextToPascal(text: bytes,) -> bytes:
    """Get Pascal case notation version of provided string."""
    ...
def TextToSnake(text: bytes,) -> bytes:
    """Get Snake case notation version of provided string."""
    ...
def TextToUpper(text: bytes,) -> bytes:
    """Get upper case version of provided string."""
    ...
def ToggleBorderlessWindowed() -> None:
    """Toggle window state: borderless windowed, resizes window to match monitor resolution."""
    ...
def ToggleFullscreen() -> None:
    """Toggle window state: fullscreen/windowed, resizes monitor to match window resolution."""
    ...
def TraceLog(*args) -> None:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def UnloadAudioStream(stream: AudioStream|list|tuple,) -> None:
    """Unload audio stream and free memory."""
    ...
def UnloadAutomationEventList(list_0: AutomationEventList|list|tuple,) -> None:
    """Unload automation events list from file."""
    ...
def UnloadCodepoints(codepoints: Any,) -> None:
    """Unload codepoints data from memory."""
    ...
def UnloadDirectoryFiles(files: FilePathList|list|tuple,) -> None:
    """Unload filepaths."""
    ...
def UnloadDroppedFiles(files: FilePathList|list|tuple,) -> None:
    """Unload dropped filepaths."""
    ...
def UnloadFileData(data: bytes,) -> None:
    """Unload file data allocated by LoadFileData()."""
    ...
def UnloadFileText(text: bytes,) -> None:
    """Unload file text data allocated by LoadFileText()."""
    ...
def UnloadFont(font: Font|list|tuple,) -> None:
    """Unload font from GPU memory (VRAM)."""
    ...
def UnloadFontData(glyphs: Any|list|tuple,glyphCount: int,) -> None:
    """Unload font chars info data (RAM)."""
    ...
def UnloadImage(image: Image|list|tuple,) -> None:
    """Unload image from CPU memory (RAM)."""
    ...
def UnloadImageColors(colors: Any|list|tuple,) -> None:
    """Unload color data loaded with LoadImageColors()."""
    ...
def UnloadImagePalette(colors: Any|list|tuple,) -> None:
    """Unload colors palette loaded with LoadImagePalette()."""
    ...
def UnloadMaterial(material: Material|list|tuple,) -> None:
    """Unload material from GPU memory (VRAM)."""
    ...
def UnloadMesh(mesh: Mesh|list|tuple,) -> None:
    """Unload mesh data from CPU and GPU."""
    ...
def UnloadModel(model: Model|list|tuple,) -> None:
    """Unload model (including meshes) from memory (RAM and/or VRAM)."""
    ...
def UnloadModelAnimation(anim: ModelAnimation|list|tuple,) -> None:
    """Unload animation data."""
    ...
def UnloadModelAnimations(animations: Any|list|tuple,animCount: int,) -> None:
    """Unload animation array data."""
    ...
def UnloadMusicStream(music: Music|list|tuple,) -> None:
    """Unload music stream."""
    ...
def UnloadRandomSequence(sequence: Any,) -> None:
    """Unload random values sequence."""
    ...
def UnloadRenderTexture(target: RenderTexture|list|tuple,) -> None:
    """Unload render texture from GPU memory (VRAM)."""
    ...
def UnloadShader(shader: Shader|list|tuple,) -> None:
    """Unload shader from GPU memory (VRAM)."""
    ...
def UnloadSound(sound: Sound|list|tuple,) -> None:
    """Unload sound."""
    ...
def UnloadSoundAlias(alias: Sound|list|tuple,) -> None:
    """Unload a sound alias (does not deallocate sample data)."""
    ...
def UnloadTexture(texture: Texture|list|tuple,) -> None:
    """Unload texture from GPU memory (VRAM)."""
    ...
def UnloadUTF8(text: bytes,) -> None:
    """Unload UTF-8 text encoded from codepoints array."""
    ...
def UnloadVrStereoConfig(config: VrStereoConfig|list|tuple,) -> None:
    """Unload VR stereo config."""
    ...
def UnloadWave(wave: Wave|list|tuple,) -> None:
    """Unload wave data."""
    ...
def UnloadWaveSamples(samples: Any,) -> None:
    """Unload samples data loaded with LoadWaveSamples()."""
    ...
def UpdateAudioStream(stream: AudioStream|list|tuple,data: Any,frameCount: int,) -> None:
    """Update audio stream buffers with data."""
    ...
def UpdateCamera(camera: Any|list|tuple,mode: int,) -> None:
    """Update camera position for selected mode."""
    ...
def UpdateCameraPro(camera: Any|list|tuple,movement: Vector3|list|tuple,rotation: Vector3|list|tuple,zoom: float,) -> None:
    """Update camera movement/rotation."""
    ...
def UpdateMeshBuffer(mesh: Mesh|list|tuple,index: int,data: Any,dataSize: int,offset: int,) -> None:
    """Update mesh vertex data in GPU for a specific buffer index."""
    ...
def UpdateModelAnimation(model: Model|list|tuple,anim: ModelAnimation|list|tuple,frame: int,) -> None:
    """Update model animation pose (CPU)."""
    ...
def UpdateModelAnimationBones(model: Model|list|tuple,anim: ModelAnimation|list|tuple,frame: int,) -> None:
    """Update model animation mesh bone matrices (GPU skinning)."""
    ...
def UpdateMusicStream(music: Music|list|tuple,) -> None:
    """Updates buffers for music streaming."""
    ...
def UpdateSound(sound: Sound|list|tuple,data: Any,sampleCount: int,) -> None:
    """Update sound buffer with new data."""
    ...
def UpdateTexture(texture: Texture|list|tuple,pixels: Any,) -> None:
    """Update GPU texture with new data."""
    ...
def UpdateTextureRec(texture: Texture|list|tuple,rec: Rectangle|list|tuple,pixels: Any,) -> None:
    """Update GPU texture rectangle with new data."""
    ...
def UploadMesh(mesh: Any|list|tuple,dynamic: bool,) -> None:
    """Upload mesh vertex data in GPU and provide VAO/VBO ids."""
    ...
VALUEBOX: int
def Vector2Add(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2AddValue(v: Vector2|list|tuple,add: float,) -> Vector2:
    """."""
    ...
def Vector2Angle(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> float:
    """."""
    ...
def Vector2Clamp(v: Vector2|list|tuple,min_1: Vector2|list|tuple,max_2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2ClampValue(v: Vector2|list|tuple,min_1: float,max_2: float,) -> Vector2:
    """."""
    ...
def Vector2Distance(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> float:
    """."""
    ...
def Vector2DistanceSqr(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> float:
    """."""
    ...
def Vector2Divide(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2DotProduct(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> float:
    """."""
    ...
def Vector2Equals(p: Vector2|list|tuple,q: Vector2|list|tuple,) -> int:
    """."""
    ...
def Vector2Invert(v: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2Length(v: Vector2|list|tuple,) -> float:
    """."""
    ...
def Vector2LengthSqr(v: Vector2|list|tuple,) -> float:
    """."""
    ...
def Vector2Lerp(v1: Vector2|list|tuple,v2: Vector2|list|tuple,amount: float,) -> Vector2:
    """."""
    ...
def Vector2LineAngle(start: Vector2|list|tuple,end: Vector2|list|tuple,) -> float:
    """."""
    ...
def Vector2Max(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2Min(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2MoveTowards(v: Vector2|list|tuple,target: Vector2|list|tuple,maxDistance: float,) -> Vector2:
    """."""
    ...
def Vector2Multiply(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2Negate(v: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2Normalize(v: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2One() -> Vector2:
    """."""
    ...
def Vector2Reflect(v: Vector2|list|tuple,normal: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2Refract(v: Vector2|list|tuple,n: Vector2|list|tuple,r: float,) -> Vector2:
    """."""
    ...
def Vector2Rotate(v: Vector2|list|tuple,angle: float,) -> Vector2:
    """."""
    ...
def Vector2Scale(v: Vector2|list|tuple,scale: float,) -> Vector2:
    """."""
    ...
def Vector2Subtract(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2SubtractValue(v: Vector2|list|tuple,sub: float,) -> Vector2:
    """."""
    ...
def Vector2Transform(v: Vector2|list|tuple,mat: Matrix|list|tuple,) -> Vector2:
    """."""
    ...
def Vector2Zero() -> Vector2:
    """."""
    ...
def Vector3Add(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3AddValue(v: Vector3|list|tuple,add: float,) -> Vector3:
    """."""
    ...
def Vector3Angle(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> float:
    """."""
    ...
def Vector3Barycenter(p: Vector3|list|tuple,a: Vector3|list|tuple,b: Vector3|list|tuple,c: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Clamp(v: Vector3|list|tuple,min_1: Vector3|list|tuple,max_2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3ClampValue(v: Vector3|list|tuple,min_1: float,max_2: float,) -> Vector3:
    """."""
    ...
def Vector3CrossProduct(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3CubicHermite(v1: Vector3|list|tuple,tangent1: Vector3|list|tuple,v2: Vector3|list|tuple,tangent2: Vector3|list|tuple,amount: float,) -> Vector3:
    """."""
    ...
def Vector3Distance(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> float:
    """."""
    ...
def Vector3DistanceSqr(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> float:
    """."""
    ...
def Vector3Divide(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3DotProduct(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> float:
    """."""
    ...
def Vector3Equals(p: Vector3|list|tuple,q: Vector3|list|tuple,) -> int:
    """."""
    ...
def Vector3Invert(v: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Length(v: Vector3|list|tuple,) -> float:
    """."""
    ...
def Vector3LengthSqr(v: Vector3|list|tuple,) -> float:
    """."""
    ...
def Vector3Lerp(v1: Vector3|list|tuple,v2: Vector3|list|tuple,amount: float,) -> Vector3:
    """."""
    ...
def Vector3Max(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Min(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3MoveTowards(v: Vector3|list|tuple,target: Vector3|list|tuple,maxDistance: float,) -> Vector3:
    """."""
    ...
def Vector3Multiply(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Negate(v: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Normalize(v: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3One() -> Vector3:
    """."""
    ...
def Vector3OrthoNormalize(v1: Any|list|tuple,v2: Any|list|tuple,) -> None:
    """."""
    ...
def Vector3Perpendicular(v: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Project(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Reflect(v: Vector3|list|tuple,normal: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Refract(v: Vector3|list|tuple,n: Vector3|list|tuple,r: float,) -> Vector3:
    """."""
    ...
def Vector3Reject(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3RotateByAxisAngle(v: Vector3|list|tuple,axis: Vector3|list|tuple,angle: float,) -> Vector3:
    """."""
    ...
def Vector3RotateByQuaternion(v: Vector3|list|tuple,q: Vector4|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Scale(v: Vector3|list|tuple,scalar: float,) -> Vector3:
    """."""
    ...
def Vector3Subtract(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3SubtractValue(v: Vector3|list|tuple,sub: float,) -> Vector3:
    """."""
    ...
def Vector3ToFloatV(v: Vector3|list|tuple,) -> float3:
    """."""
    ...
def Vector3Transform(v: Vector3|list|tuple,mat: Matrix|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Unproject(source: Vector3|list|tuple,projection: Matrix|list|tuple,view: Matrix|list|tuple,) -> Vector3:
    """."""
    ...
def Vector3Zero() -> Vector3:
    """."""
    ...
def Vector4Add(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def Vector4AddValue(v: Vector4|list|tuple,add: float,) -> Vector4:
    """."""
    ...
def Vector4Distance(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> float:
    """."""
    ...
def Vector4DistanceSqr(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> float:
    """."""
    ...
def Vector4Divide(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def Vector4DotProduct(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> float:
    """."""
    ...
def Vector4Equals(p: Vector4|list|tuple,q: Vector4|list|tuple,) -> int:
    """."""
    ...
def Vector4Invert(v: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def Vector4Length(v: Vector4|list|tuple,) -> float:
    """."""
    ...
def Vector4LengthSqr(v: Vector4|list|tuple,) -> float:
    """."""
    ...
def Vector4Lerp(v1: Vector4|list|tuple,v2: Vector4|list|tuple,amount: float,) -> Vector4:
    """."""
    ...
def Vector4Max(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def Vector4Min(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def Vector4MoveTowards(v: Vector4|list|tuple,target: Vector4|list|tuple,maxDistance: float,) -> Vector4:
    """."""
    ...
def Vector4Multiply(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def Vector4Negate(v: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def Vector4Normalize(v: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def Vector4One() -> Vector4:
    """."""
    ...
def Vector4Scale(v: Vector4|list|tuple,scale: float,) -> Vector4:
    """."""
    ...
def Vector4Subtract(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def Vector4SubtractValue(v: Vector4|list|tuple,add: float,) -> Vector4:
    """."""
    ...
def Vector4Zero() -> Vector4:
    """."""
    ...
def WaitTime(seconds: float,) -> None:
    """Wait for some time (halt program execution)."""
    ...
def WaveCopy(wave: Wave|list|tuple,) -> Wave:
    """Copy a wave to a new wave."""
    ...
def WaveCrop(wave: Any|list|tuple,initFrame: int,finalFrame: int,) -> None:
    """Crop a wave to defined frames range."""
    ...
def WaveFormat(wave: Any|list|tuple,sampleRate: int,sampleSize: int,channels: int,) -> None:
    """Convert wave data to desired format."""
    ...
def WindowShouldClose() -> bool:
    """Check if application should close (KEY_ESCAPE pressed or windows close icon clicked)."""
    ...
def Wrap(value: float,min_1: float,max_2: float,) -> float:
    """."""
    ...
def glfwCreateCursor(image: Any|list|tuple,xhot: int,yhot: int,) -> Any:
    """."""
    ...
def glfwCreateStandardCursor(shape: int,) -> Any:
    """."""
    ...
def glfwCreateWindow(width: int,height: int,title: bytes,monitor: Any|list|tuple,share: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwDefaultWindowHints() -> None:
    """."""
    ...
def glfwDestroyCursor(cursor: Any|list|tuple,) -> None:
    """."""
    ...
def glfwDestroyWindow(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwExtensionSupported(extension: bytes,) -> int:
    """."""
    ...
def glfwFocusWindow(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwGetClipboardString(window: Any|list|tuple,) -> bytes:
    """."""
    ...
def glfwGetCurrentContext() -> Any:
    """."""
    ...
def glfwGetCursorPos(window: Any|list|tuple,xpos: Any,ypos: Any,) -> None:
    """."""
    ...
def glfwGetError(description: list[bytes],) -> int:
    """."""
    ...
def glfwGetFramebufferSize(window: Any|list|tuple,width: Any,height: Any,) -> None:
    """."""
    ...
def glfwGetGamepadName(jid: int,) -> bytes:
    """."""
    ...
def glfwGetGamepadState(jid: int,state: Any|list|tuple,) -> int:
    """."""
    ...
def glfwGetGammaRamp(monitor: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwGetInputMode(window: Any|list|tuple,mode: int,) -> int:
    """."""
    ...
def glfwGetJoystickAxes(jid: int,count: Any,) -> Any:
    """."""
    ...
def glfwGetJoystickButtons(jid: int,count: Any,) -> bytes:
    """."""
    ...
def glfwGetJoystickGUID(jid: int,) -> bytes:
    """."""
    ...
def glfwGetJoystickHats(jid: int,count: Any,) -> bytes:
    """."""
    ...
def glfwGetJoystickName(jid: int,) -> bytes:
    """."""
    ...
def glfwGetJoystickUserPointer(jid: int,) -> Any:
    """."""
    ...
def glfwGetKey(window: Any|list|tuple,key: int,) -> int:
    """."""
    ...
def glfwGetKeyName(key: int,scancode: int,) -> bytes:
    """."""
    ...
def glfwGetKeyScancode(key: int,) -> int:
    """."""
    ...
def glfwGetMonitorContentScale(monitor: Any|list|tuple,xscale: Any,yscale: Any,) -> None:
    """."""
    ...
def glfwGetMonitorName(monitor: Any|list|tuple,) -> bytes:
    """."""
    ...
def glfwGetMonitorPhysicalSize(monitor: Any|list|tuple,widthMM: Any,heightMM: Any,) -> None:
    """."""
    ...
def glfwGetMonitorPos(monitor: Any|list|tuple,xpos: Any,ypos: Any,) -> None:
    """."""
    ...
def glfwGetMonitorUserPointer(monitor: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwGetMonitorWorkarea(monitor: Any|list|tuple,xpos: Any,ypos: Any,width: Any,height: Any,) -> None:
    """."""
    ...
def glfwGetMonitors(count: Any,) -> Any:
    """."""
    ...
def glfwGetMouseButton(window: Any|list|tuple,button: int,) -> int:
    """."""
    ...
def glfwGetPlatform() -> int:
    """."""
    ...
def glfwGetPrimaryMonitor() -> Any:
    """."""
    ...
def glfwGetProcAddress(procname: bytes,) -> Any:
    """."""
    ...
def glfwGetRequiredInstanceExtensions(count: Any,) -> list[bytes]:
    """."""
    ...
def glfwGetTime() -> float:
    """."""
    ...
def glfwGetTimerFrequency() -> int:
    """."""
    ...
def glfwGetTimerValue() -> int:
    """."""
    ...
def glfwGetVersion(major: Any,minor: Any,rev: Any,) -> None:
    """."""
    ...
def glfwGetVersionString() -> bytes:
    """."""
    ...
def glfwGetVideoMode(monitor: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwGetVideoModes(monitor: Any|list|tuple,count: Any,) -> Any:
    """."""
    ...
def glfwGetWindowAttrib(window: Any|list|tuple,attrib: int,) -> int:
    """."""
    ...
def glfwGetWindowContentScale(window: Any|list|tuple,xscale: Any,yscale: Any,) -> None:
    """."""
    ...
def glfwGetWindowFrameSize(window: Any|list|tuple,left: Any,top: Any,right: Any,bottom: Any,) -> None:
    """."""
    ...
def glfwGetWindowMonitor(window: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwGetWindowOpacity(window: Any|list|tuple,) -> float:
    """."""
    ...
def glfwGetWindowPos(window: Any|list|tuple,xpos: Any,ypos: Any,) -> None:
    """."""
    ...
def glfwGetWindowSize(window: Any|list|tuple,width: Any,height: Any,) -> None:
    """."""
    ...
def glfwGetWindowTitle(window: Any|list|tuple,) -> bytes:
    """."""
    ...
def glfwGetWindowUserPointer(window: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwHideWindow(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwIconifyWindow(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwInit() -> int:
    """."""
    ...
def glfwInitAllocator(allocator: Any|list|tuple,) -> None:
    """."""
    ...
def glfwInitHint(hint: int,value: int,) -> None:
    """."""
    ...
def glfwJoystickIsGamepad(jid: int,) -> int:
    """."""
    ...
def glfwJoystickPresent(jid: int,) -> int:
    """."""
    ...
def glfwMakeContextCurrent(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwMaximizeWindow(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwPlatformSupported(platform: int,) -> int:
    """."""
    ...
def glfwPollEvents() -> None:
    """."""
    ...
def glfwPostEmptyEvent() -> None:
    """."""
    ...
def glfwRawMouseMotionSupported() -> int:
    """."""
    ...
def glfwRequestWindowAttention(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwRestoreWindow(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwSetCharCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetCharModsCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetClipboardString(window: Any|list|tuple,string: bytes,) -> None:
    """."""
    ...
def glfwSetCursor(window: Any|list|tuple,cursor: Any|list|tuple,) -> None:
    """."""
    ...
def glfwSetCursorEnterCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetCursorPos(window: Any|list|tuple,xpos: float,ypos: float,) -> None:
    """."""
    ...
def glfwSetCursorPosCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetDropCallback(window: Any|list|tuple,callback: list[bytes]|list|tuple,) -> list[bytes]:
    """."""
    ...
def glfwSetErrorCallback(callback: bytes,) -> bytes:
    """."""
    ...
def glfwSetFramebufferSizeCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetGamma(monitor: Any|list|tuple,gamma: float,) -> None:
    """."""
    ...
def glfwSetGammaRamp(monitor: Any|list|tuple,ramp: Any|list|tuple,) -> None:
    """."""
    ...
def glfwSetInputMode(window: Any|list|tuple,mode: int,value: int,) -> None:
    """."""
    ...
def glfwSetJoystickCallback(callback: Any,) -> Any:
    """."""
    ...
def glfwSetJoystickUserPointer(jid: int,pointer: Any,) -> None:
    """."""
    ...
def glfwSetKeyCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetMonitorCallback(callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetMonitorUserPointer(monitor: Any|list|tuple,pointer: Any,) -> None:
    """."""
    ...
def glfwSetMouseButtonCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetScrollCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetTime(time: float,) -> None:
    """."""
    ...
def glfwSetWindowAspectRatio(window: Any|list|tuple,numer: int,denom: int,) -> None:
    """."""
    ...
def glfwSetWindowAttrib(window: Any|list|tuple,attrib: int,value: int,) -> None:
    """."""
    ...
def glfwSetWindowCloseCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetWindowContentScaleCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetWindowFocusCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetWindowIcon(window: Any|list|tuple,count: int,images: Any|list|tuple,) -> None:
    """."""
    ...
def glfwSetWindowIconifyCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetWindowMaximizeCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetWindowMonitor(window: Any|list|tuple,monitor: Any|list|tuple,xpos: int,ypos: int,width: int,height: int,refreshRate: int,) -> None:
    """."""
    ...
def glfwSetWindowOpacity(window: Any|list|tuple,opacity: float,) -> None:
    """."""
    ...
def glfwSetWindowPos(window: Any|list|tuple,xpos: int,ypos: int,) -> None:
    """."""
    ...
def glfwSetWindowPosCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetWindowRefreshCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetWindowShouldClose(window: Any|list|tuple,value: int,) -> None:
    """."""
    ...
def glfwSetWindowSize(window: Any|list|tuple,width: int,height: int,) -> None:
    """."""
    ...
def glfwSetWindowSizeCallback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfwSetWindowSizeLimits(window: Any|list|tuple,minwidth: int,minheight: int,maxwidth: int,maxheight: int,) -> None:
    """."""
    ...
def glfwSetWindowTitle(window: Any|list|tuple,title: bytes,) -> None:
    """."""
    ...
def glfwSetWindowUserPointer(window: Any|list|tuple,pointer: Any,) -> None:
    """."""
    ...
def glfwShowWindow(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwSwapBuffers(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfwSwapInterval(interval: int,) -> None:
    """."""
    ...
def glfwTerminate() -> None:
    """."""
    ...
def glfwUpdateGamepadMappings(string: bytes,) -> int:
    """."""
    ...
def glfwVulkanSupported() -> int:
    """."""
    ...
def glfwWaitEvents() -> None:
    """."""
    ...
def glfwWaitEventsTimeout(timeout: float,) -> None:
    """."""
    ...
def glfwWindowHint(hint: int,value: int,) -> None:
    """."""
    ...
def glfwWindowHintString(hint: int,value: bytes,) -> None:
    """."""
    ...
def glfwWindowShouldClose(window: Any|list|tuple,) -> int:
    """."""
    ...
def rlActiveDrawBuffers(count: int,) -> None:
    """Activate multiple draw color buffers."""
    ...
def rlActiveTextureSlot(slot: int,) -> None:
    """Select and active a texture slot."""
    ...
def rlBegin(mode: int,) -> None:
    """Initialize drawing mode (how to organize vertex)."""
    ...
def rlBindFramebuffer(target: int,framebuffer: int,) -> None:
    """Bind framebuffer (FBO)."""
    ...
def rlBindImageTexture(id: int,index: int,format: int,readonly: bool,) -> None:
    """Bind image texture."""
    ...
def rlBindShaderBuffer(id: int,index: int,) -> None:
    """Bind SSBO buffer."""
    ...
def rlBlitFramebuffer(srcX: int,srcY: int,srcWidth: int,srcHeight: int,dstX: int,dstY: int,dstWidth: int,dstHeight: int,bufferMask: int,) -> None:
    """Blit active framebuffer to main framebuffer."""
    ...
def rlCheckErrors() -> None:
    """Check and log OpenGL error codes."""
    ...
def rlCheckRenderBatchLimit(vCount: int,) -> bool:
    """Check internal buffer overflow for a given number of vertex."""
    ...
def rlClearColor(r: bytes,g: bytes,b: bytes,a: bytes,) -> None:
    """Clear color buffer with color."""
    ...
def rlClearScreenBuffers() -> None:
    """Clear used screen buffers (color and depth)."""
    ...
def rlColor3f(x: float,y: float,z: float,) -> None:
    """Define one vertex (color) - 3 float."""
    ...
def rlColor4f(x: float,y: float,z: float,w: float,) -> None:
    """Define one vertex (color) - 4 float."""
    ...
def rlColor4ub(r: bytes,g: bytes,b: bytes,a: bytes,) -> None:
    """Define one vertex (color) - 4 byte."""
    ...
def rlColorMask(r: bool,g: bool,b: bool,a: bool,) -> None:
    """Color mask control."""
    ...
def rlCompileShader(shaderCode: bytes,type: int,) -> int:
    """Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)."""
    ...
def rlComputeShaderDispatch(groupX: int,groupY: int,groupZ: int,) -> None:
    """Dispatch compute shader (equivalent to *draw* for graphics pipeline)."""
    ...
def rlCopyShaderBuffer(destId: int,srcId: int,destOffset: int,srcOffset: int,count: int,) -> None:
    """Copy SSBO data between buffers."""
    ...
def rlCubemapParameters(id: int,param: int,value: int,) -> None:
    """Set cubemap parameters (filter, wrap)."""
    ...
def rlDisableBackfaceCulling() -> None:
    """Disable backface culling."""
    ...
def rlDisableColorBlend() -> None:
    """Disable color blending."""
    ...
def rlDisableDepthMask() -> None:
    """Disable depth write."""
    ...
def rlDisableDepthTest() -> None:
    """Disable depth test."""
    ...
def rlDisableFramebuffer() -> None:
    """Disable render texture (fbo), return to default framebuffer."""
    ...
def rlDisableScissorTest() -> None:
    """Disable scissor test."""
    ...
def rlDisableShader() -> None:
    """Disable shader program."""
    ...
def rlDisableSmoothLines() -> None:
    """Disable line aliasing."""
    ...
def rlDisableStereoRender() -> None:
    """Disable stereo rendering."""
    ...
def rlDisableTexture() -> None:
    """Disable texture."""
    ...
def rlDisableTextureCubemap() -> None:
    """Disable texture cubemap."""
    ...
def rlDisableVertexArray() -> None:
    """Disable vertex array (VAO, if supported)."""
    ...
def rlDisableVertexAttribute(index: int,) -> None:
    """Disable vertex attribute index."""
    ...
def rlDisableVertexBuffer() -> None:
    """Disable vertex buffer (VBO)."""
    ...
def rlDisableVertexBufferElement() -> None:
    """Disable vertex buffer element (VBO element)."""
    ...
def rlDisableWireMode() -> None:
    """Disable wire (and point) mode."""
    ...
def rlDrawRenderBatch(batch: Any|list|tuple,) -> None:
    """Draw render batch data (Update->Draw->Reset)."""
    ...
def rlDrawRenderBatchActive() -> None:
    """Update and draw internal render batch."""
    ...
def rlDrawVertexArray(offset: int,count: int,) -> None:
    """Draw vertex array (currently active vao)."""
    ...
def rlDrawVertexArrayElements(offset: int,count: int,buffer: Any,) -> None:
    """Draw vertex array elements."""
    ...
def rlDrawVertexArrayElementsInstanced(offset: int,count: int,buffer: Any,instances: int,) -> None:
    """Draw vertex array elements with instancing."""
    ...
def rlDrawVertexArrayInstanced(offset: int,count: int,instances: int,) -> None:
    """Draw vertex array (currently active vao) with instancing."""
    ...
def rlEnableBackfaceCulling() -> None:
    """Enable backface culling."""
    ...
def rlEnableColorBlend() -> None:
    """Enable color blending."""
    ...
def rlEnableDepthMask() -> None:
    """Enable depth write."""
    ...
def rlEnableDepthTest() -> None:
    """Enable depth test."""
    ...
def rlEnableFramebuffer(id: int,) -> None:
    """Enable render texture (fbo)."""
    ...
def rlEnablePointMode() -> None:
    """Enable point mode."""
    ...
def rlEnableScissorTest() -> None:
    """Enable scissor test."""
    ...
def rlEnableShader(id: int,) -> None:
    """Enable shader program."""
    ...
def rlEnableSmoothLines() -> None:
    """Enable line aliasing."""
    ...
def rlEnableStereoRender() -> None:
    """Enable stereo rendering."""
    ...
def rlEnableTexture(id: int,) -> None:
    """Enable texture."""
    ...
def rlEnableTextureCubemap(id: int,) -> None:
    """Enable texture cubemap."""
    ...
def rlEnableVertexArray(vaoId: int,) -> bool:
    """Enable vertex array (VAO, if supported)."""
    ...
def rlEnableVertexAttribute(index: int,) -> None:
    """Enable vertex attribute index."""
    ...
def rlEnableVertexBuffer(id: int,) -> None:
    """Enable vertex buffer (VBO)."""
    ...
def rlEnableVertexBufferElement(id: int,) -> None:
    """Enable vertex buffer element (VBO element)."""
    ...
def rlEnableWireMode() -> None:
    """Enable wire mode."""
    ...
def rlEnd() -> None:
    """Finish vertex providing."""
    ...
def rlFramebufferAttach(fboId: int,texId: int,attachType: int,texType: int,mipLevel: int,) -> None:
    """Attach texture/renderbuffer to a framebuffer."""
    ...
def rlFramebufferComplete(id: int,) -> bool:
    """Verify framebuffer is complete."""
    ...
def rlFrustum(left: float,right: float,bottom: float,top: float,znear: float,zfar: float,) -> None:
    """."""
    ...
def rlGenTextureMipmaps(id: int,width: int,height: int,format: int,mipmaps: Any,) -> None:
    """Generate mipmap data for selected texture."""
    ...
def rlGetActiveFramebuffer() -> int:
    """Get the currently active render texture (fbo), 0 for default framebuffer."""
    ...
def rlGetCullDistanceFar() -> float:
    """Get cull plane distance far."""
    ...
def rlGetCullDistanceNear() -> float:
    """Get cull plane distance near."""
    ...
def rlGetFramebufferHeight() -> int:
    """Get default framebuffer height."""
    ...
def rlGetFramebufferWidth() -> int:
    """Get default framebuffer width."""
    ...
def rlGetGlTextureFormats(format: int,glInternalFormat: Any,glFormat: Any,glType: Any,) -> None:
    """Get OpenGL internal formats."""
    ...
def rlGetLineWidth() -> float:
    """Get the line drawing width."""
    ...
def rlGetLocationAttrib(shaderId: int,attribName: bytes,) -> int:
    """Get shader location attribute."""
    ...
def rlGetLocationUniform(shaderId: int,uniformName: bytes,) -> int:
    """Get shader location uniform."""
    ...
def rlGetMatrixModelview() -> Matrix:
    """Get internal modelview matrix."""
    ...
def rlGetMatrixProjection() -> Matrix:
    """Get internal projection matrix."""
    ...
def rlGetMatrixProjectionStereo(eye: int,) -> Matrix:
    """Get internal projection matrix for stereo render (selected eye)."""
    ...
def rlGetMatrixTransform() -> Matrix:
    """Get internal accumulated transform matrix."""
    ...
def rlGetMatrixViewOffsetStereo(eye: int,) -> Matrix:
    """Get internal view offset matrix for stereo render (selected eye)."""
    ...
def rlGetPixelFormatName(format: int,) -> bytes:
    """Get name string for pixel format."""
    ...
def rlGetShaderBufferSize(id: int,) -> int:
    """Get SSBO buffer size."""
    ...
def rlGetShaderIdDefault() -> int:
    """Get default shader id."""
    ...
def rlGetShaderLocsDefault() -> Any:
    """Get default shader locations."""
    ...
def rlGetTextureIdDefault() -> int:
    """Get default texture id."""
    ...
def rlGetVersion() -> int:
    """Get current OpenGL version."""
    ...
def rlIsStereoRenderEnabled() -> bool:
    """Check if stereo render is enabled."""
    ...
def rlLoadComputeShaderProgram(shaderId: int,) -> int:
    """Load compute shader program."""
    ...
def rlLoadDrawCube() -> None:
    """Load and draw a cube."""
    ...
def rlLoadDrawQuad() -> None:
    """Load and draw a quad."""
    ...
def rlLoadExtensions(loader: Any,) -> None:
    """Load OpenGL extensions (loader function required)."""
    ...
def rlLoadFramebuffer() -> int:
    """Load an empty framebuffer."""
    ...
def rlLoadIdentity() -> None:
    """Reset current matrix to identity matrix."""
    ...
def rlLoadRenderBatch(numBuffers: int,bufferElements: int,) -> rlRenderBatch:
    """Load a render batch system."""
    ...
def rlLoadShaderBuffer(size: int,data: Any,usageHint: int,) -> int:
    """Load shader storage buffer object (SSBO)."""
    ...
def rlLoadShaderCode(vsCode: bytes,fsCode: bytes,) -> int:
    """Load shader from code strings."""
    ...
def rlLoadShaderProgram(vShaderId: int,fShaderId: int,) -> int:
    """Load custom shader program."""
    ...
def rlLoadTexture(data: Any,width: int,height: int,format: int,mipmapCount: int,) -> int:
    """Load texture data."""
    ...
def rlLoadTextureCubemap(data: Any,size: int,format: int,mipmapCount: int,) -> int:
    """Load texture cubemap data."""
    ...
def rlLoadTextureDepth(width: int,height: int,useRenderBuffer: bool,) -> int:
    """Load depth texture/renderbuffer (to be attached to fbo)."""
    ...
def rlLoadVertexArray() -> int:
    """Load vertex array (vao) if supported."""
    ...
def rlLoadVertexBuffer(buffer: Any,size: int,dynamic: bool,) -> int:
    """Load a vertex buffer object."""
    ...
def rlLoadVertexBufferElement(buffer: Any,size: int,dynamic: bool,) -> int:
    """Load vertex buffer elements object."""
    ...
def rlMatrixMode(mode: int,) -> None:
    """Choose the current matrix to be transformed."""
    ...
def rlMultMatrixf(matf: Any,) -> None:
    """Multiply the current matrix by another matrix."""
    ...
def rlNormal3f(x: float,y: float,z: float,) -> None:
    """Define one vertex (normal) - 3 float."""
    ...
def rlOrtho(left: float,right: float,bottom: float,top: float,znear: float,zfar: float,) -> None:
    """."""
    ...
def rlPopMatrix() -> None:
    """Pop latest inserted matrix from stack."""
    ...
def rlPushMatrix() -> None:
    """Push the current matrix to stack."""
    ...
def rlReadScreenPixels(width: int,height: int,) -> bytes:
    """Read screen pixel data (color buffer)."""
    ...
def rlReadShaderBuffer(id: int,dest: Any,count: int,offset: int,) -> None:
    """Read SSBO buffer data (GPU->CPU)."""
    ...
def rlReadTexturePixels(id: int,width: int,height: int,format: int,) -> Any:
    """Read texture pixel data."""
    ...
def rlRotatef(angle: float,x: float,y: float,z: float,) -> None:
    """Multiply the current matrix by a rotation matrix."""
    ...
def rlScalef(x: float,y: float,z: float,) -> None:
    """Multiply the current matrix by a scaling matrix."""
    ...
def rlScissor(x: int,y: int,width: int,height: int,) -> None:
    """Scissor test."""
    ...
def rlSetBlendFactors(glSrcFactor: int,glDstFactor: int,glEquation: int,) -> None:
    """Set blending mode factor and equation (using OpenGL factors)."""
    ...
def rlSetBlendFactorsSeparate(glSrcRGB: int,glDstRGB: int,glSrcAlpha: int,glDstAlpha: int,glEqRGB: int,glEqAlpha: int,) -> None:
    """Set blending mode factors and equations separately (using OpenGL factors)."""
    ...
def rlSetBlendMode(mode: int,) -> None:
    """Set blending mode."""
    ...
def rlSetClipPlanes(nearPlane: float,farPlane: float,) -> None:
    """Set clip planes distances."""
    ...
def rlSetCullFace(mode: int,) -> None:
    """Set face culling mode."""
    ...
def rlSetFramebufferHeight(height: int,) -> None:
    """Set current framebuffer height."""
    ...
def rlSetFramebufferWidth(width: int,) -> None:
    """Set current framebuffer width."""
    ...
def rlSetLineWidth(width: float,) -> None:
    """Set the line drawing width."""
    ...
def rlSetMatrixModelview(view: Matrix|list|tuple,) -> None:
    """Set a custom modelview matrix (replaces internal modelview matrix)."""
    ...
def rlSetMatrixProjection(proj: Matrix|list|tuple,) -> None:
    """Set a custom projection matrix (replaces internal projection matrix)."""
    ...
def rlSetMatrixProjectionStereo(right: Matrix|list|tuple,left: Matrix|list|tuple,) -> None:
    """Set eyes projection matrices for stereo rendering."""
    ...
def rlSetMatrixViewOffsetStereo(right: Matrix|list|tuple,left: Matrix|list|tuple,) -> None:
    """Set eyes view offsets matrices for stereo rendering."""
    ...
def rlSetRenderBatchActive(batch: Any|list|tuple,) -> None:
    """Set the active render batch for rlgl (NULL for default internal)."""
    ...
def rlSetShader(id: int,locs: Any,) -> None:
    """Set shader currently active (id and locations)."""
    ...
def rlSetTexture(id: int,) -> None:
    """Set current texture for render batch and check buffers limits."""
    ...
def rlSetUniform(locIndex: int,value: Any,uniformType: int,count: int,) -> None:
    """Set shader value uniform."""
    ...
def rlSetUniformMatrices(locIndex: int,mat: Any|list|tuple,count: int,) -> None:
    """Set shader value matrices."""
    ...
def rlSetUniformMatrix(locIndex: int,mat: Matrix|list|tuple,) -> None:
    """Set shader value matrix."""
    ...
def rlSetUniformSampler(locIndex: int,textureId: int,) -> None:
    """Set shader value sampler."""
    ...
def rlSetVertexAttribute(index: int,compSize: int,type: int,normalized: bool,stride: int,offset: int,) -> None:
    """Set vertex attribute data configuration."""
    ...
def rlSetVertexAttributeDefault(locIndex: int,value: Any,attribType: int,count: int,) -> None:
    """Set vertex attribute default value, when attribute to provided."""
    ...
def rlSetVertexAttributeDivisor(index: int,divisor: int,) -> None:
    """Set vertex attribute data divisor."""
    ...
def rlTexCoord2f(x: float,y: float,) -> None:
    """Define one vertex (texture coordinate) - 2 float."""
    ...
def rlTextureParameters(id: int,param: int,value: int,) -> None:
    """Set texture parameters (filter, wrap)."""
    ...
def rlTranslatef(x: float,y: float,z: float,) -> None:
    """Multiply the current matrix by a translation matrix."""
    ...
def rlUnloadFramebuffer(id: int,) -> None:
    """Delete framebuffer from GPU."""
    ...
def rlUnloadRenderBatch(batch: rlRenderBatch|list|tuple,) -> None:
    """Unload render batch system."""
    ...
def rlUnloadShaderBuffer(ssboId: int,) -> None:
    """Unload shader storage buffer object (SSBO)."""
    ...
def rlUnloadShaderProgram(id: int,) -> None:
    """Unload shader program."""
    ...
def rlUnloadTexture(id: int,) -> None:
    """Unload texture from GPU memory."""
    ...
def rlUnloadVertexArray(vaoId: int,) -> None:
    """Unload vertex array (vao)."""
    ...
def rlUnloadVertexBuffer(vboId: int,) -> None:
    """Unload vertex buffer object."""
    ...
def rlUpdateShaderBuffer(id: int,data: Any,dataSize: int,offset: int,) -> None:
    """Update SSBO buffer data."""
    ...
def rlUpdateTexture(id: int,offsetX: int,offsetY: int,width: int,height: int,format: int,data: Any,) -> None:
    """Update texture with new data on GPU."""
    ...
def rlUpdateVertexBuffer(bufferId: int,data: Any,dataSize: int,offset: int,) -> None:
    """Update vertex buffer object data on GPU buffer."""
    ...
def rlUpdateVertexBufferElements(id: int,data: Any,dataSize: int,offset: int,) -> None:
    """Update vertex buffer elements data on GPU buffer."""
    ...
def rlVertex2f(x: float,y: float,) -> None:
    """Define one vertex (position) - 2 float."""
    ...
def rlVertex2i(x: int,y: int,) -> None:
    """Define one vertex (position) - 2 int."""
    ...
def rlVertex3f(x: float,y: float,z: float,) -> None:
    """Define one vertex (position) - 3 float."""
    ...
def rlViewport(x: int,y: int,width: int,height: int,) -> None:
    """Set the viewport area."""
    ...
def rlglClose() -> None:
    """De-initialize rlgl (buffers, shaders, textures)."""
    ...
def rlglInit(width: int,height: int,) -> None:
    """Initialize rlgl (buffers, shaders, textures, states)."""
    ...
class AudioStream:
    buffer: Any
    processor: Any
    sampleRate: int
    sampleSize: int
    channels: int
class AutomationEvent:
    frame: int
    type: int
    params: list
class AutomationEventList:
    capacity: int
    count: int
    events: Any
BlendMode = int
class BoneInfo:
    name: bytes
    parent: int
class BoundingBox:
    min: Vector3
    max: Vector3
class Camera:
    position: Vector3
    target: Vector3
    up: Vector3
    fovy: float
    projection: int
class Camera2D:
    offset: Vector2
    target: Vector2
    rotation: float
    zoom: float
class Camera3D:
    position: Vector3
    target: Vector3
    up: Vector3
    fovy: float
    projection: int
CameraMode = int
CameraProjection = int
class Color:
    r: bytes
    g: bytes
    b: bytes
    a: bytes
ConfigFlags = int
CubemapLayout = int
class FilePathList:
    capacity: int
    count: int
    paths: list[bytes]
class Font:
    baseSize: int
    glyphCount: int
    glyphPadding: int
    texture: Texture
    recs: Any
    glyphs: Any
FontType = int
class GLFWallocator:
    allocate: Any
    reallocate: Any
    deallocate: Any
    user: Any
class GLFWcursor:
    ...
class GLFWgamepadstate:
    buttons: bytes
    axes: list
class GLFWgammaramp:
    red: Any
    green: Any
    blue: Any
    size: int
class GLFWimage:
    width: int
    height: int
    pixels: bytes
class GLFWmonitor:
    ...
class GLFWvidmode:
    width: int
    height: int
    redBits: int
    greenBits: int
    blueBits: int
    refreshRate: int
class GLFWwindow:
    ...
GamepadAxis = int
GamepadButton = int
Gesture = int
class GlyphInfo:
    value: int
    offsetX: int
    offsetY: int
    advanceX: int
    image: Image
GuiCheckBoxProperty = int
GuiColorPickerProperty = int
GuiComboBoxProperty = int
GuiControl = int
GuiControlProperty = int
GuiDefaultProperty = int
GuiDropdownBoxProperty = int
GuiIconName = int
GuiListViewProperty = int
GuiProgressBarProperty = int
GuiScrollBarProperty = int
GuiSliderProperty = int
GuiSpinnerProperty = int
GuiState = int
class GuiStyleProp:
    controlId: int
    propertyId: int
    propertyValue: int
GuiTextAlignment = int
GuiTextAlignmentVertical = int
GuiTextBoxProperty = int
GuiTextWrapMode = int
GuiToggleProperty = int
class Image:
    data: Any
    width: int
    height: int
    mipmaps: int
    format: int
KeyboardKey = int
class Mat2:
    m00: float
    m01: float
    m10: float
    m11: float
class Material:
    shader: Shader
    maps: Any
    params: list
class MaterialMap:
    texture: Texture
    color: Color
    value: float
MaterialMapIndex = int
class Matrix:
    m0: float
    m4: float
    m8: float
    m12: float
    m1: float
    m5: float
    m9: float
    m13: float
    m2: float
    m6: float
    m10: float
    m14: float
    m3: float
    m7: float
    m11: float
    m15: float
class Mesh:
    vertexCount: int
    triangleCount: int
    vertices: Any
    texcoords: Any
    texcoords2: Any
    normals: Any
    tangents: Any
    colors: bytes
    indices: Any
    animVertices: Any
    animNormals: Any
    boneIds: bytes
    boneWeights: Any
    boneMatrices: Any
    boneCount: int
    vaoId: int
    vboId: Any
class Model:
    transform: Matrix
    meshCount: int
    materialCount: int
    meshes: Any
    materials: Any
    meshMaterial: Any
    boneCount: int
    bones: Any
    bindPose: Any
class ModelAnimation:
    boneCount: int
    frameCount: int
    bones: Any
    framePoses: Any
    name: bytes
MouseButton = int
MouseCursor = int
class Music:
    stream: AudioStream
    frameCount: int
    looping: bool
    ctxType: int
    ctxData: Any
class NPatchInfo:
    source: Rectangle
    left: int
    top: int
    right: int
    bottom: int
    layout: int
NPatchLayout = int
class PhysicsBodyData:
    id: int
    enabled: bool
    position: Vector2
    velocity: Vector2
    force: Vector2
    angularVelocity: float
    torque: float
    orient: float
    inertia: float
    inverseInertia: float
    mass: float
    inverseMass: float
    staticFriction: float
    dynamicFriction: float
    restitution: float
    useGravity: bool
    isGrounded: bool
    freezeOrient: bool
    shape: PhysicsShape
class PhysicsManifoldData:
    id: int
    bodyA: Any
    bodyB: Any
    penetration: float
    normal: Vector2
    contacts: list
    contactsCount: int
    restitution: float
    dynamicFriction: float
    staticFriction: float
class PhysicsShape:
    type: PhysicsShapeType
    body: Any
    radius: float
    transform: Mat2
    vertexData: PolygonData
PhysicsShapeType = int
PixelFormat = int
class PolygonData:
    vertexCount: int
    positions: list
    normals: list
class Quaternion:
    x: float
    y: float
    z: float
    w: float
class Ray:
    position: Vector3
    direction: Vector3
class RayCollision:
    hit: bool
    distance: float
    point: Vector3
    normal: Vector3
class Rectangle:
    x: float
    y: float
    width: float
    height: float
class RenderTexture:
    id: int
    texture: Texture
    depth: Texture
class RenderTexture2D:
    id: int
    texture: Texture
    depth: Texture
class Shader:
    id: int
    locs: Any
ShaderAttributeDataType = int
ShaderLocationIndex = int
ShaderUniformDataType = int
class Sound:
    stream: AudioStream
    frameCount: int
class Texture:
    id: int
    width: int
    height: int
    mipmaps: int
    format: int
class Texture2D:
    id: int
    width: int
    height: int
    mipmaps: int
    format: int
class TextureCubemap:
    id: int
    width: int
    height: int
    mipmaps: int
    format: int
TextureFilter = int
TextureWrap = int
TraceLogLevel = int
class Transform:
    translation: Vector3
    rotation: Vector4
    scale: Vector3
class Vector2:
    x: float
    y: float
class Vector3:
    x: float
    y: float
    z: float
class Vector4:
    x: float
    y: float
    z: float
    w: float
class VrDeviceInfo:
    hResolution: int
    vResolution: int
    hScreenSize: float
    vScreenSize: float
    eyeToScreenDistance: float
    lensSeparationDistance: float
    interpupillaryDistance: float
    lensDistortionValues: list
    chromaAbCorrection: list
class VrStereoConfig:
    projection: list
    viewOffset: list
    leftLensCenter: list
    rightLensCenter: list
    leftScreenCenter: list
    rightScreenCenter: list
    scale: list
    scaleIn: list
class Wave:
    frameCount: int
    sampleRate: int
    sampleSize: int
    channels: int
    data: Any
class float16:
    v: list
class float3:
    v: list
class rAudioBuffer:
    ...
class rAudioProcessor:
    ...
rlBlendMode = int
rlCullMode = int
class rlDrawCall:
    mode: int
    vertexCount: int
    vertexAlignment: int
    textureId: int
rlFramebufferAttachTextureType = int
rlFramebufferAttachType = int
rlGlVersion = int
rlPixelFormat = int
class rlRenderBatch:
    bufferCount: int
    currentBuffer: int
    vertexBuffer: Any
    draws: Any
    drawCounter: int
    currentDepth: float
rlShaderAttributeDataType = int
rlShaderLocationIndex = int
rlShaderUniformDataType = int
rlTextureFilter = int
rlTraceLogLevel = int
class rlVertexBuffer:
    elementCount: int
    vertices: Any
    texcoords: Any
    normals: Any
    colors: bytes
    indices: Any
    vaoId: int
    vboId: list

LIGHTGRAY  : Color
GRAY       : Color
DARKGRAY   : Color
YELLOW     : Color
GOLD       : Color
ORANGE     : Color
PINK       : Color
RED        : Color
MAROON     : Color
GREEN      : Color
LIME       : Color
DARKGREEN  : Color
SKYBLUE    : Color
BLUE       : Color
DARKBLUE   : Color
PURPLE     : Color
VIOLET     : Color
DARKPURPLE : Color
BEIGE      : Color
BROWN      : Color
DARKBROWN  : Color
WHITE      : Color
BLACK      : Color
BLANK      : Color
MAGENTA    : Color
RAYWHITE   : Color


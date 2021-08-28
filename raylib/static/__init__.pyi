from typing import Any

class struct: ...


BLEND_ADDITIVE: int
BLEND_ADD_COLORS: int
BLEND_ALPHA: int
BLEND_CUSTOM: int
BLEND_MULTIPLIED: int
BLEND_SUBTRACT_COLORS: int
def BeginBlendMode(int_0: int,) -> None:
        """void BeginBlendMode(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def BeginDrawing() -> None:
        """void BeginDrawing();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def BeginMode2D(Camera2D_0: Camera2D,) -> None:
        """void BeginMode2D(struct Camera2D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def BeginMode3D(Camera3D_0: Camera3D,) -> None:
        """void BeginMode3D(struct Camera3D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def BeginScissorMode(int_0: int,int_1: int,int_2: int,int_3: int,) -> None:
        """void BeginScissorMode(int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def BeginShaderMode(Shader_0: Shader,) -> None:
        """void BeginShaderMode(struct Shader);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def BeginTextureMode(RenderTexture_0: RenderTexture,) -> None:
        """void BeginTextureMode(struct RenderTexture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def BeginVrStereoMode(VrStereoConfig_0: VrStereoConfig,) -> None:
        """void BeginVrStereoMode(struct VrStereoConfig);

CFFI C function from raylib.static._raylib_cffi.lib"""
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
def ChangeDirectory(str_0: str,) -> bool:
        """_Bool ChangeDirectory(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionBoxSphere(BoundingBox_0: BoundingBox,Vector3_1: Vector3,float_2: float,) -> bool:
        """_Bool CheckCollisionBoxSphere(struct BoundingBox, struct Vector3, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionBoxes(BoundingBox_0: BoundingBox,BoundingBox_1: BoundingBox,) -> bool:
        """_Bool CheckCollisionBoxes(struct BoundingBox, struct BoundingBox);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionCircleRec(Vector2_0: Vector2,float_1: float,Rectangle_2: Rectangle,) -> bool:
        """_Bool CheckCollisionCircleRec(struct Vector2, float, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionCircles(Vector2_0: Vector2,float_1: float,Vector2_2: Vector2,float_3: float,) -> bool:
        """_Bool CheckCollisionCircles(struct Vector2, float, struct Vector2, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionLines(Vector2_0: Vector2,Vector2_1: Vector2,Vector2_2: Vector2,Vector2_3: Vector2,Vector2_pointer_4: Any,) -> bool:
        """_Bool CheckCollisionLines(struct Vector2, struct Vector2, struct Vector2, struct Vector2, struct Vector2 *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionPointCircle(Vector2_0: Vector2,Vector2_1: Vector2,float_2: float,) -> bool:
        """_Bool CheckCollisionPointCircle(struct Vector2, struct Vector2, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionPointRec(Vector2_0: Vector2,Rectangle_1: Rectangle,) -> bool:
        """_Bool CheckCollisionPointRec(struct Vector2, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionPointTriangle(Vector2_0: Vector2,Vector2_1: Vector2,Vector2_2: Vector2,Vector2_3: Vector2,) -> bool:
        """_Bool CheckCollisionPointTriangle(struct Vector2, struct Vector2, struct Vector2, struct Vector2);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionRayBox(Ray_0: Ray,BoundingBox_1: BoundingBox,) -> bool:
        """_Bool CheckCollisionRayBox(struct Ray, struct BoundingBox);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionRaySphere(Ray_0: Ray,Vector3_1: Vector3,float_2: float,) -> bool:
        """_Bool CheckCollisionRaySphere(struct Ray, struct Vector3, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionRaySphereEx(Ray_0: Ray,Vector3_1: Vector3,float_2: float,Vector3_pointer_3: Any,) -> bool:
        """_Bool CheckCollisionRaySphereEx(struct Ray, struct Vector3, float, struct Vector3 *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionRecs(Rectangle_0: Rectangle,Rectangle_1: Rectangle,) -> bool:
        """_Bool CheckCollisionRecs(struct Rectangle, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CheckCollisionSpheres(Vector3_0: Vector3,float_1: float,Vector3_2: Vector3,float_3: float,) -> bool:
        """_Bool CheckCollisionSpheres(struct Vector3, float, struct Vector3, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ClearBackground(Color_0: Color,) -> None:
        """void ClearBackground(struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ClearDirectoryFiles() -> None:
        """void ClearDirectoryFiles();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ClearDroppedFiles() -> None:
        """void ClearDroppedFiles();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ClearWindowState(unsignedint_0: int,) -> None:
        """void ClearWindowState(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CloseAudioDevice() -> None:
        """void CloseAudioDevice();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CloseAudioStream(AudioStream_0: AudioStream,) -> None:
        """void CloseAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CloseWindow() -> None:
        """void CloseWindow();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CodepointToUtf8(int_0: int,int_pointer_1: Any,) -> str:
        """char *CodepointToUtf8(int, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ColorAlpha(Color_0: Color,float_1: float,) -> Color:
        """struct Color ColorAlpha(struct Color, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ColorAlphaBlend(Color_0: Color,Color_1: Color,Color_2: Color,) -> Color:
        """struct Color ColorAlphaBlend(struct Color, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ColorFromHSV(float_0: float,float_1: float,float_2: float,) -> Color:
        """struct Color ColorFromHSV(float, float, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ColorFromNormalized(Vector4_0: Vector4,) -> Color:
        """struct Color ColorFromNormalized(struct Vector4);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ColorNormalize(Color_0: Color,) -> Vector4:
        """struct Vector4 ColorNormalize(struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ColorToHSV(Color_0: Color,) -> Vector3:
        """struct Vector3 ColorToHSV(struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ColorToInt(Color_0: Color,) -> int:
        """int ColorToInt(struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def CompressData(unsignedstr_0: str,int_1: int,int_pointer_2: Any,) -> str:
        """unsigned char *CompressData(unsigned char *, int, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DecompressData(unsignedstr_0: str,int_1: int,int_pointer_2: Any,) -> str:
        """unsigned char *DecompressData(unsigned char *, int, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DirectoryExists(str_0: str,) -> bool:
        """_Bool DirectoryExists(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DisableCursor() -> None:
        """void DisableCursor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawBillboard(Camera3D_0: Camera3D,Texture_1: Texture,Vector3_2: Vector3,float_3: float,Color_4: Color,) -> None:
        """void DrawBillboard(struct Camera3D, struct Texture, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawBillboardRec(Camera3D_0: Camera3D,Texture_1: Texture,Rectangle_2: Rectangle,Vector3_3: Vector3,float_4: float,Color_5: Color,) -> None:
        """void DrawBillboardRec(struct Camera3D, struct Texture, struct Rectangle, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawBoundingBox(BoundingBox_0: BoundingBox,Color_1: Color,) -> None:
        """void DrawBoundingBox(struct BoundingBox, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCircle(int_0: int,int_1: int,float_2: float,Color_3: Color,) -> None:
        """void DrawCircle(int, int, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCircle3D(Vector3_0: Vector3,float_1: float,Vector3_2: Vector3,float_3: float,Color_4: Color,) -> None:
        """void DrawCircle3D(struct Vector3, float, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCircleGradient(int_0: int,int_1: int,float_2: float,Color_3: Color,Color_4: Color,) -> None:
        """void DrawCircleGradient(int, int, float, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCircleLines(int_0: int,int_1: int,float_2: float,Color_3: Color,) -> None:
        """void DrawCircleLines(int, int, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCircleSector(Vector2_0: Vector2,float_1: float,float_2: float,float_3: float,int_4: int,Color_5: Color,) -> None:
        """void DrawCircleSector(struct Vector2, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCircleSectorLines(Vector2_0: Vector2,float_1: float,float_2: float,float_3: float,int_4: int,Color_5: Color,) -> None:
        """void DrawCircleSectorLines(struct Vector2, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCircleV(Vector2_0: Vector2,float_1: float,Color_2: Color,) -> None:
        """void DrawCircleV(struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCube(Vector3_0: Vector3,float_1: float,float_2: float,float_3: float,Color_4: Color,) -> None:
        """void DrawCube(struct Vector3, float, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCubeTexture(Texture_0: Texture,Vector3_1: Vector3,float_2: float,float_3: float,float_4: float,Color_5: Color,) -> None:
        """void DrawCubeTexture(struct Texture, struct Vector3, float, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCubeV(Vector3_0: Vector3,Vector3_1: Vector3,Color_2: Color,) -> None:
        """void DrawCubeV(struct Vector3, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCubeWires(Vector3_0: Vector3,float_1: float,float_2: float,float_3: float,Color_4: Color,) -> None:
        """void DrawCubeWires(struct Vector3, float, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCubeWiresV(Vector3_0: Vector3,Vector3_1: Vector3,Color_2: Color,) -> None:
        """void DrawCubeWiresV(struct Vector3, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCylinder(Vector3_0: Vector3,float_1: float,float_2: float,float_3: float,int_4: int,Color_5: Color,) -> None:
        """void DrawCylinder(struct Vector3, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawCylinderWires(Vector3_0: Vector3,float_1: float,float_2: float,float_3: float,int_4: int,Color_5: Color,) -> None:
        """void DrawCylinderWires(struct Vector3, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawEllipse(int_0: int,int_1: int,float_2: float,float_3: float,Color_4: Color,) -> None:
        """void DrawEllipse(int, int, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawEllipseLines(int_0: int,int_1: int,float_2: float,float_3: float,Color_4: Color,) -> None:
        """void DrawEllipseLines(int, int, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawFPS(int_0: int,int_1: int,) -> None:
        """void DrawFPS(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawGrid(int_0: int,float_1: float,) -> None:
        """void DrawGrid(int, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawLine(int_0: int,int_1: int,int_2: int,int_3: int,Color_4: Color,) -> None:
        """void DrawLine(int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawLine3D(Vector3_0: Vector3,Vector3_1: Vector3,Color_2: Color,) -> None:
        """void DrawLine3D(struct Vector3, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawLineBezier(Vector2_0: Vector2,Vector2_1: Vector2,float_2: float,Color_3: Color,) -> None:
        """void DrawLineBezier(struct Vector2, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawLineBezierQuad(Vector2_0: Vector2,Vector2_1: Vector2,Vector2_2: Vector2,float_3: float,Color_4: Color,) -> None:
        """void DrawLineBezierQuad(struct Vector2, struct Vector2, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawLineEx(Vector2_0: Vector2,Vector2_1: Vector2,float_2: float,Color_3: Color,) -> None:
        """void DrawLineEx(struct Vector2, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawLineStrip(Vector2_pointer_0: Any,int_1: int,Color_2: Color,) -> None:
        """void DrawLineStrip(struct Vector2 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawLineV(Vector2_0: Vector2,Vector2_1: Vector2,Color_2: Color,) -> None:
        """void DrawLineV(struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawMesh(Mesh_0: Mesh,Material_1: Material,Matrix_2: Matrix,) -> None:
        """void DrawMesh(struct Mesh, struct Material, struct Matrix);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawMeshInstanced(Mesh_0: Mesh,Material_1: Material,Matrix_pointer_2: Any,int_3: int,) -> None:
        """void DrawMeshInstanced(struct Mesh, struct Material, struct Matrix *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawModel(Model_0: Model,Vector3_1: Vector3,float_2: float,Color_3: Color,) -> None:
        """void DrawModel(struct Model, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawModelEx(Model_0: Model,Vector3_1: Vector3,Vector3_2: Vector3,float_3: float,Vector3_4: Vector3,Color_5: Color,) -> None:
        """void DrawModelEx(struct Model, struct Vector3, struct Vector3, float, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawModelWires(Model_0: Model,Vector3_1: Vector3,float_2: float,Color_3: Color,) -> None:
        """void DrawModelWires(struct Model, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawModelWiresEx(Model_0: Model,Vector3_1: Vector3,Vector3_2: Vector3,float_3: float,Vector3_4: Vector3,Color_5: Color,) -> None:
        """void DrawModelWiresEx(struct Model, struct Vector3, struct Vector3, float, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawPixel(int_0: int,int_1: int,Color_2: Color,) -> None:
        """void DrawPixel(int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawPixelV(Vector2_0: Vector2,Color_1: Color,) -> None:
        """void DrawPixelV(struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawPlane(Vector3_0: Vector3,Vector2_1: Vector2,Color_2: Color,) -> None:
        """void DrawPlane(struct Vector3, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawPoint3D(Vector3_0: Vector3,Color_1: Color,) -> None:
        """void DrawPoint3D(struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawPoly(Vector2_0: Vector2,int_1: int,float_2: float,float_3: float,Color_4: Color,) -> None:
        """void DrawPoly(struct Vector2, int, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawPolyLines(Vector2_0: Vector2,int_1: int,float_2: float,float_3: float,Color_4: Color,) -> None:
        """void DrawPolyLines(struct Vector2, int, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRay(Ray_0: Ray,Color_1: Color,) -> None:
        """void DrawRay(struct Ray, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangle(int_0: int,int_1: int,int_2: int,int_3: int,Color_4: Color,) -> None:
        """void DrawRectangle(int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangleGradientEx(Rectangle_0: Rectangle,Color_1: Color,Color_2: Color,Color_3: Color,Color_4: Color,) -> None:
        """void DrawRectangleGradientEx(struct Rectangle, struct Color, struct Color, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangleGradientH(int_0: int,int_1: int,int_2: int,int_3: int,Color_4: Color,Color_5: Color,) -> None:
        """void DrawRectangleGradientH(int, int, int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangleGradientV(int_0: int,int_1: int,int_2: int,int_3: int,Color_4: Color,Color_5: Color,) -> None:
        """void DrawRectangleGradientV(int, int, int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangleLines(int_0: int,int_1: int,int_2: int,int_3: int,Color_4: Color,) -> None:
        """void DrawRectangleLines(int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangleLinesEx(Rectangle_0: Rectangle,int_1: int,Color_2: Color,) -> None:
        """void DrawRectangleLinesEx(struct Rectangle, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectanglePro(Rectangle_0: Rectangle,Vector2_1: Vector2,float_2: float,Color_3: Color,) -> None:
        """void DrawRectanglePro(struct Rectangle, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangleRec(Rectangle_0: Rectangle,Color_1: Color,) -> None:
        """void DrawRectangleRec(struct Rectangle, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangleRounded(Rectangle_0: Rectangle,float_1: float,int_2: int,Color_3: Color,) -> None:
        """void DrawRectangleRounded(struct Rectangle, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangleRoundedLines(Rectangle_0: Rectangle,float_1: float,int_2: int,int_3: int,Color_4: Color,) -> None:
        """void DrawRectangleRoundedLines(struct Rectangle, float, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRectangleV(Vector2_0: Vector2,Vector2_1: Vector2,Color_2: Color,) -> None:
        """void DrawRectangleV(struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRing(Vector2_0: Vector2,float_1: float,float_2: float,float_3: float,float_4: float,int_5: int,Color_6: Color,) -> None:
        """void DrawRing(struct Vector2, float, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawRingLines(Vector2_0: Vector2,float_1: float,float_2: float,float_3: float,float_4: float,int_5: int,Color_6: Color,) -> None:
        """void DrawRingLines(struct Vector2, float, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawSphere(Vector3_0: Vector3,float_1: float,Color_2: Color,) -> None:
        """void DrawSphere(struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawSphereEx(Vector3_0: Vector3,float_1: float,int_2: int,int_3: int,Color_4: Color,) -> None:
        """void DrawSphereEx(struct Vector3, float, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawSphereWires(Vector3_0: Vector3,float_1: float,int_2: int,int_3: int,Color_4: Color,) -> None:
        """void DrawSphereWires(struct Vector3, float, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawText(str_0: str,int_1: int,int_2: int,int_3: int,Color_4: Color,) -> None:
        """void DrawText(char *, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextCodepoint(Font_0: Font,int_1: int,Vector2_2: Vector2,float_3: float,Color_4: Color,) -> None:
        """void DrawTextCodepoint(struct Font, int, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextEx(Font_0: Font,str_1: str,Vector2_2: Vector2,float_3: float,float_4: float,Color_5: Color,) -> None:
        """void DrawTextEx(struct Font, char *, struct Vector2, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextRec(Font_0: Font,str_1: str,Rectangle_2: Rectangle,float_3: float,float_4: float,_Bool_5: bool,Color_6: Color,) -> None:
        """void DrawTextRec(struct Font, char *, struct Rectangle, float, float, _Bool, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextRecEx(Font_0: Font,str_1: str,Rectangle_2: Rectangle,float_3: float,float_4: float,_Bool_5: bool,Color_6: Color,int_7: int,int_8: int,Color_9: Color,Color_10: Color,) -> None:
        """void DrawTextRecEx(struct Font, char *, struct Rectangle, float, float, _Bool, struct Color, int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTexture(Texture_0: Texture,int_1: int,int_2: int,Color_3: Color,) -> None:
        """void DrawTexture(struct Texture, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextureEx(Texture_0: Texture,Vector2_1: Vector2,float_2: float,float_3: float,Color_4: Color,) -> None:
        """void DrawTextureEx(struct Texture, struct Vector2, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextureNPatch(Texture_0: Texture,NPatchInfo_1: NPatchInfo,Rectangle_2: Rectangle,Vector2_3: Vector2,float_4: float,Color_5: Color,) -> None:
        """void DrawTextureNPatch(struct Texture, struct NPatchInfo, struct Rectangle, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTexturePoly(Texture_0: Texture,Vector2_1: Vector2,Vector2_pointer_2: Any,Vector2_pointer_3: Any,int_4: int,Color_5: Color,) -> None:
        """void DrawTexturePoly(struct Texture, struct Vector2, struct Vector2 *, struct Vector2 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTexturePro(Texture_0: Texture,Rectangle_1: Rectangle,Rectangle_2: Rectangle,Vector2_3: Vector2,float_4: float,Color_5: Color,) -> None:
        """void DrawTexturePro(struct Texture, struct Rectangle, struct Rectangle, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextureQuad(Texture_0: Texture,Vector2_1: Vector2,Vector2_2: Vector2,Rectangle_3: Rectangle,Color_4: Color,) -> None:
        """void DrawTextureQuad(struct Texture, struct Vector2, struct Vector2, struct Rectangle, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextureRec(Texture_0: Texture,Rectangle_1: Rectangle,Vector2_2: Vector2,Color_3: Color,) -> None:
        """void DrawTextureRec(struct Texture, struct Rectangle, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextureTiled(Texture_0: Texture,Rectangle_1: Rectangle,Rectangle_2: Rectangle,Vector2_3: Vector2,float_4: float,float_5: float,Color_6: Color,) -> None:
        """void DrawTextureTiled(struct Texture, struct Rectangle, struct Rectangle, struct Vector2, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTextureV(Texture_0: Texture,Vector2_1: Vector2,Color_2: Color,) -> None:
        """void DrawTextureV(struct Texture, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTriangle(Vector2_0: Vector2,Vector2_1: Vector2,Vector2_2: Vector2,Color_3: Color,) -> None:
        """void DrawTriangle(struct Vector2, struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTriangle3D(Vector3_0: Vector3,Vector3_1: Vector3,Vector3_2: Vector3,Color_3: Color,) -> None:
        """void DrawTriangle3D(struct Vector3, struct Vector3, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTriangleFan(Vector2_pointer_0: Any,int_1: int,Color_2: Color,) -> None:
        """void DrawTriangleFan(struct Vector2 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTriangleLines(Vector2_0: Vector2,Vector2_1: Vector2,Vector2_2: Vector2,Color_3: Color,) -> None:
        """void DrawTriangleLines(struct Vector2, struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTriangleStrip(Vector2_pointer_0: Any,int_1: int,Color_2: Color,) -> None:
        """void DrawTriangleStrip(struct Vector2 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def DrawTriangleStrip3D(Vector3_pointer_0: Any,int_1: int,Color_2: Color,) -> None:
        """void DrawTriangleStrip3D(struct Vector3 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def EnableCursor() -> None:
        """void EnableCursor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def EndBlendMode() -> None:
        """void EndBlendMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def EndDrawing() -> None:
        """void EndDrawing();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def EndMode2D() -> None:
        """void EndMode2D();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def EndMode3D() -> None:
        """void EndMode3D();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def EndScissorMode() -> None:
        """void EndScissorMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def EndShaderMode() -> None:
        """void EndShaderMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def EndTextureMode() -> None:
        """void EndTextureMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def EndVrStereoMode() -> None:
        """void EndVrStereoMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ExportImage(Image_0: Image,str_1: str,) -> bool:
        """_Bool ExportImage(struct Image, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ExportImageAsCode(Image_0: Image,str_1: str,) -> bool:
        """_Bool ExportImageAsCode(struct Image, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ExportMesh(Mesh_0: Mesh,str_1: str,) -> bool:
        """_Bool ExportMesh(struct Mesh, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ExportWave(Wave_0: Wave,str_1: str,) -> bool:
        """_Bool ExportWave(struct Wave, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ExportWaveAsCode(Wave_0: Wave,str_1: str,) -> bool:
        """_Bool ExportWaveAsCode(struct Wave, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
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
def Fade(Color_0: Color,float_1: float,) -> Color:
        """struct Color Fade(struct Color, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def FileExists(str_0: str,) -> bool:
        """_Bool FileExists(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
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
def GenImageCellular(int_0: int,int_1: int,int_2: int,) -> Image:
        """struct Image GenImageCellular(int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenImageChecked(int_0: int,int_1: int,int_2: int,int_3: int,Color_4: Color,Color_5: Color,) -> Image:
        """struct Image GenImageChecked(int, int, int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenImageColor(int_0: int,int_1: int,Color_2: Color,) -> Image:
        """struct Image GenImageColor(int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenImageFontAtlas(CharInfo_pointer_0: Any,Rectangle_pointer_pointer_1: Any,int_2: int,int_3: int,int_4: int,int_5: int,) -> Image:
        """struct Image GenImageFontAtlas(struct CharInfo *, struct Rectangle * *, int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenImageGradientH(int_0: int,int_1: int,Color_2: Color,Color_3: Color,) -> Image:
        """struct Image GenImageGradientH(int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenImageGradientRadial(int_0: int,int_1: int,float_2: float,Color_3: Color,Color_4: Color,) -> Image:
        """struct Image GenImageGradientRadial(int, int, float, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenImageGradientV(int_0: int,int_1: int,Color_2: Color,Color_3: Color,) -> Image:
        """struct Image GenImageGradientV(int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenImagePerlinNoise(int_0: int,int_1: int,int_2: int,int_3: int,float_4: float,) -> Image:
        """struct Image GenImagePerlinNoise(int, int, int, int, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenImageWhiteNoise(int_0: int,int_1: int,float_2: float,) -> Image:
        """struct Image GenImageWhiteNoise(int, int, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshCube(float_0: float,float_1: float,float_2: float,) -> Mesh:
        """struct Mesh GenMeshCube(float, float, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshCubicmap(Image_0: Image,Vector3_1: Vector3,) -> Mesh:
        """struct Mesh GenMeshCubicmap(struct Image, struct Vector3);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshCylinder(float_0: float,float_1: float,int_2: int,) -> Mesh:
        """struct Mesh GenMeshCylinder(float, float, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshHeightmap(Image_0: Image,Vector3_1: Vector3,) -> Mesh:
        """struct Mesh GenMeshHeightmap(struct Image, struct Vector3);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshHemiSphere(float_0: float,int_1: int,int_2: int,) -> Mesh:
        """struct Mesh GenMeshHemiSphere(float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshKnot(float_0: float,float_1: float,int_2: int,int_3: int,) -> Mesh:
        """struct Mesh GenMeshKnot(float, float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshPlane(float_0: float,float_1: float,int_2: int,int_3: int,) -> Mesh:
        """struct Mesh GenMeshPlane(float, float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshPoly(int_0: int,float_1: float,) -> Mesh:
        """struct Mesh GenMeshPoly(int, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshSphere(float_0: float,int_1: int,int_2: int,) -> Mesh:
        """struct Mesh GenMeshSphere(float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenMeshTorus(float_0: float,float_1: float,int_2: int,int_3: int,) -> Mesh:
        """struct Mesh GenMeshTorus(float, float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GenTextureMipmaps(Texture_pointer_0: Any,) -> None:
        """void GenTextureMipmaps(struct Texture *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCameraMatrix(Camera3D_0: Camera3D,) -> Matrix:
        """struct Matrix GetCameraMatrix(struct Camera3D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCameraMatrix2D(Camera2D_0: Camera2D,) -> Matrix:
        """struct Matrix GetCameraMatrix2D(struct Camera2D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCharPressed() -> int:
        """int GetCharPressed();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetClipboardText() -> str:
        """char *GetClipboardText();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCodepoints(str_0: str,int_pointer_1: Any,) -> Any:
        """int *GetCodepoints(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCodepointsCount(str_0: str,) -> int:
        """int GetCodepointsCount(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCollisionRayGround(Ray_0: Ray,float_1: float,) -> RayHitInfo:
        """struct RayHitInfo GetCollisionRayGround(struct Ray, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCollisionRayMesh(Ray_0: Ray,Mesh_1: Mesh,Matrix_2: Matrix,) -> RayHitInfo:
        """struct RayHitInfo GetCollisionRayMesh(struct Ray, struct Mesh, struct Matrix);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCollisionRayModel(Ray_0: Ray,Model_1: Model,) -> RayHitInfo:
        """struct RayHitInfo GetCollisionRayModel(struct Ray, struct Model);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCollisionRayTriangle(Ray_0: Ray,Vector3_1: Vector3,Vector3_2: Vector3,Vector3_3: Vector3,) -> RayHitInfo:
        """struct RayHitInfo GetCollisionRayTriangle(struct Ray, struct Vector3, struct Vector3, struct Vector3);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCollisionRec(Rectangle_0: Rectangle,Rectangle_1: Rectangle,) -> Rectangle:
        """struct Rectangle GetCollisionRec(struct Rectangle, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetColor(unsignedint_0: int,) -> Color:
        """struct Color GetColor(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetCurrentMonitor() -> int:
        """int GetCurrentMonitor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetDirectoryFiles(str_0: str,int_pointer_1: Any,) -> str:
        """char * *GetDirectoryFiles(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetDirectoryPath(str_0: str,) -> str:
        """char *GetDirectoryPath(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetDroppedFiles(int_pointer_0: Any,) -> str:
        """char * *GetDroppedFiles(int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetFPS() -> int:
        """int GetFPS();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetFileExtension(str_0: str,) -> str:
        """char *GetFileExtension(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetFileModTime(str_0: str,) -> int:
        """long GetFileModTime(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetFileName(str_0: str,) -> str:
        """char *GetFileName(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetFileNameWithoutExt(str_0: str,) -> str:
        """char *GetFileNameWithoutExt(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetFontDefault() -> Font:
        """struct Font GetFontDefault();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetFrameTime() -> float:
        """float GetFrameTime();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGamepadAxisCount(int_0: int,) -> int:
        """int GetGamepadAxisCount(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGamepadAxisMovement(int_0: int,int_1: int,) -> float:
        """float GetGamepadAxisMovement(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGamepadButtonPressed() -> int:
        """int GetGamepadButtonPressed();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGamepadName(int_0: int,) -> str:
        """char *GetGamepadName(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGestureDetected() -> int:
        """int GetGestureDetected();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGestureDragAngle() -> float:
        """float GetGestureDragAngle();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGestureDragVector() -> Vector2:
        """struct Vector2 GetGestureDragVector();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGestureHoldDuration() -> float:
        """float GetGestureHoldDuration();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGesturePinchAngle() -> float:
        """float GetGesturePinchAngle();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGesturePinchVector() -> Vector2:
        """struct Vector2 GetGesturePinchVector();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetGlyphIndex(Font_0: Font,int_1: int,) -> int:
        """int GetGlyphIndex(struct Font, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetImageAlphaBorder(Image_0: Image,float_1: float,) -> Rectangle:
        """struct Rectangle GetImageAlphaBorder(struct Image, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetKeyPressed() -> int:
        """int GetKeyPressed();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMonitorCount() -> int:
        """int GetMonitorCount();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMonitorHeight(int_0: int,) -> int:
        """int GetMonitorHeight(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMonitorName(int_0: int,) -> str:
        """char *GetMonitorName(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMonitorPhysicalHeight(int_0: int,) -> int:
        """int GetMonitorPhysicalHeight(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMonitorPhysicalWidth(int_0: int,) -> int:
        """int GetMonitorPhysicalWidth(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMonitorPosition(int_0: int,) -> Vector2:
        """struct Vector2 GetMonitorPosition(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMonitorRefreshRate(int_0: int,) -> int:
        """int GetMonitorRefreshRate(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMonitorWidth(int_0: int,) -> int:
        """int GetMonitorWidth(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMousePosition() -> Vector2:
        """struct Vector2 GetMousePosition();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMouseRay(Vector2_0: Vector2,Camera3D_1: Camera3D,) -> Ray:
        """struct Ray GetMouseRay(struct Vector2, struct Camera3D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMouseWheelMove() -> float:
        """float GetMouseWheelMove();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMouseX() -> int:
        """int GetMouseX();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMouseY() -> int:
        """int GetMouseY();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMusicTimeLength(Music_0: Music,) -> float:
        """float GetMusicTimeLength(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetMusicTimePlayed(Music_0: Music,) -> float:
        """float GetMusicTimePlayed(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetNextCodepoint(str_0: str,int_pointer_1: Any,) -> int:
        """int GetNextCodepoint(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetPixelColor(void_pointer_0: Any,int_1: int,) -> Color:
        """struct Color GetPixelColor(void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetPixelDataSize(int_0: int,int_1: int,int_2: int,) -> int:
        """int GetPixelDataSize(int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetPrevDirectoryPath(str_0: str,) -> str:
        """char *GetPrevDirectoryPath(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetRandomValue(int_0: int,int_1: int,) -> int:
        """int GetRandomValue(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetScreenData() -> Image:
        """struct Image GetScreenData();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetScreenHeight() -> int:
        """int GetScreenHeight();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetScreenToWorld2D(Vector2_0: Vector2,Camera2D_1: Camera2D,) -> Vector2:
        """struct Vector2 GetScreenToWorld2D(struct Vector2, struct Camera2D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetScreenWidth() -> int:
        """int GetScreenWidth();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetShaderLocation(Shader_0: Shader,str_1: str,) -> int:
        """int GetShaderLocation(struct Shader, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetShaderLocationAttrib(Shader_0: Shader,str_1: str,) -> int:
        """int GetShaderLocationAttrib(struct Shader, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetSoundsPlaying() -> int:
        """int GetSoundsPlaying();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetTextureData(Texture_0: Texture,) -> Image:
        """struct Image GetTextureData(struct Texture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetTime() -> float:
        """double GetTime();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetTouchPointsCount() -> int:
        """int GetTouchPointsCount();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetTouchPosition(int_0: int,) -> Vector2:
        """struct Vector2 GetTouchPosition(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetTouchX() -> int:
        """int GetTouchX();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetTouchY() -> int:
        """int GetTouchY();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetWindowHandle() -> Any:
        """void *GetWindowHandle();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetWindowPosition() -> Vector2:
        """struct Vector2 GetWindowPosition();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetWindowScaleDPI() -> Vector2:
        """struct Vector2 GetWindowScaleDPI();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetWorkingDirectory() -> str:
        """char *GetWorkingDirectory();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetWorldToScreen(Vector3_0: Vector3,Camera3D_1: Camera3D,) -> Vector2:
        """struct Vector2 GetWorldToScreen(struct Vector3, struct Camera3D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetWorldToScreen2D(Vector2_0: Vector2,Camera2D_1: Camera2D,) -> Vector2:
        """struct Vector2 GetWorldToScreen2D(struct Vector2, struct Camera2D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def GetWorldToScreenEx(Vector3_0: Vector3,Camera3D_1: Camera3D,int_2: int,int_3: int,) -> Vector2:
        """struct Vector2 GetWorldToScreenEx(struct Vector3, struct Camera3D, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def HideCursor() -> None:
        """void HideCursor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageAlphaClear(Image_pointer_0: Any,Color_1: Color,float_2: float,) -> None:
        """void ImageAlphaClear(struct Image *, struct Color, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageAlphaCrop(Image_pointer_0: Any,float_1: float,) -> None:
        """void ImageAlphaCrop(struct Image *, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageAlphaMask(Image_pointer_0: Any,Image_1: Image,) -> None:
        """void ImageAlphaMask(struct Image *, struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageAlphaPremultiply(Image_pointer_0: Any,) -> None:
        """void ImageAlphaPremultiply(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageClearBackground(Image_pointer_0: Any,Color_1: Color,) -> None:
        """void ImageClearBackground(struct Image *, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageColorBrightness(Image_pointer_0: Any,int_1: int,) -> None:
        """void ImageColorBrightness(struct Image *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageColorContrast(Image_pointer_0: Any,float_1: float,) -> None:
        """void ImageColorContrast(struct Image *, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageColorGrayscale(Image_pointer_0: Any,) -> None:
        """void ImageColorGrayscale(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageColorInvert(Image_pointer_0: Any,) -> None:
        """void ImageColorInvert(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageColorReplace(Image_pointer_0: Any,Color_1: Color,Color_2: Color,) -> None:
        """void ImageColorReplace(struct Image *, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageColorTint(Image_pointer_0: Any,Color_1: Color,) -> None:
        """void ImageColorTint(struct Image *, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageCopy(Image_0: Image,) -> Image:
        """struct Image ImageCopy(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageCrop(Image_pointer_0: Any,Rectangle_1: Rectangle,) -> None:
        """void ImageCrop(struct Image *, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDither(Image_pointer_0: Any,int_1: int,int_2: int,int_3: int,int_4: int,) -> None:
        """void ImageDither(struct Image *, int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDraw(Image_pointer_0: Any,Image_1: Image,Rectangle_2: Rectangle,Rectangle_3: Rectangle,Color_4: Color,) -> None:
        """void ImageDraw(struct Image *, struct Image, struct Rectangle, struct Rectangle, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawCircle(Image_pointer_0: Any,int_1: int,int_2: int,int_3: int,Color_4: Color,) -> None:
        """void ImageDrawCircle(struct Image *, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawCircleV(Image_pointer_0: Any,Vector2_1: Vector2,int_2: int,Color_3: Color,) -> None:
        """void ImageDrawCircleV(struct Image *, struct Vector2, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawLine(Image_pointer_0: Any,int_1: int,int_2: int,int_3: int,int_4: int,Color_5: Color,) -> None:
        """void ImageDrawLine(struct Image *, int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawLineV(Image_pointer_0: Any,Vector2_1: Vector2,Vector2_2: Vector2,Color_3: Color,) -> None:
        """void ImageDrawLineV(struct Image *, struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawPixel(Image_pointer_0: Any,int_1: int,int_2: int,Color_3: Color,) -> None:
        """void ImageDrawPixel(struct Image *, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawPixelV(Image_pointer_0: Any,Vector2_1: Vector2,Color_2: Color,) -> None:
        """void ImageDrawPixelV(struct Image *, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawRectangle(Image_pointer_0: Any,int_1: int,int_2: int,int_3: int,int_4: int,Color_5: Color,) -> None:
        """void ImageDrawRectangle(struct Image *, int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawRectangleLines(Image_pointer_0: Any,Rectangle_1: Rectangle,int_2: int,Color_3: Color,) -> None:
        """void ImageDrawRectangleLines(struct Image *, struct Rectangle, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawRectangleRec(Image_pointer_0: Any,Rectangle_1: Rectangle,Color_2: Color,) -> None:
        """void ImageDrawRectangleRec(struct Image *, struct Rectangle, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawRectangleV(Image_pointer_0: Any,Vector2_1: Vector2,Vector2_2: Vector2,Color_3: Color,) -> None:
        """void ImageDrawRectangleV(struct Image *, struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawText(Image_pointer_0: Any,str_1: str,int_2: int,int_3: int,int_4: int,Color_5: Color,) -> None:
        """void ImageDrawText(struct Image *, char *, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageDrawTextEx(Image_pointer_0: Any,Font_1: Font,str_2: str,Vector2_3: Vector2,float_4: float,float_5: float,Color_6: Color,) -> None:
        """void ImageDrawTextEx(struct Image *, struct Font, char *, struct Vector2, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageFlipHorizontal(Image_pointer_0: Any,) -> None:
        """void ImageFlipHorizontal(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageFlipVertical(Image_pointer_0: Any,) -> None:
        """void ImageFlipVertical(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageFormat(Image_pointer_0: Any,int_1: int,) -> None:
        """void ImageFormat(struct Image *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageFromImage(Image_0: Image,Rectangle_1: Rectangle,) -> Image:
        """struct Image ImageFromImage(struct Image, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageMipmaps(Image_pointer_0: Any,) -> None:
        """void ImageMipmaps(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageResize(Image_pointer_0: Any,int_1: int,int_2: int,) -> None:
        """void ImageResize(struct Image *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageResizeCanvas(Image_pointer_0: Any,int_1: int,int_2: int,int_3: int,int_4: int,Color_5: Color,) -> None:
        """void ImageResizeCanvas(struct Image *, int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageResizeNN(Image_pointer_0: Any,int_1: int,int_2: int,) -> None:
        """void ImageResizeNN(struct Image *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageRotateCCW(Image_pointer_0: Any,) -> None:
        """void ImageRotateCCW(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageRotateCW(Image_pointer_0: Any,) -> None:
        """void ImageRotateCW(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageText(str_0: str,int_1: int,Color_2: Color,) -> Image:
        """struct Image ImageText(char *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageTextEx(Font_0: Font,str_1: str,float_2: float,float_3: float,Color_4: Color,) -> Image:
        """struct Image ImageTextEx(struct Font, char *, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ImageToPOT(Image_pointer_0: Any,Color_1: Color,) -> None:
        """void ImageToPOT(struct Image *, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def InitAudioDevice() -> None:
        """void InitAudioDevice();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def InitAudioStream(unsignedint_0: int,unsignedint_1: int,unsignedint_2: int,) -> AudioStream:
        """struct AudioStream InitAudioStream(unsigned int, unsigned int, unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def InitWindow(int_0: int,int_1: int,str_2: str,) -> None:
        """void InitWindow(int, int, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsAudioDeviceReady() -> bool:
        """_Bool IsAudioDeviceReady();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsAudioStreamPlaying(AudioStream_0: AudioStream,) -> bool:
        """_Bool IsAudioStreamPlaying(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsAudioStreamProcessed(AudioStream_0: AudioStream,) -> bool:
        """_Bool IsAudioStreamProcessed(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsCursorHidden() -> bool:
        """_Bool IsCursorHidden();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsCursorOnScreen() -> bool:
        """_Bool IsCursorOnScreen();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsFileDropped() -> bool:
        """_Bool IsFileDropped();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsFileExtension(str_0: str,str_1: str,) -> bool:
        """_Bool IsFileExtension(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsGamepadAvailable(int_0: int,) -> bool:
        """_Bool IsGamepadAvailable(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsGamepadButtonDown(int_0: int,int_1: int,) -> bool:
        """_Bool IsGamepadButtonDown(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsGamepadButtonPressed(int_0: int,int_1: int,) -> bool:
        """_Bool IsGamepadButtonPressed(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsGamepadButtonReleased(int_0: int,int_1: int,) -> bool:
        """_Bool IsGamepadButtonReleased(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsGamepadButtonUp(int_0: int,int_1: int,) -> bool:
        """_Bool IsGamepadButtonUp(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsGamepadName(int_0: int,str_1: str,) -> bool:
        """_Bool IsGamepadName(int, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsGestureDetected(int_0: int,) -> bool:
        """_Bool IsGestureDetected(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsKeyDown(int_0: int,) -> bool:
        """_Bool IsKeyDown(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsKeyPressed(int_0: int,) -> bool:
        """_Bool IsKeyPressed(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsKeyReleased(int_0: int,) -> bool:
        """_Bool IsKeyReleased(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsKeyUp(int_0: int,) -> bool:
        """_Bool IsKeyUp(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsModelAnimationValid(Model_0: Model,ModelAnimation_1: ModelAnimation,) -> bool:
        """_Bool IsModelAnimationValid(struct Model, struct ModelAnimation);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsMouseButtonDown(int_0: int,) -> bool:
        """_Bool IsMouseButtonDown(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsMouseButtonPressed(int_0: int,) -> bool:
        """_Bool IsMouseButtonPressed(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsMouseButtonReleased(int_0: int,) -> bool:
        """_Bool IsMouseButtonReleased(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsMouseButtonUp(int_0: int,) -> bool:
        """_Bool IsMouseButtonUp(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsMusicPlaying(Music_0: Music,) -> bool:
        """_Bool IsMusicPlaying(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsSoundPlaying(Sound_0: Sound,) -> bool:
        """_Bool IsSoundPlaying(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsWindowFocused() -> bool:
        """_Bool IsWindowFocused();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsWindowFullscreen() -> bool:
        """_Bool IsWindowFullscreen();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsWindowHidden() -> bool:
        """_Bool IsWindowHidden();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsWindowMaximized() -> bool:
        """_Bool IsWindowMaximized();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsWindowMinimized() -> bool:
        """_Bool IsWindowMinimized();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsWindowReady() -> bool:
        """_Bool IsWindowReady();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsWindowResized() -> bool:
        """_Bool IsWindowResized();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def IsWindowState(unsignedint_0: int,) -> bool:
        """_Bool IsWindowState(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
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
def LoadFileData(str_0: str,unsignedint_pointer_1: Any,) -> str:
        """unsigned char *LoadFileData(char *, unsigned int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadFileText(str_0: str,) -> str:
        """char *LoadFileText(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadFont(str_0: str,) -> Font:
        """struct Font LoadFont(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadFontData(unsignedstr_0: str,int_1: int,int_2: int,int_pointer_3: Any,int_4: int,int_5: int,) -> Any:
        """struct CharInfo *LoadFontData(unsigned char *, int, int, int *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadFontEx(str_0: str,int_1: int,int_pointer_2: Any,int_3: int,) -> Font:
        """struct Font LoadFontEx(char *, int, int *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadFontFromImage(Image_0: Image,Color_1: Color,int_2: int,) -> Font:
        """struct Font LoadFontFromImage(struct Image, struct Color, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadFontFromMemory(str_0: str,unsignedstr_1: str,int_2: int,int_3: int,int_pointer_4: Any,int_5: int,) -> Font:
        """struct Font LoadFontFromMemory(char *, unsigned char *, int, int, int *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadImage(str_0: str,) -> Image:
        """struct Image LoadImage(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadImageAnim(str_0: str,int_pointer_1: Any,) -> Image:
        """struct Image LoadImageAnim(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadImageColors(Image_0: Image,) -> Any:
        """struct Color *LoadImageColors(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadImageFromMemory(str_0: str,unsignedstr_1: str,int_2: int,) -> Image:
        """struct Image LoadImageFromMemory(char *, unsigned char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadImagePalette(Image_0: Image,int_1: int,int_pointer_2: Any,) -> Any:
        """struct Color *LoadImagePalette(struct Image, int, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadImageRaw(str_0: str,int_1: int,int_2: int,int_3: int,int_4: int,) -> Image:
        """struct Image LoadImageRaw(char *, int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadMaterialDefault() -> Material:
        """struct Material LoadMaterialDefault();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadMaterials(str_0: str,int_pointer_1: Any,) -> Any:
        """struct Material *LoadMaterials(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadModel(str_0: str,) -> Model:
        """struct Model LoadModel(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadModelAnimations(str_0: str,int_pointer_1: Any,) -> Any:
        """struct ModelAnimation *LoadModelAnimations(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadModelFromMesh(Mesh_0: Mesh,) -> Model:
        """struct Model LoadModelFromMesh(struct Mesh);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadMusicStream(str_0: str,) -> Music:
        """struct Music LoadMusicStream(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadMusicStreamFromMemory(str_0: str,unsignedstr_1: str,int_2: int,) -> Music:
        """struct Music LoadMusicStreamFromMemory(char *, unsigned char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadRenderTexture(int_0: int,int_1: int,) -> RenderTexture:
        """struct RenderTexture LoadRenderTexture(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadShader(str_0: str,str_1: str,) -> Shader:
        """struct Shader LoadShader(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadShaderFromMemory(str_0: str,str_1: str,) -> Shader:
        """struct Shader LoadShaderFromMemory(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadSound(str_0: str,) -> Sound:
        """struct Sound LoadSound(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadSoundFromWave(Wave_0: Wave,) -> Sound:
        """struct Sound LoadSoundFromWave(struct Wave);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadStorageValue(unsignedint_0: int,) -> int:
        """int LoadStorageValue(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadTexture(str_0: str,) -> Texture:
        """struct Texture LoadTexture(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadTextureCubemap(Image_0: Image,int_1: int,) -> Texture:
        """struct Texture LoadTextureCubemap(struct Image, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadTextureFromImage(Image_0: Image,) -> Texture:
        """struct Texture LoadTextureFromImage(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadVrStereoConfig(VrDeviceInfo_0: VrDeviceInfo,) -> VrStereoConfig:
        """struct VrStereoConfig LoadVrStereoConfig(struct VrDeviceInfo);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadWave(str_0: str,) -> Wave:
        """struct Wave LoadWave(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadWaveFromMemory(str_0: str,unsignedstr_1: str,int_2: int,) -> Wave:
        """struct Wave LoadWaveFromMemory(char *, unsigned char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def LoadWaveSamples(Wave_0: Wave,) -> Any:
        """float *LoadWaveSamples(struct Wave);

CFFI C function from raylib.static._raylib_cffi.lib"""
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
def MaximizeWindow() -> None:
        """void MaximizeWindow();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def MeasureText(str_0: str,int_1: int,) -> int:
        """int MeasureText(char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def MeasureTextEx(Font_0: Font,str_1: str,float_2: float,float_3: float,) -> Vector2:
        """struct Vector2 MeasureTextEx(struct Font, char *, float, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def MemAlloc(int_0: int,) -> Any:
        """void *MemAlloc(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def MemFree(void_pointer_0: Any,) -> None:
        """void MemFree(void *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def MemRealloc(void_pointer_0: Any,int_1: int,) -> Any:
        """void *MemRealloc(void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def MeshBinormals(Mesh_pointer_0: Any,) -> None:
        """void MeshBinormals(struct Mesh *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def MeshBoundingBox(Mesh_0: Mesh,) -> BoundingBox:
        """struct BoundingBox MeshBoundingBox(struct Mesh);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def MeshTangents(Mesh_pointer_0: Any,) -> None:
        """void MeshTangents(struct Mesh *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def MinimizeWindow() -> None:
        """void MinimizeWindow();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
NPATCH_NINE_PATCH: int
NPATCH_THREE_PATCH_HORIZONTAL: int
NPATCH_THREE_PATCH_VERTICAL: int
def OpenURL(str_0: str,) -> None:
        """void OpenURL(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
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
def PauseAudioStream(AudioStream_0: AudioStream,) -> None:
        """void PauseAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def PauseMusicStream(Music_0: Music,) -> None:
        """void PauseMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def PauseSound(Sound_0: Sound,) -> None:
        """void PauseSound(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def PlayAudioStream(AudioStream_0: AudioStream,) -> None:
        """void PlayAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def PlayMusicStream(Music_0: Music,) -> None:
        """void PlayMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def PlaySound(Sound_0: Sound,) -> None:
        """void PlaySound(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def PlaySoundMulti(Sound_0: Sound,) -> None:
        """void PlaySoundMulti(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def RestoreWindow() -> None:
        """void RestoreWindow();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ResumeAudioStream(AudioStream_0: AudioStream,) -> None:
        """void ResumeAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ResumeMusicStream(Music_0: Music,) -> None:
        """void ResumeMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ResumeSound(Sound_0: Sound,) -> None:
        """void ResumeSound(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
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
def SaveFileData(str_0: str,void_pointer_1: Any,unsignedint_2: int,) -> bool:
        """_Bool SaveFileData(char *, void *, unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SaveFileText(str_0: str,str_1: str,) -> bool:
        """_Bool SaveFileText(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SaveStorageValue(unsignedint_0: int,int_1: int,) -> bool:
        """_Bool SaveStorageValue(unsigned int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetAudioStreamBufferSizeDefault(int_0: int,) -> None:
        """void SetAudioStreamBufferSizeDefault(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetAudioStreamPitch(AudioStream_0: AudioStream,float_1: float,) -> None:
        """void SetAudioStreamPitch(struct AudioStream, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetAudioStreamVolume(AudioStream_0: AudioStream,float_1: float,) -> None:
        """void SetAudioStreamVolume(struct AudioStream, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetCameraAltControl(int_0: int,) -> None:
        """void SetCameraAltControl(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetCameraMode(Camera3D_0: Camera3D,int_1: int,) -> None:
        """void SetCameraMode(struct Camera3D, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetCameraMoveControls(int_0: int,int_1: int,int_2: int,int_3: int,int_4: int,int_5: int,) -> None:
        """void SetCameraMoveControls(int, int, int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetCameraPanControl(int_0: int,) -> None:
        """void SetCameraPanControl(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetCameraSmoothZoomControl(int_0: int,) -> None:
        """void SetCameraSmoothZoomControl(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetClipboardText(str_0: str,) -> None:
        """void SetClipboardText(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetConfigFlags(unsignedint_0: int,) -> None:
        """void SetConfigFlags(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetExitKey(int_0: int,) -> None:
        """void SetExitKey(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetGamepadMappings(str_0: str,) -> int:
        """int SetGamepadMappings(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetGesturesEnabled(unsignedint_0: int,) -> None:
        """void SetGesturesEnabled(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetMasterVolume(float_0: float,) -> None:
        """void SetMasterVolume(float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetMaterialTexture(Material_pointer_0: Any,int_1: int,Texture_2: Texture,) -> None:
        """void SetMaterialTexture(struct Material *, int, struct Texture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetModelMeshMaterial(Model_pointer_0: Any,int_1: int,int_2: int,) -> None:
        """void SetModelMeshMaterial(struct Model *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetMouseCursor(int_0: int,) -> None:
        """void SetMouseCursor(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetMouseOffset(int_0: int,int_1: int,) -> None:
        """void SetMouseOffset(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetMousePosition(int_0: int,int_1: int,) -> None:
        """void SetMousePosition(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetMouseScale(float_0: float,float_1: float,) -> None:
        """void SetMouseScale(float, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetMusicPitch(Music_0: Music,float_1: float,) -> None:
        """void SetMusicPitch(struct Music, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetMusicVolume(Music_0: Music,float_1: float,) -> None:
        """void SetMusicVolume(struct Music, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetPixelColor(void_pointer_0: Any,Color_1: Color,int_2: int,) -> None:
        """void SetPixelColor(void *, struct Color, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetShaderValue(Shader_0: Shader,int_1: int,void_pointer_2: Any,int_3: int,) -> None:
        """void SetShaderValue(struct Shader, int, void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetShaderValueMatrix(Shader_0: Shader,int_1: int,Matrix_2: Matrix,) -> None:
        """void SetShaderValueMatrix(struct Shader, int, struct Matrix);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetShaderValueTexture(Shader_0: Shader,int_1: int,Texture_2: Texture,) -> None:
        """void SetShaderValueTexture(struct Shader, int, struct Texture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetShaderValueV(Shader_0: Shader,int_1: int,void_pointer_2: Any,int_3: int,int_4: int,) -> None:
        """void SetShaderValueV(struct Shader, int, void *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetShapesTexture(Texture_0: Texture,Rectangle_1: Rectangle,) -> None:
        """void SetShapesTexture(struct Texture, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetSoundPitch(Sound_0: Sound,float_1: float,) -> None:
        """void SetSoundPitch(struct Sound, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetSoundVolume(Sound_0: Sound,float_1: float,) -> None:
        """void SetSoundVolume(struct Sound, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetTargetFPS(int_0: int,) -> None:
        """void SetTargetFPS(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetTextureFilter(Texture_0: Texture,int_1: int,) -> None:
        """void SetTextureFilter(struct Texture, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetTextureWrap(Texture_0: Texture,int_1: int,) -> None:
        """void SetTextureWrap(struct Texture, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetTraceLogLevel(int_0: int,) -> None:
        """void SetTraceLogLevel(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetWindowIcon(Image_0: Image,) -> None:
        """void SetWindowIcon(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetWindowMinSize(int_0: int,int_1: int,) -> None:
        """void SetWindowMinSize(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetWindowMonitor(int_0: int,) -> None:
        """void SetWindowMonitor(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetWindowPosition(int_0: int,int_1: int,) -> None:
        """void SetWindowPosition(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetWindowSize(int_0: int,int_1: int,) -> None:
        """void SetWindowSize(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetWindowState(unsignedint_0: int,) -> None:
        """void SetWindowState(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def SetWindowTitle(str_0: str,) -> None:
        """void SetWindowTitle(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ShowCursor() -> None:
        """void ShowCursor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def StopAudioStream(AudioStream_0: AudioStream,) -> None:
        """void StopAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def StopMusicStream(Music_0: Music,) -> None:
        """void StopMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def StopSound(Sound_0: Sound,) -> None:
        """void StopSound(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def StopSoundMulti() -> None:
        """void StopSoundMulti();

CFFI C function from raylib.static._raylib_cffi.lib"""
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
def TakeScreenshot(str_0: str,) -> None:
        """void TakeScreenshot(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextAppend(str_0: str,str_1: str,int_pointer_2: Any,) -> None:
        """void TextAppend(char *, char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextCopy(str_0: str,str_1: str,) -> int:
        """int TextCopy(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextFindIndex(str_0: str,str_1: str,) -> int:
        """int TextFindIndex(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextFormat(*args) -> str:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def TextInsert(str_0: str,str_1: str,int_2: int,) -> str:
        """char *TextInsert(char *, char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextIsEqual(str_0: str,str_1: str,) -> bool:
        """_Bool TextIsEqual(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextJoin(str_pointer_0: str,int_1: int,str_2: str,) -> str:
        """char *TextJoin(char * *, int, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextLength(str_0: str,) -> int:
        """unsigned int TextLength(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextReplace(str_0: str,str_1: str,str_2: str,) -> str:
        """char *TextReplace(char *, char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextSplit(str_0: str,char_1: str,int_pointer_2: Any,) -> str:
        """char * *TextSplit(char *, char, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextSubtext(str_0: str,int_1: int,int_2: int,) -> str:
        """char *TextSubtext(char *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextToInteger(str_0: str,) -> int:
        """int TextToInteger(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextToLower(str_0: str,) -> str:
        """char *TextToLower(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextToPascal(str_0: str,) -> str:
        """char *TextToPascal(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextToUpper(str_0: str,) -> str:
        """char *TextToUpper(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TextToUtf8(int_pointer_0: Any,int_1: int,) -> str:
        """char *TextToUtf8(int *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def ToggleFullscreen() -> None:
        """void ToggleFullscreen();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def TraceLog(*args) -> None:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def UnloadFileData(unsignedstr_0: str,) -> None:
        """void UnloadFileData(unsigned char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadFileText(unsignedstr_0: str,) -> None:
        """void UnloadFileText(unsigned char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadFont(Font_0: Font,) -> None:
        """void UnloadFont(struct Font);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadFontData(CharInfo_pointer_0: Any,int_1: int,) -> None:
        """void UnloadFontData(struct CharInfo *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadImage(Image_0: Image,) -> None:
        """void UnloadImage(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadImageColors(Color_pointer_0: Any,) -> None:
        """void UnloadImageColors(struct Color *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadImagePalette(Color_pointer_0: Any,) -> None:
        """void UnloadImagePalette(struct Color *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadMaterial(Material_0: Material,) -> None:
        """void UnloadMaterial(struct Material);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadMesh(Mesh_0: Mesh,) -> None:
        """void UnloadMesh(struct Mesh);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadModel(Model_0: Model,) -> None:
        """void UnloadModel(struct Model);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadModelAnimation(ModelAnimation_0: ModelAnimation,) -> None:
        """void UnloadModelAnimation(struct ModelAnimation);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadModelAnimations(ModelAnimation_pointer_0: Any,unsignedint_1: int,) -> None:
        """void UnloadModelAnimations(struct ModelAnimation *, unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadModelKeepMeshes(Model_0: Model,) -> None:
        """void UnloadModelKeepMeshes(struct Model);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadMusicStream(Music_0: Music,) -> None:
        """void UnloadMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadRenderTexture(RenderTexture_0: RenderTexture,) -> None:
        """void UnloadRenderTexture(struct RenderTexture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadShader(Shader_0: Shader,) -> None:
        """void UnloadShader(struct Shader);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadSound(Sound_0: Sound,) -> None:
        """void UnloadSound(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadTexture(Texture_0: Texture,) -> None:
        """void UnloadTexture(struct Texture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadVrStereoConfig(VrStereoConfig_0: VrStereoConfig,) -> None:
        """void UnloadVrStereoConfig(struct VrStereoConfig);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadWave(Wave_0: Wave,) -> None:
        """void UnloadWave(struct Wave);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UnloadWaveSamples(float_pointer_0: Any,) -> None:
        """void UnloadWaveSamples(float *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UpdateAudioStream(AudioStream_0: AudioStream,void_pointer_1: Any,int_2: int,) -> None:
        """void UpdateAudioStream(struct AudioStream, void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UpdateCamera(Camera3D_pointer_0: Any,) -> None:
        """void UpdateCamera(struct Camera3D *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UpdateMeshBuffer(Mesh_0: Mesh,int_1: int,void_pointer_2: Any,int_3: int,int_4: int,) -> None:
        """void UpdateMeshBuffer(struct Mesh, int, void *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UpdateModelAnimation(Model_0: Model,ModelAnimation_1: ModelAnimation,int_2: int,) -> None:
        """void UpdateModelAnimation(struct Model, struct ModelAnimation, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UpdateMusicStream(Music_0: Music,) -> None:
        """void UpdateMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UpdateSound(Sound_0: Sound,void_pointer_1: Any,int_2: int,) -> None:
        """void UpdateSound(struct Sound, void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UpdateTexture(Texture_0: Texture,void_pointer_1: Any,) -> None:
        """void UpdateTexture(struct Texture, void *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UpdateTextureRec(Texture_0: Texture,Rectangle_1: Rectangle,void_pointer_2: Any,) -> None:
        """void UpdateTextureRec(struct Texture, struct Rectangle, void *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def UploadMesh(Mesh_pointer_0: Any,_Bool_1: bool,) -> None:
        """void UploadMesh(struct Mesh *, _Bool);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def WaveCopy(Wave_0: Wave,) -> Wave:
        """struct Wave WaveCopy(struct Wave);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def WaveCrop(Wave_pointer_0: Any,int_1: int,int_2: int,) -> None:
        """void WaveCrop(struct Wave *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def WaveFormat(Wave_pointer_0: Any,int_1: int,int_2: int,int_3: int,) -> None:
        """void WaveFormat(struct Wave *, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
def WindowShouldClose() -> bool:
        """_Bool WindowShouldClose();

CFFI C function from raylib.static._raylib_cffi.lib"""
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
CharInfo: struct
Color: struct
ConfigFlags: int
CubemapLayout: int
Font: struct
FontType: int
GamepadAxis: int
GamepadButton: int
Gestures: int
Image: struct
KeyboardKey: int
Material: struct
MaterialMap: struct
MaterialMapIndex: int
Matrix: struct
Mesh: struct
Model: struct
ModelAnimation: struct
MouseButton: int
MouseCursor: int
Music: struct
NPatchInfo: struct
NPatchLayout: int
PixelFormat: int
Quaternion: struct
Ray: struct
RayHitInfo: struct
Rectangle: struct
RenderTexture: struct
RenderTexture2D: struct
Shader: struct
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

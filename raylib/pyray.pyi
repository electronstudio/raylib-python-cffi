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
    def begin_blend_mode(self, int_0: int) -> None:
        """void BeginBlendMode(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_drawing(self) -> None:
        """void BeginDrawing();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_mode_2d(self, Camera2D_0: Camera2D) -> None:
        """void BeginMode2D(struct Camera2D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_mode_3d(self, Camera3D_0: Camera3D) -> None:
        """void BeginMode3D(struct Camera3D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_scissor_mode(self, int_0: int, int_1: int, int_2: int, int_3: int) -> None:
        """void BeginScissorMode(int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_shader_mode(self, Shader_0: Shader) -> None:
        """void BeginShaderMode(struct Shader);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_texture_mode(self, RenderTexture_0: RenderTexture) -> None:
        """void BeginTextureMode(struct RenderTexture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_vr_stereo_mode(self, VrStereoConfig_0: VrStereoConfig) -> None:
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
    def change_directory(self, str_0: str) -> bool:
        """_Bool ChangeDirectory(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_box_sphere(self, BoundingBox_0: BoundingBox, Vector3_1: Vector3, float_2: float) -> bool:
        """_Bool CheckCollisionBoxSphere(struct BoundingBox, struct Vector3, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_boxes(self, BoundingBox_0: BoundingBox, BoundingBox_1: BoundingBox) -> bool:
        """_Bool CheckCollisionBoxes(struct BoundingBox, struct BoundingBox);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_circle_rec(self, Vector2_0: Vector2, float_1: float, Rectangle_2: Rectangle) -> bool:
        """_Bool CheckCollisionCircleRec(struct Vector2, float, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_circles(self, Vector2_0: Vector2, float_1: float, Vector2_2: Vector2, float_3: float) -> bool:
        """_Bool CheckCollisionCircles(struct Vector2, float, struct Vector2, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_lines(self, Vector2_0: Vector2, Vector2_1: Vector2, Vector2_2: Vector2, Vector2_3: Vector2, Vector2_pointer_4: Any) -> bool:
        """_Bool CheckCollisionLines(struct Vector2, struct Vector2, struct Vector2, struct Vector2, struct Vector2 *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_point_circle(self, Vector2_0: Vector2, Vector2_1: Vector2, float_2: float) -> bool:
        """_Bool CheckCollisionPointCircle(struct Vector2, struct Vector2, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_point_rec(self, Vector2_0: Vector2, Rectangle_1: Rectangle) -> bool:
        """_Bool CheckCollisionPointRec(struct Vector2, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_point_triangle(self, Vector2_0: Vector2, Vector2_1: Vector2, Vector2_2: Vector2, Vector2_3: Vector2) -> bool:
        """_Bool CheckCollisionPointTriangle(struct Vector2, struct Vector2, struct Vector2, struct Vector2);

CFFI C function from raylib.static._raylib_cffi.lib"""
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
    def check_collision_recs(self, Rectangle_0: Rectangle, Rectangle_1: Rectangle) -> bool:
        """_Bool CheckCollisionRecs(struct Rectangle, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_spheres(self, Vector3_0: Vector3, float_1: float, Vector3_2: Vector3, float_3: float) -> bool:
        """_Bool CheckCollisionSpheres(struct Vector3, float, struct Vector3, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def clear_background(self, Color_0: Color) -> None:
        """void ClearBackground(struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def clear_directory_files(self) -> None:
        """void ClearDirectoryFiles();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def clear_dropped_files(self) -> None:
        """void ClearDroppedFiles();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def clear_window_state(self, unsignedint_0: int) -> None:
        """void ClearWindowState(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def close_audio_device(self) -> None:
        """void CloseAudioDevice();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def close_audio_stream(self, AudioStream_0: AudioStream) -> None:
        """void CloseAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def close_window(self) -> None:
        """void CloseWindow();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def codepoint_to_utf8(self, int_0: int, int_pointer_1: Any) -> str:
        """char *CodepointToUtf8(int, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_alpha(self, Color_0: Color, float_1: float) -> Color:
        """struct Color ColorAlpha(struct Color, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_alpha_blend(self, Color_0: Color, Color_1: Color, Color_2: Color) -> Color:
        """struct Color ColorAlphaBlend(struct Color, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_from_hsv(self, float_0: float, float_1: float, float_2: float) -> Color:
        """struct Color ColorFromHSV(float, float, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_from_normalized(self, Vector4_0: Vector4) -> Color:
        """struct Color ColorFromNormalized(struct Vector4);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_normalize(self, Color_0: Color) -> Vector4:
        """struct Vector4 ColorNormalize(struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_to_hsv(self, Color_0: Color) -> Vector3:
        """struct Vector3 ColorToHSV(struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_to_int(self, Color_0: Color) -> int:
        """int ColorToInt(struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def compress_data(self, unsignedstr_0: str, int_1: int, int_pointer_2: Any) -> str:
        """unsigned char *CompressData(unsigned char *, int, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def decompress_data(self, unsignedstr_0: str, int_1: int, int_pointer_2: Any) -> str:
        """unsigned char *DecompressData(unsigned char *, int, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def directory_exists(self, str_0: str) -> bool:
        """_Bool DirectoryExists(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def disable_cursor(self) -> None:
        """void DisableCursor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_billboard(self, Camera3D_0: Camera3D, Texture_1: Texture, Vector3_2: Vector3, float_3: float, Color_4: Color) -> None:
        """void DrawBillboard(struct Camera3D, struct Texture, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_billboard_rec(self, Camera3D_0: Camera3D, Texture_1: Texture, Rectangle_2: Rectangle, Vector3_3: Vector3, float_4: float, Color_5: Color) -> None:
        """void DrawBillboardRec(struct Camera3D, struct Texture, struct Rectangle, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_bounding_box(self, BoundingBox_0: BoundingBox, Color_1: Color) -> None:
        """void DrawBoundingBox(struct BoundingBox, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle(self, int_0: int, int_1: int, float_2: float, Color_3: Color) -> None:
        """void DrawCircle(int, int, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_3d(self, Vector3_0: Vector3, float_1: float, Vector3_2: Vector3, float_3: float, Color_4: Color) -> None:
        """void DrawCircle3D(struct Vector3, float, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_gradient(self, int_0: int, int_1: int, float_2: float, Color_3: Color, Color_4: Color) -> None:
        """void DrawCircleGradient(int, int, float, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_lines(self, int_0: int, int_1: int, float_2: float, Color_3: Color) -> None:
        """void DrawCircleLines(int, int, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_sector(self, Vector2_0: Vector2, float_1: float, float_2: float, float_3: float, int_4: int, Color_5: Color) -> None:
        """void DrawCircleSector(struct Vector2, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_sector_lines(self, Vector2_0: Vector2, float_1: float, float_2: float, float_3: float, int_4: int, Color_5: Color) -> None:
        """void DrawCircleSectorLines(struct Vector2, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_v(self, Vector2_0: Vector2, float_1: float, Color_2: Color) -> None:
        """void DrawCircleV(struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube(self, Vector3_0: Vector3, float_1: float, float_2: float, float_3: float, Color_4: Color) -> None:
        """void DrawCube(struct Vector3, float, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube_texture(self, Texture_0: Texture, Vector3_1: Vector3, float_2: float, float_3: float, float_4: float, Color_5: Color) -> None:
        """void DrawCubeTexture(struct Texture, struct Vector3, float, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube_v(self, Vector3_0: Vector3, Vector3_1: Vector3, Color_2: Color) -> None:
        """void DrawCubeV(struct Vector3, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube_wires(self, Vector3_0: Vector3, float_1: float, float_2: float, float_3: float, Color_4: Color) -> None:
        """void DrawCubeWires(struct Vector3, float, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube_wires_v(self, Vector3_0: Vector3, Vector3_1: Vector3, Color_2: Color) -> None:
        """void DrawCubeWiresV(struct Vector3, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cylinder(self, Vector3_0: Vector3, float_1: float, float_2: float, float_3: float, int_4: int, Color_5: Color) -> None:
        """void DrawCylinder(struct Vector3, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cylinder_wires(self, Vector3_0: Vector3, float_1: float, float_2: float, float_3: float, int_4: int, Color_5: Color) -> None:
        """void DrawCylinderWires(struct Vector3, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ellipse(self, int_0: int, int_1: int, float_2: float, float_3: float, Color_4: Color) -> None:
        """void DrawEllipse(int, int, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ellipse_lines(self, int_0: int, int_1: int, float_2: float, float_3: float, Color_4: Color) -> None:
        """void DrawEllipseLines(int, int, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_fps(self, int_0: int, int_1: int) -> None:
        """void DrawFPS(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_grid(self, int_0: int, float_1: float) -> None:
        """void DrawGrid(int, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line(self, int_0: int, int_1: int, int_2: int, int_3: int, Color_4: Color) -> None:
        """void DrawLine(int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_3d(self, Vector3_0: Vector3, Vector3_1: Vector3, Color_2: Color) -> None:
        """void DrawLine3D(struct Vector3, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_bezier(self, Vector2_0: Vector2, Vector2_1: Vector2, float_2: float, Color_3: Color) -> None:
        """void DrawLineBezier(struct Vector2, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_bezier_quad(self, Vector2_0: Vector2, Vector2_1: Vector2, Vector2_2: Vector2, float_3: float, Color_4: Color) -> None:
        """void DrawLineBezierQuad(struct Vector2, struct Vector2, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_ex(self, Vector2_0: Vector2, Vector2_1: Vector2, float_2: float, Color_3: Color) -> None:
        """void DrawLineEx(struct Vector2, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_strip(self, Vector2_pointer_0: Any, int_1: int, Color_2: Color) -> None:
        """void DrawLineStrip(struct Vector2 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_v(self, Vector2_0: Vector2, Vector2_1: Vector2, Color_2: Color) -> None:
        """void DrawLineV(struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_mesh(self, Mesh_0: Mesh, Material_1: Material, Matrix_2: Matrix) -> None:
        """void DrawMesh(struct Mesh, struct Material, struct Matrix);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_mesh_instanced(self, Mesh_0: Mesh, Material_1: Material, Matrix_pointer_2: Any, int_3: int) -> None:
        """void DrawMeshInstanced(struct Mesh, struct Material, struct Matrix *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_model(self, Model_0: Model, Vector3_1: Vector3, float_2: float, Color_3: Color) -> None:
        """void DrawModel(struct Model, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_model_ex(self, Model_0: Model, Vector3_1: Vector3, Vector3_2: Vector3, float_3: float, Vector3_4: Vector3, Color_5: Color) -> None:
        """void DrawModelEx(struct Model, struct Vector3, struct Vector3, float, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_model_wires(self, Model_0: Model, Vector3_1: Vector3, float_2: float, Color_3: Color) -> None:
        """void DrawModelWires(struct Model, struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_model_wires_ex(self, Model_0: Model, Vector3_1: Vector3, Vector3_2: Vector3, float_3: float, Vector3_4: Vector3, Color_5: Color) -> None:
        """void DrawModelWiresEx(struct Model, struct Vector3, struct Vector3, float, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_pixel(self, int_0: int, int_1: int, Color_2: Color) -> None:
        """void DrawPixel(int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_pixel_v(self, Vector2_0: Vector2, Color_1: Color) -> None:
        """void DrawPixelV(struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_plane(self, Vector3_0: Vector3, Vector2_1: Vector2, Color_2: Color) -> None:
        """void DrawPlane(struct Vector3, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_point_3d(self, Vector3_0: Vector3, Color_1: Color) -> None:
        """void DrawPoint3D(struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_poly(self, Vector2_0: Vector2, int_1: int, float_2: float, float_3: float, Color_4: Color) -> None:
        """void DrawPoly(struct Vector2, int, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_poly_lines(self, Vector2_0: Vector2, int_1: int, float_2: float, float_3: float, Color_4: Color) -> None:
        """void DrawPolyLines(struct Vector2, int, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ray(self, Ray_0: Ray, Color_1: Color) -> None:
        """void DrawRay(struct Ray, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle(self, int_0: int, int_1: int, int_2: int, int_3: int, Color_4: Color) -> None:
        """void DrawRectangle(int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_gradient_ex(self, Rectangle_0: Rectangle, Color_1: Color, Color_2: Color, Color_3: Color, Color_4: Color) -> None:
        """void DrawRectangleGradientEx(struct Rectangle, struct Color, struct Color, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_gradient_h(self, int_0: int, int_1: int, int_2: int, int_3: int, Color_4: Color, Color_5: Color) -> None:
        """void DrawRectangleGradientH(int, int, int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_gradient_v(self, int_0: int, int_1: int, int_2: int, int_3: int, Color_4: Color, Color_5: Color) -> None:
        """void DrawRectangleGradientV(int, int, int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_lines(self, int_0: int, int_1: int, int_2: int, int_3: int, Color_4: Color) -> None:
        """void DrawRectangleLines(int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_lines_ex(self, Rectangle_0: Rectangle, int_1: int, Color_2: Color) -> None:
        """void DrawRectangleLinesEx(struct Rectangle, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_pro(self, Rectangle_0: Rectangle, Vector2_1: Vector2, float_2: float, Color_3: Color) -> None:
        """void DrawRectanglePro(struct Rectangle, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_rec(self, Rectangle_0: Rectangle, Color_1: Color) -> None:
        """void DrawRectangleRec(struct Rectangle, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_rounded(self, Rectangle_0: Rectangle, float_1: float, int_2: int, Color_3: Color) -> None:
        """void DrawRectangleRounded(struct Rectangle, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_rounded_lines(self, Rectangle_0: Rectangle, float_1: float, int_2: int, int_3: int, Color_4: Color) -> None:
        """void DrawRectangleRoundedLines(struct Rectangle, float, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_v(self, Vector2_0: Vector2, Vector2_1: Vector2, Color_2: Color) -> None:
        """void DrawRectangleV(struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ring(self, Vector2_0: Vector2, float_1: float, float_2: float, float_3: float, float_4: float, int_5: int, Color_6: Color) -> None:
        """void DrawRing(struct Vector2, float, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ring_lines(self, Vector2_0: Vector2, float_1: float, float_2: float, float_3: float, float_4: float, int_5: int, Color_6: Color) -> None:
        """void DrawRingLines(struct Vector2, float, float, float, float, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_sphere(self, Vector3_0: Vector3, float_1: float, Color_2: Color) -> None:
        """void DrawSphere(struct Vector3, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_sphere_ex(self, Vector3_0: Vector3, float_1: float, int_2: int, int_3: int, Color_4: Color) -> None:
        """void DrawSphereEx(struct Vector3, float, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_sphere_wires(self, Vector3_0: Vector3, float_1: float, int_2: int, int_3: int, Color_4: Color) -> None:
        """void DrawSphereWires(struct Vector3, float, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text(self, str_0: str, int_1: int, int_2: int, int_3: int, Color_4: Color) -> None:
        """void DrawText(char *, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text_codepoint(self, Font_0: Font, int_1: int, Vector2_2: Vector2, float_3: float, Color_4: Color) -> None:
        """void DrawTextCodepoint(struct Font, int, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text_ex(self, Font_0: Font, str_1: str, Vector2_2: Vector2, float_3: float, float_4: float, Color_5: Color) -> None:
        """void DrawTextEx(struct Font, char *, struct Vector2, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text_rec(self, Font_0: Font, str_1: str, Rectangle_2: Rectangle, float_3: float, float_4: float, _Bool_5: bool, Color_6: Color) -> None:
        """void DrawTextRec(struct Font, char *, struct Rectangle, float, float, _Bool, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text_rec_ex(self, Font_0: Font, str_1: str, Rectangle_2: Rectangle, float_3: float, float_4: float, _Bool_5: bool, Color_6: Color, int_7: int, int_8: int, Color_9: Color, Color_10: Color) -> None:
        """void DrawTextRecEx(struct Font, char *, struct Rectangle, float, float, _Bool, struct Color, int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture(self, Texture_0: Texture, int_1: int, int_2: int, Color_3: Color) -> None:
        """void DrawTexture(struct Texture, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_ex(self, Texture_0: Texture, Vector2_1: Vector2, float_2: float, float_3: float, Color_4: Color) -> None:
        """void DrawTextureEx(struct Texture, struct Vector2, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_n_patch(self, Texture_0: Texture, NPatchInfo_1: NPatchInfo, Rectangle_2: Rectangle, Vector2_3: Vector2, float_4: float, Color_5: Color) -> None:
        """void DrawTextureNPatch(struct Texture, struct NPatchInfo, struct Rectangle, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_poly(self, Texture_0: Texture, Vector2_1: Vector2, Vector2_pointer_2: Any, Vector2_pointer_3: Any, int_4: int, Color_5: Color) -> None:
        """void DrawTexturePoly(struct Texture, struct Vector2, struct Vector2 *, struct Vector2 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_pro(self, Texture_0: Texture, Rectangle_1: Rectangle, Rectangle_2: Rectangle, Vector2_3: Vector2, float_4: float, Color_5: Color) -> None:
        """void DrawTexturePro(struct Texture, struct Rectangle, struct Rectangle, struct Vector2, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_quad(self, Texture_0: Texture, Vector2_1: Vector2, Vector2_2: Vector2, Rectangle_3: Rectangle, Color_4: Color) -> None:
        """void DrawTextureQuad(struct Texture, struct Vector2, struct Vector2, struct Rectangle, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_rec(self, Texture_0: Texture, Rectangle_1: Rectangle, Vector2_2: Vector2, Color_3: Color) -> None:
        """void DrawTextureRec(struct Texture, struct Rectangle, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_tiled(self, Texture_0: Texture, Rectangle_1: Rectangle, Rectangle_2: Rectangle, Vector2_3: Vector2, float_4: float, float_5: float, Color_6: Color) -> None:
        """void DrawTextureTiled(struct Texture, struct Rectangle, struct Rectangle, struct Vector2, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_v(self, Texture_0: Texture, Vector2_1: Vector2, Color_2: Color) -> None:
        """void DrawTextureV(struct Texture, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle(self, Vector2_0: Vector2, Vector2_1: Vector2, Vector2_2: Vector2, Color_3: Color) -> None:
        """void DrawTriangle(struct Vector2, struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_3d(self, Vector3_0: Vector3, Vector3_1: Vector3, Vector3_2: Vector3, Color_3: Color) -> None:
        """void DrawTriangle3D(struct Vector3, struct Vector3, struct Vector3, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_fan(self, Vector2_pointer_0: Any, int_1: int, Color_2: Color) -> None:
        """void DrawTriangleFan(struct Vector2 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_lines(self, Vector2_0: Vector2, Vector2_1: Vector2, Vector2_2: Vector2, Color_3: Color) -> None:
        """void DrawTriangleLines(struct Vector2, struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_strip(self, Vector2_pointer_0: Any, int_1: int, Color_2: Color) -> None:
        """void DrawTriangleStrip(struct Vector2 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_strip_3d(self, Vector3_pointer_0: Any, int_1: int, Color_2: Color) -> None:
        """void DrawTriangleStrip3D(struct Vector3 *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def enable_cursor(self) -> None:
        """void EnableCursor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_blend_mode(self) -> None:
        """void EndBlendMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_drawing(self) -> None:
        """void EndDrawing();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_mode_2d(self) -> None:
        """void EndMode2D();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_mode_3d(self) -> None:
        """void EndMode3D();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_scissor_mode(self) -> None:
        """void EndScissorMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_shader_mode(self) -> None:
        """void EndShaderMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_texture_mode(self) -> None:
        """void EndTextureMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_vr_stereo_mode(self) -> None:
        """void EndVrStereoMode();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_image(self, Image_0: Image, str_1: str) -> bool:
        """_Bool ExportImage(struct Image, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_image_as_code(self, Image_0: Image, str_1: str) -> bool:
        """_Bool ExportImageAsCode(struct Image, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_mesh(self, Mesh_0: Mesh, str_1: str) -> bool:
        """_Bool ExportMesh(struct Mesh, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_wave(self, Wave_0: Wave, str_1: str) -> bool:
        """_Bool ExportWave(struct Wave, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_wave_as_code(self, Wave_0: Wave, str_1: str) -> bool:
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
    def fade(self, Color_0: Color, float_1: float) -> Color:
        """struct Color Fade(struct Color, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def file_exists(self, str_0: str) -> bool:
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
    def gen_image_cellular(self, int_0: int, int_1: int, int_2: int) -> Image:
        """struct Image GenImageCellular(int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_checked(self, int_0: int, int_1: int, int_2: int, int_3: int, Color_4: Color, Color_5: Color) -> Image:
        """struct Image GenImageChecked(int, int, int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_color(self, int_0: int, int_1: int, Color_2: Color) -> Image:
        """struct Image GenImageColor(int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_font_atlas(self, CharInfo_pointer_0: Any, Rectangle_pointer_pointer_1: Any, int_2: int, int_3: int, int_4: int, int_5: int) -> Image:
        """struct Image GenImageFontAtlas(struct CharInfo *, struct Rectangle * *, int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_gradient_h(self, int_0: int, int_1: int, Color_2: Color, Color_3: Color) -> Image:
        """struct Image GenImageGradientH(int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_gradient_radial(self, int_0: int, int_1: int, float_2: float, Color_3: Color, Color_4: Color) -> Image:
        """struct Image GenImageGradientRadial(int, int, float, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_gradient_v(self, int_0: int, int_1: int, Color_2: Color, Color_3: Color) -> Image:
        """struct Image GenImageGradientV(int, int, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_perlin_noise(self, int_0: int, int_1: int, int_2: int, int_3: int, float_4: float) -> Image:
        """struct Image GenImagePerlinNoise(int, int, int, int, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_white_noise(self, int_0: int, int_1: int, float_2: float) -> Image:
        """struct Image GenImageWhiteNoise(int, int, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_cube(self, float_0: float, float_1: float, float_2: float) -> Mesh:
        """struct Mesh GenMeshCube(float, float, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_cubicmap(self, Image_0: Image, Vector3_1: Vector3) -> Mesh:
        """struct Mesh GenMeshCubicmap(struct Image, struct Vector3);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_cylinder(self, float_0: float, float_1: float, int_2: int) -> Mesh:
        """struct Mesh GenMeshCylinder(float, float, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_heightmap(self, Image_0: Image, Vector3_1: Vector3) -> Mesh:
        """struct Mesh GenMeshHeightmap(struct Image, struct Vector3);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_hemi_sphere(self, float_0: float, int_1: int, int_2: int) -> Mesh:
        """struct Mesh GenMeshHemiSphere(float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_knot(self, float_0: float, float_1: float, int_2: int, int_3: int) -> Mesh:
        """struct Mesh GenMeshKnot(float, float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_plane(self, float_0: float, float_1: float, int_2: int, int_3: int) -> Mesh:
        """struct Mesh GenMeshPlane(float, float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_poly(self, int_0: int, float_1: float) -> Mesh:
        """struct Mesh GenMeshPoly(int, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_sphere(self, float_0: float, int_1: int, int_2: int) -> Mesh:
        """struct Mesh GenMeshSphere(float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_torus(self, float_0: float, float_1: float, int_2: int, int_3: int) -> Mesh:
        """struct Mesh GenMeshTorus(float, float, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_texture_mipmaps(self, Texture_pointer_0: Any) -> None:
        """void GenTextureMipmaps(struct Texture *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_camera_matrix(self, Camera3D_0: Camera3D) -> Matrix:
        """struct Matrix GetCameraMatrix(struct Camera3D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_camera_matrix_2d(self, Camera2D_0: Camera2D) -> Matrix:
        """struct Matrix GetCameraMatrix2D(struct Camera2D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_char_pressed(self) -> int:
        """int GetCharPressed();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_clipboard_text(self) -> str:
        """char *GetClipboardText();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_codepoints(self, str_0: str, int_pointer_1: Any) -> Any:
        """int *GetCodepoints(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_codepoints_count(self, str_0: str) -> int:
        """int GetCodepointsCount(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
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
    def get_collision_rec(self, Rectangle_0: Rectangle, Rectangle_1: Rectangle) -> Rectangle:
        """struct Rectangle GetCollisionRec(struct Rectangle, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_color(self, unsignedint_0: int) -> Color:
        """struct Color GetColor(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_current_monitor(self) -> int:
        """int GetCurrentMonitor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_directory_files(self, str_0: str, int_pointer_1: Any) -> str:
        """char * *GetDirectoryFiles(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_directory_path(self, str_0: str) -> str:
        """char *GetDirectoryPath(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_dropped_files(self, int_pointer_0: Any) -> str:
        """char * *GetDroppedFiles(int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_fps(self) -> int:
        """int GetFPS();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_file_extension(self, str_0: str) -> str:
        """char *GetFileExtension(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_file_mod_time(self, str_0: str) -> int:
        """long GetFileModTime(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_file_name(self, str_0: str) -> str:
        """char *GetFileName(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_file_name_without_ext(self, str_0: str) -> str:
        """char *GetFileNameWithoutExt(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_font_default(self) -> Font:
        """struct Font GetFontDefault();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_frame_time(self) -> float:
        """float GetFrameTime();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gamepad_axis_count(self, int_0: int) -> int:
        """int GetGamepadAxisCount(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gamepad_axis_movement(self, int_0: int, int_1: int) -> float:
        """float GetGamepadAxisMovement(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gamepad_button_pressed(self) -> int:
        """int GetGamepadButtonPressed();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gamepad_name(self, int_0: int) -> str:
        """char *GetGamepadName(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_detected(self) -> int:
        """int GetGestureDetected();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_drag_angle(self) -> float:
        """float GetGestureDragAngle();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_drag_vector(self) -> Vector2:
        """struct Vector2 GetGestureDragVector();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_hold_duration(self) -> float:
        """float GetGestureHoldDuration();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_pinch_angle(self) -> float:
        """float GetGesturePinchAngle();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_pinch_vector(self) -> Vector2:
        """struct Vector2 GetGesturePinchVector();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_glyph_index(self, Font_0: Font, int_1: int) -> int:
        """int GetGlyphIndex(struct Font, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_image_alpha_border(self, Image_0: Image, float_1: float) -> Rectangle:
        """struct Rectangle GetImageAlphaBorder(struct Image, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_key_pressed(self) -> int:
        """int GetKeyPressed();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_count(self) -> int:
        """int GetMonitorCount();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_height(self, int_0: int) -> int:
        """int GetMonitorHeight(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_name(self, int_0: int) -> str:
        """char *GetMonitorName(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_physical_height(self, int_0: int) -> int:
        """int GetMonitorPhysicalHeight(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_physical_width(self, int_0: int) -> int:
        """int GetMonitorPhysicalWidth(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_position(self, int_0: int) -> Vector2:
        """struct Vector2 GetMonitorPosition(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_refresh_rate(self, int_0: int) -> int:
        """int GetMonitorRefreshRate(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_width(self, int_0: int) -> int:
        """int GetMonitorWidth(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_position(self) -> Vector2:
        """struct Vector2 GetMousePosition();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_ray(self, Vector2_0: Vector2, Camera3D_1: Camera3D) -> Ray:
        """struct Ray GetMouseRay(struct Vector2, struct Camera3D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_wheel_move(self) -> float:
        """float GetMouseWheelMove();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_x(self) -> int:
        """int GetMouseX();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_y(self) -> int:
        """int GetMouseY();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_music_time_length(self, Music_0: Music) -> float:
        """float GetMusicTimeLength(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_music_time_played(self, Music_0: Music) -> float:
        """float GetMusicTimePlayed(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_next_codepoint(self, str_0: str, int_pointer_1: Any) -> int:
        """int GetNextCodepoint(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_pixel_color(self, void_pointer_0: Any, int_1: int) -> Color:
        """struct Color GetPixelColor(void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_pixel_data_size(self, int_0: int, int_1: int, int_2: int) -> int:
        """int GetPixelDataSize(int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_prev_directory_path(self, str_0: str) -> str:
        """char *GetPrevDirectoryPath(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_random_value(self, int_0: int, int_1: int) -> int:
        """int GetRandomValue(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_screen_data(self) -> Image:
        """struct Image GetScreenData();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_screen_height(self) -> int:
        """int GetScreenHeight();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_screen_to_world_2d(self, Vector2_0: Vector2, Camera2D_1: Camera2D) -> Vector2:
        """struct Vector2 GetScreenToWorld2D(struct Vector2, struct Camera2D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_screen_width(self) -> int:
        """int GetScreenWidth();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_shader_location(self, Shader_0: Shader, str_1: str) -> int:
        """int GetShaderLocation(struct Shader, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_shader_location_attrib(self, Shader_0: Shader, str_1: str) -> int:
        """int GetShaderLocationAttrib(struct Shader, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_sounds_playing(self) -> int:
        """int GetSoundsPlaying();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_texture_data(self, Texture_0: Texture) -> Image:
        """struct Image GetTextureData(struct Texture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_time(self) -> float:
        """double GetTime();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_touch_points_count(self) -> int:
        """int GetTouchPointsCount();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_touch_position(self, int_0: int) -> Vector2:
        """struct Vector2 GetTouchPosition(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_touch_x(self) -> int:
        """int GetTouchX();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_touch_y(self) -> int:
        """int GetTouchY();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_window_handle(self) -> Any:
        """void *GetWindowHandle();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_window_position(self) -> Vector2:
        """struct Vector2 GetWindowPosition();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_window_scale_dpi(self) -> Vector2:
        """struct Vector2 GetWindowScaleDPI();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_working_directory(self) -> str:
        """char *GetWorkingDirectory();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_world_to_screen(self, Vector3_0: Vector3, Camera3D_1: Camera3D) -> Vector2:
        """struct Vector2 GetWorldToScreen(struct Vector3, struct Camera3D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_world_to_screen_2d(self, Vector2_0: Vector2, Camera2D_1: Camera2D) -> Vector2:
        """struct Vector2 GetWorldToScreen2D(struct Vector2, struct Camera2D);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_world_to_screen_ex(self, Vector3_0: Vector3, Camera3D_1: Camera3D, int_2: int, int_3: int) -> Vector2:
        """struct Vector2 GetWorldToScreenEx(struct Vector3, struct Camera3D, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def hide_cursor(self) -> None:
        """void HideCursor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_alpha_clear(self, Image_pointer_0: Any, Color_1: Color, float_2: float) -> None:
        """void ImageAlphaClear(struct Image *, struct Color, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_alpha_crop(self, Image_pointer_0: Any, float_1: float) -> None:
        """void ImageAlphaCrop(struct Image *, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_alpha_mask(self, Image_pointer_0: Any, Image_1: Image) -> None:
        """void ImageAlphaMask(struct Image *, struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_alpha_premultiply(self, Image_pointer_0: Any) -> None:
        """void ImageAlphaPremultiply(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_clear_background(self, Image_pointer_0: Any, Color_1: Color) -> None:
        """void ImageClearBackground(struct Image *, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_brightness(self, Image_pointer_0: Any, int_1: int) -> None:
        """void ImageColorBrightness(struct Image *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_contrast(self, Image_pointer_0: Any, float_1: float) -> None:
        """void ImageColorContrast(struct Image *, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_grayscale(self, Image_pointer_0: Any) -> None:
        """void ImageColorGrayscale(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_invert(self, Image_pointer_0: Any) -> None:
        """void ImageColorInvert(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_replace(self, Image_pointer_0: Any, Color_1: Color, Color_2: Color) -> None:
        """void ImageColorReplace(struct Image *, struct Color, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_tint(self, Image_pointer_0: Any, Color_1: Color) -> None:
        """void ImageColorTint(struct Image *, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_copy(self, Image_0: Image) -> Image:
        """struct Image ImageCopy(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_crop(self, Image_pointer_0: Any, Rectangle_1: Rectangle) -> None:
        """void ImageCrop(struct Image *, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_dither(self, Image_pointer_0: Any, int_1: int, int_2: int, int_3: int, int_4: int) -> None:
        """void ImageDither(struct Image *, int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw(self, Image_pointer_0: Any, Image_1: Image, Rectangle_2: Rectangle, Rectangle_3: Rectangle, Color_4: Color) -> None:
        """void ImageDraw(struct Image *, struct Image, struct Rectangle, struct Rectangle, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_circle(self, Image_pointer_0: Any, int_1: int, int_2: int, int_3: int, Color_4: Color) -> None:
        """void ImageDrawCircle(struct Image *, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_circle_v(self, Image_pointer_0: Any, Vector2_1: Vector2, int_2: int, Color_3: Color) -> None:
        """void ImageDrawCircleV(struct Image *, struct Vector2, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_line(self, Image_pointer_0: Any, int_1: int, int_2: int, int_3: int, int_4: int, Color_5: Color) -> None:
        """void ImageDrawLine(struct Image *, int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_line_v(self, Image_pointer_0: Any, Vector2_1: Vector2, Vector2_2: Vector2, Color_3: Color) -> None:
        """void ImageDrawLineV(struct Image *, struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_pixel(self, Image_pointer_0: Any, int_1: int, int_2: int, Color_3: Color) -> None:
        """void ImageDrawPixel(struct Image *, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_pixel_v(self, Image_pointer_0: Any, Vector2_1: Vector2, Color_2: Color) -> None:
        """void ImageDrawPixelV(struct Image *, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_rectangle(self, Image_pointer_0: Any, int_1: int, int_2: int, int_3: int, int_4: int, Color_5: Color) -> None:
        """void ImageDrawRectangle(struct Image *, int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_rectangle_lines(self, Image_pointer_0: Any, Rectangle_1: Rectangle, int_2: int, Color_3: Color) -> None:
        """void ImageDrawRectangleLines(struct Image *, struct Rectangle, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_rectangle_rec(self, Image_pointer_0: Any, Rectangle_1: Rectangle, Color_2: Color) -> None:
        """void ImageDrawRectangleRec(struct Image *, struct Rectangle, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_rectangle_v(self, Image_pointer_0: Any, Vector2_1: Vector2, Vector2_2: Vector2, Color_3: Color) -> None:
        """void ImageDrawRectangleV(struct Image *, struct Vector2, struct Vector2, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_text(self, Image_pointer_0: Any, str_1: str, int_2: int, int_3: int, int_4: int, Color_5: Color) -> None:
        """void ImageDrawText(struct Image *, char *, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_text_ex(self, Image_pointer_0: Any, Font_1: Font, str_2: str, Vector2_3: Vector2, float_4: float, float_5: float, Color_6: Color) -> None:
        """void ImageDrawTextEx(struct Image *, struct Font, char *, struct Vector2, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_flip_horizontal(self, Image_pointer_0: Any) -> None:
        """void ImageFlipHorizontal(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_flip_vertical(self, Image_pointer_0: Any) -> None:
        """void ImageFlipVertical(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_format(self, Image_pointer_0: Any, int_1: int) -> None:
        """void ImageFormat(struct Image *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_from_image(self, Image_0: Image, Rectangle_1: Rectangle) -> Image:
        """struct Image ImageFromImage(struct Image, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_mipmaps(self, Image_pointer_0: Any) -> None:
        """void ImageMipmaps(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_resize(self, Image_pointer_0: Any, int_1: int, int_2: int) -> None:
        """void ImageResize(struct Image *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_resize_canvas(self, Image_pointer_0: Any, int_1: int, int_2: int, int_3: int, int_4: int, Color_5: Color) -> None:
        """void ImageResizeCanvas(struct Image *, int, int, int, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_resize_nn(self, Image_pointer_0: Any, int_1: int, int_2: int) -> None:
        """void ImageResizeNN(struct Image *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_rotate_ccw(self, Image_pointer_0: Any) -> None:
        """void ImageRotateCCW(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_rotate_cw(self, Image_pointer_0: Any) -> None:
        """void ImageRotateCW(struct Image *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_text(self, str_0: str, int_1: int, Color_2: Color) -> Image:
        """struct Image ImageText(char *, int, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_text_ex(self, Font_0: Font, str_1: str, float_2: float, float_3: float, Color_4: Color) -> Image:
        """struct Image ImageTextEx(struct Font, char *, float, float, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_to_pot(self, Image_pointer_0: Any, Color_1: Color) -> None:
        """void ImageToPOT(struct Image *, struct Color);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def init_audio_device(self) -> None:
        """void InitAudioDevice();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def init_audio_stream(self, unsignedint_0: int, unsignedint_1: int, unsignedint_2: int) -> AudioStream:
        """struct AudioStream InitAudioStream(unsigned int, unsigned int, unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def init_window(self, int_0: int, int_1: int, str_2: str) -> None:
        """void InitWindow(int, int, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_audio_device_ready(self) -> bool:
        """_Bool IsAudioDeviceReady();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_audio_stream_playing(self, AudioStream_0: AudioStream) -> bool:
        """_Bool IsAudioStreamPlaying(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_audio_stream_processed(self, AudioStream_0: AudioStream) -> bool:
        """_Bool IsAudioStreamProcessed(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_cursor_hidden(self) -> bool:
        """_Bool IsCursorHidden();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_cursor_on_screen(self) -> bool:
        """_Bool IsCursorOnScreen();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_file_dropped(self) -> bool:
        """_Bool IsFileDropped();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_file_extension(self, str_0: str, str_1: str) -> bool:
        """_Bool IsFileExtension(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_available(self, int_0: int) -> bool:
        """_Bool IsGamepadAvailable(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_button_down(self, int_0: int, int_1: int) -> bool:
        """_Bool IsGamepadButtonDown(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_button_pressed(self, int_0: int, int_1: int) -> bool:
        """_Bool IsGamepadButtonPressed(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_button_released(self, int_0: int, int_1: int) -> bool:
        """_Bool IsGamepadButtonReleased(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_button_up(self, int_0: int, int_1: int) -> bool:
        """_Bool IsGamepadButtonUp(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_name(self, int_0: int, str_1: str) -> bool:
        """_Bool IsGamepadName(int, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gesture_detected(self, int_0: int) -> bool:
        """_Bool IsGestureDetected(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_key_down(self, int_0: int) -> bool:
        """_Bool IsKeyDown(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_key_pressed(self, int_0: int) -> bool:
        """_Bool IsKeyPressed(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_key_released(self, int_0: int) -> bool:
        """_Bool IsKeyReleased(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_key_up(self, int_0: int) -> bool:
        """_Bool IsKeyUp(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_model_animation_valid(self, Model_0: Model, ModelAnimation_1: ModelAnimation) -> bool:
        """_Bool IsModelAnimationValid(struct Model, struct ModelAnimation);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_mouse_button_down(self, int_0: int) -> bool:
        """_Bool IsMouseButtonDown(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_mouse_button_pressed(self, int_0: int) -> bool:
        """_Bool IsMouseButtonPressed(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_mouse_button_released(self, int_0: int) -> bool:
        """_Bool IsMouseButtonReleased(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_mouse_button_up(self, int_0: int) -> bool:
        """_Bool IsMouseButtonUp(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_music_playing(self, Music_0: Music) -> bool:
        """_Bool IsMusicPlaying(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_sound_playing(self, Sound_0: Sound) -> bool:
        """_Bool IsSoundPlaying(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_focused(self) -> bool:
        """_Bool IsWindowFocused();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_fullscreen(self) -> bool:
        """_Bool IsWindowFullscreen();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_hidden(self) -> bool:
        """_Bool IsWindowHidden();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_maximized(self) -> bool:
        """_Bool IsWindowMaximized();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_minimized(self) -> bool:
        """_Bool IsWindowMinimized();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_ready(self) -> bool:
        """_Bool IsWindowReady();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_resized(self) -> bool:
        """_Bool IsWindowResized();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_state(self, unsignedint_0: int) -> bool:
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
    def load_file_data(self, str_0: str, unsignedint_pointer_1: Any) -> str:
        """unsigned char *LoadFileData(char *, unsigned int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_file_text(self, str_0: str) -> str:
        """char *LoadFileText(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font(self, str_0: str) -> Font:
        """struct Font LoadFont(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font_data(self, unsignedstr_0: str, int_1: int, int_2: int, int_pointer_3: Any, int_4: int, int_5: int) -> Any:
        """struct CharInfo *LoadFontData(unsigned char *, int, int, int *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font_ex(self, str_0: str, int_1: int, int_pointer_2: Any, int_3: int) -> Font:
        """struct Font LoadFontEx(char *, int, int *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font_from_image(self, Image_0: Image, Color_1: Color, int_2: int) -> Font:
        """struct Font LoadFontFromImage(struct Image, struct Color, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font_from_memory(self, str_0: str, unsignedstr_1: str, int_2: int, int_3: int, int_pointer_4: Any, int_5: int) -> Font:
        """struct Font LoadFontFromMemory(char *, unsigned char *, int, int, int *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image(self, str_0: str) -> Image:
        """struct Image LoadImage(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_anim(self, str_0: str, int_pointer_1: Any) -> Image:
        """struct Image LoadImageAnim(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_colors(self, Image_0: Image) -> Any:
        """struct Color *LoadImageColors(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_from_memory(self, str_0: str, unsignedstr_1: str, int_2: int) -> Image:
        """struct Image LoadImageFromMemory(char *, unsigned char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_palette(self, Image_0: Image, int_1: int, int_pointer_2: Any) -> Any:
        """struct Color *LoadImagePalette(struct Image, int, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_raw(self, str_0: str, int_1: int, int_2: int, int_3: int, int_4: int) -> Image:
        """struct Image LoadImageRaw(char *, int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_material_default(self) -> Material:
        """struct Material LoadMaterialDefault();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_materials(self, str_0: str, int_pointer_1: Any) -> Any:
        """struct Material *LoadMaterials(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_model(self, str_0: str) -> Model:
        """struct Model LoadModel(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_model_animations(self, str_0: str, int_pointer_1: Any) -> Any:
        """struct ModelAnimation *LoadModelAnimations(char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_model_from_mesh(self, Mesh_0: Mesh) -> Model:
        """struct Model LoadModelFromMesh(struct Mesh);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_music_stream(self, str_0: str) -> Music:
        """struct Music LoadMusicStream(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_music_stream_from_memory(self, str_0: str, unsignedstr_1: str, int_2: int) -> Music:
        """struct Music LoadMusicStreamFromMemory(char *, unsigned char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_render_texture(self, int_0: int, int_1: int) -> RenderTexture:
        """struct RenderTexture LoadRenderTexture(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_shader(self, str_0: str, str_1: str) -> Shader:
        """struct Shader LoadShader(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_shader_from_memory(self, str_0: str, str_1: str) -> Shader:
        """struct Shader LoadShaderFromMemory(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_sound(self, str_0: str) -> Sound:
        """struct Sound LoadSound(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_sound_from_wave(self, Wave_0: Wave) -> Sound:
        """struct Sound LoadSoundFromWave(struct Wave);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_storage_value(self, unsignedint_0: int) -> int:
        """int LoadStorageValue(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_texture(self, str_0: str) -> Texture:
        """struct Texture LoadTexture(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_texture_cubemap(self, Image_0: Image, int_1: int) -> Texture:
        """struct Texture LoadTextureCubemap(struct Image, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_texture_from_image(self, Image_0: Image) -> Texture:
        """struct Texture LoadTextureFromImage(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_vr_stereo_config(self, VrDeviceInfo_0: VrDeviceInfo) -> VrStereoConfig:
        """struct VrStereoConfig LoadVrStereoConfig(struct VrDeviceInfo);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_wave(self, str_0: str) -> Wave:
        """struct Wave LoadWave(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_wave_from_memory(self, str_0: str, unsignedstr_1: str, int_2: int) -> Wave:
        """struct Wave LoadWaveFromMemory(char *, unsigned char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_wave_samples(self, Wave_0: Wave) -> Any:
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
    def maximize_window(self) -> None:
        """void MaximizeWindow();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def measure_text(self, str_0: str, int_1: int) -> int:
        """int MeasureText(char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def measure_text_ex(self, Font_0: Font, str_1: str, float_2: float, float_3: float) -> Vector2:
        """struct Vector2 MeasureTextEx(struct Font, char *, float, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mem_alloc(self, int_0: int) -> Any:
        """void *MemAlloc(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mem_free(self, void_pointer_0: Any) -> None:
        """void MemFree(void *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mem_realloc(self, void_pointer_0: Any, int_1: int) -> Any:
        """void *MemRealloc(void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mesh_binormals(self, Mesh_pointer_0: Any) -> None:
        """void MeshBinormals(struct Mesh *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mesh_bounding_box(self, Mesh_0: Mesh) -> BoundingBox:
        """struct BoundingBox MeshBoundingBox(struct Mesh);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mesh_tangents(self, Mesh_pointer_0: Any) -> None:
        """void MeshTangents(struct Mesh *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def minimize_window(self) -> None:
        """void MinimizeWindow();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    NPATCH_NINE_PATCH: int
    NPATCH_THREE_PATCH_HORIZONTAL: int
    NPATCH_THREE_PATCH_VERTICAL: int
    def open_url(self, str_0: str) -> None:
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
    def pause_audio_stream(self, AudioStream_0: AudioStream) -> None:
        """void PauseAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def pause_music_stream(self, Music_0: Music) -> None:
        """void PauseMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def pause_sound(self, Sound_0: Sound) -> None:
        """void PauseSound(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def play_audio_stream(self, AudioStream_0: AudioStream) -> None:
        """void PlayAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def play_music_stream(self, Music_0: Music) -> None:
        """void PlayMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def play_sound(self, Sound_0: Sound) -> None:
        """void PlaySound(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def play_sound_multi(self, Sound_0: Sound) -> None:
        """void PlaySoundMulti(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def restore_window(self) -> None:
        """void RestoreWindow();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def resume_audio_stream(self, AudioStream_0: AudioStream) -> None:
        """void ResumeAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def resume_music_stream(self, Music_0: Music) -> None:
        """void ResumeMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def resume_sound(self, Sound_0: Sound) -> None:
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
    def save_file_data(self, str_0: str, void_pointer_1: Any, unsignedint_2: int) -> bool:
        """_Bool SaveFileData(char *, void *, unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def save_file_text(self, str_0: str, str_1: str) -> bool:
        """_Bool SaveFileText(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def save_storage_value(self, unsignedint_0: int, int_1: int) -> bool:
        """_Bool SaveStorageValue(unsigned int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_audio_stream_buffer_size_default(self, int_0: int) -> None:
        """void SetAudioStreamBufferSizeDefault(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_audio_stream_pitch(self, AudioStream_0: AudioStream, float_1: float) -> None:
        """void SetAudioStreamPitch(struct AudioStream, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_audio_stream_volume(self, AudioStream_0: AudioStream, float_1: float) -> None:
        """void SetAudioStreamVolume(struct AudioStream, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_alt_control(self, int_0: int) -> None:
        """void SetCameraAltControl(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_mode(self, Camera3D_0: Camera3D, int_1: int) -> None:
        """void SetCameraMode(struct Camera3D, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_move_controls(self, int_0: int, int_1: int, int_2: int, int_3: int, int_4: int, int_5: int) -> None:
        """void SetCameraMoveControls(int, int, int, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_pan_control(self, int_0: int) -> None:
        """void SetCameraPanControl(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_smooth_zoom_control(self, int_0: int) -> None:
        """void SetCameraSmoothZoomControl(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_clipboard_text(self, str_0: str) -> None:
        """void SetClipboardText(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_config_flags(self, unsignedint_0: int) -> None:
        """void SetConfigFlags(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_exit_key(self, int_0: int) -> None:
        """void SetExitKey(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_gamepad_mappings(self, str_0: str) -> int:
        """int SetGamepadMappings(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_gestures_enabled(self, unsignedint_0: int) -> None:
        """void SetGesturesEnabled(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_master_volume(self, float_0: float) -> None:
        """void SetMasterVolume(float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_material_texture(self, Material_pointer_0: Any, int_1: int, Texture_2: Texture) -> None:
        """void SetMaterialTexture(struct Material *, int, struct Texture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_model_mesh_material(self, Model_pointer_0: Any, int_1: int, int_2: int) -> None:
        """void SetModelMeshMaterial(struct Model *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_mouse_cursor(self, int_0: int) -> None:
        """void SetMouseCursor(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_mouse_offset(self, int_0: int, int_1: int) -> None:
        """void SetMouseOffset(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_mouse_position(self, int_0: int, int_1: int) -> None:
        """void SetMousePosition(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_mouse_scale(self, float_0: float, float_1: float) -> None:
        """void SetMouseScale(float, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_music_pitch(self, Music_0: Music, float_1: float) -> None:
        """void SetMusicPitch(struct Music, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_music_volume(self, Music_0: Music, float_1: float) -> None:
        """void SetMusicVolume(struct Music, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_pixel_color(self, void_pointer_0: Any, Color_1: Color, int_2: int) -> None:
        """void SetPixelColor(void *, struct Color, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shader_value(self, Shader_0: Shader, int_1: int, void_pointer_2: Any, int_3: int) -> None:
        """void SetShaderValue(struct Shader, int, void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shader_value_matrix(self, Shader_0: Shader, int_1: int, Matrix_2: Matrix) -> None:
        """void SetShaderValueMatrix(struct Shader, int, struct Matrix);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shader_value_texture(self, Shader_0: Shader, int_1: int, Texture_2: Texture) -> None:
        """void SetShaderValueTexture(struct Shader, int, struct Texture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shader_value_v(self, Shader_0: Shader, int_1: int, void_pointer_2: Any, int_3: int, int_4: int) -> None:
        """void SetShaderValueV(struct Shader, int, void *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shapes_texture(self, Texture_0: Texture, Rectangle_1: Rectangle) -> None:
        """void SetShapesTexture(struct Texture, struct Rectangle);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_sound_pitch(self, Sound_0: Sound, float_1: float) -> None:
        """void SetSoundPitch(struct Sound, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_sound_volume(self, Sound_0: Sound, float_1: float) -> None:
        """void SetSoundVolume(struct Sound, float);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_target_fps(self, int_0: int) -> None:
        """void SetTargetFPS(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_texture_filter(self, Texture_0: Texture, int_1: int) -> None:
        """void SetTextureFilter(struct Texture, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_texture_wrap(self, Texture_0: Texture, int_1: int) -> None:
        """void SetTextureWrap(struct Texture, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_trace_log_level(self, int_0: int) -> None:
        """void SetTraceLogLevel(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_icon(self, Image_0: Image) -> None:
        """void SetWindowIcon(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_min_size(self, int_0: int, int_1: int) -> None:
        """void SetWindowMinSize(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_monitor(self, int_0: int) -> None:
        """void SetWindowMonitor(int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_position(self, int_0: int, int_1: int) -> None:
        """void SetWindowPosition(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_size(self, int_0: int, int_1: int) -> None:
        """void SetWindowSize(int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_state(self, unsignedint_0: int) -> None:
        """void SetWindowState(unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_title(self, str_0: str) -> None:
        """void SetWindowTitle(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def show_cursor(self) -> None:
        """void ShowCursor();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def stop_audio_stream(self, AudioStream_0: AudioStream) -> None:
        """void StopAudioStream(struct AudioStream);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def stop_music_stream(self, Music_0: Music) -> None:
        """void StopMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def stop_sound(self, Sound_0: Sound) -> None:
        """void StopSound(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def stop_sound_multi(self) -> None:
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
    def take_screenshot(self, str_0: str) -> None:
        """void TakeScreenshot(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_append(self, str_0: str, str_1: str, int_pointer_2: Any) -> None:
        """void TextAppend(char *, char *, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_copy(self, str_0: str, str_1: str) -> int:
        """int TextCopy(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_find_index(self, str_0: str, str_1: str) -> int:
        """int TextFindIndex(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_format(self, *args) -> str:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
    def text_insert(self, str_0: str, str_1: str, int_2: int) -> str:
        """char *TextInsert(char *, char *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_is_equal(self, str_0: str, str_1: str) -> bool:
        """_Bool TextIsEqual(char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_join(self, str_pointer_0: str, int_1: int, str_2: str) -> str:
        """char *TextJoin(char * *, int, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_length(self, str_0: str) -> int:
        """unsigned int TextLength(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_replace(self, str_0: str, str_1: str, str_2: str) -> str:
        """char *TextReplace(char *, char *, char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_split(self, str_0: str, char_1: str, int_pointer_2: Any) -> str:
        """char * *TextSplit(char *, char, int *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_subtext(self, str_0: str, int_1: int, int_2: int) -> str:
        """char *TextSubtext(char *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_integer(self, str_0: str) -> int:
        """int TextToInteger(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_lower(self, str_0: str) -> str:
        """char *TextToLower(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_pascal(self, str_0: str) -> str:
        """char *TextToPascal(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_upper(self, str_0: str) -> str:
        """char *TextToUpper(char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_utf8(self, int_pointer_0: Any, int_1: int) -> str:
        """char *TextToUtf8(int *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def toggle_fullscreen(self) -> None:
        """void ToggleFullscreen();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def trace_log(self, *args) -> None:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
    def unload_file_data(self, unsignedstr_0: str) -> None:
        """void UnloadFileData(unsigned char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_file_text(self, unsignedstr_0: str) -> None:
        """void UnloadFileText(unsigned char *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_font(self, Font_0: Font) -> None:
        """void UnloadFont(struct Font);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_font_data(self, CharInfo_pointer_0: Any, int_1: int) -> None:
        """void UnloadFontData(struct CharInfo *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_image(self, Image_0: Image) -> None:
        """void UnloadImage(struct Image);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_image_colors(self, Color_pointer_0: Any) -> None:
        """void UnloadImageColors(struct Color *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_image_palette(self, Color_pointer_0: Any) -> None:
        """void UnloadImagePalette(struct Color *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_material(self, Material_0: Material) -> None:
        """void UnloadMaterial(struct Material);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_mesh(self, Mesh_0: Mesh) -> None:
        """void UnloadMesh(struct Mesh);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_model(self, Model_0: Model) -> None:
        """void UnloadModel(struct Model);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_model_animation(self, ModelAnimation_0: ModelAnimation) -> None:
        """void UnloadModelAnimation(struct ModelAnimation);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_model_animations(self, ModelAnimation_pointer_0: Any, unsignedint_1: int) -> None:
        """void UnloadModelAnimations(struct ModelAnimation *, unsigned int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_model_keep_meshes(self, Model_0: Model) -> None:
        """void UnloadModelKeepMeshes(struct Model);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_music_stream(self, Music_0: Music) -> None:
        """void UnloadMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_render_texture(self, RenderTexture_0: RenderTexture) -> None:
        """void UnloadRenderTexture(struct RenderTexture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_shader(self, Shader_0: Shader) -> None:
        """void UnloadShader(struct Shader);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_sound(self, Sound_0: Sound) -> None:
        """void UnloadSound(struct Sound);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_texture(self, Texture_0: Texture) -> None:
        """void UnloadTexture(struct Texture);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_vr_stereo_config(self, VrStereoConfig_0: VrStereoConfig) -> None:
        """void UnloadVrStereoConfig(struct VrStereoConfig);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_wave(self, Wave_0: Wave) -> None:
        """void UnloadWave(struct Wave);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_wave_samples(self, float_pointer_0: Any) -> None:
        """void UnloadWaveSamples(float *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_audio_stream(self, AudioStream_0: AudioStream, void_pointer_1: Any, int_2: int) -> None:
        """void UpdateAudioStream(struct AudioStream, void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_camera(self, Camera3D_pointer_0: Any) -> None:
        """void UpdateCamera(struct Camera3D *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_mesh_buffer(self, Mesh_0: Mesh, int_1: int, void_pointer_2: Any, int_3: int, int_4: int) -> None:
        """void UpdateMeshBuffer(struct Mesh, int, void *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_model_animation(self, Model_0: Model, ModelAnimation_1: ModelAnimation, int_2: int) -> None:
        """void UpdateModelAnimation(struct Model, struct ModelAnimation, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_music_stream(self, Music_0: Music) -> None:
        """void UpdateMusicStream(struct Music);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_sound(self, Sound_0: Sound, void_pointer_1: Any, int_2: int) -> None:
        """void UpdateSound(struct Sound, void *, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_texture(self, Texture_0: Texture, void_pointer_1: Any) -> None:
        """void UpdateTexture(struct Texture, void *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_texture_rec(self, Texture_0: Texture, Rectangle_1: Rectangle, void_pointer_2: Any) -> None:
        """void UpdateTextureRec(struct Texture, struct Rectangle, void *);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def upload_mesh(self, Mesh_pointer_0: Any, _Bool_1: bool) -> None:
        """void UploadMesh(struct Mesh *, _Bool);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def wave_copy(self, Wave_0: Wave) -> Wave:
        """struct Wave WaveCopy(struct Wave);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def wave_crop(self, Wave_pointer_0: Any, int_1: int, int_2: int) -> None:
        """void WaveCrop(struct Wave *, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def wave_format(self, Wave_pointer_0: Any, int_1: int, int_2: int, int_3: int) -> None:
        """void WaveFormat(struct Wave *, int, int, int);

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def window_should_close(self) -> bool:
        """_Bool WindowShouldClose();

CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    class AudioStream:
        def __init__(self, buffer, sampleRate, sampleSize, channels):
            self.buffer=buffer
            self.sampleRate=sampleRate
            self.sampleSize=sampleSize
            self.channels=channels
    BlendMode: int
    class BoneInfo:
        def __init__(self, name, parent):
            self.name=name
            self.parent=parent
    class BoundingBox:
        def __init__(self, min, max):
            self.min=min
            self.max=max
    class Camera:
        def __init__(self, position, target, up, fovy, projection):
            self.position=position
            self.target=target
            self.up=up
            self.fovy=fovy
            self.projection=projection
    class Camera2D:
        def __init__(self, offset, target, rotation, zoom):
            self.offset=offset
            self.target=target
            self.rotation=rotation
            self.zoom=zoom
    class Camera3D:
        def __init__(self, position, target, up, fovy, projection):
            self.position=position
            self.target=target
            self.up=up
            self.fovy=fovy
            self.projection=projection
    CameraMode: int
    CameraProjection: int
    class CharInfo:
        def __init__(self, value, offsetX, offsetY, advanceX, image):
            self.value=value
            self.offsetX=offsetX
            self.offsetY=offsetY
            self.advanceX=advanceX
            self.image=image
    class Color:
        def __init__(self, r, g, b, a):
            self.r=r
            self.g=g
            self.b=b
            self.a=a
    ConfigFlags: int
    CubemapLayout: int
    class Font:
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
        def __init__(self, data, width, height, mipmaps, format):
            self.data=data
            self.width=width
            self.height=height
            self.mipmaps=mipmaps
            self.format=format
    KeyboardKey: int
    class Material:
        def __init__(self, shader, maps, params):
            self.shader=shader
            self.maps=maps
            self.params=params
    class MaterialMap:
        def __init__(self, texture, color, value):
            self.texture=texture
            self.color=color
            self.value=value
    MaterialMapIndex: int
    class Matrix:
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
        def __init__(self, boneCount, frameCount, bones, framePoses):
            self.boneCount=boneCount
            self.frameCount=frameCount
            self.bones=bones
            self.framePoses=framePoses
    MouseButton: int
    MouseCursor: int
    class Music:
        def __init__(self, stream, sampleCount, looping, ctxType, ctxData):
            self.stream=stream
            self.sampleCount=sampleCount
            self.looping=looping
            self.ctxType=ctxType
            self.ctxData=ctxData
    class NPatchInfo:
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
        def __init__(self, x, y, z, w):
            self.x=x
            self.y=y
            self.z=z
            self.w=w
    class Ray:
        def __init__(self, position, direction):
            self.position=position
            self.direction=direction
    class RayHitInfo:
        def __init__(self, hit, distance, position, normal):
            self.hit=hit
            self.distance=distance
            self.position=position
            self.normal=normal
    class Rectangle:
        def __init__(self, x, y, width, height):
            self.x=x
            self.y=y
            self.width=width
            self.height=height
    class RenderTexture:
        def __init__(self, id, texture, depth):
            self.id=id
            self.texture=texture
            self.depth=depth
    class RenderTexture2D:
        def __init__(self, id, texture, depth):
            self.id=id
            self.texture=texture
            self.depth=depth
    class Shader:
        def __init__(self, id, locs):
            self.id=id
            self.locs=locs
    ShaderLocationIndex: int
    ShaderUniformDataType: int
    class Sound:
        def __init__(self, stream, sampleCount):
            self.stream=stream
            self.sampleCount=sampleCount
    class Texture:
        def __init__(self, id, width, height, mipmaps, format):
            self.id=id
            self.width=width
            self.height=height
            self.mipmaps=mipmaps
            self.format=format
    class Texture2D:
        def __init__(self, id, width, height, mipmaps, format):
            self.id=id
            self.width=width
            self.height=height
            self.mipmaps=mipmaps
            self.format=format
    class TextureCubemap:
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
        def __init__(self, translation, rotation, scale):
            self.translation=translation
            self.rotation=rotation
            self.scale=scale
    class Vector2:
        def __init__(self, x, y):
            self.x=x
            self.y=y
    class Vector3:
        def __init__(self, x, y, z):
            self.x=x
            self.y=y
            self.z=z
    class Vector4:
        def __init__(self, x, y, z, w):
            self.x=x
            self.y=y
            self.z=z
            self.w=w
    class VrDeviceInfo:
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
        def __init__(self, sampleCount, sampleRate, sampleSize, channels, data):
            self.sampleCount=sampleCount
            self.sampleRate=sampleRate
            self.sampleSize=sampleSize
            self.channels=channels
            self.data=data

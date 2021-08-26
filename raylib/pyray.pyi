class PyRay:
    BLEND_ADDITIVE: int
    BLEND_ADD_COLORS: int
    BLEND_ALPHA: int
    BLEND_CUSTOM: int
    BLEND_MULTIPLIED: int
    BLEND_SUBTRACT_COLORS: int
    def begin_blend_mode(self, int_0) -> None :
        """void BeginBlendMode(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_drawing(self) -> None :
        """void BeginDrawing();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_mode_2d(self, struct_camera2_d_0) -> None :
        """void BeginMode2D(struct Camera2D);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_mode_3d(self, struct_camera3_d_0) -> None :
        """void BeginMode3D(struct Camera3D);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_scissor_mode(self, int_0, int_1, int_2, int_3) -> None :
        """void BeginScissorMode(int, int, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_shader_mode(self, struct_shader_0) -> None :
        """void BeginShaderMode(struct Shader);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_texture_mode(self, struct_render_texture_0) -> None :
        """void BeginTextureMode(struct RenderTexture);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def begin_vr_stereo_mode(self, struct_vr_stereo_config_0) -> None :
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
    def change_directory(self, str_0) -> int :
        """int ChangeDirectory(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_box_sphere(self, struct_bounding_box_0, struct_vector3_1, float_2) -> int :
        """int CheckCollisionBoxSphere(struct BoundingBox, struct Vector3, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_boxes(self, struct_bounding_box_0, struct_bounding_box_1) -> int :
        """int CheckCollisionBoxes(struct BoundingBox, struct BoundingBox);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_circle_rec(self, struct_vector2_0, float_1, struct_rectangle_2) -> int :
        """int CheckCollisionCircleRec(struct Vector2, float, struct Rectangle);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_circles(self, struct_vector2_0, float_1, struct_vector2_2, float_3) -> int :
        """int CheckCollisionCircles(struct Vector2, float, struct Vector2, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_lines(self, struct_vector2_0, struct_vector2_1, struct_vector2_2, struct_vector2_3, struct_vector2_4) -> int :
        """int CheckCollisionLines(struct Vector2, struct Vector2, struct Vector2, struct Vector2, struct Vector2 *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_point_circle(self, struct_vector2_0, struct_vector2_1, float_2) -> int :
        """int CheckCollisionPointCircle(struct Vector2, struct Vector2, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_point_rec(self, struct_vector2_0, struct_rectangle_1) -> int :
        """int CheckCollisionPointRec(struct Vector2, struct Rectangle);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_point_triangle(self, struct_vector2_0, struct_vector2_1, struct_vector2_2, struct_vector2_3) -> int :
        """int CheckCollisionPointTriangle(struct Vector2, struct Vector2, struct Vector2, struct Vector2);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_ray_box(self, struct_ray_0, struct_bounding_box_1) -> int :
        """int CheckCollisionRayBox(struct Ray, struct BoundingBox);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_ray_sphere(self, struct_ray_0, struct_vector3_1, float_2) -> int :
        """int CheckCollisionRaySphere(struct Ray, struct Vector3, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_ray_sphere_ex(self, struct_ray_0, struct_vector3_1, float_2, struct_vector3_3) -> int :
        """int CheckCollisionRaySphereEx(struct Ray, struct Vector3, float, struct Vector3 *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_recs(self, struct_rectangle_0, struct_rectangle_1) -> int :
        """int CheckCollisionRecs(struct Rectangle, struct Rectangle);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def check_collision_spheres(self, struct_vector3_0, float_1, struct_vector3_2, float_3) -> int :
        """int CheckCollisionSpheres(struct Vector3, float, struct Vector3, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def clear_background(self, struct_color_0) -> None :
        """void ClearBackground(struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def clear_directory_files(self) -> None :
        """void ClearDirectoryFiles();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def clear_dropped_files(self) -> None :
        """void ClearDroppedFiles();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def clear_window_state(self, int_0) -> None :
        """void ClearWindowState(unsigned int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def close_audio_device(self) -> None :
        """void CloseAudioDevice();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def close_audio_stream(self, struct_audio_stream_0) -> None :
        """void CloseAudioStream(struct AudioStream);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def close_window(self) -> None :
        """void CloseWindow();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def codepoint_to_utf8(self, int_0, int_1) -> str :
        """char *CodepointToUtf8(int, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_alpha(self, struct_color_0, float_1) -> struct :
        """struct Color ColorAlpha(struct Color, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_alpha_blend(self, struct_color_0, struct_color_1, struct_color_2) -> struct :
        """struct Color ColorAlphaBlend(struct Color, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_from_hsv(self, float_0, float_1, float_2) -> struct :
        """struct Color ColorFromHSV(float, float, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_from_normalized(self, struct_vector4_0) -> struct :
        """struct Color ColorFromNormalized(struct Vector4);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_normalize(self, struct_color_0) -> struct :
        """struct Vector4 ColorNormalize(struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_to_hsv(self, struct_color_0) -> struct :
        """struct Vector3 ColorToHSV(struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def color_to_int(self, struct_color_0) -> int :
        """int ColorToInt(struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def compress_data(self, str_0, int_1, int_2) -> str :
        """unsigned char *CompressData(unsigned char *, int, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def decompress_data(self, str_0, int_1, int_2) -> str :
        """unsigned char *DecompressData(unsigned char *, int, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def directory_exists(self, str_0) -> int :
        """int DirectoryExists(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def disable_cursor(self) -> None :
        """void DisableCursor();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_billboard(self, struct_camera3_d_0, struct_texture_1, struct_vector3_2, float_3, struct_color_4) -> None :
        """void DrawBillboard(struct Camera3D, struct Texture, struct Vector3, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_billboard_rec(self, struct_camera3_d_0, struct_texture_1, struct_rectangle_2, struct_vector3_3, float_4, struct_color_5) -> None :
        """void DrawBillboardRec(struct Camera3D, struct Texture, struct Rectangle, struct Vector3, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_bounding_box(self, struct_bounding_box_0, struct_color_1) -> None :
        """void DrawBoundingBox(struct BoundingBox, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle(self, int_0, int_1, float_2, struct_color_3) -> None :
        """void DrawCircle(int, int, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_3d(self, struct_vector3_0, float_1, struct_vector3_2, float_3, struct_color_4) -> None :
        """void DrawCircle3D(struct Vector3, float, struct Vector3, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_gradient(self, int_0, int_1, float_2, struct_color_3, struct_color_4) -> None :
        """void DrawCircleGradient(int, int, float, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_lines(self, int_0, int_1, float_2, struct_color_3) -> None :
        """void DrawCircleLines(int, int, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_sector(self, struct_vector2_0, float_1, float_2, float_3, int_4, struct_color_5) -> None :
        """void DrawCircleSector(struct Vector2, float, float, float, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_sector_lines(self, struct_vector2_0, float_1, float_2, float_3, int_4, struct_color_5) -> None :
        """void DrawCircleSectorLines(struct Vector2, float, float, float, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_circle_v(self, struct_vector2_0, float_1, struct_color_2) -> None :
        """void DrawCircleV(struct Vector2, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube(self, struct_vector3_0, float_1, float_2, float_3, struct_color_4) -> None :
        """void DrawCube(struct Vector3, float, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube_texture(self, struct_texture_0, struct_vector3_1, float_2, float_3, float_4, struct_color_5) -> None :
        """void DrawCubeTexture(struct Texture, struct Vector3, float, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube_v(self, struct_vector3_0, struct_vector3_1, struct_color_2) -> None :
        """void DrawCubeV(struct Vector3, struct Vector3, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube_wires(self, struct_vector3_0, float_1, float_2, float_3, struct_color_4) -> None :
        """void DrawCubeWires(struct Vector3, float, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cube_wires_v(self, struct_vector3_0, struct_vector3_1, struct_color_2) -> None :
        """void DrawCubeWiresV(struct Vector3, struct Vector3, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cylinder(self, struct_vector3_0, float_1, float_2, float_3, int_4, struct_color_5) -> None :
        """void DrawCylinder(struct Vector3, float, float, float, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_cylinder_wires(self, struct_vector3_0, float_1, float_2, float_3, int_4, struct_color_5) -> None :
        """void DrawCylinderWires(struct Vector3, float, float, float, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ellipse(self, int_0, int_1, float_2, float_3, struct_color_4) -> None :
        """void DrawEllipse(int, int, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ellipse_lines(self, int_0, int_1, float_2, float_3, struct_color_4) -> None :
        """void DrawEllipseLines(int, int, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_fps(self, int_0, int_1) -> None :
        """void DrawFPS(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_grid(self, int_0, float_1) -> None :
        """void DrawGrid(int, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line(self, int_0, int_1, int_2, int_3, struct_color_4) -> None :
        """void DrawLine(int, int, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_3d(self, struct_vector3_0, struct_vector3_1, struct_color_2) -> None :
        """void DrawLine3D(struct Vector3, struct Vector3, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_bezier(self, struct_vector2_0, struct_vector2_1, float_2, struct_color_3) -> None :
        """void DrawLineBezier(struct Vector2, struct Vector2, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_bezier_quad(self, struct_vector2_0, struct_vector2_1, struct_vector2_2, float_3, struct_color_4) -> None :
        """void DrawLineBezierQuad(struct Vector2, struct Vector2, struct Vector2, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_ex(self, struct_vector2_0, struct_vector2_1, float_2, struct_color_3) -> None :
        """void DrawLineEx(struct Vector2, struct Vector2, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_strip(self, struct_vector2_0, int_1, struct_color_2) -> None :
        """void DrawLineStrip(struct Vector2 *, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_line_v(self, struct_vector2_0, struct_vector2_1, struct_color_2) -> None :
        """void DrawLineV(struct Vector2, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_mesh(self, struct_mesh_0, struct_material_1, struct_matrix_2) -> None :
        """void DrawMesh(struct Mesh, struct Material, struct Matrix);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_mesh_instanced(self, struct_mesh_0, struct_material_1, struct_matrix_2, int_3) -> None :
        """void DrawMeshInstanced(struct Mesh, struct Material, struct Matrix *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_model(self, struct_model_0, struct_vector3_1, float_2, struct_color_3) -> None :
        """void DrawModel(struct Model, struct Vector3, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_model_ex(self, struct_model_0, struct_vector3_1, struct_vector3_2, float_3, struct_vector3_4, struct_color_5) -> None :
        """void DrawModelEx(struct Model, struct Vector3, struct Vector3, float, struct Vector3, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_model_wires(self, struct_model_0, struct_vector3_1, float_2, struct_color_3) -> None :
        """void DrawModelWires(struct Model, struct Vector3, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_model_wires_ex(self, struct_model_0, struct_vector3_1, struct_vector3_2, float_3, struct_vector3_4, struct_color_5) -> None :
        """void DrawModelWiresEx(struct Model, struct Vector3, struct Vector3, float, struct Vector3, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_pixel(self, int_0, int_1, struct_color_2) -> None :
        """void DrawPixel(int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_pixel_v(self, struct_vector2_0, struct_color_1) -> None :
        """void DrawPixelV(struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_plane(self, struct_vector3_0, struct_vector2_1, struct_color_2) -> None :
        """void DrawPlane(struct Vector3, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_point_3d(self, struct_vector3_0, struct_color_1) -> None :
        """void DrawPoint3D(struct Vector3, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_poly(self, struct_vector2_0, int_1, float_2, float_3, struct_color_4) -> None :
        """void DrawPoly(struct Vector2, int, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_poly_lines(self, struct_vector2_0, int_1, float_2, float_3, struct_color_4) -> None :
        """void DrawPolyLines(struct Vector2, int, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ray(self, struct_ray_0, struct_color_1) -> None :
        """void DrawRay(struct Ray, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle(self, int_0, int_1, int_2, int_3, struct_color_4) -> None :
        """void DrawRectangle(int, int, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_gradient_ex(self, struct_rectangle_0, struct_color_1, struct_color_2, struct_color_3, struct_color_4) -> None :
        """void DrawRectangleGradientEx(struct Rectangle, struct Color, struct Color, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_gradient_h(self, int_0, int_1, int_2, int_3, struct_color_4, struct_color_5) -> None :
        """void DrawRectangleGradientH(int, int, int, int, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_gradient_v(self, int_0, int_1, int_2, int_3, struct_color_4, struct_color_5) -> None :
        """void DrawRectangleGradientV(int, int, int, int, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_lines(self, int_0, int_1, int_2, int_3, struct_color_4) -> None :
        """void DrawRectangleLines(int, int, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_lines_ex(self, struct_rectangle_0, int_1, struct_color_2) -> None :
        """void DrawRectangleLinesEx(struct Rectangle, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_pro(self, struct_rectangle_0, struct_vector2_1, float_2, struct_color_3) -> None :
        """void DrawRectanglePro(struct Rectangle, struct Vector2, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_rec(self, struct_rectangle_0, struct_color_1) -> None :
        """void DrawRectangleRec(struct Rectangle, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_rounded(self, struct_rectangle_0, float_1, int_2, struct_color_3) -> None :
        """void DrawRectangleRounded(struct Rectangle, float, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_rounded_lines(self, struct_rectangle_0, float_1, int_2, int_3, struct_color_4) -> None :
        """void DrawRectangleRoundedLines(struct Rectangle, float, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_rectangle_v(self, struct_vector2_0, struct_vector2_1, struct_color_2) -> None :
        """void DrawRectangleV(struct Vector2, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ring(self, struct_vector2_0, float_1, float_2, float_3, float_4, int_5, struct_color_6) -> None :
        """void DrawRing(struct Vector2, float, float, float, float, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_ring_lines(self, struct_vector2_0, float_1, float_2, float_3, float_4, int_5, struct_color_6) -> None :
        """void DrawRingLines(struct Vector2, float, float, float, float, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_sphere(self, struct_vector3_0, float_1, struct_color_2) -> None :
        """void DrawSphere(struct Vector3, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_sphere_ex(self, struct_vector3_0, float_1, int_2, int_3, struct_color_4) -> None :
        """void DrawSphereEx(struct Vector3, float, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_sphere_wires(self, struct_vector3_0, float_1, int_2, int_3, struct_color_4) -> None :
        """void DrawSphereWires(struct Vector3, float, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text(self, str_0, int_1, int_2, int_3, struct_color_4) -> None :
        """void DrawText(char *, int, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text_codepoint(self, struct_font_0, int_1, struct_vector2_2, float_3, struct_color_4) -> None :
        """void DrawTextCodepoint(struct Font, int, struct Vector2, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text_ex(self, struct_font_0, str_1, struct_vector2_2, float_3, float_4, struct_color_5) -> None :
        """void DrawTextEx(struct Font, char *, struct Vector2, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text_rec(self, struct_font_0, str_1, struct_rectangle_2, float_3, float_4, int_5, struct_color_6) -> None :
        """void DrawTextRec(struct Font, char *, struct Rectangle, float, float, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_text_rec_ex(self, struct_font_0, str_1, struct_rectangle_2, float_3, float_4, int_5, struct_color_6, int_7, int_8, struct_color_9, struct_color_10) -> None :
        """void DrawTextRecEx(struct Font, char *, struct Rectangle, float, float, int, struct Color, int, int, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture(self, struct_texture_0, int_1, int_2, struct_color_3) -> None :
        """void DrawTexture(struct Texture, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_ex(self, struct_texture_0, struct_vector2_1, float_2, float_3, struct_color_4) -> None :
        """void DrawTextureEx(struct Texture, struct Vector2, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_n_patch(self, struct_texture_0, struct_n_patch_info_1, struct_rectangle_2, struct_vector2_3, float_4, struct_color_5) -> None :
        """void DrawTextureNPatch(struct Texture, struct NPatchInfo, struct Rectangle, struct Vector2, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_poly(self, struct_texture_0, struct_vector2_1, struct_vector2_2, struct_vector2_3, int_4, struct_color_5) -> None :
        """void DrawTexturePoly(struct Texture, struct Vector2, struct Vector2 *, struct Vector2 *, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_pro(self, struct_texture_0, struct_rectangle_1, struct_rectangle_2, struct_vector2_3, float_4, struct_color_5) -> None :
        """void DrawTexturePro(struct Texture, struct Rectangle, struct Rectangle, struct Vector2, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_quad(self, struct_texture_0, struct_vector2_1, struct_vector2_2, struct_rectangle_3, struct_color_4) -> None :
        """void DrawTextureQuad(struct Texture, struct Vector2, struct Vector2, struct Rectangle, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_rec(self, struct_texture_0, struct_rectangle_1, struct_vector2_2, struct_color_3) -> None :
        """void DrawTextureRec(struct Texture, struct Rectangle, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_tiled(self, struct_texture_0, struct_rectangle_1, struct_rectangle_2, struct_vector2_3, float_4, float_5, struct_color_6) -> None :
        """void DrawTextureTiled(struct Texture, struct Rectangle, struct Rectangle, struct Vector2, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_texture_v(self, struct_texture_0, struct_vector2_1, struct_color_2) -> None :
        """void DrawTextureV(struct Texture, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle(self, struct_vector2_0, struct_vector2_1, struct_vector2_2, struct_color_3) -> None :
        """void DrawTriangle(struct Vector2, struct Vector2, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_3d(self, struct_vector3_0, struct_vector3_1, struct_vector3_2, struct_color_3) -> None :
        """void DrawTriangle3D(struct Vector3, struct Vector3, struct Vector3, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_fan(self, struct_vector2_0, int_1, struct_color_2) -> None :
        """void DrawTriangleFan(struct Vector2 *, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_lines(self, struct_vector2_0, struct_vector2_1, struct_vector2_2, struct_color_3) -> None :
        """void DrawTriangleLines(struct Vector2, struct Vector2, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_strip(self, struct_vector2_0, int_1, struct_color_2) -> None :
        """void DrawTriangleStrip(struct Vector2 *, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def draw_triangle_strip_3d(self, struct_vector3_0, int_1, struct_color_2) -> None :
        """void DrawTriangleStrip3D(struct Vector3 *, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def enable_cursor(self) -> None :
        """void EnableCursor();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_blend_mode(self) -> None :
        """void EndBlendMode();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_drawing(self) -> None :
        """void EndDrawing();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_mode_2d(self) -> None :
        """void EndMode2D();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_mode_3d(self) -> None :
        """void EndMode3D();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_scissor_mode(self) -> None :
        """void EndScissorMode();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_shader_mode(self) -> None :
        """void EndShaderMode();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_texture_mode(self) -> None :
        """void EndTextureMode();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def end_vr_stereo_mode(self) -> None :
        """void EndVrStereoMode();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_image(self, struct_image_0, str_1) -> int :
        """int ExportImage(struct Image, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_image_as_code(self, struct_image_0, str_1) -> int :
        """int ExportImageAsCode(struct Image, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_mesh(self, struct_mesh_0, str_1) -> int :
        """int ExportMesh(struct Mesh, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_wave(self, struct_wave_0, str_1) -> int :
        """int ExportWave(struct Wave, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def export_wave_as_code(self, struct_wave_0, str_1) -> int :
        """int ExportWaveAsCode(struct Wave, char *);
        
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
    def fade(self, struct_color_0, float_1) -> struct :
        """struct Color Fade(struct Color, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def file_exists(self, str_0) -> int :
        """int FileExists(char *);
        
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
    def gen_image_cellular(self, int_0, int_1, int_2) -> struct :
        """struct Image GenImageCellular(int, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_checked(self, int_0, int_1, int_2, int_3, struct_color_4, struct_color_5) -> struct :
        """struct Image GenImageChecked(int, int, int, int, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_color(self, int_0, int_1, struct_color_2) -> struct :
        """struct Image GenImageColor(int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_font_atlas(self, struct_char_info_0, struct_rectangle_1, int_2, int_3, int_4, int_5) -> struct :
        """struct Image GenImageFontAtlas(struct CharInfo *, struct Rectangle * *, int, int, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_gradient_h(self, int_0, int_1, struct_color_2, struct_color_3) -> struct :
        """struct Image GenImageGradientH(int, int, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_gradient_radial(self, int_0, int_1, float_2, struct_color_3, struct_color_4) -> struct :
        """struct Image GenImageGradientRadial(int, int, float, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_gradient_v(self, int_0, int_1, struct_color_2, struct_color_3) -> struct :
        """struct Image GenImageGradientV(int, int, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_perlin_noise(self, int_0, int_1, int_2, int_3, float_4) -> struct :
        """struct Image GenImagePerlinNoise(int, int, int, int, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_image_white_noise(self, int_0, int_1, float_2) -> struct :
        """struct Image GenImageWhiteNoise(int, int, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_cube(self, float_0, float_1, float_2) -> struct :
        """struct Mesh GenMeshCube(float, float, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_cubicmap(self, struct_image_0, struct_vector3_1) -> struct :
        """struct Mesh GenMeshCubicmap(struct Image, struct Vector3);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_cylinder(self, float_0, float_1, int_2) -> struct :
        """struct Mesh GenMeshCylinder(float, float, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_heightmap(self, struct_image_0, struct_vector3_1) -> struct :
        """struct Mesh GenMeshHeightmap(struct Image, struct Vector3);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_hemi_sphere(self, float_0, int_1, int_2) -> struct :
        """struct Mesh GenMeshHemiSphere(float, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_knot(self, float_0, float_1, int_2, int_3) -> struct :
        """struct Mesh GenMeshKnot(float, float, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_plane(self, float_0, float_1, int_2, int_3) -> struct :
        """struct Mesh GenMeshPlane(float, float, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_poly(self, int_0, float_1) -> struct :
        """struct Mesh GenMeshPoly(int, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_sphere(self, float_0, int_1, int_2) -> struct :
        """struct Mesh GenMeshSphere(float, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_mesh_torus(self, float_0, float_1, int_2, int_3) -> struct :
        """struct Mesh GenMeshTorus(float, float, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def gen_texture_mipmaps(self, struct_texture_0) -> None :
        """void GenTextureMipmaps(struct Texture *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_camera_matrix(self, struct_camera3_d_0) -> struct :
        """struct Matrix GetCameraMatrix(struct Camera3D);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_camera_matrix_2d(self, struct_camera2_d_0) -> struct :
        """struct Matrix GetCameraMatrix2D(struct Camera2D);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_char_pressed(self) -> int :
        """int GetCharPressed();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_clipboard_text(self) -> str :
        """char *GetClipboardText();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_codepoints(self, str_0, int_1) -> int :
        """int *GetCodepoints(char *, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_codepoints_count(self, str_0) -> int :
        """int GetCodepointsCount(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_collision_ray_ground(self, struct_ray_0, float_1) -> struct :
        """struct RayHitInfo GetCollisionRayGround(struct Ray, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_collision_ray_mesh(self, struct_ray_0, struct_mesh_1, struct_matrix_2) -> struct :
        """struct RayHitInfo GetCollisionRayMesh(struct Ray, struct Mesh, struct Matrix);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_collision_ray_model(self, struct_ray_0, struct_model_1) -> struct :
        """struct RayHitInfo GetCollisionRayModel(struct Ray, struct Model);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_collision_ray_triangle(self, struct_ray_0, struct_vector3_1, struct_vector3_2, struct_vector3_3) -> struct :
        """struct RayHitInfo GetCollisionRayTriangle(struct Ray, struct Vector3, struct Vector3, struct Vector3);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_collision_rec(self, struct_rectangle_0, struct_rectangle_1) -> struct :
        """struct Rectangle GetCollisionRec(struct Rectangle, struct Rectangle);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_color(self, int_0) -> struct :
        """struct Color GetColor(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_current_monitor(self) -> int :
        """int GetCurrentMonitor();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_directory_files(self, str_0, int_1) -> str :
        """char * *GetDirectoryFiles(char *, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_directory_path(self, str_0) -> str :
        """char *GetDirectoryPath(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_dropped_files(self, int_0) -> str :
        """char * *GetDroppedFiles(int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_fps(self) -> int :
        """int GetFPS();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_file_extension(self, str_0) -> str :
        """char *GetFileExtension(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_file_mod_time(self, str_0) -> int :
        """long GetFileModTime(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_file_name(self, str_0) -> str :
        """char *GetFileName(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_file_name_without_ext(self, str_0) -> str :
        """char *GetFileNameWithoutExt(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_font_default(self) -> struct :
        """struct Font GetFontDefault();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_frame_time(self) -> float :
        """float GetFrameTime();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gamepad_axis_count(self, int_0) -> int :
        """int GetGamepadAxisCount(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gamepad_axis_movement(self, int_0, int_1) -> float :
        """float GetGamepadAxisMovement(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gamepad_button_pressed(self) -> int :
        """int GetGamepadButtonPressed();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gamepad_name(self, int_0) -> str :
        """char *GetGamepadName(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_detected(self) -> int :
        """int GetGestureDetected();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_drag_angle(self) -> float :
        """float GetGestureDragAngle();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_drag_vector(self) -> struct :
        """struct Vector2 GetGestureDragVector();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_hold_duration(self) -> float :
        """float GetGestureHoldDuration();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_pinch_angle(self) -> float :
        """float GetGesturePinchAngle();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_gesture_pinch_vector(self) -> struct :
        """struct Vector2 GetGesturePinchVector();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_glyph_index(self, struct_font_0, int_1) -> int :
        """int GetGlyphIndex(struct Font, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_image_alpha_border(self, struct_image_0, float_1) -> struct :
        """struct Rectangle GetImageAlphaBorder(struct Image, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_key_pressed(self) -> int :
        """int GetKeyPressed();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_count(self) -> int :
        """int GetMonitorCount();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_height(self, int_0) -> int :
        """int GetMonitorHeight(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_name(self, int_0) -> str :
        """char *GetMonitorName(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_physical_height(self, int_0) -> int :
        """int GetMonitorPhysicalHeight(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_physical_width(self, int_0) -> int :
        """int GetMonitorPhysicalWidth(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_position(self, int_0) -> struct :
        """struct Vector2 GetMonitorPosition(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_refresh_rate(self, int_0) -> int :
        """int GetMonitorRefreshRate(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_monitor_width(self, int_0) -> int :
        """int GetMonitorWidth(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_position(self) -> struct :
        """struct Vector2 GetMousePosition();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_ray(self, struct_vector2_0, struct_camera3_d_1) -> struct :
        """struct Ray GetMouseRay(struct Vector2, struct Camera3D);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_wheel_move(self) -> float :
        """float GetMouseWheelMove();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_x(self) -> int :
        """int GetMouseX();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_mouse_y(self) -> int :
        """int GetMouseY();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_music_time_length(self, struct_music_0) -> float :
        """float GetMusicTimeLength(struct Music);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_music_time_played(self, struct_music_0) -> float :
        """float GetMusicTimePlayed(struct Music);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_next_codepoint(self, str_0, int_1) -> int :
        """int GetNextCodepoint(char *, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_pixel_color(self, none_0, int_1) -> struct :
        """struct Color GetPixelColor(void *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_pixel_data_size(self, int_0, int_1, int_2) -> int :
        """int GetPixelDataSize(int, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_prev_directory_path(self, str_0) -> str :
        """char *GetPrevDirectoryPath(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_random_value(self, int_0, int_1) -> int :
        """int GetRandomValue(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_screen_data(self) -> struct :
        """struct Image GetScreenData();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_screen_height(self) -> int :
        """int GetScreenHeight();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_screen_to_world_2d(self, struct_vector2_0, struct_camera2_d_1) -> struct :
        """struct Vector2 GetScreenToWorld2D(struct Vector2, struct Camera2D);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_screen_width(self) -> int :
        """int GetScreenWidth();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_shader_location(self, struct_shader_0, str_1) -> int :
        """int GetShaderLocation(struct Shader, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_shader_location_attrib(self, struct_shader_0, str_1) -> int :
        """int GetShaderLocationAttrib(struct Shader, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_sounds_playing(self) -> int :
        """int GetSoundsPlaying();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_texture_data(self, struct_texture_0) -> struct :
        """struct Image GetTextureData(struct Texture);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_time(self) -> float :
        """double GetTime();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_touch_points_count(self) -> int :
        """int GetTouchPointsCount();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_touch_position(self, int_0) -> struct :
        """struct Vector2 GetTouchPosition(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_touch_x(self) -> int :
        """int GetTouchX();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_touch_y(self) -> int :
        """int GetTouchY();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_window_handle(self) -> None :
        """void *GetWindowHandle();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_window_position(self) -> struct :
        """struct Vector2 GetWindowPosition();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_window_scale_dpi(self) -> struct :
        """struct Vector2 GetWindowScaleDPI();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_working_directory(self) -> str :
        """char *GetWorkingDirectory();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_world_to_screen(self, struct_vector3_0, struct_camera3_d_1) -> struct :
        """struct Vector2 GetWorldToScreen(struct Vector3, struct Camera3D);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_world_to_screen_2d(self, struct_vector2_0, struct_camera2_d_1) -> struct :
        """struct Vector2 GetWorldToScreen2D(struct Vector2, struct Camera2D);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def get_world_to_screen_ex(self, struct_vector3_0, struct_camera3_d_1, int_2, int_3) -> struct :
        """struct Vector2 GetWorldToScreenEx(struct Vector3, struct Camera3D, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def hide_cursor(self) -> None :
        """void HideCursor();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_alpha_clear(self, struct_image_0, struct_color_1, float_2) -> None :
        """void ImageAlphaClear(struct Image *, struct Color, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_alpha_crop(self, struct_image_0, float_1) -> None :
        """void ImageAlphaCrop(struct Image *, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_alpha_mask(self, struct_image_0, struct_image_1) -> None :
        """void ImageAlphaMask(struct Image *, struct Image);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_alpha_premultiply(self, struct_image_0) -> None :
        """void ImageAlphaPremultiply(struct Image *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_clear_background(self, struct_image_0, struct_color_1) -> None :
        """void ImageClearBackground(struct Image *, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_brightness(self, struct_image_0, int_1) -> None :
        """void ImageColorBrightness(struct Image *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_contrast(self, struct_image_0, float_1) -> None :
        """void ImageColorContrast(struct Image *, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_grayscale(self, struct_image_0) -> None :
        """void ImageColorGrayscale(struct Image *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_invert(self, struct_image_0) -> None :
        """void ImageColorInvert(struct Image *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_replace(self, struct_image_0, struct_color_1, struct_color_2) -> None :
        """void ImageColorReplace(struct Image *, struct Color, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_color_tint(self, struct_image_0, struct_color_1) -> None :
        """void ImageColorTint(struct Image *, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_copy(self, struct_image_0) -> struct :
        """struct Image ImageCopy(struct Image);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_crop(self, struct_image_0, struct_rectangle_1) -> None :
        """void ImageCrop(struct Image *, struct Rectangle);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_dither(self, struct_image_0, int_1, int_2, int_3, int_4) -> None :
        """void ImageDither(struct Image *, int, int, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw(self, struct_image_0, struct_image_1, struct_rectangle_2, struct_rectangle_3, struct_color_4) -> None :
        """void ImageDraw(struct Image *, struct Image, struct Rectangle, struct Rectangle, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_circle(self, struct_image_0, int_1, int_2, int_3, struct_color_4) -> None :
        """void ImageDrawCircle(struct Image *, int, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_circle_v(self, struct_image_0, struct_vector2_1, int_2, struct_color_3) -> None :
        """void ImageDrawCircleV(struct Image *, struct Vector2, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_line(self, struct_image_0, int_1, int_2, int_3, int_4, struct_color_5) -> None :
        """void ImageDrawLine(struct Image *, int, int, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_line_v(self, struct_image_0, struct_vector2_1, struct_vector2_2, struct_color_3) -> None :
        """void ImageDrawLineV(struct Image *, struct Vector2, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_pixel(self, struct_image_0, int_1, int_2, struct_color_3) -> None :
        """void ImageDrawPixel(struct Image *, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_pixel_v(self, struct_image_0, struct_vector2_1, struct_color_2) -> None :
        """void ImageDrawPixelV(struct Image *, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_rectangle(self, struct_image_0, int_1, int_2, int_3, int_4, struct_color_5) -> None :
        """void ImageDrawRectangle(struct Image *, int, int, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_rectangle_lines(self, struct_image_0, struct_rectangle_1, int_2, struct_color_3) -> None :
        """void ImageDrawRectangleLines(struct Image *, struct Rectangle, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_rectangle_rec(self, struct_image_0, struct_rectangle_1, struct_color_2) -> None :
        """void ImageDrawRectangleRec(struct Image *, struct Rectangle, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_rectangle_v(self, struct_image_0, struct_vector2_1, struct_vector2_2, struct_color_3) -> None :
        """void ImageDrawRectangleV(struct Image *, struct Vector2, struct Vector2, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_text(self, struct_image_0, str_1, int_2, int_3, int_4, struct_color_5) -> None :
        """void ImageDrawText(struct Image *, char *, int, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_draw_text_ex(self, struct_image_0, struct_font_1, str_2, struct_vector2_3, float_4, float_5, struct_color_6) -> None :
        """void ImageDrawTextEx(struct Image *, struct Font, char *, struct Vector2, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_flip_horizontal(self, struct_image_0) -> None :
        """void ImageFlipHorizontal(struct Image *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_flip_vertical(self, struct_image_0) -> None :
        """void ImageFlipVertical(struct Image *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_format(self, struct_image_0, int_1) -> None :
        """void ImageFormat(struct Image *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_from_image(self, struct_image_0, struct_rectangle_1) -> struct :
        """struct Image ImageFromImage(struct Image, struct Rectangle);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_mipmaps(self, struct_image_0) -> None :
        """void ImageMipmaps(struct Image *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_resize(self, struct_image_0, int_1, int_2) -> None :
        """void ImageResize(struct Image *, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_resize_canvas(self, struct_image_0, int_1, int_2, int_3, int_4, struct_color_5) -> None :
        """void ImageResizeCanvas(struct Image *, int, int, int, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_resize_nn(self, struct_image_0, int_1, int_2) -> None :
        """void ImageResizeNN(struct Image *, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_rotate_ccw(self, struct_image_0) -> None :
        """void ImageRotateCCW(struct Image *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_rotate_cw(self, struct_image_0) -> None :
        """void ImageRotateCW(struct Image *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_text(self, str_0, int_1, struct_color_2) -> struct :
        """struct Image ImageText(char *, int, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_text_ex(self, struct_font_0, str_1, float_2, float_3, struct_color_4) -> struct :
        """struct Image ImageTextEx(struct Font, char *, float, float, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def image_to_pot(self, struct_image_0, struct_color_1) -> None :
        """void ImageToPOT(struct Image *, struct Color);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def init_audio_device(self) -> None :
        """void InitAudioDevice();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def init_audio_stream(self, int_0, int_1, int_2) -> struct :
        """struct AudioStream InitAudioStream(unsigned int, unsigned int, unsigned int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def init_window(self, int_0, int_1, str_2) -> None :
        """void InitWindow(int, int, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_audio_device_ready(self) -> int :
        """int IsAudioDeviceReady();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_audio_stream_playing(self, struct_audio_stream_0) -> int :
        """int IsAudioStreamPlaying(struct AudioStream);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_audio_stream_processed(self, struct_audio_stream_0) -> int :
        """int IsAudioStreamProcessed(struct AudioStream);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_cursor_hidden(self) -> int :
        """int IsCursorHidden();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_cursor_on_screen(self) -> int :
        """int IsCursorOnScreen();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_file_dropped(self) -> int :
        """int IsFileDropped();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_file_extension(self, str_0, str_1) -> int :
        """int IsFileExtension(char *, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_available(self, int_0) -> int :
        """int IsGamepadAvailable(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_button_down(self, int_0, int_1) -> int :
        """int IsGamepadButtonDown(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_button_pressed(self, int_0, int_1) -> int :
        """int IsGamepadButtonPressed(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_button_released(self, int_0, int_1) -> int :
        """int IsGamepadButtonReleased(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_button_up(self, int_0, int_1) -> int :
        """int IsGamepadButtonUp(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gamepad_name(self, int_0, str_1) -> int :
        """int IsGamepadName(int, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_gesture_detected(self, int_0) -> int :
        """int IsGestureDetected(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_key_down(self, int_0) -> int :
        """int IsKeyDown(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_key_pressed(self, int_0) -> int :
        """int IsKeyPressed(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_key_released(self, int_0) -> int :
        """int IsKeyReleased(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_key_up(self, int_0) -> int :
        """int IsKeyUp(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_model_animation_valid(self, struct_model_0, struct_model_animation_1) -> int :
        """int IsModelAnimationValid(struct Model, struct ModelAnimation);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_mouse_button_down(self, int_0) -> int :
        """int IsMouseButtonDown(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_mouse_button_pressed(self, int_0) -> int :
        """int IsMouseButtonPressed(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_mouse_button_released(self, int_0) -> int :
        """int IsMouseButtonReleased(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_mouse_button_up(self, int_0) -> int :
        """int IsMouseButtonUp(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_music_playing(self, struct_music_0) -> int :
        """int IsMusicPlaying(struct Music);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_sound_playing(self, struct_sound_0) -> int :
        """int IsSoundPlaying(struct Sound);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_focused(self) -> int :
        """int IsWindowFocused();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_fullscreen(self) -> int :
        """int IsWindowFullscreen();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_hidden(self) -> int :
        """int IsWindowHidden();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_maximized(self) -> int :
        """int IsWindowMaximized();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_minimized(self) -> int :
        """int IsWindowMinimized();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_ready(self) -> int :
        """int IsWindowReady();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_resized(self) -> int :
        """int IsWindowResized();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def is_window_state(self, int_0) -> int :
        """int IsWindowState(unsigned int);
        
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
    def load_file_data(self, str_0, int_1) -> str :
        """unsigned char *LoadFileData(char *, unsigned int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_file_text(self, str_0) -> str :
        """char *LoadFileText(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font(self, str_0) -> struct :
        """struct Font LoadFont(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font_data(self, str_0, int_1, int_2, int_3, int_4, int_5) -> struct :
        """struct CharInfo *LoadFontData(unsigned char *, int, int, int *, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font_ex(self, str_0, int_1, int_2, int_3) -> struct :
        """struct Font LoadFontEx(char *, int, int *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font_from_image(self, struct_image_0, struct_color_1, int_2) -> struct :
        """struct Font LoadFontFromImage(struct Image, struct Color, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_font_from_memory(self, str_0, str_1, int_2, int_3, int_4, int_5) -> struct :
        """struct Font LoadFontFromMemory(char *, unsigned char *, int, int, int *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image(self, str_0) -> struct :
        """struct Image LoadImage(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_anim(self, str_0, int_1) -> struct :
        """struct Image LoadImageAnim(char *, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_colors(self, struct_image_0) -> struct :
        """struct Color *LoadImageColors(struct Image);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_from_memory(self, str_0, str_1, int_2) -> struct :
        """struct Image LoadImageFromMemory(char *, unsigned char *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_palette(self, struct_image_0, int_1, int_2) -> struct :
        """struct Color *LoadImagePalette(struct Image, int, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_image_raw(self, str_0, int_1, int_2, int_3, int_4) -> struct :
        """struct Image LoadImageRaw(char *, int, int, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_material_default(self) -> struct :
        """struct Material LoadMaterialDefault();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_materials(self, str_0, int_1) -> struct :
        """struct Material *LoadMaterials(char *, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_model(self, str_0) -> struct :
        """struct Model LoadModel(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_model_animations(self, str_0, int_1) -> struct :
        """struct ModelAnimation *LoadModelAnimations(char *, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_model_from_mesh(self, struct_mesh_0) -> struct :
        """struct Model LoadModelFromMesh(struct Mesh);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_music_stream(self, str_0) -> struct :
        """struct Music LoadMusicStream(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_music_stream_from_memory(self, str_0, str_1, int_2) -> struct :
        """struct Music LoadMusicStreamFromMemory(char *, unsigned char *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_render_texture(self, int_0, int_1) -> struct :
        """struct RenderTexture LoadRenderTexture(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_shader(self, str_0, str_1) -> struct :
        """struct Shader LoadShader(char *, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_shader_from_memory(self, str_0, str_1) -> struct :
        """struct Shader LoadShaderFromMemory(char *, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_sound(self, str_0) -> struct :
        """struct Sound LoadSound(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_sound_from_wave(self, struct_wave_0) -> struct :
        """struct Sound LoadSoundFromWave(struct Wave);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_storage_value(self, int_0) -> int :
        """int LoadStorageValue(unsigned int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_texture(self, str_0) -> struct :
        """struct Texture LoadTexture(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_texture_cubemap(self, struct_image_0, int_1) -> struct :
        """struct Texture LoadTextureCubemap(struct Image, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_texture_from_image(self, struct_image_0) -> struct :
        """struct Texture LoadTextureFromImage(struct Image);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_vr_stereo_config(self, struct_vr_device_info_0) -> struct :
        """struct VrStereoConfig LoadVrStereoConfig(struct VrDeviceInfo);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_wave(self, str_0) -> struct :
        """struct Wave LoadWave(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_wave_from_memory(self, str_0, str_1, int_2) -> struct :
        """struct Wave LoadWaveFromMemory(char *, unsigned char *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def load_wave_samples(self, struct_wave_0) -> float :
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
    def maximize_window(self) -> None :
        """void MaximizeWindow();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def measure_text(self, str_0, int_1) -> int :
        """int MeasureText(char *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def measure_text_ex(self, struct_font_0, str_1, float_2, float_3) -> struct :
        """struct Vector2 MeasureTextEx(struct Font, char *, float, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mem_alloc(self, int_0) -> None :
        """void *MemAlloc(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mem_free(self, none_0) -> None :
        """void MemFree(void *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mem_realloc(self, none_0, int_1) -> None :
        """void *MemRealloc(void *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mesh_binormals(self, struct_mesh_0) -> None :
        """void MeshBinormals(struct Mesh *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mesh_bounding_box(self, struct_mesh_0) -> struct :
        """struct BoundingBox MeshBoundingBox(struct Mesh);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def mesh_tangents(self, struct_mesh_0) -> None :
        """void MeshTangents(struct Mesh *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def minimize_window(self) -> None :
        """void MinimizeWindow();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    NPATCH_NINE_PATCH: int
    NPATCH_THREE_PATCH_HORIZONTAL: int
    NPATCH_THREE_PATCH_VERTICAL: int
    def open_url(self, str_0) -> None :
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
    def pause_audio_stream(self, struct_audio_stream_0) -> None :
        """void PauseAudioStream(struct AudioStream);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def pause_music_stream(self, struct_music_0) -> None :
        """void PauseMusicStream(struct Music);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def pause_sound(self, struct_sound_0) -> None :
        """void PauseSound(struct Sound);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def play_audio_stream(self, struct_audio_stream_0) -> None :
        """void PlayAudioStream(struct AudioStream);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def play_music_stream(self, struct_music_0) -> None :
        """void PlayMusicStream(struct Music);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def play_sound(self, struct_sound_0) -> None :
        """void PlaySound(struct Sound);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def play_sound_multi(self, struct_sound_0) -> None :
        """void PlaySoundMulti(struct Sound);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def restore_window(self) -> None :
        """void RestoreWindow();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def resume_audio_stream(self, struct_audio_stream_0) -> None :
        """void ResumeAudioStream(struct AudioStream);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def resume_music_stream(self, struct_music_0) -> None :
        """void ResumeMusicStream(struct Music);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def resume_sound(self, struct_sound_0) -> None :
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
    def save_file_data(self, str_0, none_1, int_2) -> int :
        """int SaveFileData(char *, void *, unsigned int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def save_file_text(self, str_0, str_1) -> int :
        """int SaveFileText(char *, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def save_storage_value(self, int_0, int_1) -> int :
        """int SaveStorageValue(unsigned int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_audio_stream_buffer_size_default(self, int_0) -> None :
        """void SetAudioStreamBufferSizeDefault(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_audio_stream_pitch(self, struct_audio_stream_0, float_1) -> None :
        """void SetAudioStreamPitch(struct AudioStream, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_audio_stream_volume(self, struct_audio_stream_0, float_1) -> None :
        """void SetAudioStreamVolume(struct AudioStream, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_alt_control(self, int_0) -> None :
        """void SetCameraAltControl(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_mode(self, struct_camera3_d_0, int_1) -> None :
        """void SetCameraMode(struct Camera3D, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_move_controls(self, int_0, int_1, int_2, int_3, int_4, int_5) -> None :
        """void SetCameraMoveControls(int, int, int, int, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_pan_control(self, int_0) -> None :
        """void SetCameraPanControl(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_camera_smooth_zoom_control(self, int_0) -> None :
        """void SetCameraSmoothZoomControl(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_clipboard_text(self, str_0) -> None :
        """void SetClipboardText(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_config_flags(self, int_0) -> None :
        """void SetConfigFlags(unsigned int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_exit_key(self, int_0) -> None :
        """void SetExitKey(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_gamepad_mappings(self, str_0) -> int :
        """int SetGamepadMappings(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_gestures_enabled(self, int_0) -> None :
        """void SetGesturesEnabled(unsigned int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_master_volume(self, float_0) -> None :
        """void SetMasterVolume(float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_material_texture(self, struct_material_0, int_1, struct_texture_2) -> None :
        """void SetMaterialTexture(struct Material *, int, struct Texture);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_model_mesh_material(self, struct_model_0, int_1, int_2) -> None :
        """void SetModelMeshMaterial(struct Model *, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_mouse_cursor(self, int_0) -> None :
        """void SetMouseCursor(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_mouse_offset(self, int_0, int_1) -> None :
        """void SetMouseOffset(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_mouse_position(self, int_0, int_1) -> None :
        """void SetMousePosition(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_mouse_scale(self, float_0, float_1) -> None :
        """void SetMouseScale(float, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_music_pitch(self, struct_music_0, float_1) -> None :
        """void SetMusicPitch(struct Music, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_music_volume(self, struct_music_0, float_1) -> None :
        """void SetMusicVolume(struct Music, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_pixel_color(self, none_0, struct_color_1, int_2) -> None :
        """void SetPixelColor(void *, struct Color, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shader_value(self, struct_shader_0, int_1, none_2, int_3) -> None :
        """void SetShaderValue(struct Shader, int, void *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shader_value_matrix(self, struct_shader_0, int_1, struct_matrix_2) -> None :
        """void SetShaderValueMatrix(struct Shader, int, struct Matrix);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shader_value_texture(self, struct_shader_0, int_1, struct_texture_2) -> None :
        """void SetShaderValueTexture(struct Shader, int, struct Texture);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shader_value_v(self, struct_shader_0, int_1, none_2, int_3, int_4) -> None :
        """void SetShaderValueV(struct Shader, int, void *, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_shapes_texture(self, struct_texture_0, struct_rectangle_1) -> None :
        """void SetShapesTexture(struct Texture, struct Rectangle);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_sound_pitch(self, struct_sound_0, float_1) -> None :
        """void SetSoundPitch(struct Sound, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_sound_volume(self, struct_sound_0, float_1) -> None :
        """void SetSoundVolume(struct Sound, float);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_target_fps(self, int_0) -> None :
        """void SetTargetFPS(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_texture_filter(self, struct_texture_0, int_1) -> None :
        """void SetTextureFilter(struct Texture, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_texture_wrap(self, struct_texture_0, int_1) -> None :
        """void SetTextureWrap(struct Texture, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_trace_log_level(self, int_0) -> None :
        """void SetTraceLogLevel(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_icon(self, struct_image_0) -> None :
        """void SetWindowIcon(struct Image);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_min_size(self, int_0, int_1) -> None :
        """void SetWindowMinSize(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_monitor(self, int_0) -> None :
        """void SetWindowMonitor(int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_position(self, int_0, int_1) -> None :
        """void SetWindowPosition(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_size(self, int_0, int_1) -> None :
        """void SetWindowSize(int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_state(self, int_0) -> None :
        """void SetWindowState(unsigned int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def set_window_title(self, str_0) -> None :
        """void SetWindowTitle(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def show_cursor(self) -> None :
        """void ShowCursor();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def stop_audio_stream(self, struct_audio_stream_0) -> None :
        """void StopAudioStream(struct AudioStream);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def stop_music_stream(self, struct_music_0) -> None :
        """void StopMusicStream(struct Music);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def stop_sound(self, struct_sound_0) -> None :
        """void StopSound(struct Sound);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def stop_sound_multi(self) -> None :
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
    def take_screenshot(self, str_0) -> None :
        """void TakeScreenshot(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_append(self, str_0, str_1, int_2) -> None :
        """void TextAppend(char *, char *, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_copy(self, str_0, str_1) -> int :
        """int TextCopy(char *, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_find_index(self, str_0, str_1) -> int :
        """int TextFindIndex(char *, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_insert(self, str_0, str_1, int_2) -> str :
        """char *TextInsert(char *, char *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_is_equal(self, str_0, str_1) -> int :
        """int TextIsEqual(char *, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_join(self, str_0, int_1, str_2) -> str :
        """char *TextJoin(char * *, int, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_length(self, str_0) -> str :
        """unsigned int TextLength(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_replace(self, str_0, str_1, str_2) -> str :
        """char *TextReplace(char *, char *, char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_split(self, str_0, str_1, int_2) -> str :
        """char * *TextSplit(char *, char, int *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_subtext(self, str_0, int_1, int_2) -> str :
        """char *TextSubtext(char *, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_integer(self, str_0) -> int :
        """int TextToInteger(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_lower(self, str_0) -> str :
        """char *TextToLower(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_pascal(self, str_0) -> str :
        """char *TextToPascal(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_upper(self, str_0) -> str :
        """char *TextToUpper(char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def text_to_utf8(self, int_0, int_1) -> str :
        """char *TextToUtf8(int *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def toggle_fullscreen(self) -> None :
        """void ToggleFullscreen();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_file_data(self, str_0) -> None :
        """void UnloadFileData(unsigned char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_file_text(self, str_0) -> None :
        """void UnloadFileText(unsigned char *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_font(self, struct_font_0) -> None :
        """void UnloadFont(struct Font);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_font_data(self, struct_char_info_0, int_1) -> None :
        """void UnloadFontData(struct CharInfo *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_image(self, struct_image_0) -> None :
        """void UnloadImage(struct Image);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_image_colors(self, struct_color_0) -> None :
        """void UnloadImageColors(struct Color *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_image_palette(self, struct_color_0) -> None :
        """void UnloadImagePalette(struct Color *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_material(self, struct_material_0) -> None :
        """void UnloadMaterial(struct Material);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_mesh(self, struct_mesh_0) -> None :
        """void UnloadMesh(struct Mesh);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_model(self, struct_model_0) -> None :
        """void UnloadModel(struct Model);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_model_animation(self, struct_model_animation_0) -> None :
        """void UnloadModelAnimation(struct ModelAnimation);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_model_animations(self, struct_model_animation_0, int_1) -> None :
        """void UnloadModelAnimations(struct ModelAnimation *, unsigned int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_model_keep_meshes(self, struct_model_0) -> None :
        """void UnloadModelKeepMeshes(struct Model);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_music_stream(self, struct_music_0) -> None :
        """void UnloadMusicStream(struct Music);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_render_texture(self, struct_render_texture_0) -> None :
        """void UnloadRenderTexture(struct RenderTexture);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_shader(self, struct_shader_0) -> None :
        """void UnloadShader(struct Shader);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_sound(self, struct_sound_0) -> None :
        """void UnloadSound(struct Sound);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_texture(self, struct_texture_0) -> None :
        """void UnloadTexture(struct Texture);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_vr_stereo_config(self, struct_vr_stereo_config_0) -> None :
        """void UnloadVrStereoConfig(struct VrStereoConfig);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_wave(self, struct_wave_0) -> None :
        """void UnloadWave(struct Wave);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def unload_wave_samples(self, float_0) -> None :
        """void UnloadWaveSamples(float *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_audio_stream(self, struct_audio_stream_0, none_1, int_2) -> None :
        """void UpdateAudioStream(struct AudioStream, void *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_camera(self, struct_camera3_d_0) -> None :
        """void UpdateCamera(struct Camera3D *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_mesh_buffer(self, struct_mesh_0, int_1, none_2, int_3, int_4) -> None :
        """void UpdateMeshBuffer(struct Mesh, int, void *, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_model_animation(self, struct_model_0, struct_model_animation_1, int_2) -> None :
        """void UpdateModelAnimation(struct Model, struct ModelAnimation, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_music_stream(self, struct_music_0) -> None :
        """void UpdateMusicStream(struct Music);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_sound(self, struct_sound_0, none_1, int_2) -> None :
        """void UpdateSound(struct Sound, void *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_texture(self, struct_texture_0, none_1) -> None :
        """void UpdateTexture(struct Texture, void *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def update_texture_rec(self, struct_texture_0, struct_rectangle_1, none_2) -> None :
        """void UpdateTextureRec(struct Texture, struct Rectangle, void *);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def upload_mesh(self, struct_mesh_0, int_1) -> None :
        """void UploadMesh(struct Mesh *, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def wave_copy(self, struct_wave_0) -> struct :
        """struct Wave WaveCopy(struct Wave);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def wave_crop(self, struct_wave_0, int_1, int_2) -> None :
        """void WaveCrop(struct Wave *, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def wave_format(self, struct_wave_0, int_1, int_2, int_3) -> None :
        """void WaveFormat(struct Wave *, int, int, int);
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    def window_should_close(self) -> int :
        """int WindowShouldClose();
        
        CFFI C function from raylib.static._raylib_cffi.lib"""
        ...
    Vector2: struct
    Vector3: struct
    Vector4: struct
    Camera2D: struct
    Camera3D: struct
    Quaternion: struct
    Color: struct
    Rectangle: struct
    class struct:
        ...

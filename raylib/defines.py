import raylib

RAYLIB_VERSION_MAJOR: int = 5
RAYLIB_VERSION_MINOR: int = 0
RAYLIB_VERSION_PATCH: int = 0
RAYLIB_VERSION: str = "5.0"
PI: float = 3.141592653589793
DEG2RAD = PI / 180.0
RAD2DEG = 180.0 / PI
MOUSE_LEFT_BUTTON = raylib.MOUSE_BUTTON_LEFT
MOUSE_RIGHT_BUTTON = raylib.MOUSE_BUTTON_RIGHT
MOUSE_MIDDLE_BUTTON = raylib.MOUSE_BUTTON_MIDDLE
MATERIAL_MAP_DIFFUSE = raylib.MATERIAL_MAP_ALBEDO
MATERIAL_MAP_SPECULAR = raylib.MATERIAL_MAP_METALNESS
SHADER_LOC_MAP_DIFFUSE = raylib.SHADER_LOC_MAP_ALBEDO
SHADER_LOC_MAP_SPECULAR = raylib.SHADER_LOC_MAP_METALNESS
EPSILON: float = 1e-06
RLGL_VERSION: str = "4.5"
RL_DEFAULT_BATCH_BUFFER_ELEMENTS: int = 8192
RL_DEFAULT_BATCH_BUFFERS: int = 1
RL_DEFAULT_BATCH_DRAWCALLS: int = 256
RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS: int = 4
RL_MAX_MATRIX_STACK_SIZE: int = 32
RL_MAX_SHADER_LOCATIONS: int = 32
RL_TEXTURE_WRAP_S: int = 10242
RL_TEXTURE_WRAP_T: int = 10243
RL_TEXTURE_MAG_FILTER: int = 10240
RL_TEXTURE_MIN_FILTER: int = 10241
RL_TEXTURE_FILTER_NEAREST: int = 9728
RL_TEXTURE_FILTER_LINEAR: int = 9729
RL_TEXTURE_FILTER_MIP_NEAREST: int = 9984
RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR: int = 9986
RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST: int = 9985
RL_TEXTURE_FILTER_MIP_LINEAR: int = 9987
RL_TEXTURE_FILTER_ANISOTROPIC: int = 12288
RL_TEXTURE_MIPMAP_BIAS_RATIO: int = 16384
RL_TEXTURE_WRAP_REPEAT: int = 10497
RL_TEXTURE_WRAP_CLAMP: int = 33071
RL_TEXTURE_WRAP_MIRROR_REPEAT: int = 33648
RL_TEXTURE_WRAP_MIRROR_CLAMP: int = 34626
RL_MODELVIEW: int = 5888
RL_PROJECTION: int = 5889
RL_TEXTURE: int = 5890
RL_LINES: int = 1
RL_TRIANGLES: int = 4
RL_QUADS: int = 7
RL_UNSIGNED_BYTE: int = 5121
RL_FLOAT: int = 5126
RL_STREAM_DRAW: int = 35040
RL_STREAM_READ: int = 35041
RL_STREAM_COPY: int = 35042
RL_STATIC_DRAW: int = 35044
RL_STATIC_READ: int = 35045
RL_STATIC_COPY: int = 35046
RL_DYNAMIC_DRAW: int = 35048
RL_DYNAMIC_READ: int = 35049
RL_DYNAMIC_COPY: int = 35050
RL_FRAGMENT_SHADER: int = 35632
RL_VERTEX_SHADER: int = 35633
RL_COMPUTE_SHADER: int = 37305
RL_ZERO: int = 0
RL_ONE: int = 1
RL_SRC_COLOR: int = 768
RL_ONE_MINUS_SRC_COLOR: int = 769
RL_SRC_ALPHA: int = 770
RL_ONE_MINUS_SRC_ALPHA: int = 771
RL_DST_ALPHA: int = 772
RL_ONE_MINUS_DST_ALPHA: int = 773
RL_DST_COLOR: int = 774
RL_ONE_MINUS_DST_COLOR: int = 775
RL_SRC_ALPHA_SATURATE: int = 776
RL_CONSTANT_COLOR: int = 32769
RL_ONE_MINUS_CONSTANT_COLOR: int = 32770
RL_CONSTANT_ALPHA: int = 32771
RL_ONE_MINUS_CONSTANT_ALPHA: int = 32772
RL_FUNC_ADD: int = 32774
RL_MIN: int = 32775
RL_MAX: int = 32776
RL_FUNC_SUBTRACT: int = 32778
RL_FUNC_REVERSE_SUBTRACT: int = 32779
RL_BLEND_EQUATION: int = 32777
RL_BLEND_EQUATION_RGB: int = 32777
RL_BLEND_EQUATION_ALPHA: int = 34877
RL_BLEND_DST_RGB: int = 32968
RL_BLEND_SRC_RGB: int = 32969
RL_BLEND_DST_ALPHA: int = 32970
RL_BLEND_SRC_ALPHA: int = 32971
RL_BLEND_COLOR: int = 32773
RL_SHADER_LOC_MAP_DIFFUSE = raylib.RL_SHADER_LOC_MAP_ALBEDO
RL_SHADER_LOC_MAP_SPECULAR = raylib.RL_SHADER_LOC_MAP_METALNESS
GL_SHADING_LANGUAGE_VERSION: int = 35724
GL_COMPRESSED_RGB_S3TC_DXT1_EXT: int = 33776
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT: int = 33777
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT: int = 33778
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT: int = 33779
GL_ETC1_RGB8_OES: int = 36196
GL_COMPRESSED_RGB8_ETC2: int = 37492
GL_COMPRESSED_RGBA8_ETC2_EAC: int = 37496
GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG: int = 35840
GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG: int = 35842
GL_COMPRESSED_RGBA_ASTC_4x4_KHR: int = 37808
GL_COMPRESSED_RGBA_ASTC_8x8_KHR: int = 37815
GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT: int = 34047
GL_TEXTURE_MAX_ANISOTROPY_EXT: int = 34046
GL_UNSIGNED_SHORT_5_6_5: int = 33635
GL_UNSIGNED_SHORT_5_5_5_1: int = 32820
GL_UNSIGNED_SHORT_4_4_4_4: int = 32819
GL_LUMINANCE: int = 6409
GL_LUMINANCE_ALPHA: int = 6410
RL_DEFAULT_SHADER_ATTRIB_NAME_POSITION: str = "vertexPosition"
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD: str = "vertexTexCoord"
RL_DEFAULT_SHADER_ATTRIB_NAME_NORMAL: str = "vertexNormal"
RL_DEFAULT_SHADER_ATTRIB_NAME_COLOR: str = "vertexColor"
RL_DEFAULT_SHADER_ATTRIB_NAME_TANGENT: str = "vertexTangent"
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD2: str = "vertexTexCoord2"
RL_DEFAULT_SHADER_UNIFORM_NAME_MVP: str = "mvp"
RL_DEFAULT_SHADER_UNIFORM_NAME_VIEW: str = "matView"
RL_DEFAULT_SHADER_UNIFORM_NAME_PROJECTION: str = "matProjection"
RL_DEFAULT_SHADER_UNIFORM_NAME_MODEL: str = "matModel"
RL_DEFAULT_SHADER_UNIFORM_NAME_NORMAL: str = "matNormal"
RL_DEFAULT_SHADER_UNIFORM_NAME_COLOR: str = "colDiffuse"
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE0: str = "texture0"
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE1: str = "texture1"
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE2: str = "texture2"
RAYGUI_VERSION_MAJOR: int = 4
RAYGUI_VERSION_MINOR: int = 0
RAYGUI_VERSION_PATCH: int = 0
RAYGUI_VERSION: str = "4.0"
SCROLLBAR_LEFT_SIDE: int = 0
SCROLLBAR_RIGHT_SIDE: int = 1
RAYGUI_ICON_SIZE: int = 16
RAYGUI_ICON_MAX_ICONS: int = 256
RAYGUI_ICON_MAX_NAME_LENGTH: int = 32
RAYGUI_MAX_CONTROLS: int = 16
RAYGUI_MAX_PROPS_BASE: int = 16
RAYGUI_MAX_PROPS_EXTENDED: int = 8
KEY_RIGHT: int = 262
KEY_LEFT: int = 263
KEY_DOWN: int = 264
KEY_UP: int = 265
KEY_BACKSPACE: int = 259
KEY_ENTER: int = 257
MOUSE_LEFT_BUTTON: int = 0
RAYGUI_WINDOWBOX_STATUSBAR_HEIGHT: int = 24
RAYGUI_GROUPBOX_LINE_THICK: int = 1
RAYGUI_LINE_MARGIN_TEXT: int = 12
RAYGUI_LINE_TEXT_PADDING: int = 4
RAYGUI_PANEL_BORDER_WIDTH: int = 1
RAYGUI_TABBAR_ITEM_WIDTH: int = 160
RAYGUI_MIN_SCROLLBAR_WIDTH: int = 40
RAYGUI_MIN_SCROLLBAR_HEIGHT: int = 40
RAYGUI_TOGGLEGROUP_MAX_ITEMS: int = 32
RAYGUI_TEXTBOX_AUTO_CURSOR_COOLDOWN: int = 40
RAYGUI_TEXTBOX_AUTO_CURSOR_DELAY: int = 1
RAYGUI_VALUEBOX_MAX_CHARS: int = 32
RAYGUI_COLORBARALPHA_CHECKED_SIZE: int = 10
RAYGUI_MESSAGEBOX_BUTTON_HEIGHT: int = 24
RAYGUI_MESSAGEBOX_BUTTON_PADDING: int = 12
RAYGUI_TEXTINPUTBOX_BUTTON_HEIGHT: int = 24
RAYGUI_TEXTINPUTBOX_BUTTON_PADDING: int = 12
RAYGUI_TEXTINPUTBOX_HEIGHT: int = 26
RAYGUI_GRID_ALPHA: float = 0.15
MAX_LINE_BUFFER_SIZE: int = 256
ICON_TEXT_PADDING: int = 4
RAYGUI_MAX_TEXT_LINES: int = 128
RAYGUI_TEXTSPLIT_MAX_ITEMS: int = 128
RAYGUI_TEXTSPLIT_MAX_TEXT_SIZE: int = 1024
RAYGUI_TEXTFORMAT_MAX_SIZE: int = 256
PHYSAC_MAX_BODIES: int = 64
PHYSAC_MAX_MANIFOLDS: int = 4096
PHYSAC_MAX_VERTICES: int = 24
PHYSAC_DEFAULT_CIRCLE_VERTICES: int = 24
PHYSAC_COLLISION_ITERATIONS: int = 100
PHYSAC_PENETRATION_ALLOWANCE: float = 0.05
PHYSAC_PENETRATION_CORRECTION: float = 0.4
PHYSAC_PI: float = 3.141592653589793
PHYSAC_DEG2RAD = PHYSAC_PI / 180.0
PHYSAC_FLT_MAX: float = 3.402823466e+38
PHYSAC_EPSILON: float = 1e-06
GLFW_VERSION_MAJOR: int = 3
GLFW_VERSION_MINOR: int = 4
GLFW_VERSION_REVISION: int = 0
GLFW_TRUE: int = 1
GLFW_FALSE: int = 0
GLFW_RELEASE: int = 0
GLFW_PRESS: int = 1
GLFW_REPEAT: int = 2
GLFW_HAT_CENTERED: int = 0
GLFW_HAT_UP: int = 1
GLFW_HAT_RIGHT: int = 2
GLFW_HAT_DOWN: int = 4
GLFW_HAT_LEFT: int = 8
GLFW_HAT_RIGHT_UP = GLFW_HAT_RIGHT | GLFW_HAT_UP
GLFW_HAT_RIGHT_DOWN = GLFW_HAT_RIGHT | GLFW_HAT_DOWN
GLFW_HAT_LEFT_UP = GLFW_HAT_LEFT | GLFW_HAT_UP
GLFW_HAT_LEFT_DOWN = GLFW_HAT_LEFT | GLFW_HAT_DOWN
GLFW_KEY_SPACE: int = 32
GLFW_KEY_APOSTROPHE: int = 39
GLFW_KEY_COMMA: int = 44
GLFW_KEY_MINUS: int = 45
GLFW_KEY_PERIOD: int = 46
GLFW_KEY_SLASH: int = 47
GLFW_KEY_0: int = 48
GLFW_KEY_1: int = 49
GLFW_KEY_2: int = 50
GLFW_KEY_3: int = 51
GLFW_KEY_4: int = 52
GLFW_KEY_5: int = 53
GLFW_KEY_6: int = 54
GLFW_KEY_7: int = 55
GLFW_KEY_8: int = 56
GLFW_KEY_9: int = 57
GLFW_KEY_SEMICOLON: int = 59
GLFW_KEY_EQUAL: int = 61
GLFW_KEY_A: int = 65
GLFW_KEY_B: int = 66
GLFW_KEY_C: int = 67
GLFW_KEY_D: int = 68
GLFW_KEY_E: int = 69
GLFW_KEY_F: int = 70
GLFW_KEY_G: int = 71
GLFW_KEY_H: int = 72
GLFW_KEY_I: int = 73
GLFW_KEY_J: int = 74
GLFW_KEY_K: int = 75
GLFW_KEY_L: int = 76
GLFW_KEY_M: int = 77
GLFW_KEY_N: int = 78
GLFW_KEY_O: int = 79
GLFW_KEY_P: int = 80
GLFW_KEY_Q: int = 81
GLFW_KEY_R: int = 82
GLFW_KEY_S: int = 83
GLFW_KEY_T: int = 84
GLFW_KEY_U: int = 85
GLFW_KEY_V: int = 86
GLFW_KEY_W: int = 87
GLFW_KEY_X: int = 88
GLFW_KEY_Y: int = 89
GLFW_KEY_Z: int = 90
GLFW_KEY_LEFT_BRACKET: int = 91
GLFW_KEY_BACKSLASH: int = 92
GLFW_KEY_RIGHT_BRACKET: int = 93
GLFW_KEY_GRAVE_ACCENT: int = 96
GLFW_KEY_WORLD_1: int = 161
GLFW_KEY_WORLD_2: int = 162
GLFW_KEY_ESCAPE: int = 256
GLFW_KEY_ENTER: int = 257
GLFW_KEY_TAB: int = 258
GLFW_KEY_BACKSPACE: int = 259
GLFW_KEY_INSERT: int = 260
GLFW_KEY_DELETE: int = 261
GLFW_KEY_RIGHT: int = 262
GLFW_KEY_LEFT: int = 263
GLFW_KEY_DOWN: int = 264
GLFW_KEY_UP: int = 265
GLFW_KEY_PAGE_UP: int = 266
GLFW_KEY_PAGE_DOWN: int = 267
GLFW_KEY_HOME: int = 268
GLFW_KEY_END: int = 269
GLFW_KEY_CAPS_LOCK: int = 280
GLFW_KEY_SCROLL_LOCK: int = 281
GLFW_KEY_NUM_LOCK: int = 282
GLFW_KEY_PRINT_SCREEN: int = 283
GLFW_KEY_PAUSE: int = 284
GLFW_KEY_F1: int = 290
GLFW_KEY_F2: int = 291
GLFW_KEY_F3: int = 292
GLFW_KEY_F4: int = 293
GLFW_KEY_F5: int = 294
GLFW_KEY_F6: int = 295
GLFW_KEY_F7: int = 296
GLFW_KEY_F8: int = 297
GLFW_KEY_F9: int = 298
GLFW_KEY_F10: int = 299
GLFW_KEY_F11: int = 300
GLFW_KEY_F12: int = 301
GLFW_KEY_F13: int = 302
GLFW_KEY_F14: int = 303
GLFW_KEY_F15: int = 304
GLFW_KEY_F16: int = 305
GLFW_KEY_F17: int = 306
GLFW_KEY_F18: int = 307
GLFW_KEY_F19: int = 308
GLFW_KEY_F20: int = 309
GLFW_KEY_F21: int = 310
GLFW_KEY_F22: int = 311
GLFW_KEY_F23: int = 312
GLFW_KEY_F24: int = 313
GLFW_KEY_F25: int = 314
GLFW_KEY_KP_0: int = 320
GLFW_KEY_KP_1: int = 321
GLFW_KEY_KP_2: int = 322
GLFW_KEY_KP_3: int = 323
GLFW_KEY_KP_4: int = 324
GLFW_KEY_KP_5: int = 325
GLFW_KEY_KP_6: int = 326
GLFW_KEY_KP_7: int = 327
GLFW_KEY_KP_8: int = 328
GLFW_KEY_KP_9: int = 329
GLFW_KEY_KP_DECIMAL: int = 330
GLFW_KEY_KP_DIVIDE: int = 331
GLFW_KEY_KP_MULTIPLY: int = 332
GLFW_KEY_KP_SUBTRACT: int = 333
GLFW_KEY_KP_ADD: int = 334
GLFW_KEY_KP_ENTER: int = 335
GLFW_KEY_KP_EQUAL: int = 336
GLFW_KEY_LEFT_SHIFT: int = 340
GLFW_KEY_LEFT_CONTROL: int = 341
GLFW_KEY_LEFT_ALT: int = 342
GLFW_KEY_LEFT_SUPER: int = 343
GLFW_KEY_RIGHT_SHIFT: int = 344
GLFW_KEY_RIGHT_CONTROL: int = 345
GLFW_KEY_RIGHT_ALT: int = 346
GLFW_KEY_RIGHT_SUPER: int = 347
GLFW_KEY_MENU: int = 348
GLFW_MOD_SHIFT: int = 1
GLFW_MOD_CONTROL: int = 2
GLFW_MOD_ALT: int = 4
GLFW_MOD_SUPER: int = 8
GLFW_MOD_CAPS_LOCK: int = 16
GLFW_MOD_NUM_LOCK: int = 32
GLFW_MOUSE_BUTTON_1: int = 0
GLFW_MOUSE_BUTTON_2: int = 1
GLFW_MOUSE_BUTTON_3: int = 2
GLFW_MOUSE_BUTTON_4: int = 3
GLFW_MOUSE_BUTTON_5: int = 4
GLFW_MOUSE_BUTTON_6: int = 5
GLFW_MOUSE_BUTTON_7: int = 6
GLFW_MOUSE_BUTTON_8: int = 7
GLFW_JOYSTICK_1: int = 0
GLFW_JOYSTICK_2: int = 1
GLFW_JOYSTICK_3: int = 2
GLFW_JOYSTICK_4: int = 3
GLFW_JOYSTICK_5: int = 4
GLFW_JOYSTICK_6: int = 5
GLFW_JOYSTICK_7: int = 6
GLFW_JOYSTICK_8: int = 7
GLFW_JOYSTICK_9: int = 8
GLFW_JOYSTICK_10: int = 9
GLFW_JOYSTICK_11: int = 10
GLFW_JOYSTICK_12: int = 11
GLFW_JOYSTICK_13: int = 12
GLFW_JOYSTICK_14: int = 13
GLFW_JOYSTICK_15: int = 14
GLFW_JOYSTICK_16: int = 15
GLFW_GAMEPAD_BUTTON_A: int = 0
GLFW_GAMEPAD_BUTTON_B: int = 1
GLFW_GAMEPAD_BUTTON_X: int = 2
GLFW_GAMEPAD_BUTTON_Y: int = 3
GLFW_GAMEPAD_BUTTON_LEFT_BUMPER: int = 4
GLFW_GAMEPAD_BUTTON_RIGHT_BUMPER: int = 5
GLFW_GAMEPAD_BUTTON_BACK: int = 6
GLFW_GAMEPAD_BUTTON_START: int = 7
GLFW_GAMEPAD_BUTTON_GUIDE: int = 8
GLFW_GAMEPAD_BUTTON_LEFT_THUMB: int = 9
GLFW_GAMEPAD_BUTTON_RIGHT_THUMB: int = 10
GLFW_GAMEPAD_BUTTON_DPAD_UP: int = 11
GLFW_GAMEPAD_BUTTON_DPAD_RIGHT: int = 12
GLFW_GAMEPAD_BUTTON_DPAD_DOWN: int = 13
GLFW_GAMEPAD_BUTTON_DPAD_LEFT: int = 14
GLFW_GAMEPAD_AXIS_LEFT_X: int = 0
GLFW_GAMEPAD_AXIS_LEFT_Y: int = 1
GLFW_GAMEPAD_AXIS_RIGHT_X: int = 2
GLFW_GAMEPAD_AXIS_RIGHT_Y: int = 3
GLFW_GAMEPAD_AXIS_LEFT_TRIGGER: int = 4
GLFW_GAMEPAD_AXIS_RIGHT_TRIGGER: int = 5
GLFW_NO_ERROR: int = 0
GLFW_NOT_INITIALIZED: int = 65537
GLFW_NO_CURRENT_CONTEXT: int = 65538
GLFW_INVALID_ENUM: int = 65539
GLFW_INVALID_VALUE: int = 65540
GLFW_OUT_OF_MEMORY: int = 65541
GLFW_API_UNAVAILABLE: int = 65542
GLFW_VERSION_UNAVAILABLE: int = 65543
GLFW_PLATFORM_ERROR: int = 65544
GLFW_FORMAT_UNAVAILABLE: int = 65545
GLFW_NO_WINDOW_CONTEXT: int = 65546
GLFW_CURSOR_UNAVAILABLE: int = 65547
GLFW_FEATURE_UNAVAILABLE: int = 65548
GLFW_FEATURE_UNIMPLEMENTED: int = 65549
GLFW_PLATFORM_UNAVAILABLE: int = 65550
GLFW_FOCUSED: int = 131073
GLFW_ICONIFIED: int = 131074
GLFW_RESIZABLE: int = 131075
GLFW_VISIBLE: int = 131076
GLFW_DECORATED: int = 131077
GLFW_AUTO_ICONIFY: int = 131078
GLFW_FLOATING: int = 131079
GLFW_MAXIMIZED: int = 131080
GLFW_CENTER_CURSOR: int = 131081
GLFW_TRANSPARENT_FRAMEBUFFER: int = 131082
GLFW_HOVERED: int = 131083
GLFW_FOCUS_ON_SHOW: int = 131084
GLFW_MOUSE_PASSTHROUGH: int = 131085
GLFW_POSITION_X: int = 131086
GLFW_POSITION_Y: int = 131087
GLFW_RED_BITS: int = 135169
GLFW_GREEN_BITS: int = 135170
GLFW_BLUE_BITS: int = 135171
GLFW_ALPHA_BITS: int = 135172
GLFW_DEPTH_BITS: int = 135173
GLFW_STENCIL_BITS: int = 135174
GLFW_ACCUM_RED_BITS: int = 135175
GLFW_ACCUM_GREEN_BITS: int = 135176
GLFW_ACCUM_BLUE_BITS: int = 135177
GLFW_ACCUM_ALPHA_BITS: int = 135178
GLFW_AUX_BUFFERS: int = 135179
GLFW_STEREO: int = 135180
GLFW_SAMPLES: int = 135181
GLFW_SRGB_CAPABLE: int = 135182
GLFW_REFRESH_RATE: int = 135183
GLFW_DOUBLEBUFFER: int = 135184
GLFW_CLIENT_API: int = 139265
GLFW_CONTEXT_VERSION_MAJOR: int = 139266
GLFW_CONTEXT_VERSION_MINOR: int = 139267
GLFW_CONTEXT_REVISION: int = 139268
GLFW_CONTEXT_ROBUSTNESS: int = 139269
GLFW_OPENGL_FORWARD_COMPAT: int = 139270
GLFW_CONTEXT_DEBUG: int = 139271
GLFW_OPENGL_PROFILE: int = 139272
GLFW_CONTEXT_RELEASE_BEHAVIOR: int = 139273
GLFW_CONTEXT_NO_ERROR: int = 139274
GLFW_CONTEXT_CREATION_API: int = 139275
GLFW_SCALE_TO_MONITOR: int = 139276
GLFW_COCOA_RETINA_FRAMEBUFFER: int = 143361
GLFW_COCOA_FRAME_NAME: int = 143362
GLFW_COCOA_GRAPHICS_SWITCHING: int = 143363
GLFW_X11_CLASS_NAME: int = 147457
GLFW_X11_INSTANCE_NAME: int = 147458
GLFW_WIN32_KEYBOARD_MENU: int = 151553
GLFW_WAYLAND_APP_ID: int = 155649
GLFW_NO_API: int = 0
GLFW_OPENGL_API: int = 196609
GLFW_OPENGL_ES_API: int = 196610
GLFW_NO_ROBUSTNESS: int = 0
GLFW_NO_RESET_NOTIFICATION: int = 200705
GLFW_LOSE_CONTEXT_ON_RESET: int = 200706
GLFW_OPENGL_ANY_PROFILE: int = 0
GLFW_OPENGL_CORE_PROFILE: int = 204801
GLFW_OPENGL_COMPAT_PROFILE: int = 204802
GLFW_CURSOR: int = 208897
GLFW_STICKY_KEYS: int = 208898
GLFW_STICKY_MOUSE_BUTTONS: int = 208899
GLFW_LOCK_KEY_MODS: int = 208900
GLFW_RAW_MOUSE_MOTION: int = 208901
GLFW_CURSOR_NORMAL: int = 212993
GLFW_CURSOR_HIDDEN: int = 212994
GLFW_CURSOR_DISABLED: int = 212995
GLFW_CURSOR_CAPTURED: int = 212996
GLFW_ANY_RELEASE_BEHAVIOR: int = 0
GLFW_RELEASE_BEHAVIOR_FLUSH: int = 217089
GLFW_RELEASE_BEHAVIOR_NONE: int = 217090
GLFW_NATIVE_CONTEXT_API: int = 221185
GLFW_EGL_CONTEXT_API: int = 221186
GLFW_OSMESA_CONTEXT_API: int = 221187
GLFW_ANGLE_PLATFORM_TYPE_NONE: int = 225281
GLFW_ANGLE_PLATFORM_TYPE_OPENGL: int = 225282
GLFW_ANGLE_PLATFORM_TYPE_OPENGLES: int = 225283
GLFW_ANGLE_PLATFORM_TYPE_D3D9: int = 225284
GLFW_ANGLE_PLATFORM_TYPE_D3D11: int = 225285
GLFW_ANGLE_PLATFORM_TYPE_VULKAN: int = 225287
GLFW_ANGLE_PLATFORM_TYPE_METAL: int = 225288
GLFW_ANY_POSITION: int = 2147483648
GLFW_ARROW_CURSOR: int = 221185
GLFW_IBEAM_CURSOR: int = 221186
GLFW_CROSSHAIR_CURSOR: int = 221187
GLFW_POINTING_HAND_CURSOR: int = 221188
GLFW_RESIZE_EW_CURSOR: int = 221189
GLFW_RESIZE_NS_CURSOR: int = 221190
GLFW_RESIZE_NWSE_CURSOR: int = 221191
GLFW_RESIZE_NESW_CURSOR: int = 221192
GLFW_RESIZE_ALL_CURSOR: int = 221193
GLFW_NOT_ALLOWED_CURSOR: int = 221194
GLFW_CONNECTED: int = 262145
GLFW_DISCONNECTED: int = 262146
GLFW_JOYSTICK_HAT_BUTTONS: int = 327681
GLFW_ANGLE_PLATFORM_TYPE: int = 327682
GLFW_PLATFORM: int = 327683
GLFW_COCOA_CHDIR_RESOURCES: int = 331777
GLFW_COCOA_MENUBAR: int = 331778
GLFW_X11_XCB_VULKAN_SURFACE: int = 335873
GLFW_ANY_PLATFORM: int = 393216
GLFW_PLATFORM_WIN32: int = 393217
GLFW_PLATFORM_COCOA: int = 393218
GLFW_PLATFORM_WAYLAND: int = 393219
GLFW_PLATFORM_X11: int = 393220
GLFW_PLATFORM_NULL: int = 393221

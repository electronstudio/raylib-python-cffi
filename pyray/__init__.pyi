class ConfigFlags(int):
    """System/Window config flags."""
    FLAG_VSYNC_HINT = 64
    FLAG_FULLSCREEN_MODE = 2
    FLAG_WINDOW_RESIZABLE = 4
    FLAG_WINDOW_UNDECORATED = 8
    FLAG_WINDOW_HIDDEN = 128
    FLAG_WINDOW_MINIMIZED = 512
    FLAG_WINDOW_MAXIMIZED = 1024
    FLAG_WINDOW_UNFOCUSED = 2048
    FLAG_WINDOW_TOPMOST = 4096
    FLAG_WINDOW_ALWAYS_RUN = 256
    FLAG_WINDOW_TRANSPARENT = 16
    FLAG_WINDOW_HIGHDPI = 8192
    FLAG_WINDOW_MOUSE_PASSTHROUGH = 16384
    FLAG_BORDERLESS_WINDOWED_MODE = 32768
    FLAG_MSAA_4X_HINT = 32
    FLAG_INTERLACED_HINT = 65536

class TraceLogLevel(int):
    """Trace log level."""
    LOG_ALL = 0
    LOG_TRACE = 1
    LOG_DEBUG = 2
    LOG_INFO = 3
    LOG_WARNING = 4
    LOG_ERROR = 5
    LOG_FATAL = 6
    LOG_NONE = 7

class KeyboardKey(int):
    """Keyboard keys (US keyboard layout)."""
    KEY_NULL = 0
    KEY_APOSTROPHE = 39
    KEY_COMMA = 44
    KEY_MINUS = 45
    KEY_PERIOD = 46
    KEY_SLASH = 47
    KEY_ZERO = 48
    KEY_ONE = 49
    KEY_TWO = 50
    KEY_THREE = 51
    KEY_FOUR = 52
    KEY_FIVE = 53
    KEY_SIX = 54
    KEY_SEVEN = 55
    KEY_EIGHT = 56
    KEY_NINE = 57
    KEY_SEMICOLON = 59
    KEY_EQUAL = 61
    KEY_A = 65
    KEY_B = 66
    KEY_C = 67
    KEY_D = 68
    KEY_E = 69
    KEY_F = 70
    KEY_G = 71
    KEY_H = 72
    KEY_I = 73
    KEY_J = 74
    KEY_K = 75
    KEY_L = 76
    KEY_M = 77
    KEY_N = 78
    KEY_O = 79
    KEY_P = 80
    KEY_Q = 81
    KEY_R = 82
    KEY_S = 83
    KEY_T = 84
    KEY_U = 85
    KEY_V = 86
    KEY_W = 87
    KEY_X = 88
    KEY_Y = 89
    KEY_Z = 90
    KEY_LEFT_BRACKET = 91
    KEY_BACKSLASH = 92
    KEY_RIGHT_BRACKET = 93
    KEY_GRAVE = 96
    KEY_SPACE = 32
    KEY_ESCAPE = 256
    KEY_ENTER = 257
    KEY_TAB = 258
    KEY_BACKSPACE = 259
    KEY_INSERT = 260
    KEY_DELETE = 261
    KEY_RIGHT = 262
    KEY_LEFT = 263
    KEY_DOWN = 264
    KEY_UP = 265
    KEY_PAGE_UP = 266
    KEY_PAGE_DOWN = 267
    KEY_HOME = 268
    KEY_END = 269
    KEY_CAPS_LOCK = 280
    KEY_SCROLL_LOCK = 281
    KEY_NUM_LOCK = 282
    KEY_PRINT_SCREEN = 283
    KEY_PAUSE = 284
    KEY_F1 = 290
    KEY_F2 = 291
    KEY_F3 = 292
    KEY_F4 = 293
    KEY_F5 = 294
    KEY_F6 = 295
    KEY_F7 = 296
    KEY_F8 = 297
    KEY_F9 = 298
    KEY_F10 = 299
    KEY_F11 = 300
    KEY_F12 = 301
    KEY_LEFT_SHIFT = 340
    KEY_LEFT_CONTROL = 341
    KEY_LEFT_ALT = 342
    KEY_LEFT_SUPER = 343
    KEY_RIGHT_SHIFT = 344
    KEY_RIGHT_CONTROL = 345
    KEY_RIGHT_ALT = 346
    KEY_RIGHT_SUPER = 347
    KEY_KB_MENU = 348
    KEY_KP_0 = 320
    KEY_KP_1 = 321
    KEY_KP_2 = 322
    KEY_KP_3 = 323
    KEY_KP_4 = 324
    KEY_KP_5 = 325
    KEY_KP_6 = 326
    KEY_KP_7 = 327
    KEY_KP_8 = 328
    KEY_KP_9 = 329
    KEY_KP_DECIMAL = 330
    KEY_KP_DIVIDE = 331
    KEY_KP_MULTIPLY = 332
    KEY_KP_SUBTRACT = 333
    KEY_KP_ADD = 334
    KEY_KP_ENTER = 335
    KEY_KP_EQUAL = 336
    KEY_BACK = 4
    KEY_MENU = 5
    KEY_VOLUME_UP = 24
    KEY_VOLUME_DOWN = 25

class MouseButton(int):
    """Mouse buttons."""
    MOUSE_BUTTON_LEFT = 0
    MOUSE_BUTTON_RIGHT = 1
    MOUSE_BUTTON_MIDDLE = 2
    MOUSE_BUTTON_SIDE = 3
    MOUSE_BUTTON_EXTRA = 4
    MOUSE_BUTTON_FORWARD = 5
    MOUSE_BUTTON_BACK = 6

class MouseCursor(int):
    """Mouse cursor."""
    MOUSE_CURSOR_DEFAULT = 0
    MOUSE_CURSOR_ARROW = 1
    MOUSE_CURSOR_IBEAM = 2
    MOUSE_CURSOR_CROSSHAIR = 3
    MOUSE_CURSOR_POINTING_HAND = 4
    MOUSE_CURSOR_RESIZE_EW = 5
    MOUSE_CURSOR_RESIZE_NS = 6
    MOUSE_CURSOR_RESIZE_NWSE = 7
    MOUSE_CURSOR_RESIZE_NESW = 8
    MOUSE_CURSOR_RESIZE_ALL = 9
    MOUSE_CURSOR_NOT_ALLOWED = 10

class GamepadButton(int):
    """Gamepad buttons."""
    GAMEPAD_BUTTON_UNKNOWN = 0
    GAMEPAD_BUTTON_LEFT_FACE_UP = 1
    GAMEPAD_BUTTON_LEFT_FACE_RIGHT = 2
    GAMEPAD_BUTTON_LEFT_FACE_DOWN = 3
    GAMEPAD_BUTTON_LEFT_FACE_LEFT = 4
    GAMEPAD_BUTTON_RIGHT_FACE_UP = 5
    GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = 6
    GAMEPAD_BUTTON_RIGHT_FACE_DOWN = 7
    GAMEPAD_BUTTON_RIGHT_FACE_LEFT = 8
    GAMEPAD_BUTTON_LEFT_TRIGGER_1 = 9
    GAMEPAD_BUTTON_LEFT_TRIGGER_2 = 10
    GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = 11
    GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = 12
    GAMEPAD_BUTTON_MIDDLE_LEFT = 13
    GAMEPAD_BUTTON_MIDDLE = 14
    GAMEPAD_BUTTON_MIDDLE_RIGHT = 15
    GAMEPAD_BUTTON_LEFT_THUMB = 16
    GAMEPAD_BUTTON_RIGHT_THUMB = 17

class GamepadAxis(int):
    """Gamepad axis."""
    GAMEPAD_AXIS_LEFT_X = 0
    GAMEPAD_AXIS_LEFT_Y = 1
    GAMEPAD_AXIS_RIGHT_X = 2
    GAMEPAD_AXIS_RIGHT_Y = 3
    GAMEPAD_AXIS_LEFT_TRIGGER = 4
    GAMEPAD_AXIS_RIGHT_TRIGGER = 5

class MaterialMapIndex(int):
    """Material map index."""
    MATERIAL_MAP_ALBEDO = 0
    MATERIAL_MAP_METALNESS = 1
    MATERIAL_MAP_NORMAL = 2
    MATERIAL_MAP_ROUGHNESS = 3
    MATERIAL_MAP_OCCLUSION = 4
    MATERIAL_MAP_EMISSION = 5
    MATERIAL_MAP_HEIGHT = 6
    MATERIAL_MAP_CUBEMAP = 7
    MATERIAL_MAP_IRRADIANCE = 8
    MATERIAL_MAP_PREFILTER = 9
    MATERIAL_MAP_BRDF = 10

class ShaderLocationIndex(int):
    """Shader location index."""
    SHADER_LOC_VERTEX_POSITION = 0
    SHADER_LOC_VERTEX_TEXCOORD01 = 1
    SHADER_LOC_VERTEX_TEXCOORD02 = 2
    SHADER_LOC_VERTEX_NORMAL = 3
    SHADER_LOC_VERTEX_TANGENT = 4
    SHADER_LOC_VERTEX_COLOR = 5
    SHADER_LOC_MATRIX_MVP = 6
    SHADER_LOC_MATRIX_VIEW = 7
    SHADER_LOC_MATRIX_PROJECTION = 8
    SHADER_LOC_MATRIX_MODEL = 9
    SHADER_LOC_MATRIX_NORMAL = 10
    SHADER_LOC_VECTOR_VIEW = 11
    SHADER_LOC_COLOR_DIFFUSE = 12
    SHADER_LOC_COLOR_SPECULAR = 13
    SHADER_LOC_COLOR_AMBIENT = 14
    SHADER_LOC_MAP_ALBEDO = 15
    SHADER_LOC_MAP_METALNESS = 16
    SHADER_LOC_MAP_NORMAL = 17
    SHADER_LOC_MAP_ROUGHNESS = 18
    SHADER_LOC_MAP_OCCLUSION = 19
    SHADER_LOC_MAP_EMISSION = 20
    SHADER_LOC_MAP_HEIGHT = 21
    SHADER_LOC_MAP_CUBEMAP = 22
    SHADER_LOC_MAP_IRRADIANCE = 23
    SHADER_LOC_MAP_PREFILTER = 24
    SHADER_LOC_MAP_BRDF = 25
    SHADER_LOC_VERTEX_BONEIDS = 26
    SHADER_LOC_VERTEX_BONEWEIGHTS = 27
    SHADER_LOC_BONE_MATRICES = 28

class ShaderUniformDataType(int):
    """Shader uniform data type."""
    SHADER_UNIFORM_FLOAT = 0
    SHADER_UNIFORM_VEC2 = 1
    SHADER_UNIFORM_VEC3 = 2
    SHADER_UNIFORM_VEC4 = 3
    SHADER_UNIFORM_INT = 4
    SHADER_UNIFORM_IVEC2 = 5
    SHADER_UNIFORM_IVEC3 = 6
    SHADER_UNIFORM_IVEC4 = 7
    SHADER_UNIFORM_SAMPLER2D = 8

class ShaderAttributeDataType(int):
    """Shader attribute data types."""
    SHADER_ATTRIB_FLOAT = 0
    SHADER_ATTRIB_VEC2 = 1
    SHADER_ATTRIB_VEC3 = 2
    SHADER_ATTRIB_VEC4 = 3

class PixelFormat(int):
    """Pixel formats."""
    PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1
    PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = 2
    PIXELFORMAT_UNCOMPRESSED_R5G6B5 = 3
    PIXELFORMAT_UNCOMPRESSED_R8G8B8 = 4
    PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = 5
    PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = 6
    PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = 7
    PIXELFORMAT_UNCOMPRESSED_R32 = 8
    PIXELFORMAT_UNCOMPRESSED_R32G32B32 = 9
    PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10
    PIXELFORMAT_UNCOMPRESSED_R16 = 11
    PIXELFORMAT_UNCOMPRESSED_R16G16B16 = 12
    PIXELFORMAT_UNCOMPRESSED_R16G16B16A16 = 13
    PIXELFORMAT_COMPRESSED_DXT1_RGB = 14
    PIXELFORMAT_COMPRESSED_DXT1_RGBA = 15
    PIXELFORMAT_COMPRESSED_DXT3_RGBA = 16
    PIXELFORMAT_COMPRESSED_DXT5_RGBA = 17
    PIXELFORMAT_COMPRESSED_ETC1_RGB = 18
    PIXELFORMAT_COMPRESSED_ETC2_RGB = 19
    PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 20
    PIXELFORMAT_COMPRESSED_PVRT_RGB = 21
    PIXELFORMAT_COMPRESSED_PVRT_RGBA = 22
    PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 23
    PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 24

class TextureFilter(int):
    """Texture parameters: filter mode."""
    TEXTURE_FILTER_POINT = 0
    TEXTURE_FILTER_BILINEAR = 1
    TEXTURE_FILTER_TRILINEAR = 2
    TEXTURE_FILTER_ANISOTROPIC_4X = 3
    TEXTURE_FILTER_ANISOTROPIC_8X = 4
    TEXTURE_FILTER_ANISOTROPIC_16X = 5

class TextureWrap(int):
    """Texture parameters: wrap mode."""
    TEXTURE_WRAP_REPEAT = 0
    TEXTURE_WRAP_CLAMP = 1
    TEXTURE_WRAP_MIRROR_REPEAT = 2
    TEXTURE_WRAP_MIRROR_CLAMP = 3

class CubemapLayout(int):
    """Cubemap layouts."""
    CUBEMAP_LAYOUT_AUTO_DETECT = 0
    CUBEMAP_LAYOUT_LINE_VERTICAL = 1
    CUBEMAP_LAYOUT_LINE_HORIZONTAL = 2
    CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = 3
    CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = 4

class FontType(int):
    """Font type, defines generation method."""
    FONT_DEFAULT = 0
    FONT_BITMAP = 1
    FONT_SDF = 2

class BlendMode(int):
    """Color blending modes (pre-defined)."""
    BLEND_ALPHA = 0
    BLEND_ADDITIVE = 1
    BLEND_MULTIPLIED = 2
    BLEND_ADD_COLORS = 3
    BLEND_SUBTRACT_COLORS = 4
    BLEND_ALPHA_PREMULTIPLY = 5
    BLEND_CUSTOM = 6
    BLEND_CUSTOM_SEPARATE = 7

class Gesture(int):
    """Gesture."""
    GESTURE_NONE = 0
    GESTURE_TAP = 1
    GESTURE_DOUBLETAP = 2
    GESTURE_HOLD = 4
    GESTURE_DRAG = 8
    GESTURE_SWIPE_RIGHT = 16
    GESTURE_SWIPE_LEFT = 32
    GESTURE_SWIPE_UP = 64
    GESTURE_SWIPE_DOWN = 128
    GESTURE_PINCH_IN = 256
    GESTURE_PINCH_OUT = 512

class CameraMode(int):
    """Camera system modes."""
    CAMERA_CUSTOM = 0
    CAMERA_FREE = 1
    CAMERA_ORBITAL = 2
    CAMERA_FIRST_PERSON = 3
    CAMERA_THIRD_PERSON = 4

class CameraProjection(int):
    """Camera projection."""
    CAMERA_PERSPECTIVE = 0
    CAMERA_ORTHOGRAPHIC = 1

class NPatchLayout(int):
    """N-patch layout."""
    NPATCH_NINE_PATCH = 0
    NPATCH_THREE_PATCH_VERTICAL = 1
    NPATCH_THREE_PATCH_HORIZONTAL = 2

class rlGlVersion(int):
    """OpenGL version."""
    RL_OPENGL_11 = 1
    RL_OPENGL_21 = 2
    RL_OPENGL_33 = 3
    RL_OPENGL_43 = 4
    RL_OPENGL_ES_20 = 5
    RL_OPENGL_ES_30 = 6

class rlTraceLogLevel(int):
    """Trace log level."""
    RL_LOG_ALL = 0
    RL_LOG_TRACE = 1
    RL_LOG_DEBUG = 2
    RL_LOG_INFO = 3
    RL_LOG_WARNING = 4
    RL_LOG_ERROR = 5
    RL_LOG_FATAL = 6
    RL_LOG_NONE = 7

class rlPixelFormat(int):
    """Texture pixel formats."""
    RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1
    RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = 2
    RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5 = 3
    RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8 = 4
    RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = 5
    RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = 6
    RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = 7
    RL_PIXELFORMAT_UNCOMPRESSED_R32 = 8
    RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32 = 9
    RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10
    RL_PIXELFORMAT_UNCOMPRESSED_R16 = 11
    RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16 = 12
    RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16A16 = 13
    RL_PIXELFORMAT_COMPRESSED_DXT1_RGB = 14
    RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA = 15
    RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA = 16
    RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA = 17
    RL_PIXELFORMAT_COMPRESSED_ETC1_RGB = 18
    RL_PIXELFORMAT_COMPRESSED_ETC2_RGB = 19
    RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 20
    RL_PIXELFORMAT_COMPRESSED_PVRT_RGB = 21
    RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA = 22
    RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 23
    RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 24

class rlTextureFilter(int):
    """Texture parameters: filter mode."""
    RL_TEXTURE_FILTER_POINT = 0
    RL_TEXTURE_FILTER_BILINEAR = 1
    RL_TEXTURE_FILTER_TRILINEAR = 2
    RL_TEXTURE_FILTER_ANISOTROPIC_4X = 3
    RL_TEXTURE_FILTER_ANISOTROPIC_8X = 4
    RL_TEXTURE_FILTER_ANISOTROPIC_16X = 5

class rlBlendMode(int):
    """Color blending modes (pre-defined)."""
    RL_BLEND_ALPHA = 0
    RL_BLEND_ADDITIVE = 1
    RL_BLEND_MULTIPLIED = 2
    RL_BLEND_ADD_COLORS = 3
    RL_BLEND_SUBTRACT_COLORS = 4
    RL_BLEND_ALPHA_PREMULTIPLY = 5
    RL_BLEND_CUSTOM = 6
    RL_BLEND_CUSTOM_SEPARATE = 7

class rlShaderLocationIndex(int):
    """Shader location point type."""
    RL_SHADER_LOC_VERTEX_POSITION = 0
    RL_SHADER_LOC_VERTEX_TEXCOORD01 = 1
    RL_SHADER_LOC_VERTEX_TEXCOORD02 = 2
    RL_SHADER_LOC_VERTEX_NORMAL = 3
    RL_SHADER_LOC_VERTEX_TANGENT = 4
    RL_SHADER_LOC_VERTEX_COLOR = 5
    RL_SHADER_LOC_MATRIX_MVP = 6
    RL_SHADER_LOC_MATRIX_VIEW = 7
    RL_SHADER_LOC_MATRIX_PROJECTION = 8
    RL_SHADER_LOC_MATRIX_MODEL = 9
    RL_SHADER_LOC_MATRIX_NORMAL = 10
    RL_SHADER_LOC_VECTOR_VIEW = 11
    RL_SHADER_LOC_COLOR_DIFFUSE = 12
    RL_SHADER_LOC_COLOR_SPECULAR = 13
    RL_SHADER_LOC_COLOR_AMBIENT = 14
    RL_SHADER_LOC_MAP_ALBEDO = 15
    RL_SHADER_LOC_MAP_METALNESS = 16
    RL_SHADER_LOC_MAP_NORMAL = 17
    RL_SHADER_LOC_MAP_ROUGHNESS = 18
    RL_SHADER_LOC_MAP_OCCLUSION = 19
    RL_SHADER_LOC_MAP_EMISSION = 20
    RL_SHADER_LOC_MAP_HEIGHT = 21
    RL_SHADER_LOC_MAP_CUBEMAP = 22
    RL_SHADER_LOC_MAP_IRRADIANCE = 23
    RL_SHADER_LOC_MAP_PREFILTER = 24
    RL_SHADER_LOC_MAP_BRDF = 25

class rlShaderUniformDataType(int):
    """Shader uniform data type."""
    RL_SHADER_UNIFORM_FLOAT = 0
    RL_SHADER_UNIFORM_VEC2 = 1
    RL_SHADER_UNIFORM_VEC3 = 2
    RL_SHADER_UNIFORM_VEC4 = 3
    RL_SHADER_UNIFORM_INT = 4
    RL_SHADER_UNIFORM_IVEC2 = 5
    RL_SHADER_UNIFORM_IVEC3 = 6
    RL_SHADER_UNIFORM_IVEC4 = 7
    RL_SHADER_UNIFORM_UINT = 8
    RL_SHADER_UNIFORM_UIVEC2 = 9
    RL_SHADER_UNIFORM_UIVEC3 = 10
    RL_SHADER_UNIFORM_UIVEC4 = 11
    RL_SHADER_UNIFORM_SAMPLER2D = 12

class rlShaderAttributeDataType(int):
    """Shader attribute data types."""
    RL_SHADER_ATTRIB_FLOAT = 0
    RL_SHADER_ATTRIB_VEC2 = 1
    RL_SHADER_ATTRIB_VEC3 = 2
    RL_SHADER_ATTRIB_VEC4 = 3

class rlFramebufferAttachType(int):
    """Framebuffer attachment type."""
    RL_ATTACHMENT_COLOR_CHANNEL0 = 0
    RL_ATTACHMENT_COLOR_CHANNEL1 = 1
    RL_ATTACHMENT_COLOR_CHANNEL2 = 2
    RL_ATTACHMENT_COLOR_CHANNEL3 = 3
    RL_ATTACHMENT_COLOR_CHANNEL4 = 4
    RL_ATTACHMENT_COLOR_CHANNEL5 = 5
    RL_ATTACHMENT_COLOR_CHANNEL6 = 6
    RL_ATTACHMENT_COLOR_CHANNEL7 = 7
    RL_ATTACHMENT_DEPTH = 100
    RL_ATTACHMENT_STENCIL = 200

class rlFramebufferAttachTextureType(int):
    """Framebuffer texture attachment type."""
    RL_ATTACHMENT_CUBEMAP_POSITIVE_X = 0
    RL_ATTACHMENT_CUBEMAP_NEGATIVE_X = 1
    RL_ATTACHMENT_CUBEMAP_POSITIVE_Y = 2
    RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y = 3
    RL_ATTACHMENT_CUBEMAP_POSITIVE_Z = 4
    RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z = 5
    RL_ATTACHMENT_TEXTURE2D = 100
    RL_ATTACHMENT_RENDERBUFFER = 200

class rlCullMode(int):
    """Face culling mode."""
    RL_CULL_FACE_FRONT = 0
    RL_CULL_FACE_BACK = 1

class GuiState(int):
    """Gui control state."""
    STATE_NORMAL = 0
    STATE_FOCUSED = 1
    STATE_PRESSED = 2
    STATE_DISABLED = 3

class GuiTextAlignment(int):
    """Gui control text alignment."""
    TEXT_ALIGN_LEFT = 0
    TEXT_ALIGN_CENTER = 1
    TEXT_ALIGN_RIGHT = 2

class GuiTextAlignmentVertical(int):
    """Gui control text alignment vertical."""
    TEXT_ALIGN_TOP = 0
    TEXT_ALIGN_MIDDLE = 1
    TEXT_ALIGN_BOTTOM = 2

class GuiTextWrapMode(int):
    """Gui control text wrap mode."""
    TEXT_WRAP_NONE = 0
    TEXT_WRAP_CHAR = 1
    TEXT_WRAP_WORD = 2

class GuiControl(int):
    """Gui controls."""
    DEFAULT = 0
    LABEL = 1
    BUTTON = 2
    TOGGLE = 3
    SLIDER = 4
    PROGRESSBAR = 5
    CHECKBOX = 6
    COMBOBOX = 7
    DROPDOWNBOX = 8
    TEXTBOX = 9
    VALUEBOX = 10
    SPINNER = 11
    LISTVIEW = 12
    COLORPICKER = 13
    SCROLLBAR = 14
    STATUSBAR = 15

class GuiControlProperty(int):
    """Gui base properties for every control."""
    BORDER_COLOR_NORMAL = 0
    BASE_COLOR_NORMAL = 1
    TEXT_COLOR_NORMAL = 2
    BORDER_COLOR_FOCUSED = 3
    BASE_COLOR_FOCUSED = 4
    TEXT_COLOR_FOCUSED = 5
    BORDER_COLOR_PRESSED = 6
    BASE_COLOR_PRESSED = 7
    TEXT_COLOR_PRESSED = 8
    BORDER_COLOR_DISABLED = 9
    BASE_COLOR_DISABLED = 10
    TEXT_COLOR_DISABLED = 11
    BORDER_WIDTH = 12
    TEXT_PADDING = 13
    TEXT_ALIGNMENT = 14

class GuiDefaultProperty(int):
    """DEFAULT extended properties."""
    TEXT_SIZE = 16
    TEXT_SPACING = 17
    LINE_COLOR = 18
    BACKGROUND_COLOR = 19
    TEXT_LINE_SPACING = 20
    TEXT_ALIGNMENT_VERTICAL = 21
    TEXT_WRAP_MODE = 22

class GuiToggleProperty(int):
    """Toggle/ToggleGroup."""
    GROUP_PADDING = 16

class GuiSliderProperty(int):
    """Slider/SliderBar."""
    SLIDER_WIDTH = 16
    SLIDER_PADDING = 17

class GuiProgressBarProperty(int):
    """ProgressBar."""
    PROGRESS_PADDING = 16

class GuiScrollBarProperty(int):
    """ScrollBar."""
    ARROWS_SIZE = 16
    ARROWS_VISIBLE = 17
    SCROLL_SLIDER_PADDING = 18
    SCROLL_SLIDER_SIZE = 19
    SCROLL_PADDING = 20
    SCROLL_SPEED = 21

class GuiCheckBoxProperty(int):
    """CheckBox."""
    CHECK_PADDING = 16

class GuiComboBoxProperty(int):
    """ComboBox."""
    COMBO_BUTTON_WIDTH = 16
    COMBO_BUTTON_SPACING = 17

class GuiDropdownBoxProperty(int):
    """DropdownBox."""
    ARROW_PADDING = 16
    DROPDOWN_ITEMS_SPACING = 17
    DROPDOWN_ARROW_HIDDEN = 18
    DROPDOWN_ROLL_UP = 19

class GuiTextBoxProperty(int):
    """TextBox/TextBoxMulti/ValueBox/Spinner."""
    TEXT_READONLY = 16

class GuiSpinnerProperty(int):
    """Spinner."""
    SPIN_BUTTON_WIDTH = 16
    SPIN_BUTTON_SPACING = 17

class GuiListViewProperty(int):
    """ListView."""
    LIST_ITEMS_HEIGHT = 16
    LIST_ITEMS_SPACING = 17
    SCROLLBAR_WIDTH = 18
    SCROLLBAR_SIDE = 19
    LIST_ITEMS_BORDER_WIDTH = 20

class GuiColorPickerProperty(int):
    """ColorPicker."""
    COLOR_SELECTOR_SIZE = 16
    HUEBAR_WIDTH = 17
    HUEBAR_PADDING = 18
    HUEBAR_SELECTOR_HEIGHT = 19
    HUEBAR_SELECTOR_OVERFLOW = 20

class GuiIconName(int):
    """."""
    ICON_NONE = 0
    ICON_FOLDER_FILE_OPEN = 1
    ICON_FILE_SAVE_CLASSIC = 2
    ICON_FOLDER_OPEN = 3
    ICON_FOLDER_SAVE = 4
    ICON_FILE_OPEN = 5
    ICON_FILE_SAVE = 6
    ICON_FILE_EXPORT = 7
    ICON_FILE_ADD = 8
    ICON_FILE_DELETE = 9
    ICON_FILETYPE_TEXT = 10
    ICON_FILETYPE_AUDIO = 11
    ICON_FILETYPE_IMAGE = 12
    ICON_FILETYPE_PLAY = 13
    ICON_FILETYPE_VIDEO = 14
    ICON_FILETYPE_INFO = 15
    ICON_FILE_COPY = 16
    ICON_FILE_CUT = 17
    ICON_FILE_PASTE = 18
    ICON_CURSOR_HAND = 19
    ICON_CURSOR_POINTER = 20
    ICON_CURSOR_CLASSIC = 21
    ICON_PENCIL = 22
    ICON_PENCIL_BIG = 23
    ICON_BRUSH_CLASSIC = 24
    ICON_BRUSH_PAINTER = 25
    ICON_WATER_DROP = 26
    ICON_COLOR_PICKER = 27
    ICON_RUBBER = 28
    ICON_COLOR_BUCKET = 29
    ICON_TEXT_T = 30
    ICON_TEXT_A = 31
    ICON_SCALE = 32
    ICON_RESIZE = 33
    ICON_FILTER_POINT = 34
    ICON_FILTER_BILINEAR = 35
    ICON_CROP = 36
    ICON_CROP_ALPHA = 37
    ICON_SQUARE_TOGGLE = 38
    ICON_SYMMETRY = 39
    ICON_SYMMETRY_HORIZONTAL = 40
    ICON_SYMMETRY_VERTICAL = 41
    ICON_LENS = 42
    ICON_LENS_BIG = 43
    ICON_EYE_ON = 44
    ICON_EYE_OFF = 45
    ICON_FILTER_TOP = 46
    ICON_FILTER = 47
    ICON_TARGET_POINT = 48
    ICON_TARGET_SMALL = 49
    ICON_TARGET_BIG = 50
    ICON_TARGET_MOVE = 51
    ICON_CURSOR_MOVE = 52
    ICON_CURSOR_SCALE = 53
    ICON_CURSOR_SCALE_RIGHT = 54
    ICON_CURSOR_SCALE_LEFT = 55
    ICON_UNDO = 56
    ICON_REDO = 57
    ICON_REREDO = 58
    ICON_MUTATE = 59
    ICON_ROTATE = 60
    ICON_REPEAT = 61
    ICON_SHUFFLE = 62
    ICON_EMPTYBOX = 63
    ICON_TARGET = 64
    ICON_TARGET_SMALL_FILL = 65
    ICON_TARGET_BIG_FILL = 66
    ICON_TARGET_MOVE_FILL = 67
    ICON_CURSOR_MOVE_FILL = 68
    ICON_CURSOR_SCALE_FILL = 69
    ICON_CURSOR_SCALE_RIGHT_FILL = 70
    ICON_CURSOR_SCALE_LEFT_FILL = 71
    ICON_UNDO_FILL = 72
    ICON_REDO_FILL = 73
    ICON_REREDO_FILL = 74
    ICON_MUTATE_FILL = 75
    ICON_ROTATE_FILL = 76
    ICON_REPEAT_FILL = 77
    ICON_SHUFFLE_FILL = 78
    ICON_EMPTYBOX_SMALL = 79
    ICON_BOX = 80
    ICON_BOX_TOP = 81
    ICON_BOX_TOP_RIGHT = 82
    ICON_BOX_RIGHT = 83
    ICON_BOX_BOTTOM_RIGHT = 84
    ICON_BOX_BOTTOM = 85
    ICON_BOX_BOTTOM_LEFT = 86
    ICON_BOX_LEFT = 87
    ICON_BOX_TOP_LEFT = 88
    ICON_BOX_CENTER = 89
    ICON_BOX_CIRCLE_MASK = 90
    ICON_POT = 91
    ICON_ALPHA_MULTIPLY = 92
    ICON_ALPHA_CLEAR = 93
    ICON_DITHERING = 94
    ICON_MIPMAPS = 95
    ICON_BOX_GRID = 96
    ICON_GRID = 97
    ICON_BOX_CORNERS_SMALL = 98
    ICON_BOX_CORNERS_BIG = 99
    ICON_FOUR_BOXES = 100
    ICON_GRID_FILL = 101
    ICON_BOX_MULTISIZE = 102
    ICON_ZOOM_SMALL = 103
    ICON_ZOOM_MEDIUM = 104
    ICON_ZOOM_BIG = 105
    ICON_ZOOM_ALL = 106
    ICON_ZOOM_CENTER = 107
    ICON_BOX_DOTS_SMALL = 108
    ICON_BOX_DOTS_BIG = 109
    ICON_BOX_CONCENTRIC = 110
    ICON_BOX_GRID_BIG = 111
    ICON_OK_TICK = 112
    ICON_CROSS = 113
    ICON_ARROW_LEFT = 114
    ICON_ARROW_RIGHT = 115
    ICON_ARROW_DOWN = 116
    ICON_ARROW_UP = 117
    ICON_ARROW_LEFT_FILL = 118
    ICON_ARROW_RIGHT_FILL = 119
    ICON_ARROW_DOWN_FILL = 120
    ICON_ARROW_UP_FILL = 121
    ICON_AUDIO = 122
    ICON_FX = 123
    ICON_WAVE = 124
    ICON_WAVE_SINUS = 125
    ICON_WAVE_SQUARE = 126
    ICON_WAVE_TRIANGULAR = 127
    ICON_CROSS_SMALL = 128
    ICON_PLAYER_PREVIOUS = 129
    ICON_PLAYER_PLAY_BACK = 130
    ICON_PLAYER_PLAY = 131
    ICON_PLAYER_PAUSE = 132
    ICON_PLAYER_STOP = 133
    ICON_PLAYER_NEXT = 134
    ICON_PLAYER_RECORD = 135
    ICON_MAGNET = 136
    ICON_LOCK_CLOSE = 137
    ICON_LOCK_OPEN = 138
    ICON_CLOCK = 139
    ICON_TOOLS = 140
    ICON_GEAR = 141
    ICON_GEAR_BIG = 142
    ICON_BIN = 143
    ICON_HAND_POINTER = 144
    ICON_LASER = 145
    ICON_COIN = 146
    ICON_EXPLOSION = 147
    ICON_1UP = 148
    ICON_PLAYER = 149
    ICON_PLAYER_JUMP = 150
    ICON_KEY = 151
    ICON_DEMON = 152
    ICON_TEXT_POPUP = 153
    ICON_GEAR_EX = 154
    ICON_CRACK = 155
    ICON_CRACK_POINTS = 156
    ICON_STAR = 157
    ICON_DOOR = 158
    ICON_EXIT = 159
    ICON_MODE_2D = 160
    ICON_MODE_3D = 161
    ICON_CUBE = 162
    ICON_CUBE_FACE_TOP = 163
    ICON_CUBE_FACE_LEFT = 164
    ICON_CUBE_FACE_FRONT = 165
    ICON_CUBE_FACE_BOTTOM = 166
    ICON_CUBE_FACE_RIGHT = 167
    ICON_CUBE_FACE_BACK = 168
    ICON_CAMERA = 169
    ICON_SPECIAL = 170
    ICON_LINK_NET = 171
    ICON_LINK_BOXES = 172
    ICON_LINK_MULTI = 173
    ICON_LINK = 174
    ICON_LINK_BROKE = 175
    ICON_TEXT_NOTES = 176
    ICON_NOTEBOOK = 177
    ICON_SUITCASE = 178
    ICON_SUITCASE_ZIP = 179
    ICON_MAILBOX = 180
    ICON_MONITOR = 181
    ICON_PRINTER = 182
    ICON_PHOTO_CAMERA = 183
    ICON_PHOTO_CAMERA_FLASH = 184
    ICON_HOUSE = 185
    ICON_HEART = 186
    ICON_CORNER = 187
    ICON_VERTICAL_BARS = 188
    ICON_VERTICAL_BARS_FILL = 189
    ICON_LIFE_BARS = 190
    ICON_INFO = 191
    ICON_CROSSLINE = 192
    ICON_HELP = 193
    ICON_FILETYPE_ALPHA = 194
    ICON_FILETYPE_HOME = 195
    ICON_LAYERS_VISIBLE = 196
    ICON_LAYERS = 197
    ICON_WINDOW = 198
    ICON_HIDPI = 199
    ICON_FILETYPE_BINARY = 200
    ICON_HEX = 201
    ICON_SHIELD = 202
    ICON_FILE_NEW = 203
    ICON_FOLDER_ADD = 204
    ICON_ALARM = 205
    ICON_CPU = 206
    ICON_ROM = 207
    ICON_STEP_OVER = 208
    ICON_STEP_INTO = 209
    ICON_STEP_OUT = 210
    ICON_RESTART = 211
    ICON_BREAKPOINT_ON = 212
    ICON_BREAKPOINT_OFF = 213
    ICON_BURGER_MENU = 214
    ICON_CASE_SENSITIVE = 215
    ICON_REG_EXP = 216
    ICON_FOLDER = 217
    ICON_FILE = 218
    ICON_SAND_TIMER = 219
    ICON_WARNING = 220
    ICON_HELP_BOX = 221
    ICON_INFO_BOX = 222
    ICON_PRIORITY = 223
    ICON_LAYERS_ISO = 224
    ICON_LAYERS2 = 225
    ICON_MLAYERS = 226
    ICON_MAPS = 227
    ICON_HOT = 228
    ICON_229 = 229
    ICON_230 = 230
    ICON_231 = 231
    ICON_232 = 232
    ICON_233 = 233
    ICON_234 = 234
    ICON_235 = 235
    ICON_236 = 236
    ICON_237 = 237
    ICON_238 = 238
    ICON_239 = 239
    ICON_240 = 240
    ICON_241 = 241
    ICON_242 = 242
    ICON_243 = 243
    ICON_244 = 244
    ICON_245 = 245
    ICON_246 = 246
    ICON_247 = 247
    ICON_248 = 248
    ICON_249 = 249
    ICON_250 = 250
    ICON_251 = 251
    ICON_252 = 252
    ICON_253 = 253
    ICON_254 = 254
    ICON_255 = 255

from typing import Any
from warnings import deprecated
import _cffi_backend # type: ignore

ffi: _cffi_backend.FFI
PhysicsShapeType = int

def attach_audio_mixed_processor(processor: Any,) -> None:
    """Attach audio stream processor to the entire audio pipeline, receives the samples as 'float'."""
    ...
def attach_audio_stream_processor(stream: AudioStream|list|tuple,processor: Any,) -> None:
    """Attach audio stream processor to stream, receives the samples as 'float'."""
    ...
def begin_blend_mode(mode: int,) -> None:
    """Begin blending mode (alpha, additive, multiplied, subtract, custom)."""
    ...
def begin_drawing() -> None:
    """Setup canvas (framebuffer) to start drawing."""
    ...
def begin_mode_2d(camera: Camera2D|list|tuple,) -> None:
    """Begin 2D mode with custom camera (2D)."""
    ...
def begin_mode_3d(camera: Camera3D|list|tuple,) -> None:
    """Begin 3D mode with custom camera (3D)."""
    ...
def begin_scissor_mode(x: int,y: int,width: int,height: int,) -> None:
    """Begin scissor mode (define screen area for following drawing)."""
    ...
def begin_shader_mode(shader: Shader|list|tuple,) -> None:
    """Begin custom shader drawing."""
    ...
def begin_texture_mode(target: RenderTexture|list|tuple,) -> None:
    """Begin drawing to render texture."""
    ...
def begin_vr_stereo_mode(config: VrStereoConfig|list|tuple,) -> None:
    """Begin stereo rendering (requires VR simulator)."""
    ...
def change_directory(dir: str,) -> bool:
    """Change working directory, return true on success."""
    ...
def check_collision_box_sphere(box: BoundingBox|list|tuple,center: Vector3|list|tuple,radius: float,) -> bool:
    """Check collision between box and sphere."""
    ...
def check_collision_boxes(box1: BoundingBox|list|tuple,box2: BoundingBox|list|tuple,) -> bool:
    """Check collision between two bounding boxes."""
    ...
def check_collision_circle_line(center: Vector2|list|tuple,radius: float,p1: Vector2|list|tuple,p2: Vector2|list|tuple,) -> bool:
    """Check if circle collides with a line created betweeen two points [p1] and [p2]."""
    ...
def check_collision_circle_rec(center: Vector2|list|tuple,radius: float,rec: Rectangle|list|tuple,) -> bool:
    """Check collision between circle and rectangle."""
    ...
def check_collision_circles(center1: Vector2|list|tuple,radius1: float,center2: Vector2|list|tuple,radius2: float,) -> bool:
    """Check collision between two circles."""
    ...
def check_collision_lines(startPos1: Vector2|list|tuple,endPos1: Vector2|list|tuple,startPos2: Vector2|list|tuple,endPos2: Vector2|list|tuple,collisionPoint: Any|list|tuple,) -> bool:
    """Check the collision between two lines defined by two points each, returns collision point by reference."""
    ...
def check_collision_point_circle(point: Vector2|list|tuple,center: Vector2|list|tuple,radius: float,) -> bool:
    """Check if point is inside circle."""
    ...
def check_collision_point_line(point: Vector2|list|tuple,p1: Vector2|list|tuple,p2: Vector2|list|tuple,threshold: int,) -> bool:
    """Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]."""
    ...
def check_collision_point_poly(point: Vector2|list|tuple,points: Any|list|tuple,pointCount: int,) -> bool:
    """Check if point is within a polygon described by array of vertices."""
    ...
def check_collision_point_rec(point: Vector2|list|tuple,rec: Rectangle|list|tuple,) -> bool:
    """Check if point is inside rectangle."""
    ...
def check_collision_point_triangle(point: Vector2|list|tuple,p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,) -> bool:
    """Check if point is inside a triangle."""
    ...
def check_collision_recs(rec1: Rectangle|list|tuple,rec2: Rectangle|list|tuple,) -> bool:
    """Check collision between two rectangles."""
    ...
def check_collision_spheres(center1: Vector3|list|tuple,radius1: float,center2: Vector3|list|tuple,radius2: float,) -> bool:
    """Check collision between two spheres."""
    ...
def clamp(value: float,min_1: float,max_2: float,) -> float:
    """."""
    ...
def clear_background(color: Color|list|tuple,) -> None:
    """Set background color (framebuffer clear color)."""
    ...
def clear_window_state(flags: int,) -> None:
    """Clear window configuration state flags."""
    ...
def close_audio_device() -> None:
    """Close the audio device and context."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def close_physics() -> None:
    """Unitializes physics pointers and closes physics loop thread."""
    ...
def close_window() -> None:
    """Close window and unload OpenGL context."""
    ...
def codepoint_to_utf8(codepoint: int,utf8Size: Any,) -> str:
    """Encode one codepoint into UTF-8 byte array (array length returned as parameter)."""
    ...
def color_alpha(color: Color|list|tuple,alpha: float,) -> Color:
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f."""
    ...
def color_alpha_blend(dst: Color|list|tuple,src: Color|list|tuple,tint: Color|list|tuple,) -> Color:
    """Get src alpha-blended into dst color with tint."""
    ...
def color_brightness(color: Color|list|tuple,factor: float,) -> Color:
    """Get color with brightness correction, brightness factor goes from -1.0f to 1.0f."""
    ...
def color_contrast(color: Color|list|tuple,contrast: float,) -> Color:
    """Get color with contrast correction, contrast values between -1.0f and 1.0f."""
    ...
def color_from_hsv(hue: float,saturation: float,value: float,) -> Color:
    """Get a Color from HSV values, hue [0..360], saturation/value [0..1]."""
    ...
def color_from_normalized(normalized: Vector4|list|tuple,) -> Color:
    """Get Color from normalized values [0..1]."""
    ...
def color_is_equal(col1: Color|list|tuple,col2: Color|list|tuple,) -> bool:
    """Check if two colors are equal."""
    ...
def color_lerp(color1: Color|list|tuple,color2: Color|list|tuple,factor: float,) -> Color:
    """Get color lerp interpolation between two colors, factor [0.0f..1.0f]."""
    ...
def color_normalize(color: Color|list|tuple,) -> Vector4:
    """Get Color normalized as float [0..1]."""
    ...
def color_tint(color: Color|list|tuple,tint: Color|list|tuple,) -> Color:
    """Get color multiplied with another color."""
    ...
def color_to_hsv(color: Color|list|tuple,) -> Vector3:
    """Get HSV values for a Color, hue [0..360], saturation/value [0..1]."""
    ...
def color_to_int(color: Color|list|tuple,) -> int:
    """Get hexadecimal value for a Color (0xRRGGBBAA)."""
    ...
def compress_data(data: str,dataSize: int,compDataSize: Any,) -> str:
    """Compress data (DEFLATE algorithm), memory must be MemFree()."""
    ...
def compute_crc32(data: str,dataSize: int,) -> int:
    """Compute CRC32 hash code."""
    ...
def compute_md5(data: str,dataSize: int,) -> Any:
    """Compute MD5 hash code, returns static int[4] (16 bytes)."""
    ...
def compute_sha1(data: str,dataSize: int,) -> Any:
    """Compute SHA1 hash code, returns static int[5] (20 bytes)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def create_physics_body_circle(pos: Vector2|list|tuple,radius: float,density: float,) -> Any:
    """Creates a new circle physics body with generic parameters."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def create_physics_body_polygon(pos: Vector2|list|tuple,radius: float,sides: int,density: float,) -> Any:
    """Creates a new polygon physics body with generic parameters."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def create_physics_body_rectangle(pos: Vector2|list|tuple,width: float,height: float,density: float,) -> Any:
    """Creates a new rectangle physics body with generic parameters."""
    ...
def decode_data_base64(data: str,outputSize: Any,) -> str:
    """Decode Base64 string data, memory must be MemFree()."""
    ...
def decompress_data(compData: str,compDataSize: int,dataSize: Any,) -> str:
    """Decompress data (DEFLATE algorithm), memory must be MemFree()."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def destroy_physics_body(body: Any|list|tuple,) -> None:
    """Unitializes and destroy a physics body."""
    ...
def detach_audio_mixed_processor(processor: Any,) -> None:
    """Detach audio stream processor from the entire audio pipeline."""
    ...
def detach_audio_stream_processor(stream: AudioStream|list|tuple,processor: Any,) -> None:
    """Detach audio stream processor from stream."""
    ...
def directory_exists(dirPath: str,) -> bool:
    """Check if a directory path exists."""
    ...
def disable_cursor() -> None:
    """Disables cursor (lock cursor)."""
    ...
def disable_event_waiting() -> None:
    """Disable waiting for events on EndDrawing(), automatic events polling."""
    ...
def draw_billboard(camera: Camera3D|list|tuple,texture: Texture|list|tuple,position: Vector3|list|tuple,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a billboard texture."""
    ...
def draw_billboard_pro(camera: Camera3D|list|tuple,texture: Texture|list|tuple,source: Rectangle|list|tuple,position: Vector3|list|tuple,up: Vector3|list|tuple,size: Vector2|list|tuple,origin: Vector2|list|tuple,rotation: float,tint: Color|list|tuple,) -> None:
    """Draw a billboard texture defined by source and rotation."""
    ...
def draw_billboard_rec(camera: Camera3D|list|tuple,texture: Texture|list|tuple,source: Rectangle|list|tuple,position: Vector3|list|tuple,size: Vector2|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a billboard texture defined by source."""
    ...
def draw_bounding_box(box: BoundingBox|list|tuple,color: Color|list|tuple,) -> None:
    """Draw bounding box (wires)."""
    ...
def draw_capsule(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,radius: float,slices: int,rings: int,color: Color|list|tuple,) -> None:
    """Draw a capsule with the center of its sphere caps at startPos and endPos."""
    ...
def draw_capsule_wires(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,radius: float,slices: int,rings: int,color: Color|list|tuple,) -> None:
    """Draw capsule wireframe with the center of its sphere caps at startPos and endPos."""
    ...
def draw_circle(centerX: int,centerY: int,radius: float,color: Color|list|tuple,) -> None:
    """Draw a color-filled circle."""
    ...
def draw_circle_3d(center: Vector3|list|tuple,radius: float,rotationAxis: Vector3|list|tuple,rotationAngle: float,color: Color|list|tuple,) -> None:
    """Draw a circle in 3D world space."""
    ...
def draw_circle_gradient(centerX: int,centerY: int,radius: float,inner: Color|list|tuple,outer: Color|list|tuple,) -> None:
    """Draw a gradient-filled circle."""
    ...
def draw_circle_lines(centerX: int,centerY: int,radius: float,color: Color|list|tuple,) -> None:
    """Draw circle outline."""
    ...
def draw_circle_lines_v(center: Vector2|list|tuple,radius: float,color: Color|list|tuple,) -> None:
    """Draw circle outline (Vector version)."""
    ...
def draw_circle_sector(center: Vector2|list|tuple,radius: float,startAngle: float,endAngle: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw a piece of a circle."""
    ...
def draw_circle_sector_lines(center: Vector2|list|tuple,radius: float,startAngle: float,endAngle: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw circle sector outline."""
    ...
def draw_circle_v(center: Vector2|list|tuple,radius: float,color: Color|list|tuple,) -> None:
    """Draw a color-filled circle (Vector version)."""
    ...
def draw_cube(position: Vector3|list|tuple,width: float,height: float,length: float,color: Color|list|tuple,) -> None:
    """Draw cube."""
    ...
def draw_cube_v(position: Vector3|list|tuple,size: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw cube (Vector version)."""
    ...
def draw_cube_wires(position: Vector3|list|tuple,width: float,height: float,length: float,color: Color|list|tuple,) -> None:
    """Draw cube wires."""
    ...
def draw_cube_wires_v(position: Vector3|list|tuple,size: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw cube wires (Vector version)."""
    ...
def draw_cylinder(position: Vector3|list|tuple,radiusTop: float,radiusBottom: float,height: float,slices: int,color: Color|list|tuple,) -> None:
    """Draw a cylinder/cone."""
    ...
def draw_cylinder_ex(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,startRadius: float,endRadius: float,sides: int,color: Color|list|tuple,) -> None:
    """Draw a cylinder with base at startPos and top at endPos."""
    ...
def draw_cylinder_wires(position: Vector3|list|tuple,radiusTop: float,radiusBottom: float,height: float,slices: int,color: Color|list|tuple,) -> None:
    """Draw a cylinder/cone wires."""
    ...
def draw_cylinder_wires_ex(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,startRadius: float,endRadius: float,sides: int,color: Color|list|tuple,) -> None:
    """Draw a cylinder wires with base at startPos and top at endPos."""
    ...
def draw_ellipse(centerX: int,centerY: int,radiusH: float,radiusV: float,color: Color|list|tuple,) -> None:
    """Draw ellipse."""
    ...
def draw_ellipse_lines(centerX: int,centerY: int,radiusH: float,radiusV: float,color: Color|list|tuple,) -> None:
    """Draw ellipse outline."""
    ...
def draw_fps(posX: int,posY: int,) -> None:
    """Draw current FPS."""
    ...
def draw_grid(slices: int,spacing: float,) -> None:
    """Draw a grid (centered at (0, 0, 0))."""
    ...
def draw_line(startPosX: int,startPosY: int,endPosX: int,endPosY: int,color: Color|list|tuple,) -> None:
    """Draw a line."""
    ...
def draw_line_3d(startPos: Vector3|list|tuple,endPos: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a line in 3D world space."""
    ...
def draw_line_bezier(startPos: Vector2|list|tuple,endPos: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw line segment cubic-bezier in-out interpolation."""
    ...
def draw_line_ex(startPos: Vector2|list|tuple,endPos: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw a line (using triangles/quads)."""
    ...
def draw_line_strip(points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw lines sequence (using gl lines)."""
    ...
def draw_line_v(startPos: Vector2|list|tuple,endPos: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a line (using gl lines)."""
    ...
def draw_mesh(mesh: Mesh|list|tuple,material: Material|list|tuple,transform: Matrix|list|tuple,) -> None:
    """Draw a 3d mesh with material and transform."""
    ...
def draw_mesh_instanced(mesh: Mesh|list|tuple,material: Material|list|tuple,transforms: Any|list|tuple,instances: int,) -> None:
    """Draw multiple mesh instances with material and different transforms."""
    ...
def draw_model(model: Model|list|tuple,position: Vector3|list|tuple,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a model (with texture if set)."""
    ...
def draw_model_ex(model: Model|list|tuple,position: Vector3|list|tuple,rotationAxis: Vector3|list|tuple,rotationAngle: float,scale: Vector3|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a model with extended parameters."""
    ...
def draw_model_points(model: Model|list|tuple,position: Vector3|list|tuple,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a model as points."""
    ...
def draw_model_points_ex(model: Model|list|tuple,position: Vector3|list|tuple,rotationAxis: Vector3|list|tuple,rotationAngle: float,scale: Vector3|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a model as points with extended parameters."""
    ...
def draw_model_wires(model: Model|list|tuple,position: Vector3|list|tuple,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a model wires (with texture if set)."""
    ...
def draw_model_wires_ex(model: Model|list|tuple,position: Vector3|list|tuple,rotationAxis: Vector3|list|tuple,rotationAngle: float,scale: Vector3|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a model wires (with texture if set) with extended parameters."""
    ...
def draw_pixel(posX: int,posY: int,color: Color|list|tuple,) -> None:
    """Draw a pixel using geometry [Can be slow, use with care]."""
    ...
def draw_pixel_v(position: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a pixel using geometry (Vector version) [Can be slow, use with care]."""
    ...
def draw_plane(centerPos: Vector3|list|tuple,size: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a plane XZ."""
    ...
def draw_point_3d(position: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a point in 3D space, actually a small line."""
    ...
def draw_poly(center: Vector2|list|tuple,sides: int,radius: float,rotation: float,color: Color|list|tuple,) -> None:
    """Draw a regular polygon (Vector version)."""
    ...
def draw_poly_lines(center: Vector2|list|tuple,sides: int,radius: float,rotation: float,color: Color|list|tuple,) -> None:
    """Draw a polygon outline of n sides."""
    ...
def draw_poly_lines_ex(center: Vector2|list|tuple,sides: int,radius: float,rotation: float,lineThick: float,color: Color|list|tuple,) -> None:
    """Draw a polygon outline of n sides with extended parameters."""
    ...
def draw_ray(ray: Ray|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a ray line."""
    ...
def draw_rectangle(posX: int,posY: int,width: int,height: int,color: Color|list|tuple,) -> None:
    """Draw a color-filled rectangle."""
    ...
def draw_rectangle_gradient_ex(rec: Rectangle|list|tuple,topLeft: Color|list|tuple,bottomLeft: Color|list|tuple,topRight: Color|list|tuple,bottomRight: Color|list|tuple,) -> None:
    """Draw a gradient-filled rectangle with custom vertex colors."""
    ...
def draw_rectangle_gradient_h(posX: int,posY: int,width: int,height: int,left: Color|list|tuple,right: Color|list|tuple,) -> None:
    """Draw a horizontal-gradient-filled rectangle."""
    ...
def draw_rectangle_gradient_v(posX: int,posY: int,width: int,height: int,top: Color|list|tuple,bottom: Color|list|tuple,) -> None:
    """Draw a vertical-gradient-filled rectangle."""
    ...
def draw_rectangle_lines(posX: int,posY: int,width: int,height: int,color: Color|list|tuple,) -> None:
    """Draw rectangle outline."""
    ...
def draw_rectangle_lines_ex(rec: Rectangle|list|tuple,lineThick: float,color: Color|list|tuple,) -> None:
    """Draw rectangle outline with extended parameters."""
    ...
def draw_rectangle_pro(rec: Rectangle|list|tuple,origin: Vector2|list|tuple,rotation: float,color: Color|list|tuple,) -> None:
    """Draw a color-filled rectangle with pro parameters."""
    ...
def draw_rectangle_rec(rec: Rectangle|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a color-filled rectangle."""
    ...
def draw_rectangle_rounded(rec: Rectangle|list|tuple,roundness: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw rectangle with rounded edges."""
    ...
def draw_rectangle_rounded_lines(rec: Rectangle|list|tuple,roundness: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw rectangle lines with rounded edges."""
    ...
def draw_rectangle_rounded_lines_ex(rec: Rectangle|list|tuple,roundness: float,segments: int,lineThick: float,color: Color|list|tuple,) -> None:
    """Draw rectangle with rounded edges outline."""
    ...
def draw_rectangle_v(position: Vector2|list|tuple,size: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a color-filled rectangle (Vector version)."""
    ...
def draw_ring(center: Vector2|list|tuple,innerRadius: float,outerRadius: float,startAngle: float,endAngle: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw ring."""
    ...
def draw_ring_lines(center: Vector2|list|tuple,innerRadius: float,outerRadius: float,startAngle: float,endAngle: float,segments: int,color: Color|list|tuple,) -> None:
    """Draw ring outline."""
    ...
def draw_sphere(centerPos: Vector3|list|tuple,radius: float,color: Color|list|tuple,) -> None:
    """Draw sphere."""
    ...
def draw_sphere_ex(centerPos: Vector3|list|tuple,radius: float,rings: int,slices: int,color: Color|list|tuple,) -> None:
    """Draw sphere with extended parameters."""
    ...
def draw_sphere_wires(centerPos: Vector3|list|tuple,radius: float,rings: int,slices: int,color: Color|list|tuple,) -> None:
    """Draw sphere wires."""
    ...
def draw_spline_basis(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: B-Spline, minimum 4 points."""
    ...
def draw_spline_bezier_cubic(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: Cubic Bezier, minimum 4 points (2 control points): [p1, c2, c3, p4, c5, c6...]."""
    ...
def draw_spline_bezier_quadratic(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: Quadratic Bezier, minimum 3 points (1 control point): [p1, c2, p3, c4...]."""
    ...
def draw_spline_catmull_rom(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: Catmull-Rom, minimum 4 points."""
    ...
def draw_spline_linear(points: Any|list|tuple,pointCount: int,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline: Linear, minimum 2 points."""
    ...
def draw_spline_segment_basis(p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,p4: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: B-Spline, 4 points."""
    ...
def draw_spline_segment_bezier_cubic(p1: Vector2|list|tuple,c2: Vector2|list|tuple,c3: Vector2|list|tuple,p4: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: Cubic Bezier, 2 points, 2 control points."""
    ...
def draw_spline_segment_bezier_quadratic(p1: Vector2|list|tuple,c2: Vector2|list|tuple,p3: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: Quadratic Bezier, 2 points, 1 control point."""
    ...
def draw_spline_segment_catmull_rom(p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,p4: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: Catmull-Rom, 4 points."""
    ...
def draw_spline_segment_linear(p1: Vector2|list|tuple,p2: Vector2|list|tuple,thick: float,color: Color|list|tuple,) -> None:
    """Draw spline segment: Linear, 2 points."""
    ...
def draw_text(text: str,posX: int,posY: int,fontSize: int,color: Color|list|tuple,) -> None:
    """Draw text (using default font)."""
    ...
def draw_text_codepoint(font: Font|list|tuple,codepoint: int,position: Vector2|list|tuple,fontSize: float,tint: Color|list|tuple,) -> None:
    """Draw one character (codepoint)."""
    ...
def draw_text_codepoints(font: Font|list|tuple,codepoints: Any,codepointCount: int,position: Vector2|list|tuple,fontSize: float,spacing: float,tint: Color|list|tuple,) -> None:
    """Draw multiple character (codepoint)."""
    ...
def draw_text_ex(font: Font|list|tuple,text: str,position: Vector2|list|tuple,fontSize: float,spacing: float,tint: Color|list|tuple,) -> None:
    """Draw text using font and additional parameters."""
    ...
def draw_text_pro(font: Font|list|tuple,text: str,position: Vector2|list|tuple,origin: Vector2|list|tuple,rotation: float,fontSize: float,spacing: float,tint: Color|list|tuple,) -> None:
    """Draw text using Font and pro parameters (rotation)."""
    ...
def draw_texture(texture: Texture|list|tuple,posX: int,posY: int,tint: Color|list|tuple,) -> None:
    """Draw a Texture2D."""
    ...
def draw_texture_ex(texture: Texture|list|tuple,position: Vector2|list|tuple,rotation: float,scale: float,tint: Color|list|tuple,) -> None:
    """Draw a Texture2D with extended parameters."""
    ...
def draw_texture_n_patch(texture: Texture|list|tuple,nPatchInfo: NPatchInfo|list|tuple,dest: Rectangle|list|tuple,origin: Vector2|list|tuple,rotation: float,tint: Color|list|tuple,) -> None:
    """Draws a texture (or part of it) that stretches or shrinks nicely."""
    ...
def draw_texture_pro(texture: Texture|list|tuple,source: Rectangle|list|tuple,dest: Rectangle|list|tuple,origin: Vector2|list|tuple,rotation: float,tint: Color|list|tuple,) -> None:
    """Draw a part of a texture defined by a rectangle with 'pro' parameters."""
    ...
def draw_texture_rec(texture: Texture|list|tuple,source: Rectangle|list|tuple,position: Vector2|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a part of a texture defined by a rectangle."""
    ...
def draw_texture_v(texture: Texture|list|tuple,position: Vector2|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a Texture2D with position defined as Vector2."""
    ...
def draw_triangle(v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a color-filled triangle (vertex in counter-clockwise order!)."""
    ...
def draw_triangle_3d(v1: Vector3|list|tuple,v2: Vector3|list|tuple,v3: Vector3|list|tuple,color: Color|list|tuple,) -> None:
    """Draw a color-filled triangle (vertex in counter-clockwise order!)."""
    ...
def draw_triangle_fan(points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle fan defined by points (first vertex is the center)."""
    ...
def draw_triangle_lines(v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw triangle outline (vertex in counter-clockwise order!)."""
    ...
def draw_triangle_strip(points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle strip defined by points."""
    ...
def draw_triangle_strip_3d(points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle strip defined by points."""
    ...
def enable_cursor() -> None:
    """Enables cursor (unlock cursor)."""
    ...
def enable_event_waiting() -> None:
    """Enable waiting for events on EndDrawing(), no automatic event polling."""
    ...
def encode_data_base64(data: str,dataSize: int,outputSize: Any,) -> str:
    """Encode data to Base64 string, memory must be MemFree()."""
    ...
def end_blend_mode() -> None:
    """End blending mode (reset to default: alpha blending)."""
    ...
def end_drawing() -> None:
    """End canvas drawing and swap buffers (double buffering)."""
    ...
def end_mode_2d() -> None:
    """Ends 2D mode with custom camera."""
    ...
def end_mode_3d() -> None:
    """Ends 3D mode and returns to default 2D orthographic mode."""
    ...
def end_scissor_mode() -> None:
    """End scissor mode."""
    ...
def end_shader_mode() -> None:
    """End custom shader drawing (use default shader)."""
    ...
def end_texture_mode() -> None:
    """Ends drawing to render texture."""
    ...
def end_vr_stereo_mode() -> None:
    """End stereo rendering (requires VR simulator)."""
    ...
def export_automation_event_list(list_0: AutomationEventList|list|tuple,fileName: str,) -> bool:
    """Export automation events list as text file."""
    ...
def export_data_as_code(data: str,dataSize: int,fileName: str,) -> bool:
    """Export data to code (.h), returns true on success."""
    ...
def export_font_as_code(font: Font|list|tuple,fileName: str,) -> bool:
    """Export font as code file, returns true on success."""
    ...
def export_image(image: Image|list|tuple,fileName: str,) -> bool:
    """Export image data to file, returns true on success."""
    ...
def export_image_as_code(image: Image|list|tuple,fileName: str,) -> bool:
    """Export image as code file defining an array of bytes, returns true on success."""
    ...
def export_image_to_memory(image: Image|list|tuple,fileType: str,fileSize: Any,) -> str:
    """Export image to memory buffer."""
    ...
def export_mesh(mesh: Mesh|list|tuple,fileName: str,) -> bool:
    """Export mesh data to file, returns true on success."""
    ...
def export_mesh_as_code(mesh: Mesh|list|tuple,fileName: str,) -> bool:
    """Export mesh as code file (.h) defining multiple arrays of vertex attributes."""
    ...
def export_wave(wave: Wave|list|tuple,fileName: str,) -> bool:
    """Export wave data to file, returns true on success."""
    ...
def export_wave_as_code(wave: Wave|list|tuple,fileName: str,) -> bool:
    """Export wave sample data to code (.h), returns true on success."""
    ...
def fade(color: Color|list|tuple,alpha: float,) -> Color:
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f."""
    ...
def file_exists(fileName: str,) -> bool:
    """Check if file exists."""
    ...
def float_equals(x: float,y: float,) -> int:
    """."""
    ...
def gen_image_cellular(width: int,height: int,tileSize: int,) -> Image:
    """Generate image: cellular algorithm, bigger tileSize means bigger cells."""
    ...
def gen_image_checked(width: int,height: int,checksX: int,checksY: int,col1: Color|list|tuple,col2: Color|list|tuple,) -> Image:
    """Generate image: checked."""
    ...
def gen_image_color(width: int,height: int,color: Color|list|tuple,) -> Image:
    """Generate image: plain color."""
    ...
def gen_image_font_atlas(glyphs: Any|list|tuple,glyphRecs: Any|list|tuple,glyphCount: int,fontSize: int,padding: int,packMethod: int,) -> Image:
    """Generate image font atlas using chars info."""
    ...
def gen_image_gradient_linear(width: int,height: int,direction: int,start: Color|list|tuple,end: Color|list|tuple,) -> Image:
    """Generate image: linear gradient, direction in degrees [0..360], 0=Vertical gradient."""
    ...
def gen_image_gradient_radial(width: int,height: int,density: float,inner: Color|list|tuple,outer: Color|list|tuple,) -> Image:
    """Generate image: radial gradient."""
    ...
def gen_image_gradient_square(width: int,height: int,density: float,inner: Color|list|tuple,outer: Color|list|tuple,) -> Image:
    """Generate image: square gradient."""
    ...
def gen_image_perlin_noise(width: int,height: int,offsetX: int,offsetY: int,scale: float,) -> Image:
    """Generate image: perlin noise."""
    ...
def gen_image_text(width: int,height: int,text: str,) -> Image:
    """Generate image: grayscale image from text data."""
    ...
def gen_image_white_noise(width: int,height: int,factor: float,) -> Image:
    """Generate image: white noise."""
    ...
def gen_mesh_cone(radius: float,height: float,slices: int,) -> Mesh:
    """Generate cone/pyramid mesh."""
    ...
def gen_mesh_cube(width: float,height: float,length: float,) -> Mesh:
    """Generate cuboid mesh."""
    ...
def gen_mesh_cubicmap(cubicmap: Image|list|tuple,cubeSize: Vector3|list|tuple,) -> Mesh:
    """Generate cubes-based map mesh from image data."""
    ...
def gen_mesh_cylinder(radius: float,height: float,slices: int,) -> Mesh:
    """Generate cylinder mesh."""
    ...
def gen_mesh_heightmap(heightmap: Image|list|tuple,size: Vector3|list|tuple,) -> Mesh:
    """Generate heightmap mesh from image data."""
    ...
def gen_mesh_hemi_sphere(radius: float,rings: int,slices: int,) -> Mesh:
    """Generate half-sphere mesh (no bottom cap)."""
    ...
def gen_mesh_knot(radius: float,size: float,radSeg: int,sides: int,) -> Mesh:
    """Generate trefoil knot mesh."""
    ...
def gen_mesh_plane(width: float,length: float,resX: int,resZ: int,) -> Mesh:
    """Generate plane mesh (with subdivisions)."""
    ...
def gen_mesh_poly(sides: int,radius: float,) -> Mesh:
    """Generate polygonal mesh."""
    ...
def gen_mesh_sphere(radius: float,rings: int,slices: int,) -> Mesh:
    """Generate sphere mesh (standard sphere)."""
    ...
def gen_mesh_tangents(mesh: Any|list|tuple,) -> None:
    """Compute mesh tangents."""
    ...
def gen_mesh_torus(radius: float,size: float,radSeg: int,sides: int,) -> Mesh:
    """Generate torus mesh."""
    ...
def gen_texture_mipmaps(texture: Any|list|tuple,) -> None:
    """Generate GPU mipmaps for a texture."""
    ...
def get_application_directory() -> str:
    """Get the directory of the running application (uses static string)."""
    ...
def get_camera_matrix(camera: Camera3D|list|tuple,) -> Matrix:
    """Get camera transform matrix (view matrix)."""
    ...
def get_camera_matrix_2d(camera: Camera2D|list|tuple,) -> Matrix:
    """Get camera 2d transform matrix."""
    ...
def get_char_pressed() -> int:
    """Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty."""
    ...
def get_clipboard_image() -> Image:
    """Get clipboard image content."""
    ...
def get_clipboard_text() -> str:
    """Get clipboard text content."""
    ...
def get_codepoint(text: str,codepointSize: Any,) -> int:
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure."""
    ...
def get_codepoint_count(text: str,) -> int:
    """Get total number of codepoints in a UTF-8 encoded string."""
    ...
def get_codepoint_next(text: str,codepointSize: Any,) -> int:
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure."""
    ...
def get_codepoint_previous(text: str,codepointSize: Any,) -> int:
    """Get previous codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure."""
    ...
def get_collision_rec(rec1: Rectangle|list|tuple,rec2: Rectangle|list|tuple,) -> Rectangle:
    """Get collision rectangle for two rectangles collision."""
    ...
def get_color(hexValue: int,) -> Color:
    """Get Color structure from hexadecimal value."""
    ...
def get_current_monitor() -> int:
    """Get current monitor where window is placed."""
    ...
def get_directory_path(filePath: str,) -> str:
    """Get full path for a given fileName with path (uses static string)."""
    ...
def get_fps() -> int:
    """Get current FPS."""
    ...
def get_file_extension(fileName: str,) -> str:
    """Get pointer to extension for a filename string (includes dot: '.png')."""
    ...
def get_file_length(fileName: str,) -> int:
    """Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)."""
    ...
def get_file_mod_time(fileName: str,) -> int:
    """Get file modification time (last write time)."""
    ...
def get_file_name(filePath: str,) -> str:
    """Get pointer to filename for a path string."""
    ...
def get_file_name_without_ext(filePath: str,) -> str:
    """Get filename string without extension (uses static string)."""
    ...
def get_font_default() -> Font:
    """Get the default Font."""
    ...
def get_frame_time() -> float:
    """Get time in seconds for last frame drawn (delta time)."""
    ...
def get_gamepad_axis_count(gamepad: int,) -> int:
    """Get gamepad axis count for a gamepad."""
    ...
def get_gamepad_axis_movement(gamepad: int,axis: int,) -> float:
    """Get axis movement value for a gamepad axis."""
    ...
def get_gamepad_button_pressed() -> int:
    """Get the last gamepad button pressed."""
    ...
def get_gamepad_name(gamepad: int,) -> str:
    """Get gamepad internal name id."""
    ...
def get_gesture_detected() -> int:
    """Get latest detected gesture."""
    ...
def get_gesture_drag_angle() -> float:
    """Get gesture drag angle."""
    ...
def get_gesture_drag_vector() -> Vector2:
    """Get gesture drag vector."""
    ...
def get_gesture_hold_duration() -> float:
    """Get gesture hold time in seconds."""
    ...
def get_gesture_pinch_angle() -> float:
    """Get gesture pinch angle."""
    ...
def get_gesture_pinch_vector() -> Vector2:
    """Get gesture pinch delta."""
    ...
def get_glyph_atlas_rec(font: Font|list|tuple,codepoint: int,) -> Rectangle:
    """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found."""
    ...
def get_glyph_index(font: Font|list|tuple,codepoint: int,) -> int:
    """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found."""
    ...
def get_glyph_info(font: Font|list|tuple,codepoint: int,) -> GlyphInfo:
    """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found."""
    ...
def get_image_alpha_border(image: Image|list|tuple,threshold: float,) -> Rectangle:
    """Get image alpha border rectangle."""
    ...
def get_image_color(image: Image|list|tuple,x: int,y: int,) -> Color:
    """Get image pixel color at (x, y) position."""
    ...
def get_key_pressed() -> int:
    """Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty."""
    ...
def get_master_volume() -> float:
    """Get master volume (listener)."""
    ...
def get_mesh_bounding_box(mesh: Mesh|list|tuple,) -> BoundingBox:
    """Compute mesh bounding box limits."""
    ...
def get_model_bounding_box(model: Model|list|tuple,) -> BoundingBox:
    """Compute model bounding box limits (considers all meshes)."""
    ...
def get_monitor_count() -> int:
    """Get number of connected monitors."""
    ...
def get_monitor_height(monitor: int,) -> int:
    """Get specified monitor height (current video mode used by monitor)."""
    ...
def get_monitor_name(monitor: int,) -> str:
    """Get the human-readable, UTF-8 encoded name of the specified monitor."""
    ...
def get_monitor_physical_height(monitor: int,) -> int:
    """Get specified monitor physical height in millimetres."""
    ...
def get_monitor_physical_width(monitor: int,) -> int:
    """Get specified monitor physical width in millimetres."""
    ...
def get_monitor_position(monitor: int,) -> Vector2:
    """Get specified monitor position."""
    ...
def get_monitor_refresh_rate(monitor: int,) -> int:
    """Get specified monitor refresh rate."""
    ...
def get_monitor_width(monitor: int,) -> int:
    """Get specified monitor width (current video mode used by monitor)."""
    ...
def get_mouse_delta() -> Vector2:
    """Get mouse delta between frames."""
    ...
def get_mouse_position() -> Vector2:
    """Get mouse position XY."""
    ...
def get_mouse_wheel_move() -> float:
    """Get mouse wheel movement for X or Y, whichever is larger."""
    ...
def get_mouse_wheel_move_v() -> Vector2:
    """Get mouse wheel movement for both X and Y."""
    ...
def get_mouse_x() -> int:
    """Get mouse position X."""
    ...
def get_mouse_y() -> int:
    """Get mouse position Y."""
    ...
def get_music_time_length(music: Music|list|tuple,) -> float:
    """Get music time length (in seconds)."""
    ...
def get_music_time_played(music: Music|list|tuple,) -> float:
    """Get current music time played (in seconds)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def get_physics_bodies_count() -> int:
    """Returns the current amount of created physics bodies."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def get_physics_body(index: int,) -> Any:
    """Returns a physics body of the bodies pool at a specific index."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def get_physics_shape_type(index: int,) -> int:
    """Returns the physics body shape type (PHYSICS_CIRCLE or PHYSICS_POLYGON)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def get_physics_shape_vertex(body: Any|list|tuple,vertex: int,) -> Vector2:
    """Returns transformed position of a body shape (body position + vertex transformed position)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def get_physics_shape_vertices_count(index: int,) -> int:
    """Returns the amount of vertices of a physics body shape."""
    ...
def get_pixel_color(srcPtr: Any,format: int,) -> Color:
    """Get Color from a source pixel pointer of certain format."""
    ...
def get_pixel_data_size(width: int,height: int,format: int,) -> int:
    """Get pixel data size in bytes for certain format."""
    ...
def get_prev_directory_path(dirPath: str,) -> str:
    """Get previous directory path for a given path (uses static string)."""
    ...
def get_random_value(min_0: int,max_1: int,) -> int:
    """Get a random value between min and max (both included)."""
    ...
def get_ray_collision_box(ray: Ray|list|tuple,box: BoundingBox|list|tuple,) -> RayCollision:
    """Get collision info between ray and box."""
    ...
def get_ray_collision_mesh(ray: Ray|list|tuple,mesh: Mesh|list|tuple,transform: Matrix|list|tuple,) -> RayCollision:
    """Get collision info between ray and mesh."""
    ...
def get_ray_collision_quad(ray: Ray|list|tuple,p1: Vector3|list|tuple,p2: Vector3|list|tuple,p3: Vector3|list|tuple,p4: Vector3|list|tuple,) -> RayCollision:
    """Get collision info between ray and quad."""
    ...
def get_ray_collision_sphere(ray: Ray|list|tuple,center: Vector3|list|tuple,radius: float,) -> RayCollision:
    """Get collision info between ray and sphere."""
    ...
def get_ray_collision_triangle(ray: Ray|list|tuple,p1: Vector3|list|tuple,p2: Vector3|list|tuple,p3: Vector3|list|tuple,) -> RayCollision:
    """Get collision info between ray and triangle."""
    ...
def get_render_height() -> int:
    """Get current render height (it considers HiDPI)."""
    ...
def get_render_width() -> int:
    """Get current render width (it considers HiDPI)."""
    ...
def get_screen_height() -> int:
    """Get current screen height."""
    ...
def get_screen_to_world_2d(position: Vector2|list|tuple,camera: Camera2D|list|tuple,) -> Vector2:
    """Get the world space position for a 2d camera screen space position."""
    ...
def get_screen_to_world_ray(position: Vector2|list|tuple,camera: Camera3D|list|tuple,) -> Ray:
    """Get a ray trace from screen position (i.e mouse)."""
    ...
def get_screen_to_world_ray_ex(position: Vector2|list|tuple,camera: Camera3D|list|tuple,width: int,height: int,) -> Ray:
    """Get a ray trace from screen position (i.e mouse) in a viewport."""
    ...
def get_screen_width() -> int:
    """Get current screen width."""
    ...
def get_shader_location(shader: Shader|list|tuple,uniformName: str,) -> int:
    """Get shader uniform location."""
    ...
def get_shader_location_attrib(shader: Shader|list|tuple,attribName: str,) -> int:
    """Get shader attribute location."""
    ...
def get_shapes_texture() -> Texture:
    """Get texture that is used for shapes drawing."""
    ...
def get_shapes_texture_rectangle() -> Rectangle:
    """Get texture source rectangle that is used for shapes drawing."""
    ...
def get_spline_point_basis(p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,p4: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: B-Spline."""
    ...
def get_spline_point_bezier_cubic(p1: Vector2|list|tuple,c2: Vector2|list|tuple,c3: Vector2|list|tuple,p4: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: Cubic Bezier."""
    ...
def get_spline_point_bezier_quad(p1: Vector2|list|tuple,c2: Vector2|list|tuple,p3: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: Quadratic Bezier."""
    ...
def get_spline_point_catmull_rom(p1: Vector2|list|tuple,p2: Vector2|list|tuple,p3: Vector2|list|tuple,p4: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: Catmull-Rom."""
    ...
def get_spline_point_linear(startPos: Vector2|list|tuple,endPos: Vector2|list|tuple,t: float,) -> Vector2:
    """Get (evaluate) spline point: Linear."""
    ...
def get_time() -> float:
    """Get elapsed time in seconds since InitWindow()."""
    ...
def get_touch_point_count() -> int:
    """Get number of touch points."""
    ...
def get_touch_point_id(index: int,) -> int:
    """Get touch point identifier for given index."""
    ...
def get_touch_position(index: int,) -> Vector2:
    """Get touch position XY for a touch point index (relative to screen size)."""
    ...
def get_touch_x() -> int:
    """Get touch position X for touch point 0 (relative to screen size)."""
    ...
def get_touch_y() -> int:
    """Get touch position Y for touch point 0 (relative to screen size)."""
    ...
def get_window_handle() -> Any:
    """Get native window handle."""
    ...
def get_window_position() -> Vector2:
    """Get window position XY on monitor."""
    ...
def get_window_scale_dpi() -> Vector2:
    """Get window scale DPI factor."""
    ...
def get_working_directory() -> str:
    """Get current working directory (uses static string)."""
    ...
def get_world_to_screen(position: Vector3|list|tuple,camera: Camera3D|list|tuple,) -> Vector2:
    """Get the screen space position for a 3d world space position."""
    ...
def get_world_to_screen_2d(position: Vector2|list|tuple,camera: Camera2D|list|tuple,) -> Vector2:
    """Get the screen space position for a 2d camera world space position."""
    ...
def get_world_to_screen_ex(position: Vector3|list|tuple,camera: Camera3D|list|tuple,width: int,height: int,) -> Vector2:
    """Get size position for a 3d world space position."""
    ...
def gui_button(bounds: Rectangle|list|tuple,text: str,) -> int:
    """Button control, returns true when clicked."""
    ...
def gui_check_box(bounds: Rectangle|list|tuple,text: str,checked: Any,) -> int:
    """Check Box control, returns true when active."""
    ...
def gui_color_bar_alpha(bounds: Rectangle|list|tuple,text: str,alpha: Any,) -> int:
    """Color Bar Alpha control."""
    ...
def gui_color_bar_hue(bounds: Rectangle|list|tuple,text: str,value: Any,) -> int:
    """Color Bar Hue control."""
    ...
def gui_color_panel(bounds: Rectangle|list|tuple,text: str,color: Any|list|tuple,) -> int:
    """Color Panel control."""
    ...
def gui_color_panel_hsv(bounds: Rectangle|list|tuple,text: str,colorHsv: Any|list|tuple,) -> int:
    """Color Panel control that updates Hue-Saturation-Value color value, used by GuiColorPickerHSV()."""
    ...
def gui_color_picker(bounds: Rectangle|list|tuple,text: str,color: Any|list|tuple,) -> int:
    """Color Picker control (multiple color controls)."""
    ...
def gui_color_picker_hsv(bounds: Rectangle|list|tuple,text: str,colorHsv: Any|list|tuple,) -> int:
    """Color Picker control that avoids conversion to RGB on each call (multiple color controls)."""
    ...
def gui_combo_box(bounds: Rectangle|list|tuple,text: str,active: Any,) -> int:
    """Combo Box control."""
    ...
def gui_disable() -> None:
    """Disable gui controls (global state)."""
    ...
def gui_disable_tooltip() -> None:
    """Disable gui tooltips (global state)."""
    ...
def gui_draw_icon(iconId: int,posX: int,posY: int,pixelSize: int,color: Color|list|tuple,) -> None:
    """Draw icon using pixel size at specified position."""
    ...
def gui_dropdown_box(bounds: Rectangle|list|tuple,text: str,active: Any,editMode: bool,) -> int:
    """Dropdown Box control."""
    ...
def gui_dummy_rec(bounds: Rectangle|list|tuple,text: str,) -> int:
    """Dummy control for placeholders."""
    ...
def gui_enable() -> None:
    """Enable gui controls (global state)."""
    ...
def gui_enable_tooltip() -> None:
    """Enable gui tooltips (global state)."""
    ...
def gui_get_font() -> Font:
    """Get gui custom font (global state)."""
    ...
def gui_get_icons() -> Any:
    """Get raygui icons data pointer."""
    ...
def gui_get_state() -> int:
    """Get gui state (global state)."""
    ...
def gui_get_style(control: int,property: int,) -> int:
    """Get one style property."""
    ...
def gui_grid(bounds: Rectangle|list|tuple,text: str,spacing: float,subdivs: int,mouseCell: Any|list|tuple,) -> int:
    """Grid control."""
    ...
def gui_group_box(bounds: Rectangle|list|tuple,text: str,) -> int:
    """Group Box control with text name."""
    ...
def gui_icon_text(iconId: int,text: str,) -> str:
    """Get text with icon id prepended (if supported)."""
    ...
def gui_is_locked() -> bool:
    """Check if gui is locked (global state)."""
    ...
def gui_label(bounds: Rectangle|list|tuple,text: str,) -> int:
    """Label control."""
    ...
def gui_label_button(bounds: Rectangle|list|tuple,text: str,) -> int:
    """Label button control, returns true when clicked."""
    ...
def gui_line(bounds: Rectangle|list|tuple,text: str,) -> int:
    """Line separator control, could contain text."""
    ...
def gui_list_view(bounds: Rectangle|list|tuple,text: str,scrollIndex: Any,active: Any,) -> int:
    """List View control."""
    ...
def gui_list_view_ex(bounds: Rectangle|list|tuple,text: list[str],count: int,scrollIndex: Any,active: Any,focus: Any,) -> int:
    """List View with extended parameters."""
    ...
def gui_load_icons(fileName: str,loadIconsName: bool,) -> list[str]:
    """Load raygui icons file (.rgi) into internal icons data."""
    ...
def gui_load_style(fileName: str,) -> None:
    """Load style file over global style variable (.rgs)."""
    ...
def gui_load_style_default() -> None:
    """Load style default over global style."""
    ...
def gui_lock() -> None:
    """Lock gui controls (global state)."""
    ...
def gui_message_box(bounds: Rectangle|list|tuple,title: str,message: str,buttons: str,) -> int:
    """Message Box control, displays a message."""
    ...
def gui_panel(bounds: Rectangle|list|tuple,text: str,) -> int:
    """Panel control, useful to group controls."""
    ...
def gui_progress_bar(bounds: Rectangle|list|tuple,textLeft: str,textRight: str,value: Any,minValue: float,maxValue: float,) -> int:
    """Progress Bar control."""
    ...
def gui_scroll_panel(bounds: Rectangle|list|tuple,text: str,content: Rectangle|list|tuple,scroll: Any|list|tuple,view: Any|list|tuple,) -> int:
    """Scroll Panel control."""
    ...
def gui_set_alpha(alpha: float,) -> None:
    """Set gui controls alpha (global state), alpha goes from 0.0f to 1.0f."""
    ...
def gui_set_font(font: Font|list|tuple,) -> None:
    """Set gui custom font (global state)."""
    ...
def gui_set_icon_scale(scale: int,) -> None:
    """Set default icon drawing size."""
    ...
def gui_set_state(state: int,) -> None:
    """Set gui state (global state)."""
    ...
def gui_set_style(control: int,property: int,value: int,) -> None:
    """Set one style property."""
    ...
def gui_set_tooltip(tooltip: str,) -> None:
    """Set tooltip string."""
    ...
def gui_slider(bounds: Rectangle|list|tuple,textLeft: str,textRight: str,value: Any,minValue: float,maxValue: float,) -> int:
    """Slider control."""
    ...
def gui_slider_bar(bounds: Rectangle|list|tuple,textLeft: str,textRight: str,value: Any,minValue: float,maxValue: float,) -> int:
    """Slider Bar control."""
    ...
def gui_spinner(bounds: Rectangle|list|tuple,text: str,value: Any,minValue: int,maxValue: int,editMode: bool,) -> int:
    """Spinner control."""
    ...
def gui_status_bar(bounds: Rectangle|list|tuple,text: str,) -> int:
    """Status Bar control, shows info text."""
    ...
def gui_tab_bar(bounds: Rectangle|list|tuple,text: list[str],count: int,active: Any,) -> int:
    """Tab Bar control, returns TAB to be closed or -1."""
    ...
def gui_text_box(bounds: Rectangle|list|tuple,text: str,textSize: int,editMode: bool,) -> int:
    """Text Box control, updates input text."""
    ...
def gui_text_input_box(bounds: Rectangle|list|tuple,title: str,message: str,buttons: str,text: str,textMaxSize: int,secretViewActive: Any,) -> int:
    """Text Input Box control, ask for text, supports secret."""
    ...
def gui_toggle(bounds: Rectangle|list|tuple,text: str,active: Any,) -> int:
    """Toggle Button control."""
    ...
def gui_toggle_group(bounds: Rectangle|list|tuple,text: str,active: Any,) -> int:
    """Toggle Group control."""
    ...
def gui_toggle_slider(bounds: Rectangle|list|tuple,text: str,active: Any,) -> int:
    """Toggle Slider control."""
    ...
def gui_unlock() -> None:
    """Unlock gui controls (global state)."""
    ...
def gui_value_box(bounds: Rectangle|list|tuple,text: str,value: Any,minValue: int,maxValue: int,editMode: bool,) -> int:
    """Value Box control, updates input text with numbers."""
    ...
def gui_value_box_float(bounds: Rectangle|list|tuple,text: str,textValue: str,value: Any,editMode: bool,) -> int:
    """Value box control for float values."""
    ...
def gui_window_box(bounds: Rectangle|list|tuple,title: str,) -> int:
    """Window Box control, shows a window that can be closed."""
    ...
def hide_cursor() -> None:
    """Hides cursor."""
    ...
def image_alpha_clear(image: Any|list|tuple,color: Color|list|tuple,threshold: float,) -> None:
    """Clear alpha channel to desired color."""
    ...
def image_alpha_crop(image: Any|list|tuple,threshold: float,) -> None:
    """Crop image depending on alpha value."""
    ...
def image_alpha_mask(image: Any|list|tuple,alphaMask: Image|list|tuple,) -> None:
    """Apply alpha mask to image."""
    ...
def image_alpha_premultiply(image: Any|list|tuple,) -> None:
    """Premultiply alpha channel."""
    ...
def image_blur_gaussian(image: Any|list|tuple,blurSize: int,) -> None:
    """Apply Gaussian blur using a box blur approximation."""
    ...
def image_clear_background(dst: Any|list|tuple,color: Color|list|tuple,) -> None:
    """Clear image background with given color."""
    ...
def image_color_brightness(image: Any|list|tuple,brightness: int,) -> None:
    """Modify image color: brightness (-255 to 255)."""
    ...
def image_color_contrast(image: Any|list|tuple,contrast: float,) -> None:
    """Modify image color: contrast (-100 to 100)."""
    ...
def image_color_grayscale(image: Any|list|tuple,) -> None:
    """Modify image color: grayscale."""
    ...
def image_color_invert(image: Any|list|tuple,) -> None:
    """Modify image color: invert."""
    ...
def image_color_replace(image: Any|list|tuple,color: Color|list|tuple,replace: Color|list|tuple,) -> None:
    """Modify image color: replace color."""
    ...
def image_color_tint(image: Any|list|tuple,color: Color|list|tuple,) -> None:
    """Modify image color: tint."""
    ...
def image_copy(image: Image|list|tuple,) -> Image:
    """Create an image duplicate (useful for transformations)."""
    ...
def image_crop(image: Any|list|tuple,crop: Rectangle|list|tuple,) -> None:
    """Crop an image to a defined rectangle."""
    ...
def image_dither(image: Any|list|tuple,rBpp: int,gBpp: int,bBpp: int,aBpp: int,) -> None:
    """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)."""
    ...
def image_draw(dst: Any|list|tuple,src: Image|list|tuple,srcRec: Rectangle|list|tuple,dstRec: Rectangle|list|tuple,tint: Color|list|tuple,) -> None:
    """Draw a source image within a destination image (tint applied to source)."""
    ...
def image_draw_circle(dst: Any|list|tuple,centerX: int,centerY: int,radius: int,color: Color|list|tuple,) -> None:
    """Draw a filled circle within an image."""
    ...
def image_draw_circle_lines(dst: Any|list|tuple,centerX: int,centerY: int,radius: int,color: Color|list|tuple,) -> None:
    """Draw circle outline within an image."""
    ...
def image_draw_circle_lines_v(dst: Any|list|tuple,center: Vector2|list|tuple,radius: int,color: Color|list|tuple,) -> None:
    """Draw circle outline within an image (Vector version)."""
    ...
def image_draw_circle_v(dst: Any|list|tuple,center: Vector2|list|tuple,radius: int,color: Color|list|tuple,) -> None:
    """Draw a filled circle within an image (Vector version)."""
    ...
def image_draw_line(dst: Any|list|tuple,startPosX: int,startPosY: int,endPosX: int,endPosY: int,color: Color|list|tuple,) -> None:
    """Draw line within an image."""
    ...
def image_draw_line_ex(dst: Any|list|tuple,start: Vector2|list|tuple,end: Vector2|list|tuple,thick: int,color: Color|list|tuple,) -> None:
    """Draw a line defining thickness within an image."""
    ...
def image_draw_line_v(dst: Any|list|tuple,start: Vector2|list|tuple,end: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw line within an image (Vector version)."""
    ...
def image_draw_pixel(dst: Any|list|tuple,posX: int,posY: int,color: Color|list|tuple,) -> None:
    """Draw pixel within an image."""
    ...
def image_draw_pixel_v(dst: Any|list|tuple,position: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw pixel within an image (Vector version)."""
    ...
def image_draw_rectangle(dst: Any|list|tuple,posX: int,posY: int,width: int,height: int,color: Color|list|tuple,) -> None:
    """Draw rectangle within an image."""
    ...
def image_draw_rectangle_lines(dst: Any|list|tuple,rec: Rectangle|list|tuple,thick: int,color: Color|list|tuple,) -> None:
    """Draw rectangle lines within an image."""
    ...
def image_draw_rectangle_rec(dst: Any|list|tuple,rec: Rectangle|list|tuple,color: Color|list|tuple,) -> None:
    """Draw rectangle within an image."""
    ...
def image_draw_rectangle_v(dst: Any|list|tuple,position: Vector2|list|tuple,size: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw rectangle within an image (Vector version)."""
    ...
def image_draw_text(dst: Any|list|tuple,text: str,posX: int,posY: int,fontSize: int,color: Color|list|tuple,) -> None:
    """Draw text (using default font) within an image (destination)."""
    ...
def image_draw_text_ex(dst: Any|list|tuple,font: Font|list|tuple,text: str,position: Vector2|list|tuple,fontSize: float,spacing: float,tint: Color|list|tuple,) -> None:
    """Draw text (custom sprite font) within an image (destination)."""
    ...
def image_draw_triangle(dst: Any|list|tuple,v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw triangle within an image."""
    ...
def image_draw_triangle_ex(dst: Any|list|tuple,v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,c1: Color|list|tuple,c2: Color|list|tuple,c3: Color|list|tuple,) -> None:
    """Draw triangle with interpolated colors within an image."""
    ...
def image_draw_triangle_fan(dst: Any|list|tuple,points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle fan defined by points within an image (first vertex is the center)."""
    ...
def image_draw_triangle_lines(dst: Any|list|tuple,v1: Vector2|list|tuple,v2: Vector2|list|tuple,v3: Vector2|list|tuple,color: Color|list|tuple,) -> None:
    """Draw triangle outline within an image."""
    ...
def image_draw_triangle_strip(dst: Any|list|tuple,points: Any|list|tuple,pointCount: int,color: Color|list|tuple,) -> None:
    """Draw a triangle strip defined by points within an image."""
    ...
def image_flip_horizontal(image: Any|list|tuple,) -> None:
    """Flip image horizontally."""
    ...
def image_flip_vertical(image: Any|list|tuple,) -> None:
    """Flip image vertically."""
    ...
def image_format(image: Any|list|tuple,newFormat: int,) -> None:
    """Convert image data to desired format."""
    ...
def image_from_channel(image: Image|list|tuple,selectedChannel: int,) -> Image:
    """Create an image from a selected channel of another image (GRAYSCALE)."""
    ...
def image_from_image(image: Image|list|tuple,rec: Rectangle|list|tuple,) -> Image:
    """Create an image from another image piece."""
    ...
def image_kernel_convolution(image: Any|list|tuple,kernel: Any,kernelSize: int,) -> None:
    """Apply custom square convolution kernel to image."""
    ...
def image_mipmaps(image: Any|list|tuple,) -> None:
    """Compute all mipmap levels for a provided image."""
    ...
def image_resize(image: Any|list|tuple,newWidth: int,newHeight: int,) -> None:
    """Resize image (Bicubic scaling algorithm)."""
    ...
def image_resize_canvas(image: Any|list|tuple,newWidth: int,newHeight: int,offsetX: int,offsetY: int,fill: Color|list|tuple,) -> None:
    """Resize canvas and fill with color."""
    ...
def image_resize_nn(image: Any|list|tuple,newWidth: int,newHeight: int,) -> None:
    """Resize image (Nearest-Neighbor scaling algorithm)."""
    ...
def image_rotate(image: Any|list|tuple,degrees: int,) -> None:
    """Rotate image by input angle in degrees (-359 to 359)."""
    ...
def image_rotate_ccw(image: Any|list|tuple,) -> None:
    """Rotate image counter-clockwise 90deg."""
    ...
def image_rotate_cw(image: Any|list|tuple,) -> None:
    """Rotate image clockwise 90deg."""
    ...
def image_text(text: str,fontSize: int,color: Color|list|tuple,) -> Image:
    """Create an image from text (default font)."""
    ...
def image_text_ex(font: Font|list|tuple,text: str,fontSize: float,spacing: float,tint: Color|list|tuple,) -> Image:
    """Create an image from text (custom sprite font)."""
    ...
def image_to_pot(image: Any|list|tuple,fill: Color|list|tuple,) -> None:
    """Convert image to POT (power-of-two)."""
    ...
def init_audio_device() -> None:
    """Initialize audio device and context."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def init_physics() -> None:
    """Initializes physics values, pointers and creates physics loop thread."""
    ...
def init_window(width: int,height: int,title: str,) -> None:
    """Initialize window and OpenGL context."""
    ...
def is_audio_device_ready() -> bool:
    """Check if audio device has been initialized successfully."""
    ...
def is_audio_stream_playing(stream: AudioStream|list|tuple,) -> bool:
    """Check if audio stream is playing."""
    ...
def is_audio_stream_processed(stream: AudioStream|list|tuple,) -> bool:
    """Check if any audio stream buffers requires refill."""
    ...
def is_audio_stream_valid(stream: AudioStream|list|tuple,) -> bool:
    """Checks if an audio stream is valid (buffers initialized)."""
    ...
def is_cursor_hidden() -> bool:
    """Check if cursor is not visible."""
    ...
def is_cursor_on_screen() -> bool:
    """Check if cursor is on the screen."""
    ...
def is_file_dropped() -> bool:
    """Check if a file has been dropped into window."""
    ...
def is_file_extension(fileName: str,ext: str,) -> bool:
    """Check file extension (including point: .png, .wav)."""
    ...
def is_file_name_valid(fileName: str,) -> bool:
    """Check if fileName is valid for the platform/OS."""
    ...
def is_font_valid(font: Font|list|tuple,) -> bool:
    """Check if a font is valid (font data loaded, WARNING: GPU texture not checked)."""
    ...
def is_gamepad_available(gamepad: int,) -> bool:
    """Check if a gamepad is available."""
    ...
def is_gamepad_button_down(gamepad: int,button: int,) -> bool:
    """Check if a gamepad button is being pressed."""
    ...
def is_gamepad_button_pressed(gamepad: int,button: int,) -> bool:
    """Check if a gamepad button has been pressed once."""
    ...
def is_gamepad_button_released(gamepad: int,button: int,) -> bool:
    """Check if a gamepad button has been released once."""
    ...
def is_gamepad_button_up(gamepad: int,button: int,) -> bool:
    """Check if a gamepad button is NOT being pressed."""
    ...
def is_gesture_detected(gesture: int,) -> bool:
    """Check if a gesture have been detected."""
    ...
def is_image_valid(image: Image|list|tuple,) -> bool:
    """Check if an image is valid (data and parameters)."""
    ...
def is_key_down(key: int,) -> bool:
    """Check if a key is being pressed."""
    ...
def is_key_pressed(key: int,) -> bool:
    """Check if a key has been pressed once."""
    ...
def is_key_pressed_repeat(key: int,) -> bool:
    """Check if a key has been pressed again."""
    ...
def is_key_released(key: int,) -> bool:
    """Check if a key has been released once."""
    ...
def is_key_up(key: int,) -> bool:
    """Check if a key is NOT being pressed."""
    ...
def is_material_valid(material: Material|list|tuple,) -> bool:
    """Check if a material is valid (shader assigned, map textures loaded in GPU)."""
    ...
def is_model_animation_valid(model: Model|list|tuple,anim: ModelAnimation|list|tuple,) -> bool:
    """Check model animation skeleton match."""
    ...
def is_model_valid(model: Model|list|tuple,) -> bool:
    """Check if a model is valid (loaded in GPU, VAO/VBOs)."""
    ...
def is_mouse_button_down(button: int,) -> bool:
    """Check if a mouse button is being pressed."""
    ...
def is_mouse_button_pressed(button: int,) -> bool:
    """Check if a mouse button has been pressed once."""
    ...
def is_mouse_button_released(button: int,) -> bool:
    """Check if a mouse button has been released once."""
    ...
def is_mouse_button_up(button: int,) -> bool:
    """Check if a mouse button is NOT being pressed."""
    ...
def is_music_stream_playing(music: Music|list|tuple,) -> bool:
    """Check if music is playing."""
    ...
def is_music_valid(music: Music|list|tuple,) -> bool:
    """Checks if a music stream is valid (context and buffers initialized)."""
    ...
def is_path_file(path: str,) -> bool:
    """Check if a given path is a file or a directory."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def is_physics_enabled() -> bool:
    """Returns true if physics thread is currently enabled."""
    ...
def is_render_texture_valid(target: RenderTexture|list|tuple,) -> bool:
    """Check if a render texture is valid (loaded in GPU)."""
    ...
def is_shader_valid(shader: Shader|list|tuple,) -> bool:
    """Check if a shader is valid (loaded on GPU)."""
    ...
def is_sound_playing(sound: Sound|list|tuple,) -> bool:
    """Check if a sound is currently playing."""
    ...
def is_sound_valid(sound: Sound|list|tuple,) -> bool:
    """Checks if a sound is valid (data loaded and buffers initialized)."""
    ...
def is_texture_valid(texture: Texture|list|tuple,) -> bool:
    """Check if a texture is valid (loaded in GPU)."""
    ...
def is_wave_valid(wave: Wave|list|tuple,) -> bool:
    """Checks if wave data is valid (data loaded and parameters)."""
    ...
def is_window_focused() -> bool:
    """Check if window is currently focused."""
    ...
def is_window_fullscreen() -> bool:
    """Check if window is currently fullscreen."""
    ...
def is_window_hidden() -> bool:
    """Check if window is currently hidden."""
    ...
def is_window_maximized() -> bool:
    """Check if window is currently maximized."""
    ...
def is_window_minimized() -> bool:
    """Check if window is currently minimized."""
    ...
def is_window_ready() -> bool:
    """Check if window has been initialized successfully."""
    ...
def is_window_resized() -> bool:
    """Check if window has been resized last frame."""
    ...
def is_window_state(flag: int,) -> bool:
    """Check if one specific window flag is enabled."""
    ...
def lerp(start: float,end: float,amount: float,) -> float:
    """."""
    ...
def load_audio_stream(sampleRate: int,sampleSize: int,channels: int,) -> AudioStream:
    """Load audio stream (to stream raw audio pcm data)."""
    ...
def load_automation_event_list(fileName: str,) -> AutomationEventList:
    """Load automation events list from file, NULL for empty list, capacity = MAX_AUTOMATION_EVENTS."""
    ...
def load_codepoints(text: str,count: Any,) -> Any:
    """Load all codepoints from a UTF-8 text string, codepoints count returned by parameter."""
    ...
def load_directory_files(dirPath: str,) -> FilePathList:
    """Load directory filepaths."""
    ...
def load_directory_files_ex(basePath: str,filter: str,scanSubdirs: bool,) -> FilePathList:
    """Load directory filepaths with extension filtering and recursive directory scan. Use 'DIR' in the filter string to include directories in the result."""
    ...
def load_dropped_files() -> FilePathList:
    """Load dropped filepaths."""
    ...
def load_file_data(fileName: str,dataSize: Any,) -> str:
    """Load file data as byte array (read)."""
    ...
def load_file_text(fileName: str,) -> str:
    """Load text data from file (read), returns a '\0' terminated string."""
    ...
def load_font(fileName: str,) -> Font:
    """Load font from file into GPU memory (VRAM)."""
    ...
def load_font_data(fileData: str,dataSize: int,fontSize: int,codepoints: Any,codepointCount: int,type: int,) -> Any:
    """Load font data for further use."""
    ...
def load_font_ex(fileName: str,fontSize: int,codepoints: Any,codepointCount: int,) -> Font:
    """Load font from file with extended parameters, use NULL for codepoints and 0 for codepointCount to load the default character set, font size is provided in pixels height."""
    ...
def load_font_from_image(image: Image|list|tuple,key: Color|list|tuple,firstChar: int,) -> Font:
    """Load font from Image (XNA style)."""
    ...
def load_font_from_memory(fileType: str,fileData: str,dataSize: int,fontSize: int,codepoints: Any,codepointCount: int,) -> Font:
    """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'."""
    ...
def load_image(fileName: str,) -> Image:
    """Load image from file into CPU memory (RAM)."""
    ...
def load_image_anim(fileName: str,frames: Any,) -> Image:
    """Load image sequence from file (frames appended to image.data)."""
    ...
def load_image_anim_from_memory(fileType: str,fileData: str,dataSize: int,frames: Any,) -> Image:
    """Load image sequence from memory buffer."""
    ...
def load_image_colors(image: Image|list|tuple,) -> Any:
    """Load color data from image as a Color array (RGBA - 32bit)."""
    ...
def load_image_from_memory(fileType: str,fileData: str,dataSize: int,) -> Image:
    """Load image from memory buffer, fileType refers to extension: i.e. '.png'."""
    ...
def load_image_from_screen() -> Image:
    """Load image from screen buffer and (screenshot)."""
    ...
def load_image_from_texture(texture: Texture|list|tuple,) -> Image:
    """Load image from GPU texture data."""
    ...
def load_image_palette(image: Image|list|tuple,maxPaletteSize: int,colorCount: Any,) -> Any:
    """Load colors palette from image as a Color array (RGBA - 32bit)."""
    ...
def load_image_raw(fileName: str,width: int,height: int,format: int,headerSize: int,) -> Image:
    """Load image from RAW file data."""
    ...
def load_material_default() -> Material:
    """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)."""
    ...
def load_materials(fileName: str,materialCount: Any,) -> Any:
    """Load materials from model file."""
    ...
def load_model(fileName: str,) -> Model:
    """Load model from files (meshes and materials)."""
    ...
def load_model_animations(fileName: str,animCount: Any,) -> Any:
    """Load model animations from file."""
    ...
def load_model_from_mesh(mesh: Mesh|list|tuple,) -> Model:
    """Load model from generated mesh (default material)."""
    ...
def load_music_stream(fileName: str,) -> Music:
    """Load music stream from file."""
    ...
def load_music_stream_from_memory(fileType: str,data: str,dataSize: int,) -> Music:
    """Load music stream from data."""
    ...
def load_random_sequence(count: int,min_1: int,max_2: int,) -> Any:
    """Load random values sequence, no values repeated."""
    ...
def load_render_texture(width: int,height: int,) -> RenderTexture:
    """Load texture for rendering (framebuffer)."""
    ...
def load_shader(vsFileName: str,fsFileName: str,) -> Shader:
    """Load shader from files and bind default locations."""
    ...
def load_shader_from_memory(vsCode: str,fsCode: str,) -> Shader:
    """Load shader from code strings and bind default locations."""
    ...
def load_sound(fileName: str,) -> Sound:
    """Load sound from file."""
    ...
def load_sound_alias(source: Sound|list|tuple,) -> Sound:
    """Create a new sound that shares the same sample data as the source sound, does not own the sound data."""
    ...
def load_sound_from_wave(wave: Wave|list|tuple,) -> Sound:
    """Load sound from wave data."""
    ...
def load_texture(fileName: str,) -> Texture:
    """Load texture from file into GPU memory (VRAM)."""
    ...
def load_texture_cubemap(image: Image|list|tuple,layout: int,) -> Texture:
    """Load cubemap from image, multiple image cubemap layouts supported."""
    ...
def load_texture_from_image(image: Image|list|tuple,) -> Texture:
    """Load texture from image data."""
    ...
def load_utf8(codepoints: Any,length: int,) -> str:
    """Load UTF-8 text encoded from codepoints array."""
    ...
def load_vr_stereo_config(device: VrDeviceInfo|list|tuple,) -> VrStereoConfig:
    """Load VR stereo config for VR simulator device parameters."""
    ...
def load_wave(fileName: str,) -> Wave:
    """Load wave data from file."""
    ...
def load_wave_from_memory(fileType: str,fileData: str,dataSize: int,) -> Wave:
    """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'."""
    ...
def load_wave_samples(wave: Wave|list|tuple,) -> Any:
    """Load samples data from wave as a 32bit float data array."""
    ...
def make_directory(dirPath: str,) -> int:
    """Create directories (including full path requested), returns 0 on success."""
    ...
def matrix_add(left: Matrix|list|tuple,right: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def matrix_decompose(mat: Matrix|list|tuple,translation: Any|list|tuple,rotation: Any|list|tuple,scale: Any|list|tuple,) -> None:
    """."""
    ...
def matrix_determinant(mat: Matrix|list|tuple,) -> float:
    """."""
    ...
def matrix_frustum(left: float,right: float,bottom: float,top: float,nearPlane: float,farPlane: float,) -> Matrix:
    """."""
    ...
def matrix_identity() -> Matrix:
    """."""
    ...
def matrix_invert(mat: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def matrix_look_at(eye: Vector3|list|tuple,target: Vector3|list|tuple,up: Vector3|list|tuple,) -> Matrix:
    """."""
    ...
def matrix_multiply(left: Matrix|list|tuple,right: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def matrix_ortho(left: float,right: float,bottom: float,top: float,nearPlane: float,farPlane: float,) -> Matrix:
    """."""
    ...
def matrix_perspective(fovY: float,aspect: float,nearPlane: float,farPlane: float,) -> Matrix:
    """."""
    ...
def matrix_rotate(axis: Vector3|list|tuple,angle: float,) -> Matrix:
    """."""
    ...
def matrix_rotate_x(angle: float,) -> Matrix:
    """."""
    ...
def matrix_rotate_xyz(angle: Vector3|list|tuple,) -> Matrix:
    """."""
    ...
def matrix_rotate_y(angle: float,) -> Matrix:
    """."""
    ...
def matrix_rotate_z(angle: float,) -> Matrix:
    """."""
    ...
def matrix_rotate_zyx(angle: Vector3|list|tuple,) -> Matrix:
    """."""
    ...
def matrix_scale(x: float,y: float,z: float,) -> Matrix:
    """."""
    ...
def matrix_subtract(left: Matrix|list|tuple,right: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def matrix_to_float_v(mat: Matrix|list|tuple,) -> float16:
    """."""
    ...
def matrix_trace(mat: Matrix|list|tuple,) -> float:
    """."""
    ...
def matrix_translate(x: float,y: float,z: float,) -> Matrix:
    """."""
    ...
def matrix_transpose(mat: Matrix|list|tuple,) -> Matrix:
    """."""
    ...
def maximize_window() -> None:
    """Set window state: maximized, if resizable."""
    ...
def measure_text(text: str,fontSize: int,) -> int:
    """Measure string width for default font."""
    ...
def measure_text_ex(font: Font|list|tuple,text: str,fontSize: float,spacing: float,) -> Vector2:
    """Measure string size for Font."""
    ...
def mem_alloc(size: int,) -> Any:
    """Internal memory allocator."""
    ...
def mem_free(ptr: Any,) -> None:
    """Internal memory free."""
    ...
def mem_realloc(ptr: Any,size: int,) -> Any:
    """Internal memory reallocator."""
    ...
def minimize_window() -> None:
    """Set window state: minimized, if resizable."""
    ...
def normalize(value: float,start: float,end: float,) -> float:
    """."""
    ...
def open_url(url: str,) -> None:
    """Open URL with default system browser (if available)."""
    ...
def pause_audio_stream(stream: AudioStream|list|tuple,) -> None:
    """Pause audio stream."""
    ...
def pause_music_stream(music: Music|list|tuple,) -> None:
    """Pause music playing."""
    ...
def pause_sound(sound: Sound|list|tuple,) -> None:
    """Pause a sound."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def physics_add_force(body: Any|list|tuple,force: Vector2|list|tuple,) -> None:
    """Adds a force to a physics body."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def physics_add_torque(body: Any|list|tuple,amount: float,) -> None:
    """Adds an angular force to a physics body."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def physics_shatter(body: Any|list|tuple,position: Vector2|list|tuple,force: float,) -> None:
    """Shatters a polygon shape physics body to little physics bodies with explosion force."""
    ...
def play_audio_stream(stream: AudioStream|list|tuple,) -> None:
    """Play audio stream."""
    ...
def play_automation_event(event: AutomationEvent|list|tuple,) -> None:
    """Play a recorded automation event."""
    ...
def play_music_stream(music: Music|list|tuple,) -> None:
    """Start music playing."""
    ...
def play_sound(sound: Sound|list|tuple,) -> None:
    """Play a sound."""
    ...
def poll_input_events() -> None:
    """Register all input events."""
    ...
def quaternion_add(q1: Vector4|list|tuple,q2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def quaternion_add_value(q: Vector4|list|tuple,add: float,) -> Vector4:
    """."""
    ...
def quaternion_cubic_hermite_spline(q1: Vector4|list|tuple,outTangent1: Vector4|list|tuple,q2: Vector4|list|tuple,inTangent2: Vector4|list|tuple,t: float,) -> Vector4:
    """."""
    ...
def quaternion_divide(q1: Vector4|list|tuple,q2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def quaternion_equals(p: Vector4|list|tuple,q: Vector4|list|tuple,) -> int:
    """."""
    ...
def quaternion_from_axis_angle(axis: Vector3|list|tuple,angle: float,) -> Vector4:
    """."""
    ...
def quaternion_from_euler(pitch: float,yaw: float,roll: float,) -> Vector4:
    """."""
    ...
def quaternion_from_matrix(mat: Matrix|list|tuple,) -> Vector4:
    """."""
    ...
def quaternion_from_vector3_to_vector3(from_0: Vector3|list|tuple,to: Vector3|list|tuple,) -> Vector4:
    """."""
    ...
def quaternion_identity() -> Vector4:
    """."""
    ...
def quaternion_invert(q: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def quaternion_length(q: Vector4|list|tuple,) -> float:
    """."""
    ...
def quaternion_lerp(q1: Vector4|list|tuple,q2: Vector4|list|tuple,amount: float,) -> Vector4:
    """."""
    ...
def quaternion_multiply(q1: Vector4|list|tuple,q2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def quaternion_nlerp(q1: Vector4|list|tuple,q2: Vector4|list|tuple,amount: float,) -> Vector4:
    """."""
    ...
def quaternion_normalize(q: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def quaternion_scale(q: Vector4|list|tuple,mul: float,) -> Vector4:
    """."""
    ...
def quaternion_slerp(q1: Vector4|list|tuple,q2: Vector4|list|tuple,amount: float,) -> Vector4:
    """."""
    ...
def quaternion_subtract(q1: Vector4|list|tuple,q2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def quaternion_subtract_value(q: Vector4|list|tuple,sub: float,) -> Vector4:
    """."""
    ...
def quaternion_to_axis_angle(q: Vector4|list|tuple,outAxis: Any|list|tuple,outAngle: Any,) -> None:
    """."""
    ...
def quaternion_to_euler(q: Vector4|list|tuple,) -> Vector3:
    """."""
    ...
def quaternion_to_matrix(q: Vector4|list|tuple,) -> Matrix:
    """."""
    ...
def quaternion_transform(q: Vector4|list|tuple,mat: Matrix|list|tuple,) -> Vector4:
    """."""
    ...
def remap(value: float,inputStart: float,inputEnd: float,outputStart: float,outputEnd: float,) -> float:
    """."""
    ...
def restore_window() -> None:
    """Set window state: not minimized/maximized."""
    ...
def resume_audio_stream(stream: AudioStream|list|tuple,) -> None:
    """Resume audio stream."""
    ...
def resume_music_stream(music: Music|list|tuple,) -> None:
    """Resume playing paused music."""
    ...
def resume_sound(sound: Sound|list|tuple,) -> None:
    """Resume a paused sound."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def run_physics_step() -> None:
    """Run physics step, to be used if PHYSICS_NO_THREADS is set in your main loop."""
    ...
def save_file_data(fileName: str,data: Any,dataSize: int,) -> bool:
    """Save data to file from byte array (write), returns true on success."""
    ...
def save_file_text(fileName: str,text: str,) -> bool:
    """Save text data to file (write), string must be '\0' terminated, returns true on success."""
    ...
def seek_music_stream(music: Music|list|tuple,position: float,) -> None:
    """Seek music to a position (in seconds)."""
    ...
def set_audio_stream_buffer_size_default(size: int,) -> None:
    """Default size for new audio streams."""
    ...
def set_audio_stream_callback(stream: AudioStream|list|tuple,callback: Any,) -> None:
    """Audio thread callback to request new data."""
    ...
def set_audio_stream_pan(stream: AudioStream|list|tuple,pan: float,) -> None:
    """Set pan for audio stream (0.5 is centered)."""
    ...
def set_audio_stream_pitch(stream: AudioStream|list|tuple,pitch: float,) -> None:
    """Set pitch for audio stream (1.0 is base level)."""
    ...
def set_audio_stream_volume(stream: AudioStream|list|tuple,volume: float,) -> None:
    """Set volume for audio stream (1.0 is max level)."""
    ...
def set_automation_event_base_frame(frame: int,) -> None:
    """Set automation event internal base frame to start recording."""
    ...
def set_automation_event_list(list_0: Any|list|tuple,) -> None:
    """Set automation event list to record to."""
    ...
def set_clipboard_text(text: str,) -> None:
    """Set clipboard text content."""
    ...
def set_config_flags(flags: int,) -> None:
    """Setup init configuration flags (view FLAGS)."""
    ...
def set_exit_key(key: int,) -> None:
    """Set a custom key to exit program (default is ESC)."""
    ...
def set_gamepad_mappings(mappings: str,) -> int:
    """Set internal gamepad mappings (SDL_GameControllerDB)."""
    ...
def set_gamepad_vibration(gamepad: int,leftMotor: float,rightMotor: float,duration: float,) -> None:
    """Set gamepad vibration for both motors (duration in seconds)."""
    ...
def set_gestures_enabled(flags: int,) -> None:
    """Enable a set of gestures using flags."""
    ...
def set_load_file_data_callback(callback: str,) -> None:
    """Set custom file binary data loader."""
    ...
def set_load_file_text_callback(callback: str,) -> None:
    """Set custom file text data loader."""
    ...
def set_master_volume(volume: float,) -> None:
    """Set master volume (listener)."""
    ...
def set_material_texture(material: Any|list|tuple,mapType: int,texture: Texture|list|tuple,) -> None:
    """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)."""
    ...
def set_model_mesh_material(model: Any|list|tuple,meshId: int,materialId: int,) -> None:
    """Set material for a mesh."""
    ...
def set_mouse_cursor(cursor: int,) -> None:
    """Set mouse cursor."""
    ...
def set_mouse_offset(offsetX: int,offsetY: int,) -> None:
    """Set mouse offset."""
    ...
def set_mouse_position(x: int,y: int,) -> None:
    """Set mouse position XY."""
    ...
def set_mouse_scale(scaleX: float,scaleY: float,) -> None:
    """Set mouse scaling."""
    ...
def set_music_pan(music: Music|list|tuple,pan: float,) -> None:
    """Set pan for a music (0.5 is center)."""
    ...
def set_music_pitch(music: Music|list|tuple,pitch: float,) -> None:
    """Set pitch for a music (1.0 is base level)."""
    ...
def set_music_volume(music: Music|list|tuple,volume: float,) -> None:
    """Set volume for music (1.0 is max level)."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def set_physics_body_rotation(body: Any|list|tuple,radians: float,) -> None:
    """Sets physics body shape transform based on radians parameter."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def set_physics_gravity(x: float,y: float,) -> None:
    """Sets physics global gravity force."""
    ...
@deprecated("Raylib no longer recommends the use of Physac library")
def set_physics_time_step(delta: float,) -> None:
    """Sets physics fixed time step in milliseconds. 1.666666 by default."""
    ...
def set_pixel_color(dstPtr: Any,color: Color|list|tuple,format: int,) -> None:
    """Set color formatted into destination pixel pointer."""
    ...
def set_random_seed(seed: int,) -> None:
    """Set the seed for the random number generator."""
    ...
def set_save_file_data_callback(callback: str,) -> None:
    """Set custom file binary data saver."""
    ...
def set_save_file_text_callback(callback: str,) -> None:
    """Set custom file text data saver."""
    ...
def set_shader_value(shader: Shader|list|tuple,locIndex: int,value: Any,uniformType: int,) -> None:
    """Set shader uniform value."""
    ...
def set_shader_value_matrix(shader: Shader|list|tuple,locIndex: int,mat: Matrix|list|tuple,) -> None:
    """Set shader uniform value (matrix 4x4)."""
    ...
def set_shader_value_texture(shader: Shader|list|tuple,locIndex: int,texture: Texture|list|tuple,) -> None:
    """Set shader uniform value for texture (sampler2d)."""
    ...
def set_shader_value_v(shader: Shader|list|tuple,locIndex: int,value: Any,uniformType: int,count: int,) -> None:
    """Set shader uniform value vector."""
    ...
def set_shapes_texture(texture: Texture|list|tuple,source: Rectangle|list|tuple,) -> None:
    """Set texture and rectangle to be used on shapes drawing."""
    ...
def set_sound_pan(sound: Sound|list|tuple,pan: float,) -> None:
    """Set pan for a sound (0.5 is center)."""
    ...
def set_sound_pitch(sound: Sound|list|tuple,pitch: float,) -> None:
    """Set pitch for a sound (1.0 is base level)."""
    ...
def set_sound_volume(sound: Sound|list|tuple,volume: float,) -> None:
    """Set volume for a sound (1.0 is max level)."""
    ...
def set_target_fps(fps: int,) -> None:
    """Set target FPS (maximum)."""
    ...
def set_text_line_spacing(spacing: int,) -> None:
    """Set vertical line spacing when drawing with line-breaks."""
    ...
def set_texture_filter(texture: Texture|list|tuple,filter: int,) -> None:
    """Set texture scaling filter mode."""
    ...
def set_texture_wrap(texture: Texture|list|tuple,wrap: int,) -> None:
    """Set texture wrapping mode."""
    ...
def set_trace_log_callback(callback: str,) -> None:
    """Set custom trace log."""
    ...
def set_trace_log_level(logLevel: int,) -> None:
    """Set the current threshold (minimum) log level."""
    ...
def set_window_focused() -> None:
    """Set window focused."""
    ...
def set_window_icon(image: Image|list|tuple,) -> None:
    """Set icon for window (single image, RGBA 32bit)."""
    ...
def set_window_icons(images: Any|list|tuple,count: int,) -> None:
    """Set icon for window (multiple images, RGBA 32bit)."""
    ...
def set_window_max_size(width: int,height: int,) -> None:
    """Set window maximum dimensions (for FLAG_WINDOW_RESIZABLE)."""
    ...
def set_window_min_size(width: int,height: int,) -> None:
    """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)."""
    ...
def set_window_monitor(monitor: int,) -> None:
    """Set monitor for the current window."""
    ...
def set_window_opacity(opacity: float,) -> None:
    """Set window opacity [0.0f..1.0f]."""
    ...
def set_window_position(x: int,y: int,) -> None:
    """Set window position on screen."""
    ...
def set_window_size(width: int,height: int,) -> None:
    """Set window dimensions."""
    ...
def set_window_state(flags: int,) -> None:
    """Set window configuration state using flags."""
    ...
def set_window_title(title: str,) -> None:
    """Set title for window."""
    ...
def show_cursor() -> None:
    """Shows cursor."""
    ...
def start_automation_event_recording() -> None:
    """Start recording automation events (AutomationEventList must be set)."""
    ...
def stop_audio_stream(stream: AudioStream|list|tuple,) -> None:
    """Stop audio stream."""
    ...
def stop_automation_event_recording() -> None:
    """Stop recording automation events."""
    ...
def stop_music_stream(music: Music|list|tuple,) -> None:
    """Stop music playing."""
    ...
def stop_sound(sound: Sound|list|tuple,) -> None:
    """Stop playing a sound."""
    ...
def swap_screen_buffer() -> None:
    """Swap back buffer with front buffer (screen drawing)."""
    ...
def take_screenshot(fileName: str,) -> None:
    """Takes a screenshot of current screen (filename extension defines format)."""
    ...
def text_append(text: str,append: str,position: Any,) -> None:
    """Append text at specific position and move cursor!."""
    ...
def text_copy(dst: str,src: str,) -> int:
    """Copy one string to another, returns bytes copied."""
    ...
def text_find_index(text: str,find: str,) -> int:
    """Find first text occurrence within a string."""
    ...
def text_format(*args) -> str:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def text_insert(text: str,insert: str,position: int,) -> str:
    """Insert text in a position (WARNING: memory must be freed!)."""
    ...
def text_is_equal(text1: str,text2: str,) -> bool:
    """Check if two text string are equal."""
    ...
def text_join(textList: list[str],count: int,delimiter: str,) -> str:
    """Join text strings with delimiter."""
    ...
def text_length(text: str,) -> int:
    """Get text length, checks for '\0' ending."""
    ...
def text_replace(text: str,replace: str,by: str,) -> str:
    """Replace text string (WARNING: memory must be freed!)."""
    ...
def text_split(text: str,delimiter: str,count: Any,) -> list[str]:
    """Split text into multiple strings."""
    ...
def text_subtext(text: str,position: int,length: int,) -> str:
    """Get a piece of a text string."""
    ...
def text_to_camel(text: str,) -> str:
    """Get Camel case notation version of provided string."""
    ...
def text_to_float(text: str,) -> float:
    """Get float value from text (negative values not supported)."""
    ...
def text_to_integer(text: str,) -> int:
    """Get integer value from text (negative values not supported)."""
    ...
def text_to_lower(text: str,) -> str:
    """Get lower case version of provided string."""
    ...
def text_to_pascal(text: str,) -> str:
    """Get Pascal case notation version of provided string."""
    ...
def text_to_snake(text: str,) -> str:
    """Get Snake case notation version of provided string."""
    ...
def text_to_upper(text: str,) -> str:
    """Get upper case version of provided string."""
    ...
def toggle_borderless_windowed() -> None:
    """Toggle window state: borderless windowed, resizes window to match monitor resolution."""
    ...
def toggle_fullscreen() -> None:
    """Toggle window state: fullscreen/windowed, resizes monitor to match window resolution."""
    ...
def trace_log(*args) -> None:
        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""
        ...
def unload_audio_stream(stream: AudioStream|list|tuple,) -> None:
    """Unload audio stream and free memory."""
    ...
def unload_automation_event_list(list_0: AutomationEventList|list|tuple,) -> None:
    """Unload automation events list from file."""
    ...
def unload_codepoints(codepoints: Any,) -> None:
    """Unload codepoints data from memory."""
    ...
def unload_directory_files(files: FilePathList|list|tuple,) -> None:
    """Unload filepaths."""
    ...
def unload_dropped_files(files: FilePathList|list|tuple,) -> None:
    """Unload dropped filepaths."""
    ...
def unload_file_data(data: str,) -> None:
    """Unload file data allocated by LoadFileData()."""
    ...
def unload_file_text(text: str,) -> None:
    """Unload file text data allocated by LoadFileText()."""
    ...
def unload_font(font: Font|list|tuple,) -> None:
    """Unload font from GPU memory (VRAM)."""
    ...
def unload_font_data(glyphs: Any|list|tuple,glyphCount: int,) -> None:
    """Unload font chars info data (RAM)."""
    ...
def unload_image(image: Image|list|tuple,) -> None:
    """Unload image from CPU memory (RAM)."""
    ...
def unload_image_colors(colors: Any|list|tuple,) -> None:
    """Unload color data loaded with LoadImageColors()."""
    ...
def unload_image_palette(colors: Any|list|tuple,) -> None:
    """Unload colors palette loaded with LoadImagePalette()."""
    ...
def unload_material(material: Material|list|tuple,) -> None:
    """Unload material from GPU memory (VRAM)."""
    ...
def unload_mesh(mesh: Mesh|list|tuple,) -> None:
    """Unload mesh data from CPU and GPU."""
    ...
def unload_model(model: Model|list|tuple,) -> None:
    """Unload model (including meshes) from memory (RAM and/or VRAM)."""
    ...
def unload_model_animation(anim: ModelAnimation|list|tuple,) -> None:
    """Unload animation data."""
    ...
def unload_model_animations(animations: Any|list|tuple,animCount: int,) -> None:
    """Unload animation array data."""
    ...
def unload_music_stream(music: Music|list|tuple,) -> None:
    """Unload music stream."""
    ...
def unload_random_sequence(sequence: Any,) -> None:
    """Unload random values sequence."""
    ...
def unload_render_texture(target: RenderTexture|list|tuple,) -> None:
    """Unload render texture from GPU memory (VRAM)."""
    ...
def unload_shader(shader: Shader|list|tuple,) -> None:
    """Unload shader from GPU memory (VRAM)."""
    ...
def unload_sound(sound: Sound|list|tuple,) -> None:
    """Unload sound."""
    ...
def unload_sound_alias(alias: Sound|list|tuple,) -> None:
    """Unload a sound alias (does not deallocate sample data)."""
    ...
def unload_texture(texture: Texture|list|tuple,) -> None:
    """Unload texture from GPU memory (VRAM)."""
    ...
def unload_utf8(text: str,) -> None:
    """Unload UTF-8 text encoded from codepoints array."""
    ...
def unload_vr_stereo_config(config: VrStereoConfig|list|tuple,) -> None:
    """Unload VR stereo config."""
    ...
def unload_wave(wave: Wave|list|tuple,) -> None:
    """Unload wave data."""
    ...
def unload_wave_samples(samples: Any,) -> None:
    """Unload samples data loaded with LoadWaveSamples()."""
    ...
def update_audio_stream(stream: AudioStream|list|tuple,data: Any,frameCount: int,) -> None:
    """Update audio stream buffers with data."""
    ...
def update_camera(camera: Any|list|tuple,mode: int,) -> None:
    """Update camera position for selected mode."""
    ...
def update_camera_pro(camera: Any|list|tuple,movement: Vector3|list|tuple,rotation: Vector3|list|tuple,zoom: float,) -> None:
    """Update camera movement/rotation."""
    ...
def update_mesh_buffer(mesh: Mesh|list|tuple,index: int,data: Any,dataSize: int,offset: int,) -> None:
    """Update mesh vertex data in GPU for a specific buffer index."""
    ...
def update_model_animation(model: Model|list|tuple,anim: ModelAnimation|list|tuple,frame: int,) -> None:
    """Update model animation pose (CPU)."""
    ...
def update_model_animation_bones(model: Model|list|tuple,anim: ModelAnimation|list|tuple,frame: int,) -> None:
    """Update model animation mesh bone matrices (GPU skinning)."""
    ...
def update_music_stream(music: Music|list|tuple,) -> None:
    """Updates buffers for music streaming."""
    ...
def update_sound(sound: Sound|list|tuple,data: Any,sampleCount: int,) -> None:
    """Update sound buffer with new data."""
    ...
def update_texture(texture: Texture|list|tuple,pixels: Any,) -> None:
    """Update GPU texture with new data."""
    ...
def update_texture_rec(texture: Texture|list|tuple,rec: Rectangle|list|tuple,pixels: Any,) -> None:
    """Update GPU texture rectangle with new data."""
    ...
def upload_mesh(mesh: Any|list|tuple,dynamic: bool,) -> None:
    """Upload mesh vertex data in GPU and provide VAO/VBO ids."""
    ...
def vector2_add(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_add_value(v: Vector2|list|tuple,add: float,) -> Vector2:
    """."""
    ...
def vector2_angle(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> float:
    """."""
    ...
def vector2_clamp(v: Vector2|list|tuple,min_1: Vector2|list|tuple,max_2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_clamp_value(v: Vector2|list|tuple,min_1: float,max_2: float,) -> Vector2:
    """."""
    ...
def vector2_distance(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> float:
    """."""
    ...
def vector2_distance_sqr(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> float:
    """."""
    ...
def vector2_divide(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_dot_product(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> float:
    """."""
    ...
def vector2_equals(p: Vector2|list|tuple,q: Vector2|list|tuple,) -> int:
    """."""
    ...
def vector2_invert(v: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_length(v: Vector2|list|tuple,) -> float:
    """."""
    ...
def vector2_length_sqr(v: Vector2|list|tuple,) -> float:
    """."""
    ...
def vector2_lerp(v1: Vector2|list|tuple,v2: Vector2|list|tuple,amount: float,) -> Vector2:
    """."""
    ...
def vector2_line_angle(start: Vector2|list|tuple,end: Vector2|list|tuple,) -> float:
    """."""
    ...
def vector2_max(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_min(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_move_towards(v: Vector2|list|tuple,target: Vector2|list|tuple,maxDistance: float,) -> Vector2:
    """."""
    ...
def vector2_multiply(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_negate(v: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_normalize(v: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_one() -> Vector2:
    """."""
    ...
def vector2_reflect(v: Vector2|list|tuple,normal: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_refract(v: Vector2|list|tuple,n: Vector2|list|tuple,r: float,) -> Vector2:
    """."""
    ...
def vector2_rotate(v: Vector2|list|tuple,angle: float,) -> Vector2:
    """."""
    ...
def vector2_scale(v: Vector2|list|tuple,scale: float,) -> Vector2:
    """."""
    ...
def vector2_subtract(v1: Vector2|list|tuple,v2: Vector2|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_subtract_value(v: Vector2|list|tuple,sub: float,) -> Vector2:
    """."""
    ...
def vector2_transform(v: Vector2|list|tuple,mat: Matrix|list|tuple,) -> Vector2:
    """."""
    ...
def vector2_zero() -> Vector2:
    """."""
    ...
def vector3_add(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_add_value(v: Vector3|list|tuple,add: float,) -> Vector3:
    """."""
    ...
def vector3_angle(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> float:
    """."""
    ...
def vector3_barycenter(p: Vector3|list|tuple,a: Vector3|list|tuple,b: Vector3|list|tuple,c: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_clamp(v: Vector3|list|tuple,min_1: Vector3|list|tuple,max_2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_clamp_value(v: Vector3|list|tuple,min_1: float,max_2: float,) -> Vector3:
    """."""
    ...
def vector3_cross_product(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_cubic_hermite(v1: Vector3|list|tuple,tangent1: Vector3|list|tuple,v2: Vector3|list|tuple,tangent2: Vector3|list|tuple,amount: float,) -> Vector3:
    """."""
    ...
def vector3_distance(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> float:
    """."""
    ...
def vector3_distance_sqr(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> float:
    """."""
    ...
def vector3_divide(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_dot_product(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> float:
    """."""
    ...
def vector3_equals(p: Vector3|list|tuple,q: Vector3|list|tuple,) -> int:
    """."""
    ...
def vector3_invert(v: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_length(v: Vector3|list|tuple,) -> float:
    """."""
    ...
def vector3_length_sqr(v: Vector3|list|tuple,) -> float:
    """."""
    ...
def vector3_lerp(v1: Vector3|list|tuple,v2: Vector3|list|tuple,amount: float,) -> Vector3:
    """."""
    ...
def vector3_max(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_min(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_move_towards(v: Vector3|list|tuple,target: Vector3|list|tuple,maxDistance: float,) -> Vector3:
    """."""
    ...
def vector3_multiply(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_negate(v: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_normalize(v: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_one() -> Vector3:
    """."""
    ...
def vector3_ortho_normalize(v1: Any|list|tuple,v2: Any|list|tuple,) -> None:
    """."""
    ...
def vector3_perpendicular(v: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_project(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_reflect(v: Vector3|list|tuple,normal: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_refract(v: Vector3|list|tuple,n: Vector3|list|tuple,r: float,) -> Vector3:
    """."""
    ...
def vector3_reject(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_rotate_by_axis_angle(v: Vector3|list|tuple,axis: Vector3|list|tuple,angle: float,) -> Vector3:
    """."""
    ...
def vector3_rotate_by_quaternion(v: Vector3|list|tuple,q: Vector4|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_scale(v: Vector3|list|tuple,scalar: float,) -> Vector3:
    """."""
    ...
def vector3_subtract(v1: Vector3|list|tuple,v2: Vector3|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_subtract_value(v: Vector3|list|tuple,sub: float,) -> Vector3:
    """."""
    ...
def vector3_to_float_v(v: Vector3|list|tuple,) -> float3:
    """."""
    ...
def vector3_transform(v: Vector3|list|tuple,mat: Matrix|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_unproject(source: Vector3|list|tuple,projection: Matrix|list|tuple,view: Matrix|list|tuple,) -> Vector3:
    """."""
    ...
def vector3_zero() -> Vector3:
    """."""
    ...
def vector4_add(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def vector4_add_value(v: Vector4|list|tuple,add: float,) -> Vector4:
    """."""
    ...
def vector4_distance(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> float:
    """."""
    ...
def vector4_distance_sqr(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> float:
    """."""
    ...
def vector4_divide(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def vector4_dot_product(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> float:
    """."""
    ...
def vector4_equals(p: Vector4|list|tuple,q: Vector4|list|tuple,) -> int:
    """."""
    ...
def vector4_invert(v: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def vector4_length(v: Vector4|list|tuple,) -> float:
    """."""
    ...
def vector4_length_sqr(v: Vector4|list|tuple,) -> float:
    """."""
    ...
def vector4_lerp(v1: Vector4|list|tuple,v2: Vector4|list|tuple,amount: float,) -> Vector4:
    """."""
    ...
def vector4_max(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def vector4_min(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def vector4_move_towards(v: Vector4|list|tuple,target: Vector4|list|tuple,maxDistance: float,) -> Vector4:
    """."""
    ...
def vector4_multiply(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def vector4_negate(v: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def vector4_normalize(v: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def vector4_one() -> Vector4:
    """."""
    ...
def vector4_scale(v: Vector4|list|tuple,scale: float,) -> Vector4:
    """."""
    ...
def vector4_subtract(v1: Vector4|list|tuple,v2: Vector4|list|tuple,) -> Vector4:
    """."""
    ...
def vector4_subtract_value(v: Vector4|list|tuple,add: float,) -> Vector4:
    """."""
    ...
def vector4_zero() -> Vector4:
    """."""
    ...
def wait_time(seconds: float,) -> None:
    """Wait for some time (halt program execution)."""
    ...
def wave_copy(wave: Wave|list|tuple,) -> Wave:
    """Copy a wave to a new wave."""
    ...
def wave_crop(wave: Any|list|tuple,initFrame: int,finalFrame: int,) -> None:
    """Crop a wave to defined frames range."""
    ...
def wave_format(wave: Any|list|tuple,sampleRate: int,sampleSize: int,channels: int,) -> None:
    """Convert wave data to desired format."""
    ...
def window_should_close() -> bool:
    """Check if application should close (KEY_ESCAPE pressed or windows close icon clicked)."""
    ...
def wrap(value: float,min_1: float,max_2: float,) -> float:
    """."""
    ...
def glfw_create_cursor(image: Any|list|tuple,xhot: int,yhot: int,) -> Any:
    """."""
    ...
def glfw_create_standard_cursor(shape: int,) -> Any:
    """."""
    ...
def glfw_create_window(width: int,height: int,title: str,monitor: Any|list|tuple,share: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_default_window_hints() -> None:
    """."""
    ...
def glfw_destroy_cursor(cursor: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_destroy_window(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_extension_supported(extension: str,) -> int:
    """."""
    ...
def glfw_focus_window(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_get_clipboard_string(window: Any|list|tuple,) -> str:
    """."""
    ...
def glfw_get_current_context() -> Any:
    """."""
    ...
def glfw_get_cursor_pos(window: Any|list|tuple,xpos: Any,ypos: Any,) -> None:
    """."""
    ...
def glfw_get_error(description: list[str],) -> int:
    """."""
    ...
def glfw_get_framebuffer_size(window: Any|list|tuple,width: Any,height: Any,) -> None:
    """."""
    ...
def glfw_get_gamepad_name(jid: int,) -> str:
    """."""
    ...
def glfw_get_gamepad_state(jid: int,state: Any|list|tuple,) -> int:
    """."""
    ...
def glfw_get_gamma_ramp(monitor: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_get_input_mode(window: Any|list|tuple,mode: int,) -> int:
    """."""
    ...
def glfw_get_joystick_axes(jid: int,count: Any,) -> Any:
    """."""
    ...
def glfw_get_joystick_buttons(jid: int,count: Any,) -> str:
    """."""
    ...
def glfw_get_joystick_guid(jid: int,) -> str:
    """."""
    ...
def glfw_get_joystick_hats(jid: int,count: Any,) -> str:
    """."""
    ...
def glfw_get_joystick_name(jid: int,) -> str:
    """."""
    ...
def glfw_get_joystick_user_pointer(jid: int,) -> Any:
    """."""
    ...
def glfw_get_key(window: Any|list|tuple,key: int,) -> int:
    """."""
    ...
def glfw_get_key_name(key: int,scancode: int,) -> str:
    """."""
    ...
def glfw_get_key_scancode(key: int,) -> int:
    """."""
    ...
def glfw_get_monitor_content_scale(monitor: Any|list|tuple,xscale: Any,yscale: Any,) -> None:
    """."""
    ...
def glfw_get_monitor_name(monitor: Any|list|tuple,) -> str:
    """."""
    ...
def glfw_get_monitor_physical_size(monitor: Any|list|tuple,widthMM: Any,heightMM: Any,) -> None:
    """."""
    ...
def glfw_get_monitor_pos(monitor: Any|list|tuple,xpos: Any,ypos: Any,) -> None:
    """."""
    ...
def glfw_get_monitor_user_pointer(monitor: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_get_monitor_workarea(monitor: Any|list|tuple,xpos: Any,ypos: Any,width: Any,height: Any,) -> None:
    """."""
    ...
def glfw_get_monitors(count: Any,) -> Any:
    """."""
    ...
def glfw_get_mouse_button(window: Any|list|tuple,button: int,) -> int:
    """."""
    ...
def glfw_get_platform() -> int:
    """."""
    ...
def glfw_get_primary_monitor() -> Any:
    """."""
    ...
def glfw_get_proc_address(procname: str,) -> Any:
    """."""
    ...
def glfw_get_required_instance_extensions(count: Any,) -> list[str]:
    """."""
    ...
def glfw_get_time() -> float:
    """."""
    ...
def glfw_get_timer_frequency() -> int:
    """."""
    ...
def glfw_get_timer_value() -> int:
    """."""
    ...
def glfw_get_version(major: Any,minor: Any,rev: Any,) -> None:
    """."""
    ...
def glfw_get_version_string() -> str:
    """."""
    ...
def glfw_get_video_mode(monitor: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_get_video_modes(monitor: Any|list|tuple,count: Any,) -> Any:
    """."""
    ...
def glfw_get_window_attrib(window: Any|list|tuple,attrib: int,) -> int:
    """."""
    ...
def glfw_get_window_content_scale(window: Any|list|tuple,xscale: Any,yscale: Any,) -> None:
    """."""
    ...
def glfw_get_window_frame_size(window: Any|list|tuple,left: Any,top: Any,right: Any,bottom: Any,) -> None:
    """."""
    ...
def glfw_get_window_monitor(window: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_get_window_opacity(window: Any|list|tuple,) -> float:
    """."""
    ...
def glfw_get_window_pos(window: Any|list|tuple,xpos: Any,ypos: Any,) -> None:
    """."""
    ...
def glfw_get_window_size(window: Any|list|tuple,width: Any,height: Any,) -> None:
    """."""
    ...
def glfw_get_window_title(window: Any|list|tuple,) -> str:
    """."""
    ...
def glfw_get_window_user_pointer(window: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_hide_window(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_iconify_window(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_init() -> int:
    """."""
    ...
def glfw_init_allocator(allocator: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_init_hint(hint: int,value: int,) -> None:
    """."""
    ...
def glfw_joystick_is_gamepad(jid: int,) -> int:
    """."""
    ...
def glfw_joystick_present(jid: int,) -> int:
    """."""
    ...
def glfw_make_context_current(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_maximize_window(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_platform_supported(platform: int,) -> int:
    """."""
    ...
def glfw_poll_events() -> None:
    """."""
    ...
def glfw_post_empty_event() -> None:
    """."""
    ...
def glfw_raw_mouse_motion_supported() -> int:
    """."""
    ...
def glfw_request_window_attention(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_restore_window(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_set_char_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_char_mods_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_clipboard_string(window: Any|list|tuple,string: str,) -> None:
    """."""
    ...
def glfw_set_cursor(window: Any|list|tuple,cursor: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_set_cursor_enter_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_cursor_pos(window: Any|list|tuple,xpos: float,ypos: float,) -> None:
    """."""
    ...
def glfw_set_cursor_pos_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_drop_callback(window: Any|list|tuple,callback: list[str]|list|tuple,) -> list[str]:
    """."""
    ...
def glfw_set_error_callback(callback: str,) -> str:
    """."""
    ...
def glfw_set_framebuffer_size_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_gamma(monitor: Any|list|tuple,gamma: float,) -> None:
    """."""
    ...
def glfw_set_gamma_ramp(monitor: Any|list|tuple,ramp: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_set_input_mode(window: Any|list|tuple,mode: int,value: int,) -> None:
    """."""
    ...
def glfw_set_joystick_callback(callback: Any,) -> Any:
    """."""
    ...
def glfw_set_joystick_user_pointer(jid: int,pointer: Any,) -> None:
    """."""
    ...
def glfw_set_key_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_monitor_callback(callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_monitor_user_pointer(monitor: Any|list|tuple,pointer: Any,) -> None:
    """."""
    ...
def glfw_set_mouse_button_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_scroll_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_time(time: float,) -> None:
    """."""
    ...
def glfw_set_window_aspect_ratio(window: Any|list|tuple,numer: int,denom: int,) -> None:
    """."""
    ...
def glfw_set_window_attrib(window: Any|list|tuple,attrib: int,value: int,) -> None:
    """."""
    ...
def glfw_set_window_close_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_window_content_scale_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_window_focus_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_window_icon(window: Any|list|tuple,count: int,images: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_set_window_iconify_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_window_maximize_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_window_monitor(window: Any|list|tuple,monitor: Any|list|tuple,xpos: int,ypos: int,width: int,height: int,refreshRate: int,) -> None:
    """."""
    ...
def glfw_set_window_opacity(window: Any|list|tuple,opacity: float,) -> None:
    """."""
    ...
def glfw_set_window_pos(window: Any|list|tuple,xpos: int,ypos: int,) -> None:
    """."""
    ...
def glfw_set_window_pos_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_window_refresh_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_window_should_close(window: Any|list|tuple,value: int,) -> None:
    """."""
    ...
def glfw_set_window_size(window: Any|list|tuple,width: int,height: int,) -> None:
    """."""
    ...
def glfw_set_window_size_callback(window: Any|list|tuple,callback: Any|list|tuple,) -> Any:
    """."""
    ...
def glfw_set_window_size_limits(window: Any|list|tuple,minwidth: int,minheight: int,maxwidth: int,maxheight: int,) -> None:
    """."""
    ...
def glfw_set_window_title(window: Any|list|tuple,title: str,) -> None:
    """."""
    ...
def glfw_set_window_user_pointer(window: Any|list|tuple,pointer: Any,) -> None:
    """."""
    ...
def glfw_show_window(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_swap_buffers(window: Any|list|tuple,) -> None:
    """."""
    ...
def glfw_swap_interval(interval: int,) -> None:
    """."""
    ...
def glfw_terminate() -> None:
    """."""
    ...
def glfw_update_gamepad_mappings(string: str,) -> int:
    """."""
    ...
def glfw_vulkan_supported() -> int:
    """."""
    ...
def glfw_wait_events() -> None:
    """."""
    ...
def glfw_wait_events_timeout(timeout: float,) -> None:
    """."""
    ...
def glfw_window_hint(hint: int,value: int,) -> None:
    """."""
    ...
def glfw_window_hint_string(hint: int,value: str,) -> None:
    """."""
    ...
def glfw_window_should_close(window: Any|list|tuple,) -> int:
    """."""
    ...
def rl_active_draw_buffers(count: int,) -> None:
    """Activate multiple draw color buffers."""
    ...
def rl_active_texture_slot(slot: int,) -> None:
    """Select and active a texture slot."""
    ...
def rl_begin(mode: int,) -> None:
    """Initialize drawing mode (how to organize vertex)."""
    ...
def rl_bind_framebuffer(target: int,framebuffer: int,) -> None:
    """Bind framebuffer (FBO)."""
    ...
def rl_bind_image_texture(id: int,index: int,format: int,readonly: bool,) -> None:
    """Bind image texture."""
    ...
def rl_bind_shader_buffer(id: int,index: int,) -> None:
    """Bind SSBO buffer."""
    ...
def rl_blit_framebuffer(srcX: int,srcY: int,srcWidth: int,srcHeight: int,dstX: int,dstY: int,dstWidth: int,dstHeight: int,bufferMask: int,) -> None:
    """Blit active framebuffer to main framebuffer."""
    ...
def rl_check_errors() -> None:
    """Check and log OpenGL error codes."""
    ...
def rl_check_render_batch_limit(vCount: int,) -> bool:
    """Check internal buffer overflow for a given number of vertex."""
    ...
def rl_clear_color(r: int,g: int,b: int,a: int,) -> None:
    """Clear color buffer with color."""
    ...
def rl_clear_screen_buffers() -> None:
    """Clear used screen buffers (color and depth)."""
    ...
def rl_color3f(x: float,y: float,z: float,) -> None:
    """Define one vertex (color) - 3 float."""
    ...
def rl_color4f(x: float,y: float,z: float,w: float,) -> None:
    """Define one vertex (color) - 4 float."""
    ...
def rl_color4ub(r: int,g: int,b: int,a: int,) -> None:
    """Define one vertex (color) - 4 byte."""
    ...
def rl_color_mask(r: bool,g: bool,b: bool,a: bool,) -> None:
    """Color mask control."""
    ...
def rl_compile_shader(shaderCode: str,type: int,) -> int:
    """Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)."""
    ...
def rl_compute_shader_dispatch(groupX: int,groupY: int,groupZ: int,) -> None:
    """Dispatch compute shader (equivalent to *draw* for graphics pipeline)."""
    ...
def rl_copy_shader_buffer(destId: int,srcId: int,destOffset: int,srcOffset: int,count: int,) -> None:
    """Copy SSBO data between buffers."""
    ...
def rl_cubemap_parameters(id: int,param: int,value: int,) -> None:
    """Set cubemap parameters (filter, wrap)."""
    ...
def rl_disable_backface_culling() -> None:
    """Disable backface culling."""
    ...
def rl_disable_color_blend() -> None:
    """Disable color blending."""
    ...
def rl_disable_depth_mask() -> None:
    """Disable depth write."""
    ...
def rl_disable_depth_test() -> None:
    """Disable depth test."""
    ...
def rl_disable_framebuffer() -> None:
    """Disable render texture (fbo), return to default framebuffer."""
    ...
def rl_disable_scissor_test() -> None:
    """Disable scissor test."""
    ...
def rl_disable_shader() -> None:
    """Disable shader program."""
    ...
def rl_disable_smooth_lines() -> None:
    """Disable line aliasing."""
    ...
def rl_disable_stereo_render() -> None:
    """Disable stereo rendering."""
    ...
def rl_disable_texture() -> None:
    """Disable texture."""
    ...
def rl_disable_texture_cubemap() -> None:
    """Disable texture cubemap."""
    ...
def rl_disable_vertex_array() -> None:
    """Disable vertex array (VAO, if supported)."""
    ...
def rl_disable_vertex_attribute(index: int,) -> None:
    """Disable vertex attribute index."""
    ...
def rl_disable_vertex_buffer() -> None:
    """Disable vertex buffer (VBO)."""
    ...
def rl_disable_vertex_buffer_element() -> None:
    """Disable vertex buffer element (VBO element)."""
    ...
def rl_disable_wire_mode() -> None:
    """Disable wire (and point) mode."""
    ...
def rl_draw_render_batch(batch: Any|list|tuple,) -> None:
    """Draw render batch data (Update->Draw->Reset)."""
    ...
def rl_draw_render_batch_active() -> None:
    """Update and draw internal render batch."""
    ...
def rl_draw_vertex_array(offset: int,count: int,) -> None:
    """Draw vertex array (currently active vao)."""
    ...
def rl_draw_vertex_array_elements(offset: int,count: int,buffer: Any,) -> None:
    """Draw vertex array elements."""
    ...
def rl_draw_vertex_array_elements_instanced(offset: int,count: int,buffer: Any,instances: int,) -> None:
    """Draw vertex array elements with instancing."""
    ...
def rl_draw_vertex_array_instanced(offset: int,count: int,instances: int,) -> None:
    """Draw vertex array (currently active vao) with instancing."""
    ...
def rl_enable_backface_culling() -> None:
    """Enable backface culling."""
    ...
def rl_enable_color_blend() -> None:
    """Enable color blending."""
    ...
def rl_enable_depth_mask() -> None:
    """Enable depth write."""
    ...
def rl_enable_depth_test() -> None:
    """Enable depth test."""
    ...
def rl_enable_framebuffer(id: int,) -> None:
    """Enable render texture (fbo)."""
    ...
def rl_enable_point_mode() -> None:
    """Enable point mode."""
    ...
def rl_enable_scissor_test() -> None:
    """Enable scissor test."""
    ...
def rl_enable_shader(id: int,) -> None:
    """Enable shader program."""
    ...
def rl_enable_smooth_lines() -> None:
    """Enable line aliasing."""
    ...
def rl_enable_stereo_render() -> None:
    """Enable stereo rendering."""
    ...
def rl_enable_texture(id: int,) -> None:
    """Enable texture."""
    ...
def rl_enable_texture_cubemap(id: int,) -> None:
    """Enable texture cubemap."""
    ...
def rl_enable_vertex_array(vaoId: int,) -> bool:
    """Enable vertex array (VAO, if supported)."""
    ...
def rl_enable_vertex_attribute(index: int,) -> None:
    """Enable vertex attribute index."""
    ...
def rl_enable_vertex_buffer(id: int,) -> None:
    """Enable vertex buffer (VBO)."""
    ...
def rl_enable_vertex_buffer_element(id: int,) -> None:
    """Enable vertex buffer element (VBO element)."""
    ...
def rl_enable_wire_mode() -> None:
    """Enable wire mode."""
    ...
def rl_end() -> None:
    """Finish vertex providing."""
    ...
def rl_framebuffer_attach(fboId: int,texId: int,attachType: int,texType: int,mipLevel: int,) -> None:
    """Attach texture/renderbuffer to a framebuffer."""
    ...
def rl_framebuffer_complete(id: int,) -> bool:
    """Verify framebuffer is complete."""
    ...
def rl_frustum(left: float,right: float,bottom: float,top: float,znear: float,zfar: float,) -> None:
    """."""
    ...
def rl_gen_texture_mipmaps(id: int,width: int,height: int,format: int,mipmaps: Any,) -> None:
    """Generate mipmap data for selected texture."""
    ...
def rl_get_active_framebuffer() -> int:
    """Get the currently active render texture (fbo), 0 for default framebuffer."""
    ...
def rl_get_cull_distance_far() -> float:
    """Get cull plane distance far."""
    ...
def rl_get_cull_distance_near() -> float:
    """Get cull plane distance near."""
    ...
def rl_get_framebuffer_height() -> int:
    """Get default framebuffer height."""
    ...
def rl_get_framebuffer_width() -> int:
    """Get default framebuffer width."""
    ...
def rl_get_gl_texture_formats(format: int,glInternalFormat: Any,glFormat: Any,glType: Any,) -> None:
    """Get OpenGL internal formats."""
    ...
def rl_get_line_width() -> float:
    """Get the line drawing width."""
    ...
def rl_get_location_attrib(shaderId: int,attribName: str,) -> int:
    """Get shader location attribute."""
    ...
def rl_get_location_uniform(shaderId: int,uniformName: str,) -> int:
    """Get shader location uniform."""
    ...
def rl_get_matrix_modelview() -> Matrix:
    """Get internal modelview matrix."""
    ...
def rl_get_matrix_projection() -> Matrix:
    """Get internal projection matrix."""
    ...
def rl_get_matrix_projection_stereo(eye: int,) -> Matrix:
    """Get internal projection matrix for stereo render (selected eye)."""
    ...
def rl_get_matrix_transform() -> Matrix:
    """Get internal accumulated transform matrix."""
    ...
def rl_get_matrix_view_offset_stereo(eye: int,) -> Matrix:
    """Get internal view offset matrix for stereo render (selected eye)."""
    ...
def rl_get_pixel_format_name(format: int,) -> str:
    """Get name string for pixel format."""
    ...
def rl_get_shader_buffer_size(id: int,) -> int:
    """Get SSBO buffer size."""
    ...
def rl_get_shader_id_default() -> int:
    """Get default shader id."""
    ...
def rl_get_shader_locs_default() -> Any:
    """Get default shader locations."""
    ...
def rl_get_texture_id_default() -> int:
    """Get default texture id."""
    ...
def rl_get_version() -> int:
    """Get current OpenGL version."""
    ...
def rl_is_stereo_render_enabled() -> bool:
    """Check if stereo render is enabled."""
    ...
def rl_load_compute_shader_program(shaderId: int,) -> int:
    """Load compute shader program."""
    ...
def rl_load_draw_cube() -> None:
    """Load and draw a cube."""
    ...
def rl_load_draw_quad() -> None:
    """Load and draw a quad."""
    ...
def rl_load_extensions(loader: Any,) -> None:
    """Load OpenGL extensions (loader function required)."""
    ...
def rl_load_framebuffer() -> int:
    """Load an empty framebuffer."""
    ...
def rl_load_identity() -> None:
    """Reset current matrix to identity matrix."""
    ...
def rl_load_render_batch(numBuffers: int,bufferElements: int,) -> rlRenderBatch:
    """Load a render batch system."""
    ...
def rl_load_shader_buffer(size: int,data: Any,usageHint: int,) -> int:
    """Load shader storage buffer object (SSBO)."""
    ...
def rl_load_shader_code(vsCode: str,fsCode: str,) -> int:
    """Load shader from code strings."""
    ...
def rl_load_shader_program(vShaderId: int,fShaderId: int,) -> int:
    """Load custom shader program."""
    ...
def rl_load_texture(data: Any,width: int,height: int,format: int,mipmapCount: int,) -> int:
    """Load texture data."""
    ...
def rl_load_texture_cubemap(data: Any,size: int,format: int,mipmapCount: int,) -> int:
    """Load texture cubemap data."""
    ...
def rl_load_texture_depth(width: int,height: int,useRenderBuffer: bool,) -> int:
    """Load depth texture/renderbuffer (to be attached to fbo)."""
    ...
def rl_load_vertex_array() -> int:
    """Load vertex array (vao) if supported."""
    ...
def rl_load_vertex_buffer(buffer: Any,size: int,dynamic: bool,) -> int:
    """Load a vertex buffer object."""
    ...
def rl_load_vertex_buffer_element(buffer: Any,size: int,dynamic: bool,) -> int:
    """Load vertex buffer elements object."""
    ...
def rl_matrix_mode(mode: int,) -> None:
    """Choose the current matrix to be transformed."""
    ...
def rl_mult_matrixf(matf: Any,) -> None:
    """Multiply the current matrix by another matrix."""
    ...
def rl_normal3f(x: float,y: float,z: float,) -> None:
    """Define one vertex (normal) - 3 float."""
    ...
def rl_ortho(left: float,right: float,bottom: float,top: float,znear: float,zfar: float,) -> None:
    """."""
    ...
def rl_pop_matrix() -> None:
    """Pop latest inserted matrix from stack."""
    ...
def rl_push_matrix() -> None:
    """Push the current matrix to stack."""
    ...
def rl_read_screen_pixels(width: int,height: int,) -> str:
    """Read screen pixel data (color buffer)."""
    ...
def rl_read_shader_buffer(id: int,dest: Any,count: int,offset: int,) -> None:
    """Read SSBO buffer data (GPU->CPU)."""
    ...
def rl_read_texture_pixels(id: int,width: int,height: int,format: int,) -> Any:
    """Read texture pixel data."""
    ...
def rl_rotatef(angle: float,x: float,y: float,z: float,) -> None:
    """Multiply the current matrix by a rotation matrix."""
    ...
def rl_scalef(x: float,y: float,z: float,) -> None:
    """Multiply the current matrix by a scaling matrix."""
    ...
def rl_scissor(x: int,y: int,width: int,height: int,) -> None:
    """Scissor test."""
    ...
def rl_set_blend_factors(glSrcFactor: int,glDstFactor: int,glEquation: int,) -> None:
    """Set blending mode factor and equation (using OpenGL factors)."""
    ...
def rl_set_blend_factors_separate(glSrcRGB: int,glDstRGB: int,glSrcAlpha: int,glDstAlpha: int,glEqRGB: int,glEqAlpha: int,) -> None:
    """Set blending mode factors and equations separately (using OpenGL factors)."""
    ...
def rl_set_blend_mode(mode: int,) -> None:
    """Set blending mode."""
    ...
def rl_set_clip_planes(nearPlane: float,farPlane: float,) -> None:
    """Set clip planes distances."""
    ...
def rl_set_cull_face(mode: int,) -> None:
    """Set face culling mode."""
    ...
def rl_set_framebuffer_height(height: int,) -> None:
    """Set current framebuffer height."""
    ...
def rl_set_framebuffer_width(width: int,) -> None:
    """Set current framebuffer width."""
    ...
def rl_set_line_width(width: float,) -> None:
    """Set the line drawing width."""
    ...
def rl_set_matrix_modelview(view: Matrix|list|tuple,) -> None:
    """Set a custom modelview matrix (replaces internal modelview matrix)."""
    ...
def rl_set_matrix_projection(proj: Matrix|list|tuple,) -> None:
    """Set a custom projection matrix (replaces internal projection matrix)."""
    ...
def rl_set_matrix_projection_stereo(right: Matrix|list|tuple,left: Matrix|list|tuple,) -> None:
    """Set eyes projection matrices for stereo rendering."""
    ...
def rl_set_matrix_view_offset_stereo(right: Matrix|list|tuple,left: Matrix|list|tuple,) -> None:
    """Set eyes view offsets matrices for stereo rendering."""
    ...
def rl_set_render_batch_active(batch: Any|list|tuple,) -> None:
    """Set the active render batch for rlgl (NULL for default internal)."""
    ...
def rl_set_shader(id: int,locs: Any,) -> None:
    """Set shader currently active (id and locations)."""
    ...
def rl_set_texture(id: int,) -> None:
    """Set current texture for render batch and check buffers limits."""
    ...
def rl_set_uniform(locIndex: int,value: Any,uniformType: int,count: int,) -> None:
    """Set shader value uniform."""
    ...
def rl_set_uniform_matrices(locIndex: int,mat: Any|list|tuple,count: int,) -> None:
    """Set shader value matrices."""
    ...
def rl_set_uniform_matrix(locIndex: int,mat: Matrix|list|tuple,) -> None:
    """Set shader value matrix."""
    ...
def rl_set_uniform_sampler(locIndex: int,textureId: int,) -> None:
    """Set shader value sampler."""
    ...
def rl_set_vertex_attribute(index: int,compSize: int,type: int,normalized: bool,stride: int,offset: int,) -> None:
    """Set vertex attribute data configuration."""
    ...
def rl_set_vertex_attribute_default(locIndex: int,value: Any,attribType: int,count: int,) -> None:
    """Set vertex attribute default value, when attribute to provided."""
    ...
def rl_set_vertex_attribute_divisor(index: int,divisor: int,) -> None:
    """Set vertex attribute data divisor."""
    ...
def rl_tex_coord2f(x: float,y: float,) -> None:
    """Define one vertex (texture coordinate) - 2 float."""
    ...
def rl_texture_parameters(id: int,param: int,value: int,) -> None:
    """Set texture parameters (filter, wrap)."""
    ...
def rl_translatef(x: float,y: float,z: float,) -> None:
    """Multiply the current matrix by a translation matrix."""
    ...
def rl_unload_framebuffer(id: int,) -> None:
    """Delete framebuffer from GPU."""
    ...
def rl_unload_render_batch(batch: rlRenderBatch|list|tuple,) -> None:
    """Unload render batch system."""
    ...
def rl_unload_shader_buffer(ssboId: int,) -> None:
    """Unload shader storage buffer object (SSBO)."""
    ...
def rl_unload_shader_program(id: int,) -> None:
    """Unload shader program."""
    ...
def rl_unload_texture(id: int,) -> None:
    """Unload texture from GPU memory."""
    ...
def rl_unload_vertex_array(vaoId: int,) -> None:
    """Unload vertex array (vao)."""
    ...
def rl_unload_vertex_buffer(vboId: int,) -> None:
    """Unload vertex buffer object."""
    ...
def rl_update_shader_buffer(id: int,data: Any,dataSize: int,offset: int,) -> None:
    """Update SSBO buffer data."""
    ...
def rl_update_texture(id: int,offsetX: int,offsetY: int,width: int,height: int,format: int,data: Any,) -> None:
    """Update texture with new data on GPU."""
    ...
def rl_update_vertex_buffer(bufferId: int,data: Any,dataSize: int,offset: int,) -> None:
    """Update vertex buffer object data on GPU buffer."""
    ...
def rl_update_vertex_buffer_elements(id: int,data: Any,dataSize: int,offset: int,) -> None:
    """Update vertex buffer elements data on GPU buffer."""
    ...
def rl_vertex2f(x: float,y: float,) -> None:
    """Define one vertex (position) - 2 float."""
    ...
def rl_vertex2i(x: int,y: int,) -> None:
    """Define one vertex (position) - 2 int."""
    ...
def rl_vertex3f(x: float,y: float,z: float,) -> None:
    """Define one vertex (position) - 3 float."""
    ...
def rl_viewport(x: int,y: int,width: int,height: int,) -> None:
    """Set the viewport area."""
    ...
def rlgl_close() -> None:
    """De-initialize rlgl (buffers, shaders, textures)."""
    ...
def rlgl_init(width: int,height: int,) -> None:
    """Initialize rlgl (buffers, shaders, textures, states)."""
    ...
class AudioStream:
    """AudioStream, custom audio stream."""
    def __init__(self, buffer: Any|None = None, processor: Any|None = None, sampleRate: int|None = None, sampleSize: int|None = None, channels: int|None = None):
        self.buffer:Any = buffer # type: ignore
        self.processor:Any = processor # type: ignore
        self.sampleRate:int = sampleRate # type: ignore
        self.sampleSize:int = sampleSize # type: ignore
        self.channels:int = channels # type: ignore
class AutomationEvent:
    """Automation event."""
    def __init__(self, frame: int|None = None, type: int|None = None, params: list|None = None):
        self.frame:int = frame # type: ignore
        self.type:int = type # type: ignore
        self.params:list = params # type: ignore
class AutomationEventList:
    """Automation event list."""
    def __init__(self, capacity: int|None = None, count: int|None = None, events: Any|None = None):
        self.capacity:int = capacity # type: ignore
        self.count:int = count # type: ignore
        self.events:Any = events # type: ignore
class BoneInfo:
    """Bone, skeletal animation bone."""
    def __init__(self, name: list|None = None, parent: int|None = None):
        self.name:list = name # type: ignore
        self.parent:int = parent # type: ignore
class BoundingBox:
    """BoundingBox."""
    def __init__(self, min: Vector3|list|tuple|None = None, max: Vector3|list|tuple|None = None):
        self.min:Vector3 = min # type: ignore
        self.max:Vector3 = max # type: ignore
class Camera2D:
    """Camera2D, defines position/orientation in 2d space."""
    def __init__(self, offset: Vector2|list|tuple|None = None, target: Vector2|list|tuple|None = None, rotation: float|None = None, zoom: float|None = None):
        self.offset:Vector2 = offset # type: ignore
        self.target:Vector2 = target # type: ignore
        self.rotation:float = rotation # type: ignore
        self.zoom:float = zoom # type: ignore
class Camera3D:
    """Camera, defines position/orientation in 3d space."""
    def __init__(self, position: Vector3|list|tuple|None = None, target: Vector3|list|tuple|None = None, up: Vector3|list|tuple|None = None, fovy: float|None = None, projection: int|None = None):
        self.position:Vector3 = position # type: ignore
        self.target:Vector3 = target # type: ignore
        self.up:Vector3 = up # type: ignore
        self.fovy:float = fovy # type: ignore
        self.projection:int = projection # type: ignore
class Color:
    """Color, 4 components, R8G8B8A8 (32bit)."""
    def __init__(self, r: int|None = None, g: int|None = None, b: int|None = None, a: int|None = None):
        self.r:int = r # type: ignore
        self.g:int = g # type: ignore
        self.b:int = b # type: ignore
        self.a:int = a # type: ignore
class FilePathList:
    """File path list."""
    def __init__(self, capacity: int|None = None, count: int|None = None, paths: list[str]|None = None):
        self.capacity:int = capacity # type: ignore
        self.count:int = count # type: ignore
        self.paths:list[str] = paths # type: ignore
class Font:
    """Font, font texture and GlyphInfo array data."""
    def __init__(self, baseSize: int|None = None, glyphCount: int|None = None, glyphPadding: int|None = None, texture: Texture|list|tuple|None = None, recs: Any|None = None, glyphs: Any|None = None):
        self.baseSize:int = baseSize # type: ignore
        self.glyphCount:int = glyphCount # type: ignore
        self.glyphPadding:int = glyphPadding # type: ignore
        self.texture:Texture = texture # type: ignore
        self.recs:Any = recs # type: ignore
        self.glyphs:Any = glyphs # type: ignore
class GlyphInfo:
    """GlyphInfo, font characters glyphs info."""
    def __init__(self, value: int|None = None, offsetX: int|None = None, offsetY: int|None = None, advanceX: int|None = None, image: Image|list|tuple|None = None):
        self.value:int = value # type: ignore
        self.offsetX:int = offsetX # type: ignore
        self.offsetY:int = offsetY # type: ignore
        self.advanceX:int = advanceX # type: ignore
        self.image:Image = image # type: ignore
class GuiStyleProp:
    """NOTE: Used when exporting style as code for convenience."""
    def __init__(self, controlId: int|None = None, propertyId: int|None = None, propertyValue: int|None = None):
        self.controlId:int = controlId # type: ignore
        self.propertyId:int = propertyId # type: ignore
        self.propertyValue:int = propertyValue # type: ignore
class Image:
    """Image, pixel data stored in CPU memory (RAM)."""
    def __init__(self, data: Any|None = None, width: int|None = None, height: int|None = None, mipmaps: int|None = None, format: int|None = None):
        self.data:Any = data # type: ignore
        self.width:int = width # type: ignore
        self.height:int = height # type: ignore
        self.mipmaps:int = mipmaps # type: ignore
        self.format:int = format # type: ignore
class Mat2:
    """Mat2 type (used for polygon shape rotation matrix)."""
    def __init__(self, m00: float|None = None, m01: float|None = None, m10: float|None = None, m11: float|None = None):
        self.m00:float = m00 # type: ignore
        self.m01:float = m01 # type: ignore
        self.m10:float = m10 # type: ignore
        self.m11:float = m11 # type: ignore
class Material:
    """Material, includes shader and maps."""
    def __init__(self, shader: Shader|list|tuple|None = None, maps: Any|None = None, params: list|None = None):
        self.shader:Shader = shader # type: ignore
        self.maps:Any = maps # type: ignore
        self.params:list = params # type: ignore
class MaterialMap:
    """MaterialMap."""
    def __init__(self, texture: Texture|list|tuple|None = None, color: Color|list|tuple|None = None, value: float|None = None):
        self.texture:Texture = texture # type: ignore
        self.color:Color = color # type: ignore
        self.value:float = value # type: ignore
class Matrix:
    """Matrix, 4x4 components, column major, OpenGL style, right-handed."""
    def __init__(self, m0: float|None = None, m4: float|None = None, m8: float|None = None, m12: float|None = None, m1: float|None = None, m5: float|None = None, m9: float|None = None, m13: float|None = None, m2: float|None = None, m6: float|None = None, m10: float|None = None, m14: float|None = None, m3: float|None = None, m7: float|None = None, m11: float|None = None, m15: float|None = None):
        self.m0:float = m0 # type: ignore
        self.m4:float = m4 # type: ignore
        self.m8:float = m8 # type: ignore
        self.m12:float = m12 # type: ignore
        self.m1:float = m1 # type: ignore
        self.m5:float = m5 # type: ignore
        self.m9:float = m9 # type: ignore
        self.m13:float = m13 # type: ignore
        self.m2:float = m2 # type: ignore
        self.m6:float = m6 # type: ignore
        self.m10:float = m10 # type: ignore
        self.m14:float = m14 # type: ignore
        self.m3:float = m3 # type: ignore
        self.m7:float = m7 # type: ignore
        self.m11:float = m11 # type: ignore
        self.m15:float = m15 # type: ignore
class Mesh:
    """Mesh, vertex data and vao/vbo."""
    def __init__(self, vertexCount: int|None = None, triangleCount: int|None = None, vertices: Any|None = None, texcoords: Any|None = None, texcoords2: Any|None = None, normals: Any|None = None, tangents: Any|None = None, colors: str|None = None, indices: Any|None = None, animVertices: Any|None = None, animNormals: Any|None = None, boneIds: str|None = None, boneWeights: Any|None = None, boneMatrices: Any|None = None, boneCount: int|None = None, vaoId: int|None = None, vboId: Any|None = None):
        self.vertexCount:int = vertexCount # type: ignore
        self.triangleCount:int = triangleCount # type: ignore
        self.vertices:Any = vertices # type: ignore
        self.texcoords:Any = texcoords # type: ignore
        self.texcoords2:Any = texcoords2 # type: ignore
        self.normals:Any = normals # type: ignore
        self.tangents:Any = tangents # type: ignore
        self.colors:str = colors # type: ignore
        self.indices:Any = indices # type: ignore
        self.animVertices:Any = animVertices # type: ignore
        self.animNormals:Any = animNormals # type: ignore
        self.boneIds:str = boneIds # type: ignore
        self.boneWeights:Any = boneWeights # type: ignore
        self.boneMatrices:Any = boneMatrices # type: ignore
        self.boneCount:int = boneCount # type: ignore
        self.vaoId:int = vaoId # type: ignore
        self.vboId:Any = vboId # type: ignore
class Model:
    """Model, meshes, materials and animation data."""
    def __init__(self, transform: Matrix|list|tuple|None = None, meshCount: int|None = None, materialCount: int|None = None, meshes: Any|None = None, materials: Any|None = None, meshMaterial: Any|None = None, boneCount: int|None = None, bones: Any|None = None, bindPose: Any|None = None):
        self.transform:Matrix = transform # type: ignore
        self.meshCount:int = meshCount # type: ignore
        self.materialCount:int = materialCount # type: ignore
        self.meshes:Any = meshes # type: ignore
        self.materials:Any = materials # type: ignore
        self.meshMaterial:Any = meshMaterial # type: ignore
        self.boneCount:int = boneCount # type: ignore
        self.bones:Any = bones # type: ignore
        self.bindPose:Any = bindPose # type: ignore
class ModelAnimation:
    """ModelAnimation."""
    def __init__(self, boneCount: int|None = None, frameCount: int|None = None, bones: Any|None = None, framePoses: Any|None = None, name: list|None = None):
        self.boneCount:int = boneCount # type: ignore
        self.frameCount:int = frameCount # type: ignore
        self.bones:Any = bones # type: ignore
        self.framePoses:Any = framePoses # type: ignore
        self.name:list = name # type: ignore
class Music:
    """Music, audio stream, anything longer than ~10 seconds should be streamed."""
    def __init__(self, stream: AudioStream|list|tuple|None = None, frameCount: int|None = None, looping: bool|None = None, ctxType: int|None = None, ctxData: Any|None = None):
        self.stream:AudioStream = stream # type: ignore
        self.frameCount:int = frameCount # type: ignore
        self.looping:bool = looping # type: ignore
        self.ctxType:int = ctxType # type: ignore
        self.ctxData:Any = ctxData # type: ignore
class NPatchInfo:
    """NPatchInfo, n-patch layout info."""
    def __init__(self, source: Rectangle|list|tuple|None = None, left: int|None = None, top: int|None = None, right: int|None = None, bottom: int|None = None, layout: int|None = None):
        self.source:Rectangle = source # type: ignore
        self.left:int = left # type: ignore
        self.top:int = top # type: ignore
        self.right:int = right # type: ignore
        self.bottom:int = bottom # type: ignore
        self.layout:int = layout # type: ignore
class PhysicsBodyData:
    """."""
    def __init__(self, id: int|None = None, enabled: bool|None = None, position: Vector2|list|tuple|None = None, velocity: Vector2|list|tuple|None = None, force: Vector2|list|tuple|None = None, angularVelocity: float|None = None, torque: float|None = None, orient: float|None = None, inertia: float|None = None, inverseInertia: float|None = None, mass: float|None = None, inverseMass: float|None = None, staticFriction: float|None = None, dynamicFriction: float|None = None, restitution: float|None = None, useGravity: bool|None = None, isGrounded: bool|None = None, freezeOrient: bool|None = None, shape: PhysicsShape|list|tuple|None = None):
        self.id:int = id # type: ignore
        self.enabled:bool = enabled # type: ignore
        self.position:Vector2 = position # type: ignore
        self.velocity:Vector2 = velocity # type: ignore
        self.force:Vector2 = force # type: ignore
        self.angularVelocity:float = angularVelocity # type: ignore
        self.torque:float = torque # type: ignore
        self.orient:float = orient # type: ignore
        self.inertia:float = inertia # type: ignore
        self.inverseInertia:float = inverseInertia # type: ignore
        self.mass:float = mass # type: ignore
        self.inverseMass:float = inverseMass # type: ignore
        self.staticFriction:float = staticFriction # type: ignore
        self.dynamicFriction:float = dynamicFriction # type: ignore
        self.restitution:float = restitution # type: ignore
        self.useGravity:bool = useGravity # type: ignore
        self.isGrounded:bool = isGrounded # type: ignore
        self.freezeOrient:bool = freezeOrient # type: ignore
        self.shape:PhysicsShape = shape # type: ignore
class PhysicsManifoldData:
    """."""
    def __init__(self, id: int|None = None, bodyA: Any|None = None, bodyB: Any|None = None, penetration: float|None = None, normal: Vector2|list|tuple|None = None, contacts: list|None = None, contactsCount: int|None = None, restitution: float|None = None, dynamicFriction: float|None = None, staticFriction: float|None = None):
        self.id:int = id # type: ignore
        self.bodyA:Any = bodyA # type: ignore
        self.bodyB:Any = bodyB # type: ignore
        self.penetration:float = penetration # type: ignore
        self.normal:Vector2 = normal # type: ignore
        self.contacts:list = contacts # type: ignore
        self.contactsCount:int = contactsCount # type: ignore
        self.restitution:float = restitution # type: ignore
        self.dynamicFriction:float = dynamicFriction # type: ignore
        self.staticFriction:float = staticFriction # type: ignore
class PhysicsShape:
    """."""
    def __init__(self, type: PhysicsShapeType|None = None, body: Any|None = None, radius: float|None = None, transform: Mat2|list|tuple|None = None, vertexData: PolygonData|list|tuple|None = None):
        self.type:PhysicsShapeType = type # type: ignore
        self.body:Any = body # type: ignore
        self.radius:float = radius # type: ignore
        self.transform:Mat2 = transform # type: ignore
        self.vertexData:PolygonData = vertexData # type: ignore
class PolygonData:
    """."""
    def __init__(self, vertexCount: int|None = None, positions: list|None = None, normals: list|None = None):
        self.vertexCount:int = vertexCount # type: ignore
        self.positions:list = positions # type: ignore
        self.normals:list = normals # type: ignore
class Ray:
    """Ray, ray for raycasting."""
    def __init__(self, position: Vector3|list|tuple|None = None, direction: Vector3|list|tuple|None = None):
        self.position:Vector3 = position # type: ignore
        self.direction:Vector3 = direction # type: ignore
class RayCollision:
    """RayCollision, ray hit information."""
    def __init__(self, hit: bool|None = None, distance: float|None = None, point: Vector3|list|tuple|None = None, normal: Vector3|list|tuple|None = None):
        self.hit:bool = hit # type: ignore
        self.distance:float = distance # type: ignore
        self.point:Vector3 = point # type: ignore
        self.normal:Vector3 = normal # type: ignore
class Rectangle:
    """Rectangle, 4 components."""
    def __init__(self, x: float|None = None, y: float|None = None, width: float|None = None, height: float|None = None):
        self.x:float = x # type: ignore
        self.y:float = y # type: ignore
        self.width:float = width # type: ignore
        self.height:float = height # type: ignore
class RenderTexture:
    """RenderTexture, fbo for texture rendering."""
    def __init__(self, id: int|None = None, texture: Texture|list|tuple|None = None, depth: Texture|list|tuple|None = None):
        self.id:int = id # type: ignore
        self.texture:Texture = texture # type: ignore
        self.depth:Texture = depth # type: ignore
class Shader:
    """Shader."""
    def __init__(self, id: int|None = None, locs: Any|None = None):
        self.id:int = id # type: ignore
        self.locs:Any = locs # type: ignore
class Sound:
    """Sound."""
    def __init__(self, stream: AudioStream|list|tuple|None = None, frameCount: int|None = None):
        self.stream:AudioStream = stream # type: ignore
        self.frameCount:int = frameCount # type: ignore
class Texture:
    """Texture, tex data stored in GPU memory (VRAM)."""
    def __init__(self, id: int|None = None, width: int|None = None, height: int|None = None, mipmaps: int|None = None, format: int|None = None):
        self.id:int = id # type: ignore
        self.width:int = width # type: ignore
        self.height:int = height # type: ignore
        self.mipmaps:int = mipmaps # type: ignore
        self.format:int = format # type: ignore
class Texture2D:
    """It should be redesigned to be provided by user."""
    def __init__(self, id: int|None = None, width: int|None = None, height: int|None = None, mipmaps: int|None = None, format: int|None = None):
        self.id:int = id # type: ignore
        self.width:int = width # type: ignore
        self.height:int = height # type: ignore
        self.mipmaps:int = mipmaps # type: ignore
        self.format:int = format # type: ignore
class Transform:
    """Transform, vertex transformation data."""
    def __init__(self, translation: Vector3|list|tuple|None = None, rotation: Vector4|list|tuple|None = None, scale: Vector3|list|tuple|None = None):
        self.translation:Vector3 = translation # type: ignore
        self.rotation:Vector4 = rotation # type: ignore
        self.scale:Vector3 = scale # type: ignore
class Vector2:
    """Vector2, 2 components."""
    def __init__(self, x: float|None = None, y: float|None = None):
        self.x:float = x # type: ignore
        self.y:float = y # type: ignore
class Vector3:
    """Vector3, 3 components."""
    def __init__(self, x: float|None = None, y: float|None = None, z: float|None = None):
        self.x:float = x # type: ignore
        self.y:float = y # type: ignore
        self.z:float = z # type: ignore
class Vector4:
    """Vector4, 4 components."""
    def __init__(self, x: float|None = None, y: float|None = None, z: float|None = None, w: float|None = None):
        self.x:float = x # type: ignore
        self.y:float = y # type: ignore
        self.z:float = z # type: ignore
        self.w:float = w # type: ignore
class VrDeviceInfo:
    """VrDeviceInfo, Head-Mounted-Display device parameters."""
    def __init__(self, hResolution: int|None = None, vResolution: int|None = None, hScreenSize: float|None = None, vScreenSize: float|None = None, eyeToScreenDistance: float|None = None, lensSeparationDistance: float|None = None, interpupillaryDistance: float|None = None, lensDistortionValues: list|None = None, chromaAbCorrection: list|None = None):
        self.hResolution:int = hResolution # type: ignore
        self.vResolution:int = vResolution # type: ignore
        self.hScreenSize:float = hScreenSize # type: ignore
        self.vScreenSize:float = vScreenSize # type: ignore
        self.eyeToScreenDistance:float = eyeToScreenDistance # type: ignore
        self.lensSeparationDistance:float = lensSeparationDistance # type: ignore
        self.interpupillaryDistance:float = interpupillaryDistance # type: ignore
        self.lensDistortionValues:list = lensDistortionValues # type: ignore
        self.chromaAbCorrection:list = chromaAbCorrection # type: ignore
class VrStereoConfig:
    """VrStereoConfig, VR stereo rendering configuration for simulator."""
    def __init__(self, projection: list|None = None, viewOffset: list|None = None, leftLensCenter: list|None = None, rightLensCenter: list|None = None, leftScreenCenter: list|None = None, rightScreenCenter: list|None = None, scale: list|None = None, scaleIn: list|None = None):
        self.projection:list = projection # type: ignore
        self.viewOffset:list = viewOffset # type: ignore
        self.leftLensCenter:list = leftLensCenter # type: ignore
        self.rightLensCenter:list = rightLensCenter # type: ignore
        self.leftScreenCenter:list = leftScreenCenter # type: ignore
        self.rightScreenCenter:list = rightScreenCenter # type: ignore
        self.scale:list = scale # type: ignore
        self.scaleIn:list = scaleIn # type: ignore
class Wave:
    """Wave, audio wave data."""
    def __init__(self, frameCount: int|None = None, sampleRate: int|None = None, sampleSize: int|None = None, channels: int|None = None, data: Any|None = None):
        self.frameCount:int = frameCount # type: ignore
        self.sampleRate:int = sampleRate # type: ignore
        self.sampleSize:int = sampleSize # type: ignore
        self.channels:int = channels # type: ignore
        self.data:Any = data # type: ignore
class float16:
    """."""
    def __init__(self, v: list|None = None):
        self.v:list = v # type: ignore
class float3:
    """NOTE: Helper types to be used instead of array return types for *ToFloat functions."""
    def __init__(self, v: list|None = None):
        self.v:list = v # type: ignore
class rlDrawCall:
    """of those state-change happens (this is done in core module)."""
    def __init__(self, mode: int|None = None, vertexCount: int|None = None, vertexAlignment: int|None = None, textureId: int|None = None):
        self.mode:int = mode # type: ignore
        self.vertexCount:int = vertexCount # type: ignore
        self.vertexAlignment:int = vertexAlignment # type: ignore
        self.textureId:int = textureId # type: ignore
class rlRenderBatch:
    """rlRenderBatch type."""
    def __init__(self, bufferCount: int|None = None, currentBuffer: int|None = None, vertexBuffer: Any|None = None, draws: Any|None = None, drawCounter: int|None = None, currentDepth: float|None = None):
        self.bufferCount:int = bufferCount # type: ignore
        self.currentBuffer:int = currentBuffer # type: ignore
        self.vertexBuffer:Any = vertexBuffer # type: ignore
        self.draws:Any = draws # type: ignore
        self.drawCounter:int = drawCounter # type: ignore
        self.currentDepth:float = currentDepth # type: ignore
class rlVertexBuffer:
    """Dynamic vertex buffers (position + texcoords + colors + indices arrays)."""
    def __init__(self, elementCount: int|None = None, vertices: Any|None = None, texcoords: Any|None = None, normals: Any|None = None, colors: str|None = None, indices: Any|None = None, vaoId: int|None = None, vboId: list|None = None):
        self.elementCount:int = elementCount # type: ignore
        self.vertices:Any = vertices # type: ignore
        self.texcoords:Any = texcoords # type: ignore
        self.normals:Any = normals # type: ignore
        self.colors:str = colors # type: ignore
        self.indices:Any = indices # type: ignore
        self.vaoId:int = vaoId # type: ignore
        self.vboId:list = vboId # type: ignore

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


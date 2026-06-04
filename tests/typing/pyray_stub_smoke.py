import pyray as rl


blend: int = rl.BlendMode.BLEND_ALPHA
mode: int = rl.RL_QUADS
src_alpha: int = rl.RL_SRC_ALPHA
mouse: int = rl.MouseButton.MOUSE_BUTTON_LEFT
flt: int = rl.TextureFilter.TEXTURE_FILTER_POINT


def accepts_texture(texture: rl.Texture | None) -> None:
    return None


tex2d: rl.Texture2D | None = None
accepts_texture(tex2d)

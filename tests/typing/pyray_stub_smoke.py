import pyray as rl


blend: int = rl.BLEND_ALPHA
mode: int = rl.RL_QUADS
mouse: int = rl.MOUSE_BUTTON_LEFT
flt: int = rl.TEXTURE_FILTER_POINT


def accepts_texture(texture: rl.Texture | None) -> None:
    return None


tex2d: rl.Texture2D | None = None
accepts_texture(tex2d)

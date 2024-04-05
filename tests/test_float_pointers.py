import pyray as pr
import pytest

pr.init_window(1280, 720, "any")

shader = pr.load_shader("", "shader.fs")
time = pr.ffi.new("float *", 0.0)
timeLoc = pr.get_shader_location(shader, "uTime")
pr.set_shader_value(shader, timeLoc, time, pr.SHADER_UNIFORM_FLOAT)
with pytest.raises(TypeError):
    pr.set_shader_value(shader, timeLoc, 0.0, pr.SHADER_UNIFORM_FLOAT)
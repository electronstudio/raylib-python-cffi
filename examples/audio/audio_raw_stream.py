from cffi import FFI
from pyray import *
from math import sin, pi, floor

MAX_SAMPLES = 512
MAX_SAMPLES_PER_UPDATE = 4096


frequency = 440.0
audio_frequency = 440.0
old_frequency = 1.0
sine_idx = 0.0

# Need to wrap audio callback fucntion in ffi callback
AUDIO_CALLBACK = ffi.callback("void(void *, unsigned int)")


def audio_input_callback(buffer_ptr, frames):
    global audio_frequency, sine_idx
    audio_frequency = frequency + (audio_frequency - frequency) * 0.95
    
    incr = audio_frequency/44100.0

    # cast the buffer_ptr to short (16 bit int)
    d = ffi.cast("short *", buffer_ptr)

    for i in range(frames):
        d[i] =  int((32000.0*sin(2*pi*sine_idx)))
        sine_idx += incr
        if sine_idx > 1.0:
            sine_idx -= 1.0

screen_width = 800
screen_height = 450

init_window(screen_width, screen_height, "raylib [audio] example - raw stream")

init_audio_device()

set_audio_stream_buffer_size_default(MAX_SAMPLES_PER_UPDATE)

stream = load_audio_stream(44100, 16, 1)

# Wrapping auido_input_callback in ffi callback
audio_cb = AUDIO_CALLBACK(audio_input_callback)

set_audio_stream_callback(stream, audio_cb)

data = [0 for _ in range(MAX_SAMPLES+1)]

write_buf = [0 for _ in range(MAX_SAMPLES_PER_UPDATE)]

play_audio_stream(stream)

mouse_position = Vector2(-100.0, -100.0)

wavelength = 1
position = Vector2(0.,0.)

set_target_fps(60)

while not window_should_close():
    mouse_position = get_mouse_position()

    if is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT):
        fp = mouse_position.y
        frequency = 40.0 + fp

        pan = mouse_position.x/screen_width
        set_audio_stream_pan(stream, pan)

    if frequency != old_frequency:
        wavelength = int(22050/frequency)
        if wavelength > MAX_SAMPLES/2:
            wavelength = int(MAX_SAMPLES/2)
        if wavelength < 1:
            wavelength = 1

        for i in range(floor(wavelength*2)):
            data[i] = int(sin(2*pi*(i/wavelength))*32000.0)

        for j in range(floor(wavelength*2), MAX_SAMPLES):
            data[j] = 0

        old_frequency = frequency

    begin_drawing()

    clear_background(RAYWHITE)

    draw_text(f"sine: frequency: {int(frequency)}", get_screen_width() - 220, 10, 20, RED)
    draw_text("click mouse button to change frequency or pan", 10, 10, 20, DARKGRAY)

    for i in range(screen_width):
        position.x = i
        position.y = 250 + 50 * data[int(i * MAX_SAMPLES/screen_width)]/32000.0

        draw_pixel_v(position, RED)

    end_drawing()

close_audio_device()
close_window()


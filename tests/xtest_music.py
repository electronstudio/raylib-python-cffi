from pyray import *
init_window(800, 450, "Hello")

init_audio_device()

music = load_music_stream("examples/audio/resources/country.mp3")
music.looping = True
play_music_stream(music);


while not window_should_close():
    update_music_stream(music);
    begin_drawing()
    clear_background(WHITE)
    draw_text("music "+str(music.looping), 190, 200, 20, VIOLET)
    end_drawing()
unload_music_stream(music)
close_audio_device()
close_window()

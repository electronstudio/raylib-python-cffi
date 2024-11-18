"""
FIXME this example is broken with Raylib 4.0

Requirements:
- raylib
- pytweening
- pyglm
- screeninfo

Windows-Only Requirements:
- win32gui
- win32con
- pywintypes

Mac:
- pyobjus
- Cython
"""

import sys, time
import glm # type: ignore
import pytweening as tween # type: ignore
import screeninfo # type: ignore
from raylib import rl, ffi
from raylib.colors import *


Vec2 = lambda p: glm.vec2(p.x, p.y)
CTM = lambda: round(time.perf_counter() * 1000)

monitors = screeninfo.get_monitors()
drag = False
offset = Vec2(rl.GetMousePosition())
width = height = 160
window_vel = glm.vec2()
window_pos = glm.vec2(monitors[0].width - width, monitors[0].height - height)

rl.SetConfigFlags(
	rl.FLAG_WINDOW_TRANSPARENT
	| rl.FLAG_WINDOW_UNDECORATED
	| rl.FLAG_VSYNC_HINT
	| rl.FLAG_MSAA_4X_HINT
)
rl.InitWindow(width, height, b'')
rl.SetWindowPosition(int(window_pos.x), int(window_pos.y))
#rl.SetTargetFPS(500)
target = rl.LoadRenderTexture(width, height)

# Top-Level Window Support Only On Windows
if sys.platform == 'win32':
	import win32gui, win32con, pywintypes
	
	# Set window to always top without moving it
	win32gui.SetWindowPos(
		pywintypes.HANDLE(ffi.cast('int', rl.GetWindowHandle())),
		win32con.HWND_TOPMOST,
		0, 0, 0, 0,
		win32con.SWP_NOSIZE | win32con.SWP_NOMOVE
	)


#tint = glm.vec4(255, 255, 255, 255) When mouse over, brighten everything fade
trans = 155
elapsed = CTM()
# Generate an 'L' pattern with pixels
awd = rl.LoadTextureFromImage(rl.LoadImageEx(
	[
		WHITE, WHITE,
		WHITE, [0] * 4
	],
	2, 2
))
# start1 = [0, 0]    ; end1 = [16, 16]
# start2 = [0, 160]  ; end2 = [16, 144]
# start3 = [160, 160]; end3 = [144, 144]
# start4 = [160, 0]  ; end4 = [144, 16]

start1 = [0, 0]    ; end1 = [8, 8]
start2 = [0, 160]  ; end2 = [8, 152]
start3 = [160, 160]; end3 = [152, 152]
start4 = [160, 0]  ; end4 = [152, 8]

while not rl.WindowShouldClose():
	frame_start_time = CTM()

	elapsed += 2 * rl.GetFrameTime()
	if elapsed > 1.0:
		elapsed = 0
		start1, end1 = end1, start1
		start2, end2 = end2, start2
		start3, end3 = end3, start3
		start4, end4 = end4, start4

	mouse_pos = Vec2(rl.GetMousePosition())

	if rl.IsKeyReleased(rl.KEY_ENTER):
		window_pos = glm.vec2()
		window_vel = glm.vec2()
	
	if rl.CheckCollisionPointRec(list(mouse_pos), [0, 0, width, height]):
		if rl.IsMouseButtonPressed(rl.MOUSE_LEFT_BUTTON):
			drag = True
			offset = mouse_pos
		
		trans = 255
	else:
		trans = 255

	#mouse_pos += window_vel
	window_vel *= glm.vec2(0.9, 0.9)

	if glm.length(window_vel):
		window_pos += window_vel
	 	#rl.SetWindowPosition(int(window_pos.x), int(window_pos.y))


	# Find which monitor the square is *currently within*
	wposx = window_pos.x + width // 2
	wposy = window_pos.y + height // 2
	found = False
	for monitor in reversed(monitors):
		if wposx > monitor.x and wposx < monitor.x + monitor.width:
			if wposy > monitor.y and wposy < monitor.y + monitor.height:
				found = True
				break

	# If it is out of bounds, find the closest one
	if not found:
		sorted_monitors = list(
			sorted(
				monitors,
				key=lambda m: (m.x + m.width // 2) - window_pos.x + (m.y + m.height // 2) - window_pos.y
			)
		)
		monitor = sorted_monitors[0]

	# Constrain window to bounds
	window_pos.x = max(monitor.x, window_pos.x)
	window_pos.x = min(monitor.x + monitor.width - width, window_pos.x)
	window_pos.y = max(monitor.y, window_pos.y)
	window_pos.y = min(monitor.y + monitor.height - height, window_pos.y)
	# Set here to "snap" and don't to enable "floating" back into position
	if not drag:
		rl.SetWindowPosition(int(window_pos.x), int(window_pos.y))


	if drag:
		window_pos += mouse_pos - offset
		drag = not rl.IsMouseButtonReleased(rl.MOUSE_LEFT_BUTTON)
		rl.SetWindowPosition(int(window_pos.x), int(window_pos.y))

		if not drag:
			window_vel = (mouse_pos - offset) * glm.vec2(1, 0.6) * 0.8
			if any(glm.isnan(window_vel)):
				window_vel = glm.vec2()

	rl.BeginDrawing()
	rl.ClearBackground([0] * 4)

	rl.BeginTextureMode(target)
	rl.ClearBackground([0] * 4)
	rl.DrawRectangle(0, 0, width, height, [0] * 4)

	rl.DrawTextureEx(
		awd, tween.getPointOnLine(*start1, *end1, tween.easeInOutQuad(elapsed)), 0, 32,
		[255, 200, 0, trans]  # Yellow
	)

	rl.DrawTextureEx(
		awd, tween.getPointOnLine(*start2, *end2, tween.easeInOutQuad(elapsed)), -90, 32,
		[255, 0, 55, trans]  # Red
	)

	rl.DrawTextureEx(
		awd, tween.getPointOnLine(*start3, *end3, tween.easeInOutQuad(elapsed)), -180, 32,
		[100, 200, 55, trans]  # Green
	)

	rl.DrawTextureEx(
		awd, tween.getPointOnLine(*start4, *end4, tween.easeInOutQuad(elapsed)), 90, 32,
		[55, 155, 255, trans]  # Blue
	)

	rl.EndTextureMode()

	rl.DrawTexturePro(
		target.texture,
		[0, 0, width, -height],
		[0, 0, width, height],
		[0, 0],
		0,
		WHITE
	)

	for i in range(1000):
		rl.DrawTextureEx(awd, [-32, -32], 0, 32, WHITE)

	#rl.DrawFPS(0, 0)

	rl.EndDrawing()

	# Sleep any leftover millis
	time_taken = CTM() - frame_start_time
	if time_taken < 1000 / 60:
		time.sleep((1000 / 60 - time_taken) / 1000)
	

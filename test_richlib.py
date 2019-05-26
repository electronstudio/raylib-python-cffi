from raylib.richlib import *
from raylib.static.pyray import pyray

WIDTH=800
HEIGHT=640
#CAMERA=CAMERA_FIRST_PERSON
DATA_DIR="examples/models/resources/models/"

player = Box((0, 10, 20), (10, 20, 10), 'green')
enemy_box = Box((-40, 10, 0), (20, 20, 20), (150,0,0))
enemy_sphere = Sphere((40, 15, 0), 15, 'gray')
castle = Actor("castle", collision_radius=15)
castle.z=-50
castle.scale.y=2
castle.scale.x=1
castle.scale.z=1


#def init():
#    set_camera_mode(camera, CAMERA_FIRST_PERSON)

def update():
    if keyboard.right:
        player.pos.x += 2
    elif keyboard.left:
        player.pos.x -= 2
    elif keyboard.down:
        player.pos.z += 2
    elif keyboard.up:
        player.pos.z -= 2

    if player.check_collision(enemy_box) or player.check_collision(enemy_sphere) or player.check_collision(castle):
        player.color = 'red'
    else:
        player.color = 'green'


def draw3d():
    clear('white')
    enemy_box.draw()
    enemy_sphere.draw()
    player.draw()
    castle.draw()
    pyray.draw_grid(10, 10)


def draw2d():
    pyray.draw_text("Move player with cursors to collide", 220, 40, 20, (255,0,0,255))
    rl.DrawText(b"Move player with cursors to collide", 220, 80, 20, (255,0,0,255))
    #prl.DrawFPS(10, 10)
    #pyray.foo(10,10)
    pyray.draw_fps(20,20)


run()

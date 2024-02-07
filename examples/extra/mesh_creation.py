from array import array
import pyray as pr

W, H = 640, 480


def make_cube(width, height, length):
    vertices = array('f', [
        -width / 2, -height / 2, length / 2,
        width / 2, -height / 2, length / 2,
        width / 2, height / 2, length / 2,
        -width / 2, height / 2, length / 2,
        -width / 2, -height / 2, -length / 2,
        -width / 2, height / 2, -length / 2,
        width / 2, height / 2, -length / 2,
        width / 2, -height / 2, -length / 2,
        -width / 2, height / 2, -length / 2,
        -width / 2, height / 2, length / 2,
        width / 2, height / 2, length / 2,
        width / 2, height / 2, -length / 2,
        -width / 2, -height / 2, -length / 2,
        width / 2, -height / 2, -length / 2,
        width / 2, -height / 2, length / 2,
        -width / 2, -height / 2, length / 2,
        width / 2, -height / 2, -length / 2,
        width / 2, height / 2, -length / 2,
        width / 2, height / 2, length / 2,
        width / 2, -height / 2, length / 2,
        -width / 2, -height / 2, -length / 2,
        -width / 2, -height / 2, length / 2,
        -width / 2, height / 2, length / 2,
        -width / 2, height / 2, -length / 2
    ])

    texcoords = array('f', [
        0.0, 0.0,
        1.0, 0.0,
        1.0, 1.0,
        0.0, 1.0,
        1.0, 0.0,
        1.0, 1.0,
        0.0, 1.0,
        0.0, 0.0,
        0.0, 1.0,
        0.0, 0.0,
        1.0, 0.0,
        1.0, 1.0,
        1.0, 1.0,
        0.0, 1.0,
        0.0, 0.0,
        1.0, 0.0,
        1.0, 0.0,
        1.0, 1.0,
        0.0, 1.0,
        0.0, 0.0,
        0.0, 0.0,
        1.0, 0.0,
        1.0, 1.0,
        0.0, 1.0])

    normals = array('f', [
        0.0, 0.0, 1.0,
        0.0, 0.0, 1.0,
        0.0, 0.0, 1.0,
        0.0, 0.0, 1.0,
        0.0, 0.0, -1.0,
        0.0, 0.0, -1.0,
        0.0, 0.0, -1.0,
        0.0, 0.0, -1.0,
        0.0, 1.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, -1.0, 0.0,
        0.0, -1.0, 0.0,
        0.0, -1.0, 0.0,
        0.0, -1.0, 0.0,
        1.0, 0.0, 0.0,
        1.0, 0.0, 0.0,
        1.0, 0.0, 0.0,
        1.0, 0.0, 0.0,
        -1.0, 0.0, 0.0,
        -1.0, 0.0, 0.0,
        -1.0, 0.0, 0.0,
        -1.0, 0.0, 0.0
    ])

    indices = array('h',
                    sum([[4 * k, 4 * k + 1, 4 * k + 2, 4 * k, 4 * k + 2, 4 * k + 3] for k in range(0, 6)], []))

    print(vertices, indices)

    return (pr.Mesh(24, 12, vertices, texcoords,
                   None, normals, None, None, indices,
                   None, None, None, None, 0, None))


pr.init_window(W, H, "Mesh creation")

msh = make_cube(3, 4, 40)
pr.upload_mesh(msh, False)
matdefault = pr.load_material_default()
eye = pr.matrix_identity()

camera = pr.Camera3D((30.0, 20.0, 30.0), (0.0, 0.0, 0.0), (0.0, 1.0, 0.0), 70.0,
                     pr.CameraProjection.CAMERA_PERSPECTIVE)

# Export so we can inspect it
pr.export_mesh(msh, "test-cube.obj")

while not pr.window_should_close():
    pr.update_camera(camera, pr.CameraMode.CAMERA_ORBITAL)
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    pr.begin_mode_3d(camera)
    pr.draw_grid(10, 5.0)
    pr.draw_mesh(msh, matdefault, eye)
    pr.end_mode_3d()
    pr.end_drawing()
pr.close_window()

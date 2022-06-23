"""
This shows how to use the Pyray wrapper around the static binding.
"""

import pyray as pr

v1 = pr.Vector2(10,10)
v2 = pr.Vector2(20,20)
v3 = pr.vector2_add(v1, v2)
print(v3.x, v3.y)
v4 = pr.vector2_normalize((20,10))
print(v4.x, v4.y)
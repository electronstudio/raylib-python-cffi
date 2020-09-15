# just a few functions from raymath
from raylib.dynamic import raylib as rl, ffi
import math

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2e2e575 (added shaders custom uniform)
PI = 3.14159265358979323846
DEG2RAD = (PI/180.0)
RAD2DEG = (180.0/PI)

def Clamp(value: float, minv: float, maxv: float):
    #res = value < minv ? minv : value
    res = minv if value < minv else value
    #return res > maxv ? maxv : res
    return maxv if res > maxv else res

def Lerp(start: float, end: float, amount: float):
    return start + amount*(end - start)


def Vector2Zero():
    return ffi.new("struct Vector2 *",[ 0, 0])

<<<<<<< HEAD
=======
>>>>>>> ffe4403 (complete fog example)
=======
>>>>>>> 2e2e575 (added shaders custom uniform)
def Vector3Zero():
    return ffi.new("struct Vector3 *",[ 0, 0, 0])
    
def MatrixRotateX(angle):
    result = MatrixIdentity();

    cosres = math.cos(angle);
    sinres = math.sin(angle);

    result.m5 = cosres;
    result.m6 = -sinres;
    result.m9 = sinres;
    result.m10 = cosres;

    return result;



def MatrixRotateY(angle):
    result = MatrixIdentity()

    cosres = math.cos(angle);
    sinres = math.sin(angle);

    result.m0 = cosres;
    result.m2 = sinres;
    result.m8 = -sinres;
    result.m10 = cosres;

    return result;


def MatrixIdentity():
    result = ffi.new("struct Matrix *",[ 1.0, 0.0, 0.0, 0.0,0.0, 1.0, 0.0, 0.0,    0.0, 0.0, 1.0, 0.0,   0.0, 0.0, 0.0, 1.0 ])
    return result



def MatrixRotateZ(angle):
    result = MatrixIdentity();

    cosres = math.cos(angle);
    sinres = math.sin(angle);

    result.m0 = cosres;
    result.m1 = -sinres;
    result.m4 = sinres;
    result.m5 = cosres;

    return result


def MatrixMultiply(left,  right):
    result = ffi.new("struct Matrix *")
    result.m0 = left.m0*right.m0 + left.m1*right.m4 + left.m2*right.m8 + left.m3*right.m12;
    result.m1 = left.m0*right.m1 + left.m1*right.m5 + left.m2*right.m9 + left.m3*right.m13;
    result.m2 = left.m0*right.m2 + left.m1*right.m6 + left.m2*right.m10 + left.m3*right.m14;
    result.m3 = left.m0*right.m3 + left.m1*right.m7 + left.m2*right.m11 + left.m3*right.m15;
    result.m4 = left.m4*right.m0 + left.m5*right.m4 + left.m6*right.m8 + left.m7*right.m12;
    result.m5 = left.m4*right.m1 + left.m5*right.m5 + left.m6*right.m9 + left.m7*right.m13;
    result.m6 = left.m4*right.m2 + left.m5*right.m6 + left.m6*right.m10 + left.m7*right.m14;
    result.m7 = left.m4*right.m3 + left.m5*right.m7 + left.m6*right.m11 + left.m7*right.m15;
    result.m8 = left.m8*right.m0 + left.m9*right.m4 + left.m10*right.m8 + left.m11*right.m12;
    result.m9 = left.m8*right.m1 + left.m9*right.m5 + left.m10*right.m9 + left.m11*right.m13;
    result.m10 = left.m8*right.m2 + left.m9*right.m6 + left.m10*right.m10 + left.m11*right.m14;
    result.m11 = left.m8*right.m3 + left.m9*right.m7 + left.m10*right.m11 + left.m11*right.m15;
    result.m12 = left.m12*right.m0 + left.m13*right.m4 + left.m14*right.m8 + left.m15*right.m12;
    result.m13 = left.m12*right.m1 + left.m13*right.m5 + left.m14*right.m9 + left.m15*right.m13;
    result.m14 = left.m12*right.m2 + left.m13*right.m6 + left.m14*right.m10 + left.m15*right.m14;
    result.m15 = left.m12*right.m3 + left.m13*right.m7 + left.m14*right.m11 + left.m15*right.m15;

    return result

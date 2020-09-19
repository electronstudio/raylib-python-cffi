from raylib.dynamic import raylib as rl, ffi


class LightSystem:
    MAX_LIGHTS = 4         #// Max dynamic lights supported by shader
    lightsCount = 0
    lights = []

    def __init__(self, ambient = [ 0.2, 0.2, 0.2, 1.0 ], *ls):
        self.shader = rl.LoadShader(b"resources/shaders/fogLight.vs",
                            b"resources/shaders/fogLight.fs");

        #// Get some shader loactions
        self.shader.locs[rl.LOC_MATRIX_MODEL] = rl.GetShaderLocation(self.shader, b"matModel");
        self.shader.locs[rl.LOC_VECTOR_VIEW] = rl.GetShaderLocation(self.shader, b"viewPos");

        #// ambient light level
        self.ambientLoc = rl.GetShaderLocation(self.shader, b"ambient");
        v = ffi.new("struct Vector4 *", ambient)
        rl.SetShaderValue(self.shader, self.ambientLoc, v, rl.UNIFORM_VEC4);

        for light in ls:
            self.add(light)

    def add(self, light):
        light.configure(len(self.lights), self.shader)
        self.lights.append(light)
        if len(self.lights) > self.MAX_LIGHTS:
            raise Exception("Too many lights")

    def update(self, cameraPos):
        rl.SetShaderValue(self.shader, self.shader.locs[rl.LOC_VECTOR_VIEW], ffi.new("struct Vector3 *",cameraPos), rl.UNIFORM_VEC3)
        for light in self.lights:
            light.UpdateLightValues()

    def draw(self):
        for light in self.lights:
            if light.enabled:
                rl.DrawSphereEx(light.position[0], 0.2, 8, 8, light.color)




LIGHT_DIRECTIONAL=0
LIGHT_POINT=1


class Light:
    def __init__(self, type,  position,  target, color):
        self.enabled = True
        self.type = type
        self.position = ffi.new("struct Vector3 *",position)
        self.target = target
        self.color = color




    def configure(self, id, shader):
        self.shader = shader
        #// TODO: Below code doesn't look good to me,
        #// it assumes a specific shader naming and structure
        #// Probably this implementation could be improved
        self.enabledName = f"lights[{id}].enabled"
        self.typeName = f"lights[{id}].type"
        self.posName = f"lights[{id}].position"
        self.targetName = f"lights[{id}].target"
        self.colorName = f"lights[{id}].color"

        self.enabledLoc = rl.GetShaderLocation(shader, self.enabledName.encode('utf-8'))
        self.typeLoc = rl.GetShaderLocation(shader, self.typeName.encode('utf-8'))
        self.posLoc = rl.GetShaderLocation(shader, self.posName.encode('utf-8'))
        self.targetLoc = rl.GetShaderLocation(shader, self.targetName.encode('utf-8'))
        self.colorLoc = rl.GetShaderLocation(shader, self.colorName.encode('utf-8'))

        self.UpdateLightValues()


    #// Send light properties to shader
    #// NOTE: Light shader locations should be available
    def UpdateLightValues(self):
        #// Send to shader light enabled state and type
        rl.SetShaderValue(self.shader, self.enabledLoc, ffi.new("int *",self.enabled), rl.UNIFORM_INT)
        rl.SetShaderValue(self.shader, self.typeLoc, ffi.new("int *",self.type), rl.UNIFORM_INT)

        #// Send to shader light position values
        position = [ self.position.x, self.position.y, self.position.z]
        rl.SetShaderValue(self.shader, self.posLoc, ffi.new("struct Vector3 *",position), rl.UNIFORM_VEC3)

        #// Send to shader light target position values
        target =[  self.target.x, self.target.y, self.target.z ]
        rl.SetShaderValue(self.shader, self.targetLoc, ffi.new("struct Vector3 *",target), rl.UNIFORM_VEC3)

        #// Send to shader light color values
        color = [self.color[0]/255.0, self.color[1]/255.0,  self.color[2]/255.0, self.color[3]/255.0]
        rl.SetShaderValue(self.shader, self.colorLoc, ffi.new("struct Vector4 *",color), rl.UNIFORM_VEC4)




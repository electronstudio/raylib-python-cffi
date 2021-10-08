
#define PHYSAC_MAX_BODIES               64          // Maximum number of physic bodies supported
#define PHYSAC_MAX_MANIFOLDS            4096        // Maximum number of physic bodies interactions (64x64)
#define PHYSAC_MAX_VERTICES             24          // Maximum number of vertex for polygons shapes
#define PHYSAC_DEFAULT_CIRCLE_VERTICES  24          // Default number of vertices for circle shapes




typedef enum PhysicsShapeType { PHYSICS_CIRCLE = 0, PHYSICS_POLYGON } PhysicsShapeType;

// Previously defined to be used in PhysicsShape struct as circular dependencies
typedef struct PhysicsBodyData *PhysicsBody;


// Matrix2x2 type (used for polygon shape rotation matrix)
typedef struct Matrix2x2 {
    float m00;
    float m01;
    float m10;
    float m11;
} Matrix2x2;

typedef struct PhysicsVertexData {
    unsigned int vertexCount;                   // Vertex count (positions and normals)
    Vector2 positions[PHYSAC_MAX_VERTICES];     // Vertex positions vectors
    Vector2 normals[PHYSAC_MAX_VERTICES];       // Vertex normals vectors
} PhysicsVertexData;

typedef struct PhysicsShape {
    PhysicsShapeType type;                      // Shape type (circle or polygon)
    PhysicsBody body;                           // Shape physics body data pointer
    PhysicsVertexData vertexData;               // Shape vertices data (used for polygon shapes)
    float radius;                               // Shape radius (used for circle shapes)
    Matrix2x2 transform;                        // Vertices transform matrix 2x2
} PhysicsShape;

typedef struct PhysicsBodyData {
    unsigned int id;                            // Unique identifier
    bool enabled;                               // Enabled dynamics state (collisions are calculated anyway)
    Vector2 position;                           // Physics body shape pivot
    Vector2 velocity;                           // Current linear velocity applied to position
    Vector2 force;                              // Current linear force (reset to 0 every step)
    float angularVelocity;                      // Current angular velocity applied to orient
    float torque;                               // Current angular force (reset to 0 every step)
    float orient;                               // Rotation in radians
    float inertia;                              // Moment of inertia
    float inverseInertia;                       // Inverse value of inertia
    float mass;                                 // Physics body mass
    float inverseMass;                          // Inverse value of mass
    float staticFriction;                       // Friction when the body has not movement (0 to 1)
    float dynamicFriction;                      // Friction when the body has movement (0 to 1)
    float restitution;                          // Restitution coefficient of the body (0 to 1)
    bool useGravity;                            // Apply gravity force to dynamics
    bool isGrounded;                            // Physics grounded on other body state
    bool freezeOrient;                          // Physics rotation constraint
    PhysicsShape shape;                         // Physics body shape information (type, radius, vertices, transform)
} PhysicsBodyData;

typedef struct PhysicsManifoldData {
    unsigned int id;                            // Unique identifier
    PhysicsBody bodyA;                          // Manifold first physics body reference
    PhysicsBody bodyB;                          // Manifold second physics body reference
    float penetration;                          // Depth of penetration from collision
    Vector2 normal;                             // Normal direction vector from 'a' to 'b'
    Vector2 contacts[2];                        // Points of contact during collision
    unsigned int contactsCount;                 // Current collision number of contacts
    float restitution;                          // Mixed restitution during collision
    float dynamicFriction;                      // Mixed dynamic friction during collision
    float staticFriction;                       // Mixed static friction during collision
} PhysicsManifoldData, *PhysicsManifold;


PHYSACDEF void InitPhysics(void);                                                                           // Initializes physics system
PHYSACDEF void UpdatePhysics(void);                                                                         // Update physics system
PHYSACDEF void ResetPhysics(void);                                                                          // Reset physics system (global variables)
PHYSACDEF void ClosePhysics(void);                                                                          // Close physics system and unload used memory
PHYSACDEF void SetPhysicsTimeStep(double delta);                                                            // Sets physics fixed time step in milliseconds. 1.666666 by default
PHYSACDEF void SetPhysicsGravity(float x, float y);                                                         // Sets physics global gravity force

// Physic body creation/destroy
PHYSACDEF PhysicsBody CreatePhysicsBodyCircle(Vector2 pos, float radius, float density);                    // Creates a new circle physics body with generic parameters
PHYSACDEF PhysicsBody CreatePhysicsBodyRectangle(Vector2 pos, float width, float height, float density);    // Creates a new rectangle physics body with generic parameters
PHYSACDEF PhysicsBody CreatePhysicsBodyPolygon(Vector2 pos, float radius, int sides, float density);        // Creates a new polygon physics body with generic parameters
PHYSACDEF void DestroyPhysicsBody(PhysicsBody body);                                                        // Destroy a physics body

// Physic body forces
PHYSACDEF void PhysicsAddForce(PhysicsBody body, Vector2 force);                                            // Adds a force to a physics body
PHYSACDEF void PhysicsAddTorque(PhysicsBody body, float amount);                                            // Adds an angular force to a physics body
PHYSACDEF void PhysicsShatter(PhysicsBody body, Vector2 position, float force);                             // Shatters a polygon shape physics body to little physics bodies with explosion force
PHYSACDEF void SetPhysicsBodyRotation(PhysicsBody body, float radians);                                     // Sets physics body shape transform based on radians parameter

// Query physics info
PHYSACDEF PhysicsBody GetPhysicsBody(int index);                                                            // Returns a physics body of the bodies pool at a specific index
PHYSACDEF int GetPhysicsBodiesCount(void);                                                                  // Returns the current amount of created physics bodies
PHYSACDEF int GetPhysicsShapeType(int index);                                                               // Returns the physics body shape type (PHYSICS_CIRCLE or PHYSICS_POLYGON)
PHYSACDEF int GetPhysicsShapeVerticesCount(int index);                                                      // Returns the amount of vertices of a physics body shape
PHYSACDEF Vector2 GetPhysicsShapeVertex(PhysicsBody body, int vertex);                                      // Returns transformed position of a body shape (body position + vertex transformed position)

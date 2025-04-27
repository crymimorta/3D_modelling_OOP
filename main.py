import random
from shape import Shape3D
from sphere import Sphere
from cylinder import Cylinder
from cube import Cube

def generate_random_shapes(num_shapes=10):
    shapes = []
    for _ in range(num_shapes):
        shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])
        if shape_type == 'Sphere':
            r = random.randint(1, 10)
            shapes.append(Sphere(r))
        elif shape_type == 'Cylinder':
            r = random.randint(1, 10)
            h = random.randint(5, 20)
            shapes.append(Cylinder(r, h))
        elif shape_type == 'Cube':
            a = random.randint(1, 10)
            shapes.append(Cube(a))
    return shapes

def display_shapes(shapes):
    for i, shape in enumerate(shapes, start=1):
        print(f"Shape {i}: {shape.__class__.__name__}")
        print(f"  Surface Area: {shape.surface_area():.2f}")
        print(f"  Volume: {shape.volume():.2f}")
        print("-" * 30)

if __name__ == "__main__":
    shapes = generate_random_shapes()
    display_shapes(shapes)

from .vector import Vector


class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = Vector(*position)  # Convert tuple to Vector
        self.velocity = Vector(*velocity)  # Convert tuple to Vector

    def update(self, acceleration, dt):
        self.velocity += acceleration * dt
        self.position += self.velocity * dt


print("Hello fom particle")

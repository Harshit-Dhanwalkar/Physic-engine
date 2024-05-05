from .vector import Vector
from .gravity import calculate_gravity


class Simulation:
    def __init__(self):
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def update(self, dt):
        # Update particle positions based on forces acting on them
        for particle in self.particles:
            particle.update(self.calculate_total_force(particle), dt)

    def calculate_total_force(self, particle):
        # Calculate the total force acting on a particle (e.g., gravitational force)
        total_force = Vector(0, 0)  # Initialize total force vector
        for other_particle in self.particles:
            if other_particle != particle:
                # Add gravitational force
                total_force += calculate_gravity(particle, other_particle)
        return total_force
    print("hello from stimulation")

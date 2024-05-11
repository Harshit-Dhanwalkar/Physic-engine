# simulation.py

from .vector import Vector
from .gravity import calculate_gravity


class Simulation:
    def __init__(self, gravity=Vector(0, -9.8)):
        self.particles = []
        self.gravity = gravity

    def add_particle(self, particle):
        self.particles.append(particle)

    def update(self, dt):
        # Update particle positions based on forces acting on them
        for particle in self.particles:
            total_force = self.calculate_total_force(particle)
            particle.update(total_force, dt)

    def calculate_total_force(self, particle):
        # Calculate the total force acting on a particle (e.g., gravitational force)
        total_force = Vector(0, 0)  # Initialize total force vector

        # Add gravitational force
        gravitational_force = self.gravity * particle.mass
        total_force += gravitational_force

        return total_force

    print("hello from stimulation")

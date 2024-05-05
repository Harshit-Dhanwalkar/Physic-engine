# FIXME: Ensure distance between particles is not zero to prevent ZeroDivisionError
# TODO: Implement collision detection and response
# TODO: Add visualization for gravitational forces
# TODO: Allow customization of simulation parameters through user input or configuration file
# TODO: Implement 3D visualization for particle trajectories
# TODO: Add support for additional force types such as friction or electrostatic forces

import matplotlib.pyplot as plt
from utilities.particle import Particle
from utilities.gravity import calculate_gravity
from utilities.projectile import calculate_projectile_trajectory
from utilities.simulation import Simulation
from utilities.vector import Vector
from utilities.particle_animation import animate_particle_trajectories


print("hello from main 1")

# Function to stimulate particle movement


def stimulate_simulation(simulation, total_time, dt):
    num_steps = int(total_time / dt)
    positions = [[] for _ in range(len(simulation.particles))]

    for _ in range(num_steps):
        simulation.update(dt)
        for i, particle in enumerate(simulation.particles):
            positions[i].append((particle.position.x, particle.position.y))

    return positions

# Customizing Particle Properties


def create_particles(num_particles, particle_params):
    particles = []
    for _ in range(num_particles):
        mass = particle_params.get('mass', 1.0)
        position = particle_params.get('position', (0, 0))
        velocity = particle_params.get('velocity', (0, 0))
        particle = Particle(mass, position, velocity)
        particles.append(particle)
    return particles

# Define particle parameters, create particles, and initialize the simulation


particle_params = {'mass': 10, 'position': (0, 0), 'velocity': (10, 0)}
num_particles = 2
particles = create_particles(num_particles, particle_params)
simulation = Simulation()

# Add particles to the simulation
for particle in particles:
    simulation.add_particle(particle)

# Stimulate simulation
total_time = 10
dt = 0.01
positions = stimulate_simulation(simulation, total_time, dt)

# Ask the user if they want to animate the particle trajectories
user_input = input("Do you want to animate the particle trajectories? (y/n): ")
if user_input.lower() == "y":
    animate_particle_trajectories(positions, num_particles)
else:
    print("Particle trajectories will not be animated.")


print("hello from main 2")

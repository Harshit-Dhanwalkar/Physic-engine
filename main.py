# FIX:
# TODO:

from utilities.particle import Particle
from utilities.gravity import calculate_gravity
from utilities.projectile import calculate_projectile_trajectory
from utilities.simulation import Simulation
from utilities.vector import Vector
import matplotlib.pyplot as plt

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


# Define particle parameters
particle_params = {'mass': 10, 'position': (0, 0), 'velocity': (10, 0)}
num_particles = 2

# Create particles
particles = create_particles(num_particles, particle_params)

# Create simulation
simulation = Simulation()
for particle in particles:
    simulation.add_particle(particle)

# Stimulate simulation
total_time = 10
dt = 0.01
positions = stimulate_simulation(simulation, total_time, dt)

# Plot particle trajectories

for i, particle_positions in enumerate(positions):
    x = [pos[0] for pos in particle_positions]
    y = [pos[1] for pos in particle_positions]
    plt.plot(x, y, label=f'Particle {i+1}')

plt.xlabel('X position')
plt.ylabel('Y position')
plt.title('Particle Trajectories')
plt.legend()
plt.grid(True)
plt.show()

print("hello from main 2")

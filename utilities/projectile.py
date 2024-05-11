# projectile.py

import math


def calculate_projectile_trajectory(initial_velocity, launch_angle, dt):
    vx = initial_velocity * math.cos(math.radians(launch_angle))
    vy = initial_velocity * math.sin(math.radians(launch_angle))

    x = 0  # Initial x position
    y = 0  # Initial y position

    while True:
        # Update particle's position and velocity based on projectile motion equations
        x += vx * dt
        y += vy * dt
        yield (x, y)  # Return updated position (x, y)


print("hello from projectile")

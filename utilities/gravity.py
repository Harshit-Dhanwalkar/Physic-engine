from .vector import Vector

G = 6.67430e-11  # gravitational constant


def calculate_gravity(particle1, particle2):
    r = particle2.position - particle1.position
    distance_squared = r.magnitude() ** 2

    # Add check to avoid division by zero
    if distance_squared < 1e-6:
        return Vector(0, 0)

    force_magnitude = G * particle1.mass * particle2.mass / distance_squared
    force_direction = r.normalized()
    force = force_direction * force_magnitude
    return force


print("hello from gravity")

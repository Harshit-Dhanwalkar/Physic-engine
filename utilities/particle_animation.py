# particle_animation.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate_particle_trajectories(positions, num_particles):
    fig, ax = plt.subplots()
    ax.set_xlim(-50, 50)  # Adjust the limits as needed
    ax.set_ylim(-50, 50)

    lines = [ax.plot([], [], label=f'Particle {
                     i+1}')[0] for i in range(num_particles)]

    def update_plot(frame):
        for i, line in enumerate(lines):
            line.set_data([pos[0] for pos in positions[i][:frame+1]],
                          [pos[1] for pos in positions[i][:frame+1]])
        return lines

    ani = animation.FuncAnimation(fig, update_plot, frames=len(
        positions[0]), interval=10, blit=True)
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.title('Particle Trajectories')
    plt.legend()
    plt.grid(True)
    plt.show()

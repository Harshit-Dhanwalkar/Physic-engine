# particle_animation.py

# FIX: Animate to break when paticle touch boundary


import matplotlib.pyplot as plt
import matplotlib.animation as animation

x_bound = [-40, 40]
y_bound = [-50, 50]


def animate_particle_trajectories(positions, num_particles):
    fig, ax = plt.subplots()
    plt.grid()
    ax.set_xlim(x_bound[0], x_bound[1])
    ax.set_ylim(y_bound[0], y_bound[1])

    lines = [ax.plot([], [], label=f'Particle {
                     i+1}')[0] for i in range(num_particles)]

    def update_plot(frame):
        for i, line in enumerate(lines):
            x_positions = [pos[0] for pos in positions[i][:frame + 1]]
            y_positions = [pos[1] for pos in positions[i][:frame + 1]]
            line.set_data(x_positions, y_positions)

            # Check if any particle's position goes beyond the limits
            if any(x > x_bound[1] or x < x_bound[0] or y > y_bound[1] or y < y_bound[0] for x, y in zip(x_positions, y_positions)):
                ani.event_source.stop()  # Stop the animation
                plt.close(fig)  # Close the plot window
                return lines

        return lines

    interval = 10
    ani = animation.FuncAnimation(
        fig, update_plot, frames=len(positions[0]), interval=interval, blit=True)

    # Debug statements
    print("Animation object inside function:", ani)
    print("Animation object type:", type(ani))

    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.title('Particle Trajectories')
    plt.legend()
    plt.grid(True)
    plt.show()

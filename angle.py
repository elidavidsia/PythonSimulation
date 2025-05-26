import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import math

# Constants
g = 9.8  # gravitational acceleration (m/s^2)
v0_default = 25  # default initial velocity (m/s)
theta_default = 45  # default angle (degrees)

# Time array
t = np.linspace(0, 5, 500)

# Function to calculate trajectory
def calculate_trajectory(v0, theta):
    theta_rad = np.radians(theta)
    t_flight = 2 * v0 * np.sin(theta_rad) / g
    t_vals = np.linspace(0, t_flight, 300)
    x = v0 * np.cos(theta_rad) * t_vals
    y = v0 * np.sin(theta_rad) * t_vals - 0.5 * g * t_vals**2
    return x, y, t_flight

# Initial trajectory
x, y, t_flight = calculate_trajectory(v0_default, theta_default)

# Set up plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
ax.set_xlim(0, 70)
ax.set_ylim(0, 35)
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Height (m)")
ax.set_title("🚀 Projectile Motion Simulation")

# Plot elements
trajectory_line, = ax.plot([], [], 'b--', label="Trajectory")
projectile_dot, = ax.plot([], [], 'ro', label="Projectile")
range_text = ax.text(0.7, 0.9, '', transform=ax.transAxes)

# Sliders
ax_angle = plt.axes([0.15, 0.15, 0.65, 0.03])
ax_velocity = plt.axes([0.15, 0.1, 0.65, 0.03])
slider_angle = Slider(ax_angle, 'Angle (°)', 0, 90, valinit=theta_default)
slider_velocity = Slider(ax_velocity, 'Velocity (m/s)', 5, 100, valinit=v0_default)

# Initialization function
def init():
    trajectory_line.set_data([], [])
    projectile_dot.set_data([], [])
    range_text.set_text('')
    return trajectory_line, projectile_dot, range_text

# Animation update function
def update(frame):
    v0 = slider_velocity.val
    theta = slider_angle.val
    x_vals, y_vals, t_flight = calculate_trajectory(v0, theta)

    # Plot full trajectory
    trajectory_line.set_data(x_vals, y_vals)

    # Projectile dot animation
    if frame < len(x_vals):
        projectile_dot.set_data(x_vals[frame], y_vals[frame])
    else:
        projectile_dot.set_data([], [])

    # Update range display
    range_val = (v0**2 * np.sin(np.radians(2 * theta))) / g
    range_text.set_text(f"Range ≈ {range_val:.2f} m")

    return trajectory_line, projectile_dot, range_text

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 300), init_func=init, interval=20, blit=True)

# Slider update function
def on_slider_change(val):
    update(0)

slider_angle.on_changed(on_slider_change)
slider_velocity.on_changed(on_slider_change)

plt.legend()
plt.grid(True)
plt.show()
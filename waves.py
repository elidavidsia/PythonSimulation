import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Define wave parameters
A = 1.0
λ = 1.0
f = 1.0
ω = 2 * np.pi * f
k = 2 * np.pi / λ
ϕ = 0

# Generate grid
x = np.linspace(-10, 10, 800)
y = np.linspace(-10, 10, 800)
X, Y = np.meshgrid(x, y)

# Function to generate polygon vertices (for the given number of sides)
def generate_polygon_vertices(n_sides, radius=5.0):
    angles = np.linspace(0, 2 * np.pi, n_sides, endpoint=False)
    return np.column_stack((radius * np.cos(angles), radius * np.sin(angles)))

# Function to compute total wave displacement
def compute_total_displacement(X, Y, vertices):
    total = np.zeros_like(X)
    for x0, y0 in vertices:
        R = np.sqrt((X - x0)**2 + (Y - y0)**2)
        total += A * np.sin(k * R - ω * 0 + ϕ)  # Set t=0 for static display
    return total

# Streamlit app layout
st.title("Wave Interference Simulation")
st.write("This simulation allows you to explore wave interference patterns produced by point sources at the vertices of a regular polygon.")

# Sidebar for user input
n_sides = st.slider("Select the number of sides of the polygon:", 3, 12, 6)

# Generate the wave sources (vertices)
vertices = generate_polygon_vertices(n_sides)

# Compute the interference pattern
Z = compute_total_displacement(X, Y, vertices)

# Display the interference pattern
fig, ax = plt.subplots(figsize=(8, 8))
c = ax.pcolormesh(X, Y, Z, shading='auto', cmap='Spectral')
fig.colorbar(c, ax=ax)
ax.set_title(f"Wave Interference Pattern with {n_sides}-gon Sources")
ax.set_xlabel("x")
ax.set_ylabel("y")

# Plot the sources on the interference pattern
ax.scatter(vertices[:, 0], vertices[:, 1], color='white', s=100, label="Sources", edgecolor="black")
ax.legend()

# Show the plot in the Streamlit app
st.pyplot(fig)

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Constants
G = 6.67430e-11
M = 5.972e24
R_earth = 6371000

st.title("Payload Trajectory Simulator")

# Sidebar inputs
v0_magnitude = st.sidebar.slider('Initial velocity (m/s)', 3000, 15000, 8000, 500)
dt = st.sidebar.slider('Time step (s)', 1, 100, 10)
t_max = st.sidebar.slider('Maximum simulation time (s)', 5000, 20000, 10000, 1000)

def simulate_payload(v0_magnitude, dt, t_max):
    r0 = np.array([R_earth + 500000, 0])
    v0 = np.array([0, v0_magnitude])
    time = np.arange(0, t_max, dt)

    r = np.zeros((len(time), 2))
    v = np.zeros((len(time), 2))
    r[0] = r0
    v[0] = v0

    for i in range(1, len(time)):
        r_mag = np.linalg.norm(r[i-1])
        a = -G * M * r[i-1] / r_mag**3
        v[i] = v[i-1] + a * dt
        r[i] = r[i-1] + v[i] * dt
        if r_mag > 1e7:
            break

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(r[:i, 0], r[:i, 1], label="Trajectory")
    ax.scatter([0], [0], color="red", s=100, label="Earth")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_title("Payload Trajectory")
    ax.legend()
    ax.grid(True)
    ax.set_aspect('equal')
    st.pyplot(fig)

simulate_payload(v0_magnitude, dt, t_max)

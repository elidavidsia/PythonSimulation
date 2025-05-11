import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
st.title("Charged Particle Motion in Electric and Magnetic Fields")

# --- Reset Button using Session State ---
if "reset" not in st.session_state:
    st.session_state.reset = False

def reset_defaults():
    st.session_state.q = 1.6e-19
    st.session_state.m = 1.67e-27
    st.session_state.Ex = 0.0
    st.session_state.Ey = 0.0
    st.session_state.Bx = 0.0
    st.session_state.By = 0.0
    st.session_state.Bz = 1.0
    st.session_state.v0x = 1e6
    st.session_state.v0y = 0.0
    st.session_state.v0z = 0.0
    st.session_state.T = 5e-7
    st.session_state.dt = 1e-9

if st.sidebar.button("🔄 Reset Parameters"):
    reset_defaults()

# Sidebar: Parameters
st.sidebar.header("Physical Constants")
q = st.sidebar.number_input("Charge (C)", value=st.session_state.get("q", 1.6e-19), key="q", format="%.2e")
m = st.sidebar.number_input("Mass (kg)", value=st.session_state.get("m", 1.67e-27), key="m", format="%.2e")

st.sidebar.header("Field Configuration")
Ex = st.sidebar.number_input("Electric Field Ex (V/m)", value=st.session_state.get("Ex", 0.0), key="Ex")
Ey = st.sidebar.number_input("Electric Field Ey (V/m)", value=st.session_state.get("Ey", 0.0), key="Ey")
Bx = st.sidebar.number_input("Magnetic Field Bx (T)", value=st.session_state.get("Bx", 0.0), key="Bx")
By = st.sidebar.number_input("Magnetic Field By (T)", value=st.session_state.get("By", 0.0), key="By")
Bz = st.sidebar.number_input("Magnetic Field Bz (T)", value=st.session_state.get("Bz", 1.0), key="Bz")

st.sidebar.header("Initial Conditions")
v0x = st.sidebar.number_input("Initial Velocity vx (m/s)", value=st.session_state.get("v0x", 1e6), key="v0x", format="%.2e")
v0y = st.sidebar.number_input("Initial Velocity vy (m/s)", value=st.session_state.get("v0y", 0.0), key="v0y", format="%.2e")
v0z = st.sidebar.number_input("Initial Velocity vz (m/s)", value=st.session_state.get("v0z", 0.0), key="v0z", format="%.2e")

st.sidebar.header("Simulation Settings")
T = st.sidebar.number_input("Total Time (s)", value=st.session_state.get("T", 5e-7), key="T", format="%.1e")
dt = st.sidebar.number_input("Time Step (s)", value=st.session_state.get("dt", 1e-9), key="dt", format="%.1e")

# Time array
t = np.arange(0, T, dt)

# Initial conditions
r = np.array([0.0, 0.0, 0.0])
v = np.array([v0x, v0y, v0z])
E = np.array([Ex, Ey, 0.0])
B = np.array([Bx, By, Bz])

# Storage arrays
trajectory = [r.copy()]

# Euler integration
for _ in t:
    F = q * (E + np.cross(v, B))
    a = F / m
    v = v + a * dt
    r = r + v * dt
    trajectory.append(r.copy())

trajectory = np.array(trajectory)

# Plotting
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(trajectory[:, 0], trajectory[:, 1], 'r-', label="Trajectory")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Particle Motion in E and B Fields (x-y plane)")
ax.set_aspect('equal')
ax.grid(True)
ax.legend()

st.pyplot(fig)

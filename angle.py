import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("🎯 Projectile Motion Simulator")

st.markdown("""
This app simulates the motion of a projectile launched at an angle from the ground.  
It assumes **no air resistance** and uses classical mechanics equations.
""")

# User inputs
v0 = st.slider("Initial Velocity (m/s)", 5, 100, 25)
theta_deg = st.slider("Launch Angle (°)", 0, 90, 45)

# Convert angle to radians
theta_rad = np.radians(theta_deg)
g = 9.8  # gravity (m/s²)

# Time of flight
t_flight = 2 * v0 * np.sin(theta_rad) / g

# Time values
t = np.linspace(0, t_flight, num=300)

# Trajectory equations
x = v0 * np.cos(theta_rad) * t
y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2

# Max height and range
h_max = (v0**2 * np.sin(theta_rad)**2) / (2 * g)
range_ = (v0**2 * np.sin(2 * theta_rad)) / g

# Display results
st.subheader("📊 Simulation Results")
st.markdown(f"""
- **Range**: {range_:.2f} m  
- **Maximum Height**: {h_max:.2f} m  
- **Time of Flight**: {t_flight:.2f} s
""")

# Plot
fig, ax = plt.subplots()
ax.plot(x, y, 'b', label='Projectile Path')
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Height (m)")
ax.set_title("Projectile Trajectory")
ax.grid(True)
ax.legend()
st.pyplot(fig)

st.markdown("---")
st.caption("Built with Streamlit and Python · No air resistance modeled")

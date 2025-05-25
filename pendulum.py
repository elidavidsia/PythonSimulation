import streamlit as st
import pandas as pd
import numpy as np
import math

st.title("Pendulum Experiment: Gravitational Acceleration Calculator")

st.markdown("""
This simulation allows you to input the time for 10 oscillations for a pendulum, 
and it calculates the period and gravitational acceleration \( g \) using the formula:

\[
g = \frac{4\pi^2 L}{T^2}
\]

Assuming a fixed pendulum length **L = 1.00 m** and uncertainty in \( g \) as **±0.15 m/s²**.
""")

# Constants
L = 1.00  # meters
uncertainty_g = 0.15  # m/s^2
num_trials = 10

# Input time for 10 oscillations
st.subheader("Input Time for 10 Oscillations")
times = []
default_times = [20.1, 20.3, 19.9, 20.0, 20.2, 20.0, 20.1, 19.8, 20.4, 20.2]

for i in range(num_trials):
    t = st.number_input(f"Trial {i+1}", min_value=0.0, value=default_times[i], step=0.1, key=f"time_{i}")
    times.append(t)

# Compute values
data = []
for i, t10 in enumerate(times):
    T = t10 / 10  # Period
    g = (4 * math.pi**2 * L) / (T**2)
    data.append({
        "Trial": i + 1,
        "Time for 10 Oscillations (s)": t10,
        "Period T (s)": round(T, 2),
        "Calculated g (m/s²)": round(g, 2),
        "Uncertainty Δg (m/s²)": f"±{uncertainty_g}"
    })

df = pd.DataFrame(data)

# Display data table
st.subheader("Results")
st.dataframe(df, use_container_width=True)

# Statistics
g_values = [row["Calculated g (m/s²)"] for row in data]
mean_g = np.mean(g_values)
std_dev = np.std(g_values)

st.subheader("Summary Statistics")
st.write(f"**Mean g:** {mean_g:.2f} m/s²")
st.write(f"**Standard Deviation:** {std_dev:.2f} m/s²")

# Plot
st.subheader("Gravitational Acceleration per Trial")
st.bar_chart(df.set_index("Trial")["Calculated g (m/s²)"])

# ============================================================
# ACTIVITY 1 — GUIDED: Sine Wave Explorer
# Difficulty: ★☆☆  (beginner)
#
# GOAL: Build an interactive sine wave plotter.
# Fill in every  ### YOUR CODE HERE ###  section.
# Run anytime with:  streamlit run activity_1_guided.py
# ============================================================

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ── STEP 1: Give your app a title ───────────────────────────
# Hint: st.title("Some text")

### YOUR CODE HERE ###


# ── STEP 2: Write a one-sentence description ────────────────
# Hint: st.markdown("Your text here")

### YOUR CODE HERE ###


# ── STEP 3: Sidebar sliders ─────────────────────────────────
st.sidebar.header("Controls")

# Create a slider for Amplitude (A).  Range: 0.1 → 5.0, default 1.0
# Hint: A = st.sidebar.slider("Label", min_val, max_val, default_val)

A = ### YOUR CODE HERE ###

# Create a slider for Frequency (ω).  Range: 0.1 → 5.0, default 1.0

omega = ### YOUR CODE HERE ###


# ── STEP 4: Compute the function ────────────────────────────
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)

# FIX-ME: This formula ignores A and omega — fix it!
y = np.sin(x)


# ── STEP 5: Display the formula using LaTeX ─────────────────
# Hint: st.latex(r"f(x) = A \sin(\omega x)")
# The r"..." prefix keeps backslashes intact.

### YOUR CODE HERE ###


# ── STEP 6: Plot ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, color="steelblue", linewidth=2)
ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")

# FIX-ME: The axis labels and grid are missing.
# Add:  ax.set_xlabel(...)  ax.set_ylabel(...)  ax.grid(...)

st.pyplot(fig)


# ── STEP 7: Show summary statistics ─────────────────────────
# Display the max value of y as a metric.
# Hint: st.metric("Label", f"{value:.3f}")

### YOUR CODE HERE ###


# ── BONUS: Can you add a second function? ───────────────────
# Try plotting y2 = A * cos(omega * x) on the same axes.
# Add a checkbox in the sidebar to toggle it on/off.
# Hint: show_cos = st.sidebar.checkbox("Show cos")

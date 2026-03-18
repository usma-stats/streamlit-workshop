# ============================================================
# ACTIVITY 2 — INTERMEDIATE: Statistics Dashboard
# Difficulty: ★★☆
#
# GOAL: Build a dashboard that generates random data,
#       plots a histogram, and reports key statistics.
#
# The structure is provided — fill in the blanks.
# Run anytime with:  streamlit run activity_2_stats.py
# ============================================================

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Statistics Dashboard")
st.markdown("Explore how sample size and distribution shape affect summary statistics.")

# ── SECTION 1: Controls ─────────────────────────────────────
st.sidebar.header("Distribution Settings")

dist = st.sidebar.selectbox("Distribution", ["Normal", "Uniform", "Exponential"])

n = st.sidebar.slider("Sample size", 10, 5000, 500, step=10)

seed = st.sidebar.number_input("Random seed", value=42, step=1)
rng = np.random.default_rng(int(seed))

# ── SECTION 2: Generate data ─────────────────────────────────
# TODO: Generate n samples from the selected distribution.
# Use rng.normal(), rng.uniform(), or rng.exponential()
# Store the result in a variable called `data`.

if dist == "Normal":
    mu    = st.sidebar.slider("Mean (μ)", -5.0, 5.0, 0.0, step=0.5)
    sigma = st.sidebar.slider("Std dev (σ)", 0.1, 5.0, 1.0, step=0.1)
    data  = ### YOUR CODE HERE ###   # Hint: rng.normal(mu, sigma, n)

elif dist == "Uniform":
    low  = st.sidebar.slider("Lower bound", -10.0, 0.0, 0.0)
    high = st.sidebar.slider("Upper bound",  0.0, 10.0, 1.0)
    data = ### YOUR CODE HERE ###   # Hint: rng.uniform(low, high, n)

else:  # Exponential
    scale = st.sidebar.slider("Scale (1/λ)", 0.1, 5.0, 1.0, step=0.1)
    data  = ### YOUR CODE HERE ###   # Hint: rng.exponential(scale, n)

# ── SECTION 3: Summary statistics ───────────────────────────
st.header("Summary Statistics")

col1, col2, col3, col4 = st.columns(4)

# FIX-ME: Replace each None with the correct numpy call.
col1.metric("Mean",    f"{None:.4f}")   # np.mean(data)
col2.metric("Std dev", f"{None:.4f}")   # np.std(data)
col3.metric("Min",     f"{None:.4f}")   # np.min(data)
col4.metric("Max",     f"{None:.4f}")   # np.max(data)


# ── SECTION 4: Histogram ────────────────────────────────────
st.header("Histogram")

bins = st.slider("Number of bins", 5, 100, 30)

fig, ax = plt.subplots(figsize=(8, 4))

# TODO: Plot a histogram of `data` with `bins` bins.
# Hint: ax.hist(data, bins=bins, color="steelblue", edgecolor="white", alpha=0.8)

### YOUR CODE HERE ###

ax.set_xlabel("Value")
ax.set_ylabel("Count")
ax.set_title(f"{dist} distribution  (n={n})")

# TODO: Add a vertical dashed line at the mean.
# Hint: ax.axvline(np.mean(data), color="red", linestyle="--", label="mean")
#       ax.legend()

### YOUR CODE HERE ###

st.pyplot(fig)


# ── SECTION 5: Raw data table ────────────────────────────────
with st.expander("Show raw data (first 50 rows)"):
    df = pd.DataFrame({"value": data}).head(50)

    # TODO: Display the dataframe with st.dataframe()
    ### YOUR CODE HERE ###

    # BONUS: Add a download button for the full dataset as CSV.
    # Hint: pd.DataFrame({"value": data}).to_csv(index=False)
    #       st.download_button("⬇️ Download CSV", csv_string, "data.csv")
    ### YOUR CODE HERE ###

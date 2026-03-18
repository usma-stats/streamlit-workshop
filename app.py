# ============================================================
# MATH DEPARTMENT STREAMLIT WORKSHOP
# Build a live interactive math explorer in ~30 minutes
# ============================================================
# WORKSHOP OUTLINE:
#   STEP 1 — Hello, Streamlit!        (lines 30–50)
#   STEP 2 — User input / widgets     (lines 55–80)
#   STEP 3 — Math + LaTeX rendering   (lines 85–110)
#   STEP 4 — Interactive plot         (lines 115–155)
#   STEP 5 — Data table               (lines 160–180)
#   BONUS  — Sidebar + layout         (lines 185–end)
# ============================================================

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ── page config (must be first Streamlit call) ──────────────
st.set_page_config(
    page_title="Math Explorer",
    page_icon="📐",
    layout="wide",
)

# ============================================================
# STEP 1 — Hello, Streamlit!
# Run:  streamlit run app.py
# ============================================================

st.title("📐 Math Function Explorer")
st.write("An interactive app built during the Streamlit Workshop.")

# st.write() accepts plain text, markdown, numbers, and dataframes
st.markdown("""
Welcome! Use the controls in the **sidebar** to explore different functions.
Streamlit reruns this entire script every time you interact with a widget —
that's the whole secret to how it works.
""")

# ============================================================
# STEP 2 — User input / widgets
# ============================================================

st.sidebar.header("⚙️ Controls")

# Dropdown: choose a function
func_name = st.sidebar.selectbox(
    "Function",
    ["sin", "cos", "tan", "exp decay", "polynomial"],
)

# Sliders: domain and resolution
x_min = st.sidebar.slider("x minimum", -4 * np.pi, 0.0, -2 * np.pi, step=0.1)
x_max = st.sidebar.slider("x maximum", 0.0, 4 * np.pi, 2 * np.pi, step=0.1)
n_points = st.sidebar.slider("Points", 50, 2000, 500, step=50)

# Extra parameters shown conditionally
if func_name == "polynomial":
    degree = st.sidebar.slider("Degree", 1, 8, 3)
elif func_name == "exp decay":
    decay = st.sidebar.slider("Decay constant λ", 0.1, 3.0, 1.0, step=0.1)
else:
    amplitude = st.sidebar.slider("Amplitude A", 0.1, 5.0, 1.0, step=0.1)
    frequency = st.sidebar.slider("Frequency ω", 0.1, 5.0, 1.0, step=0.1)

# ============================================================
# STEP 3 — Math + LaTeX rendering
# ============================================================

st.header("Function Definition")

x = np.linspace(x_min, x_max, n_points)

if func_name == "sin":
    y = amplitude * np.sin(frequency * x)
    st.latex(r"f(x) = A \sin(\omega x)")
    st.write(f"A = {amplitude},  ω = {frequency}")

elif func_name == "cos":
    y = amplitude * np.cos(frequency * x)
    st.latex(r"f(x) = A \cos(\omega x)")
    st.write(f"A = {amplitude},  ω = {frequency}")

elif func_name == "tan":
    y = amplitude * np.tan(frequency * x)
    y = np.where(np.abs(y) > 20, np.nan, y)   # clip near asymptotes
    st.latex(r"f(x) = A \tan(\omega x)")
    st.write(f"A = {amplitude},  ω = {frequency}")

elif func_name == "exp decay":
    x_pos = np.linspace(0, x_max if x_max > 0 else 4, n_points)
    y = np.exp(-decay * x_pos)
    x = x_pos
    st.latex(r"f(x) = e^{-\lambda x}")
    st.write(f"λ = {decay}")

else:  # polynomial
    coeffs = np.random.default_rng(42).uniform(-1, 1, degree + 1)
    y = np.polyval(coeffs, x)
    terms = " + ".join([f"{c:.2f}x^{{{degree - i}}}" for i, c in enumerate(coeffs)])
    st.latex(rf"f(x) = {terms}")

# ============================================================
# STEP 4 — Interactive plot
# ============================================================

st.header("Plot")

col1, col2 = st.columns([3, 1])   # 3:1 split

with col1:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, color="#4C72B0", linewidth=2)
    ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")
    ax.axvline(0, color="gray", linewidth=0.8, linestyle="--")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"{func_name}  ({n_points} points)")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

with col2:
    st.metric("Min", f"{np.nanmin(y):.3f}")
    st.metric("Max", f"{np.nanmax(y):.3f}")
    st.metric("Mean", f"{np.nanmean(y):.3f}")
    st.metric("Std dev", f"{np.nanstd(y):.3f}")

# ============================================================
# STEP 5 — Data table
# ============================================================

st.header("Sample Values")

with st.expander("Show data table (first 20 rows)"):
    df = pd.DataFrame({"x": x, "f(x)": y}).dropna().head(20)
    st.dataframe(df.style.format({"x": "{:.4f}", "f(x)": "{:.4f}"}))

    csv = df.to_csv(index=False)
    st.download_button("⬇️ Download CSV", csv, "data.csv", "text/csv")

# ============================================================
# BONUS — Extra info in sidebar
# ============================================================

st.sidebar.markdown("---")
st.sidebar.info(
    "**Tip:** Every widget interaction reruns this script from top to bottom. "
    "That's all Streamlit does — no callbacks, no state machines."
)

st.sidebar.markdown("---")
st.sidebar.markdown("Built at the **Math Department Streamlit Workshop**")

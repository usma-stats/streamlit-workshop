# D/Math Streamlit Workshop

Build a live interactive math app in 30 minutes — no web experience needed.

---

## How this repo is organized

```
streamlit-workshop/
├── app.py                        ← completed reference app (Math Function Explorer)
├── requirements.txt              ← Python dependencies
├── shells/
│   ├── activity_1_guided.py      ← ★☆☆  fill-in-the-blank sine wave explorer
│   ├── activity_2_stats.py       ← ★★☆  statistics dashboard with more blanks
│   └── activity_3_challenge.py   ← ★★★  blank canvas, 5 mission prompts
└── README.md                     ← you are here
```

**Suggested path through the workshop:**
1. **Setup** — install Python + dependencies (below)
2. **Brief** — instructor walks through `app.py` live, section by section
3. **Lab** — participants open a `shells/` file and fill in the blanks
4. **Deploy** — push to GitHub and share a public URL via Streamlit Cloud

---

## Setup (do this before the workshop)

### 1. Install Python
Download from **python.org/downloads** — choose Python 3.11 or 3.12.
During install on Windows, **check "Add Python to PATH"**.

### 2. Get the workshop files

**Option A — download zip (no git needed):**
Go to **github.com/usma-stats/streamlit-workshop** → click **Code → Download ZIP** → unzip anywhere.

**Option B — git clone:**
```bash
git clone https://github.com/usma-stats/streamlit-workshop.git
cd streamlit-workshop
```

### 3. Install dependencies
Open a terminal (Command Prompt on Windows, Terminal on Mac) inside the folder:
```bash
pip install -r requirements.txt
```

### 4. Verify everything works
```bash
streamlit run app.py
```
A browser tab opens at **http://localhost:8501** — your app is live. Close it with `Ctrl+C`.

---

## Part 1 — Brief (instructor-led, ~30 min)

The instructor walks through `app.py` live. Each section is marked with a `# STEP N` comment:

| Step | Time | Topic | Key commands |
|------|------|-------|--------------|
| 1 | 0–5 min | Hello, Streamlit | `st.title`, `st.write`, `st.markdown` |
| 2 | 5–15 min | Widgets | `st.selectbox`, `st.slider` |
| 3 | 15–20 min | Math rendering | `st.latex` |
| 4 | 20–28 min | Interactive plot | `st.pyplot`, `st.columns`, `st.metric` |
| 5 | 28–30 min | Data table | `st.dataframe`, `st.download_button` |
| Bonus | — | Polish | sidebar, `st.expander` |

**Key idea to emphasize:** Streamlit reruns the entire script top-to-bottom on every widget interaction. No callbacks, no state machines — that's the whole model.

---

## Part 2 — Lab Activities (self-paced)

Open a file from the `shells/` folder and fill in the blanks.
Look for `### YOUR CODE HERE ###` (something missing) and `# FIX-ME:` (something wrong).
Use `app.py` and the Quick Reference below when stuck.

| File | Difficulty | What you build |
|------|-----------|----------------|
| `shells/activity_1_guided.py` | ★☆☆ Guided | Sine wave explorer — sliders, fix the formula, LaTeX, plot, metric |
| `shells/activity_2_stats.py` | ★★☆ Intermediate | Statistics dashboard — generate data, histogram, fix 4 stats, download button |
| `shells/activity_3_challenge.py` | ★★★ Challenge | Free build — Taylor series, projectile motion, grade curve, Fourier series, or your own idea |

```bash
# run any activity directly:
streamlit run shells/activity_1_guided.py
```

Start with Activity 1. Move to 2 or 3 if you finish early or want a harder challenge.

---

## Part 3 — Deploy to the web (free)

Once your app is working locally, share it with the world in a few minutes:

1. Push your code to a **public GitHub repo**.
2. Go to **share.streamlit.io** and sign in with GitHub.
3. Select your repo, set the main file to `app.py`, click **Deploy**.

You get a permanent public URL — no server, no cost.

---

## Quick Reference

```python
# ── Text ────────────────────────────────────────────────────
st.title("Big heading")
st.header("Section heading")
st.markdown("**bold**, _italic_, inline $LaTeX$, or ---")
st.latex(r"\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}")

# ── Widgets (each returns a value) ─────────────────────────
x      = st.slider("Label", min_val, max_val, default)
choice = st.selectbox("Label", ["A", "B", "C"])
on     = st.checkbox("Enable feature")
text   = st.text_input("Enter something")
n      = st.number_input("Integer", min_value=0, value=10, step=1)

# ── Layout ──────────────────────────────────────────────────
col1, col2 = st.columns(2)          # equal columns
col1, col2 = st.columns([3, 1])     # 3:1 ratio
with col1:
    st.write("Left column")

st.sidebar.slider(...)              # put any widget in the sidebar

with st.expander("Click to expand"):
    st.write("Hidden until clicked")

# ── Charts ──────────────────────────────────────────────────
st.pyplot(fig)                      # matplotlib figure
st.plotly_chart(fig)                # plotly figure
st.line_chart(df)                   # quick built-in (no setup needed)

# ── Data & metrics ──────────────────────────────────────────
st.dataframe(df)
st.metric("Label", value, delta)    # delta shows +/- change in green/red
st.download_button("⬇️ Download", data, "filename.csv", "text/csv")
```

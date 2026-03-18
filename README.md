# Math Department Streamlit Workshop

Build a live interactive math app in 30 minutes — no web experience needed.

---

## Setup (do this before the workshop)

### 1. Install Python
Download from **python.org/downloads** — choose Python 3.11 or 3.12.
During install, **check "Add Python to PATH"**.

### 2. Get the workshop files

**Option A — download zip (no git needed):**
Go to the GitHub repo → click **Code → Download ZIP** → unzip anywhere.

**Option B — git clone (if you have git):**
```bash
git clone https://github.com/YOUR_USERNAME/streamlit-workshop.git
cd streamlit-workshop
```

### 3. Install dependencies
Open a terminal (Command Prompt on Windows, Terminal on Mac) in the folder:
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```
A browser tab opens automatically at **http://localhost:8501** — your app is live.

---

## Workshop flow

| Time | Topic | What you'll add |
|------|-------|-----------------|
| 0–5 min | Hello, Streamlit | `st.title`, `st.write`, `st.markdown` |
| 5–15 min | Widgets | `st.selectbox`, `st.slider` |
| 15–20 min | Math rendering | `st.latex` |
| 20–28 min | Plot | `matplotlib` + `st.pyplot`, `st.columns` |
| 28–30 min | Data table | `st.dataframe`, `st.download_button` |
| Bonus | Polish | sidebar, `st.expander`, `st.metric` |

All sections are marked with `# STEP N` comments inside `app.py`.

---

## Deploying to the web (free)

1. Push your repo to GitHub (public).
2. Go to **share.streamlit.io** → sign in with GitHub.
3. Select your repo and `app.py` → click **Deploy**.

Your app gets a public URL you can share in minutes — no server required.

---

## Quick reference

```python
# Text
st.title("Big heading")
st.header("Section heading")
st.markdown("**bold**, _italic_, or $LaTeX$")
st.latex(r"\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}")

# Widgets (return a value)
x = st.slider("Label", min, max, default)
choice = st.selectbox("Label", ["A", "B", "C"])
checked = st.checkbox("Enable feature")
text = st.text_input("Enter something")

# Layout
col1, col2 = st.columns(2)
with col1:
    st.write("Left column")

with st.sidebar:
    st.write("This appears in the sidebar")

with st.expander("Click to expand"):
    st.write("Hidden content")

# Charts
st.pyplot(fig)          # matplotlib figure
st.plotly_chart(fig)    # plotly figure
st.line_chart(df)       # quick built-in chart

# Data
st.dataframe(df)
st.metric("Label", value, delta)
st.download_button("Download", data, filename)
```

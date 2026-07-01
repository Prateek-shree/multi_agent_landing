import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AgentMatrix · Project Summary",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #FFFFFF;
}

.stApp {
    background: #0a0a0f;
    background-image:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(124,77,255,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 110%, rgba(255,80,30,0.08) 0%, transparent 55%);
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem; max-width: 1200px; }

/* ── Hero ── */
.hero { text-align: center; padding: 4rem 0 2rem; }
.hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem; font-weight: 500; letter-spacing: 0.25em;
    text-transform: uppercase; color: #7C4DFF; margin-bottom: 1rem; opacity: 0.9;
}
.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 6vw, 5.2rem);
    font-weight: 800; line-height: 1.0; letter-spacing: -0.03em;
    color: #FFFFFF; margin: 0 0 1.2rem;
}
.hero h1 span { color: #7C4DFF; }
.hero-sub {
    font-size: 1.1rem; font-weight: 300; color: #a09890;
    max-width: 640px; margin: 0 auto; line-height: 1.7;
    text-align: center;
}

.cta-wrap { text-align: center; margin: 2rem 0 1rem; }
div[data-testid="stLinkButton"],
div[data-testid="stButton"] {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
}
.stLinkButton, .stButton { display: flex; justify-content: center; }
.stButton > button, .stLinkButton > a, div[data-testid="stLinkButton"] a {
    background: linear-gradient(135deg, #7C4DFF 0%, #5C2ED6 100%) !important;
    color: #0a0a0f !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.03em !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.9rem 2.6rem !important;
    cursor: pointer !important;
    box-shadow: 0 4px 24px rgba(124,77,255,0.35) !important;
    transition: transform 0.15s, box-shadow 0.15s !important;
    text-decoration: none !important;
    display: inline-block !important;
    margin: 0 auto !important;
}
.stButton > button:hover, .stLinkButton > a:hover, div[data-testid="stLinkButton"] a:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 32px rgba(124,77,255,0.45) !important;
    color: #0a0a0f !important;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,77,255,0.3), transparent);
    margin: 2.5rem 0;
}

/* ── Section heading ── */
.section-eyebrow {
    font-family: 'DM Mono', monospace; font-size: 0.7rem; font-weight: 500;
    letter-spacing: 0.2em; text-transform: uppercase; color: #7C4DFF;
    text-align: center; margin-bottom: 0.6rem;
}
.section-heading {
    font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 700;
    color: #FFFFFF; text-align: center; margin: 0 0 3rem;
}

/* ── Stat cards ── */
.stat-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(124,77,255,0.18);
    border-radius: 14px;
    padding: 1.4rem 1rem;
    text-align: center;
}
.stat-num {
    font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.9rem; color: #7C4DFF;
}
.stat-label {
    font-family: 'DM Mono', monospace; font-size: 0.68rem; letter-spacing: 0.1em;
    text-transform: uppercase; color: #a09890; margin-top: 0.3rem;
}

/* ── Workflow flow ── */
.agent-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(124,77,255,0.18);
    border-radius: 16px;
    padding: 1.8rem 1.6rem;
    height: 340px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    position: relative;
    backdrop-filter: blur(8px);
    transition: transform 0.2s, border-color 0.2s;
}
.agent-card:hover { transform: translateY(-4px); border-color: rgba(124,77,255,0.45); }
.agent-num {
    font-family: 'DM Mono', monospace; font-size: 0.68rem; letter-spacing: 0.15em;
    color: #7C4DFF; opacity: 0.75; margin-bottom: 0.6rem;
}
.agent-icon { font-size: 1.8rem; margin-bottom: 0.6rem; }
.agent-title {
    font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.05rem;
    color: #FFFFFF; margin-bottom: 0.5rem;
}
.agent-desc { font-size: 0.85rem; color: #a09890; line-height: 1.55; margin-bottom: 0.9rem; flex-grow: 1; }
.agent-tool {
    display: inline-block;
    font-family: 'DM Mono', monospace; font-size: 0.65rem;
    background: rgba(124,77,255,0.08); border: 1px solid rgba(124,77,255,0.2);
    color: #7C4DFF; padding: 0.2rem 0.55rem; border-radius: 6px;
}
.flow-arrow {
    display: flex; align-items: center; justify-content: center;
    color: #7C4DFF; font-size: 1.4rem; opacity: 0.6; height: 100%;
}

/* ── Feature / build cards ── */
.feature-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 1.6rem 1.5rem;
    height: 100%;
}
.feature-icon { font-size: 1.5rem; margin-bottom: 0.7rem; }
.feature-title {
    font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.98rem;
    color: #FFFFFF; margin-bottom: 0.4rem;
}
.feature-desc { font-size: 0.85rem; color: #a09890; line-height: 1.6; }

/* ── Tech stack pills ── */
.stack-wrap { display: flex; flex-wrap: wrap; gap: 0.6rem; justify-content: center; margin-bottom: 1rem; }
.stack-pill {
    font-family: 'DM Mono', monospace; font-size: 0.78rem;
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1);
    color: #FFFFFF; padding: 0.4rem 1rem; border-radius: 999px;
}

/* ── Report panel (sample output structure) ── */
.report-panel {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(124,77,255,0.2);
    border-radius: 16px;
    padding: 1.8rem 2rem;
}
.panel-label {
    font-family: 'DM Mono', monospace; font-size: 0.7rem; letter-spacing: 0.2em;
    text-transform: uppercase; color: #7C4DFF; margin-bottom: 1.2rem;
    padding-bottom: 0.7rem; border-bottom: 1px solid rgba(124,77,255,0.15);
}
.report-item {
    font-size: 0.88rem; color: #FFFFFF; line-height: 1.9;
}
.report-item b { color: #FFFFFF; }

.notice {
    font-family: 'DM Mono', monospace; font-size: 0.72rem; color: #605850;
    text-align: center; margin-top: 3rem; letter-spacing: 0.08em;
}
</style>
""", unsafe_allow_html=True)


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">Project Summary</div>
    <h1>AGENT&nbsp;&nbsp;<span>MATRIX</span></h1>
    <p class="hero-sub" style="text-align:center; margin-left:auto; margin-right:auto;">
        A multi-agent AI research system I built with LangChain and Mistral AI.
        Four agents work in sequence — searching the live web, reading the best
        source, drafting a structured report, and critiquing their own output —
        wrapped in a Streamlit interface.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="cta-wrap">', unsafe_allow_html=True)
col_l, col_c, col_r = st.columns([1, 1, 1])
with col_c:
    st.link_button(
        "🚀  Open Live Project",
        "https://multi-agent-system-26.streamlit.app/",
        use_container_width=True,
    )
st.markdown('</div>', unsafe_allow_html=True)

# ── Quick stats ───────────────────────────────────────────────────────────────
stats = [("4", "AI Agents"), ("2", "External APIs"), ("1", "LLM Backbone"), ("100%", "Automated Pipeline")]
stat_cols = st.columns(4)
for col, (num, label) in zip(stat_cols, stats):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-num">{num}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Pipeline / What it does ─────────────────────────────────────────────────
st.markdown('<div class="section-eyebrow">The Pipeline</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Four Agents, One Workflow</div>', unsafe_allow_html=True)

agents = [
    ("01", "🔍", "Search Agent", "A LangChain agent wired to a custom Tavily search tool. Given a topic, it finds recent, relevant URLs with titles and snippets.", "Tavily API"),
    ("02", "📄", "Reader Agent", "A second agent that takes the search output, picks the most relevant link, and scrapes the page with BeautifulSoup for deeper context.", "BeautifulSoup"),
    ("03", "✍️", "Writer Chain", "A prompt chain that combines both agents' findings into a structured report: Introduction, Key Findings, Conclusion, and Sources.", "Mistral Large"),
    ("04", "🧐", "Critic Chain", "A final chain that reviews the report and returns a numeric score, strengths, areas to improve, and a one-line verdict.", "Mistral Large"),
]

cols = st.columns([1, 0.15, 1, 0.15, 1, 0.15, 1])
card_cols = [cols[0], cols[2], cols[4], cols[6]]
arrow_cols = [cols[1], cols[3], cols[5]]

for i, (num, icon, title, desc, tool) in enumerate(agents):
    with card_cols[i]:
        st.markdown(f"""
        <div class="agent-card">
            <div class="agent-num">STEP {num}</div>
            <div class="agent-icon">{icon}</div>
            <div class="agent-title">{title}</div>
            <div class="agent-desc">{desc}</div>
            <span class="agent-tool">{tool}</span>
        </div>
        """, unsafe_allow_html=True)
    if i < 3:
        with arrow_cols[i]:
            st.markdown('<div class="flow-arrow">→</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── What I built ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-eyebrow">Engineering Highlights</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">What I Built</div>', unsafe_allow_html=True)

features = [
    ("🧩", "Modular Agent Design", "Search and reading logic are separate LangChain agents, each with one dedicated tool, instead of one monolithic prompt."),
    ("🛠️", "Custom Tools", "Wrote two custom @tool functions — a Tavily-backed web_search and a BeautifulSoup-backed scrape_url — for real-world grounding."),
    ("🔗", "Chained Prompts", "Writer and Critic steps are LangChain prompt | llm | parser chains, keeping report generation and review decoupled and swappable."),
    ("🖥️", "Live Streamlit UI", "Built a stateful Streamlit front end with step-by-step progress cards, expandable raw outputs, and a markdown report download."),
]

fcols = st.columns(4)
for col, (icon, title, desc) in zip(fcols, features):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Tech stack ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-eyebrow">Under the Hood</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Tech Stack</div>', unsafe_allow_html=True)

stack = ["LangChain", "Mistral AI (mistral-large-latest)", "Tavily Search API",
         "BeautifulSoup4", "Streamlit", "Python-dotenv", "Pydantic"]
pills = "".join(f'<span class="stack-pill">{s}</span>' for s in stack)
st.markdown(f'<div class="stack-wrap">{pills}</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Report structure preview ─────────────────────────────────────────────────
st.markdown('<div class="section-eyebrow">Output Format</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">What the Pipeline Produces</div>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""
    <div class="report-panel">
        <div class="panel-label">📝 Research Report</div>
        <div class="report-item">
            <b>Introduction</b> — frames the topic<br>
            <b>Key Findings</b> — 3+ explained points<br>
            <b>Conclusion</b> — summarizes takeaways<br>
            <b>Sources</b> — every URL used
        </div>
    </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown("""
    <div class="report-panel">
        <div class="panel-label">🧐 Critic Feedback</div>
        <div class="report-item">
            <b>Score</b> — out of 10<br>
            <b>Strengths</b> — what worked<br>
            <b>Areas to Improve</b> — gaps found<br>
            <b>Verdict</b> — one-line summary
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="notice">
    AGENT MATRIX · Project built with LangChain, Mistral AI &amp; Streamlit
</div>
""", unsafe_allow_html=True)
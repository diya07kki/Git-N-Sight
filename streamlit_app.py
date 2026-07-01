import streamlit as st
from theme import apply_theme
from utils import svg

from github_api import (
    get_profile,
    get_repositories
)

from analytics import (
    github_score,
    developer_level,
    repository_dataframe,
    repository_spotlight,
    generate_insights
)

from charts import (
    language_pie_chart,
    stars_bar_chart,
    forks_bar_chart,
    repo_size_chart
)

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="GitNSight",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_theme()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.image(
        "assets/logo.png",
        width=500
    )

    st.title("GitNSight")

    st.caption("Developer Intelligence Platform")

    st.divider()

    username = st.text_input(
        "GitHub Username",
        placeholder="e.g. torvalds"
    )

    analyze = st.button(
        "Analyze Profile",
        use_container_width=True
    )

    st.divider()

    with st.expander("ℹ About"):

        st.write("GitNSight v1.0")

        st.write(
            """
A GitHub analytics dashboard that visualizes
developer statistics, repository insights
and portfolio metrics.
"""
        )

        st.write("Built using:")

        st.markdown("""
- Python
- Streamlit
- Plotly
- GitHub REST API
""")

# ---------------------------------------------------
# Hero
# ---------------------------------------------------

# ---------------------------------------------------
# Hero
# ---------------------------------------------------

logo, text = st.columns([1, 6])

with logo:
    st.image(
        "assets/logo.png",
        width=120
    )

with text:
    st.markdown("""
    <div class="hero">

    <h1>GitNSight</h1>

    <p>

    Developer Intelligence Platform

    <br><br>

    Understand your GitHub profile through
    interactive analytics,
    beautiful charts,
    and portfolio insights.

    </p>

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# Wait for Search
# ---------------------------------------------------

if not analyze:
    st.info(" Enter a GitHub username in the sidebar to begin.")
    st.stop()

# ---------------------------------------------------
# Fetch Data
# ---------------------------------------------------

with st.spinner("Fetching GitHub profile..."):

    profile = get_profile(username)

    if profile is None:

        st.error("GitHub user not found.")

        st.stop()

    repos = get_repositories(username)

score = github_score(
    profile,
    repos
)

# ---------------------------------------------------
# Profile
# ---------------------------------------------------

left, right = st.columns([1,3])

with left:

    st.image(
        profile["avatar_url"],
        width=220
    )

with right:

    display_name = (
        profile["name"]
        if profile["name"]
        else profile["login"]
    )

    st.markdown(f"# {display_name}")

    st.caption(
        f"@{profile['login']}"
    )

    if profile["bio"]:

        st.write(profile["bio"])

    info1, info2, info3 = st.columns(3)

    with info1:
        st.metric(
            "Followers",
            profile["followers"]
        )

    with info2:
        st.metric(
            "Following",
            profile["following"]
        )

    with info3:
        st.metric(
            "Repositories",
            profile["public_repos"]
        )

    st.link_button(
        "🌐 View GitHub Profile",
        profile["html_url"],
        use_container_width=True
    )

st.divider()

# ---------------------------------------------------
# Developer Snapshot
# ---------------------------------------------------

col1, col2 = st.columns([1, 20])

with col1:
    svg("assets/insight.svg", width=28)

with col2:
    st.subheader("Developer Snapshot")

snapshot = []

languages = {}

for repo in repos:

    lang = repo["language"]

    if lang:

        languages[lang] = (
            languages.get(lang,0)+1
        )

if languages:

    primary = max(
        languages,
        key=languages.get
    )

    snapshot.append(
        f"Primary language: **{primary}**"
    )

snapshot.append(
    f"Public repositories: **{profile['public_repos']}**"
)

snapshot.append(
    f"GitNSight Score: **{score}/100**"
)

st.info(
    " • ".join(snapshot)
)

st.divider()

# ---------------------------------------------------
# Dashboard Metrics
# ---------------------------------------------------

col1, col2 = st.columns([1, 20])

with col1:
    svg("assets/dashboard.svg", width=28)

with col2:
    st.subheader("Dashboard Overview")

c1, c2, c3, c4 = st.columns(4)

total_stars = sum(repo["stargazers_count"] for repo in repos)
total_forks = sum(repo["forks_count"] for repo in repos)

with c1:
    st.metric("⭐ Total Stars", total_stars)

with c2:
    st.metric("🍴 Total Forks", total_forks)

with c3:
    st.metric("🏆 GitNSight Score", score)

with c4:
    st.metric("🎖 Level", developer_level(score))

st.divider()

# ---------------------------------------------------
# Repository Spotlight
# ---------------------------------------------------

col1, col2 = st.columns([1, 20])

with col1:
    svg("assets/star.svg", width=28)

with col2:
    st.subheader("Repository Spotlight")

st.info(repository_spotlight(repos))

st.divider()

# ---------------------------------------------------
# Charts
# ---------------------------------------------------

col1, col2 = st.columns([1, 20])

with col1:
    svg("assets/chart.svg", width=28)

with col2:
    st.subheader("Repository Analytics")

left, right = st.columns(2)

with left:
    st.plotly_chart(
        language_pie_chart(repos),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        stars_bar_chart(repos),
        use_container_width=True
    )

left, right = st.columns(2)

with left:
    st.plotly_chart(
        forks_bar_chart(repos),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        repo_size_chart(repos),
        use_container_width=True
    )

st.divider()

# ---------------------------------------------------
# Repository Explorer
# ---------------------------------------------------

col1, col2 = st.columns([1, 20])

with col1:
    svg("assets/file.svg", width=28)

with col2:
    st.subheader("Repository Explorer")

df = repository_dataframe(repos)

search = st.text_input(
    "🔎 Search repository...",
    placeholder="Type repository name..."
)

if search:

    df = df[
        df["Repository"].str.contains(
            search,
            case=False
        )
    ]

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.download_button(
    "⬇ Download CSV",
    df.to_csv(index=False),
    "repositories.csv",
    "text/csv",
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# Developer Insights
# ---------------------------------------------------

col1, col2 = st.columns([1, 20])

with col1:
    svg("assets/explore.svg", width=28)

with col2:
    st.subheader("Developer Insights")

insights = generate_insights(
    profile,
    repos
)

for item in insights:
    st.markdown(
        f"""
> {item}
"""
    )


# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("""
<div class="footer">
GitNSight • Developer Intelligence Platform • Powered by GitHub REST API
</div>
""", unsafe_allow_html=True)
from collections import Counter
import plotly.express as px


def language_pie_chart(repos):
    """Create a pie chart showing language distribution."""

    counter = Counter()

    for repo in repos:
        language = repo["language"] if repo["language"] else "Unknown"
        counter[language] += 1

    fig = px.pie(
        names=list(counter.keys()),
        values=list(counter.values()),
        hole=0.45,
        title="Programming Languages"
    )

    fig.update_layout(
        template="plotly_dark",
        legend_title="Language"
    )

    return fig


def stars_bar_chart(repos):
    """Create a bar chart for stars."""

    names = [repo["name"] for repo in repos]
    stars = [repo["stargazers_count"] for repo in repos]

    fig = px.bar(
        x=names,
        y=stars,
        title="Repository Stars"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Repository",
        yaxis_title="Stars"
    )

    return fig


def forks_bar_chart(repos):
    """Create a bar chart for forks."""

    names = [repo["name"] for repo in repos]
    forks = [repo["forks_count"] for repo in repos]

    fig = px.bar(
        x=names,
        y=forks,
        orientation="h",
        title="Repository Forks"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Repository",
        yaxis_title="Forks"
    )

    return fig


def repo_size_chart(repos):
    """Create a bar chart for repository size."""

    names = [repo["name"] for repo in repos]
    sizes = [repo["size"] for repo in repos]

    fig = px.bar(
        x=names,
        y=sizes,
        orientation="h",
        title="Repository Size (KB)"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Repository",
        yaxis_title="Size (KB)"
    )

    return fig
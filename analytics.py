from collections import Counter
import pandas as pd
from datetime import datetime


def repository_dataframe(repos):
    """Convert repository data into a pandas DataFrame."""

    data = []

    for repo in repos:
        data.append({
            "Repository": repo["name"],
            "Language": repo["language"] if repo["language"] else "Unknown",
            "Stars": repo["stargazers_count"],
            "Forks": repo["forks_count"],
            "Size (KB)": repo["size"],
            "Created": repo["created_at"][:10],
            "Updated": repo["updated_at"][:10]
        })

    return pd.DataFrame(data)


def language_statistics(repos):
    """Count repositories by programming language."""

    counter = Counter()

    for repo in repos:
        if repo["language"]:
            counter[repo["language"]] += 1

    return counter


def github_score(profile, repos):
    """
    GitNSight Score (0–100)

    This is our own scoring system.
    """

    score = 0

    score += min(profile["followers"] * 2, 20)
    score += min(profile["public_repos"] * 2, 20)

    total_stars = sum(r["stargazers_count"] for r in repos)
    score += min(total_stars, 30)

    total_forks = sum(r["forks_count"] for r in repos)
    score += min(total_forks * 2, 20)

    current_year = str(datetime.now().year)

    active = sum(
        1
        for r in repos
        if r["updated_at"][:4] == current_year
    )

    score += min(active, 10)

    return min(score, 100)


def developer_level(score):
    """Return a developer level based on score."""

    if score < 20:
        return "🌱 Beginner"

    elif score < 40:
        return "🚀 Explorer"

    elif score < 60:
        return "💻 Builder"

    elif score < 80:
        return "🔥 Advanced Developer"

    else:
        return "👑 Git Master"


def repository_spotlight(repos):
    """Return the most starred repository."""

    if not repos:
        return "No repositories found."

    best = max(
        repos,
        key=lambda x: x["stargazers_count"]
    )

    return (
        f"**{best['name']}**\n\n"
        f"⭐ Stars: {best['stargazers_count']}\n\n"
        f"🍴 Forks: {best['forks_count']}\n\n"
        f"💻 Language: {best['language']}"
    )


def generate_insights(profile, repos):
    """Generate GitNSight insights."""

    insights = []

    languages = language_statistics(repos)

    if languages:
        lang = languages.most_common(1)[0][0]
        insights.append(
            f"💻 Most repositories are written in **{lang}**."
        )

    if repos:
        biggest = max(
            repos,
            key=lambda x: x["size"]
        )

        insights.append(
            f"📦 Largest repository: **{biggest['name']}** ({biggest['size']} KB)."
        )

        latest = max(
            repos,
            key=lambda x: x["updated_at"]
        )

        insights.append(
            f"🆕 Most recently updated repository: **{latest['name']}**."
        )

    if profile["followers"] == 0:
        insights.append(
            "📢 Consider sharing your projects to grow your GitHub audience."
        )

    if profile["public_repos"] >= 10:
        insights.append(
            "🏆 Great! You have a diverse portfolio of repositories."
        )
    else:
        insights.append(
            "📁 Adding more quality repositories will strengthen your GitHub profile."
        )

    return insights
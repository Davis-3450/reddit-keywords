import json
from pathlib import Path

from typer import Typer

from app.UI.web import web_ui
from app.utils.exceptions import SubredditNotFound
from app.utils.print import p

app = Typer()


@app.command()
def help() -> None:
    pass


@app.command()
def web() -> None:
    web_ui()


@app.command()
def cli(
    subreddit: str,
    #  keywords: str,
    include_comments: bool = True,
    filter_comments: bool = True,
    limit: int = 1000,
    source: str = "keywords.txt",
    max_chars: int = 10000000,
) -> None:
    """Scrape posts from a subreddit based on keywords.

    Args:
        subreddit (str): The subreddit to scrape posts from.
        include_comments (bool, optional): Whether to include comments in the posts. Defaults to True.
        filter_comments (bool, optional): Whether to filter comments. Defaults to True.
        limit (int, optional): The maximum number of posts to scrape. Defaults to 1000.
        source (str, optional): The source file to read keywords from. Defaults to "keywords.txt".
        max_length (int, optional): The maximum output lenght.

    Raises:
        SubredditNotFound: If the subreddit is not found.
    """
    # src = Source(source)
    # keywords = src.keywords or []
    from app.client.base import scraper

    if not scraper.validate_existence(subreddit):
        p.error(f"Subreddit '{subreddit}' not found.")
        raise SubredditNotFound()

    for post in scraper.explore_posts_by_keyword(
        subreddit=subreddit,
        keywords=["ftm"],
        include_comments=True,
        max_chars=max_chars,
    ):
        FILE = Path(f"{subreddit}.json")
        with FILE.open("a") as f:
            json.dump(post.out(), f)

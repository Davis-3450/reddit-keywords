from dataclasses import asdict
from pprint import pprint

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
) -> None:
    # src = Source(source)
    # keywords = src.keywords or []
    from app.client.base import scraper

    if not scraper.validate_existence(subreddit):
        p.error(f"Subreddit '{subreddit}' not found.")
        raise SubredditNotFound()

    for post in scraper.explore_posts_by_keyword(
        subreddit=subreddit,
        keywords=["a"],
        include_comments=True,
    ):
        pprint(asdict(post))

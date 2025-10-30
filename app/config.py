from enum import Enum
from os import getenv

from dotenv import load_dotenv

from app.models import UiMode

load_dotenv()


class Config:
    mode: UiMode = UiMode.TYPER
    debug: bool = False
    verbose: bool = False


class RedditAccount:
    username: str | None = getenv("REDDIT_USERNAME") or None
    client_id: str | None = getenv("REDDIT_CLIENT_ID") or None
    client_secret: str | None = getenv("REDDIT_CLIENT_SECRET") or None
    password: str | None = getenv("REDDIT_PASSWORD") or None
    user_agent: str | None = getenv("REDDIT_USER_AGENT") or "reddit-keywords-bot/0.1"


class Blacklist(str, Enum):
    """Tipos de blacklist."""

    SUBREDDITS = "[removed]"
    USERS = "[deleted]"

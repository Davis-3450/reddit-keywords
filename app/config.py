from dataclasses import dataclass
from enum import Enum
from os import getenv

from dotenv import load_dotenv

from app.models import UiMode

load_dotenv()


@dataclass
class Config:
    mode: UiMode = UiMode.TYPER
    debug: bool = False
    verbose: bool = False


class RedditAccount:
    username: str | None = getenv("REDDIT_USERNAME")
    client_id: str | None = getenv("REDDIT_CLIENT_ID")
    client_secret: str | None = getenv("REDDIT_CLIENT_SECRET")
    password: str | None = getenv("REDDIT_PASSWORD")
    user_agent: str | None = getenv("REDDIT_USER_AGENT") or "reddit-keywords-bot/0.1"


class RemovedValues(str, Enum):
    REMOVED = "[removed]"
    DELETED = "[deleted]"

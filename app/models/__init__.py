from dataclasses import dataclass
from enum import Enum


class UiMode(str, Enum):
    TYPER = "typer"
    GRADIO = "gradio"


@dataclass
class Comment:
    body: str
    comments: list["Comment"] | None = None


@dataclass
class Post:
    title: str
    url: str | None = None
    body: str | None = None
    comments: list[Comment] | None = None

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class UiMode(str, Enum):
    TYPER = "typer"
    GRADIO = "gradio"


@dataclass
class Comment:
    body: str
    comments: Optional[list["Comment"]] = None


@dataclass
class Post:
    title: str
    url: str | None = None
    body: str | None = None
    comments: Optional[list["Comment"]] = None

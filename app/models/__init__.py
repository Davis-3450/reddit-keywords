from dataclasses import dataclass
from enum import Enum


class UiMode(str, Enum):
    TYPER = "typer"
    GRADIO = "gradio"


@dataclass
class Comment:
    body: str
    comments: list["Comment"] | None = None

    def chars(self) -> int:
        return len(self.body) + (
            sum(c.chars() for c in self.comments) if self.comments else 0
        )


@dataclass
class Post:
    title: str
    url: str | None = None
    body: str | None = None
    comments: list[Comment] | None = None

    def chars(self) -> int:
        return (
            len(self.title)
            + (len(self.body) if self.body else 0)
            + (sum(c.chars() for c in self.comments) if self.comments else 0)
        )

    def out(self) -> dict:
        return {
            "title": self.title,
            "body": self.body,
            "comments": [c.body for c in self.comments] if self.comments else None,
        }

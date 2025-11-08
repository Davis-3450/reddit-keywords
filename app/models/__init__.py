from dataclasses import dataclass
from enum import Enum


class UiMode(str, Enum):
    TYPER = "typer"
    GRADIO = "gradio"


@dataclass
class Comment:
    body: str
    comments: list["Comment"] | None = None

    def __len__(self) -> int:
        return len(self.body) + (
            sum(len(c) for c in self.comments) if self.comments else 0
        )


@dataclass
class Post:
    title: str
    url: str | None = None
    body: str | None = None
    comments: list[Comment] | None = None

    def __len__(self) -> int:
        return (
            len(self.title)
            + (len(self.body) if self.body else 0)
            + (sum(len(c) for c in self.comments) if self.comments else 0)
        )

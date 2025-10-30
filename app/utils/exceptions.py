from dataclasses import dataclass


@dataclass
class AppException(Exception):
    message: str
    pass

    def __str__(self) -> str:
        return self.message


class SourcesNotFound(AppException):
    def __init__(
        self,
        message: str = "No valid source files found. Please provide at least one valid .txt file path.",
    ):
        self.message = message
        super().__init__(self.message)


class SubredditNotFound(AppException):
    def __init__(
        self,
        message: str = "The specified subreddit was not found. Please check the subreddit name and try again.",
    ) -> None:
        self.message = message
        super().__init__(self.message)

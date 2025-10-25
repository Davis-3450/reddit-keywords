class BaseException(Exception):
    pass


class SourcesNotFound(BaseException):
    def __init__(
        self,
        message: str = "No valid source files found. Please provide at least one valid .txt file path.",
    ):
        self.message = message
        super().__init__(self.message)


class SubredditNotFound(BaseException):
    def __init__(
        self,
        message: str = "The specified subreddit was not found. Please check the subreddit name and try again.",
    ):
        self.message = message
        super().__init__(self.message)

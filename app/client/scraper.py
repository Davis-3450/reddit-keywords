from praw import Reddit
from praw.models import Comment as RedditComment
from praw.models import Subreddit
from praw.models.reddit.more import MoreComments

from app.models import Comment as CommentModel
from app.models import Post as PostModel
from app.utils.exceptions import SubredditNotFound


class Scraper:
    def __init__(self, client: Reddit):
        """Initialize Scraper."""
        self.client = client

    def explore_posts_by_keyword(
        self,
        subreddit: str | Subreddit,
        keywords: list[str],
        limit: int = 100,
        include_comments: bool = False,
    ):
        if isinstance(subreddit, str):
            if not self._validate_existence(subreddit):
                raise SubredditNotFound()
            sub: Subreddit = self.client.subreddit(subreddit)
        else:
            sub = subreddit

        query = (
            " ".join(keywords) if isinstance(keywords, (list, tuple)) else str(keywords)
        )

        for post in sub.search(query, limit=limit):
            if include_comments:
                comments: list[CommentModel] = []
                for comment in post.comments.list():
                    comments.append(self._build_comments(comment))

            yield PostModel(title=post.title, url=post.url, body=post.selftext)

    def _build_comments(self, reddit_comment: RedditComment) -> CommentModel:
        comment: CommentModel = CommentModel(body=reddit_comment.body)

        if reddit_comment.replies:
            reddit_comment.replies.replace_more(limit=None)
            comment.comments = []

            for reply in reddit_comment.replies.list():
                if (
                    isinstance(reply, MoreComments)
                    or not hasattr(reply, "body")
                    or not reply.body
                ):
                    continue
                comment.comments.append(self._build_comments(reply))

        return comment

    def _validate_existence(self, subreddit: str) -> bool:
        try:
            self.client.subreddit(subreddit).id
            return True
        except Exception:
            return False

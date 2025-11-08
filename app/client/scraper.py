from typing import Generator

from praw import Reddit
from praw.models import Comment as RedditComment
from praw.models import Subreddit
from praw.models.reddit.more import MoreComments

from app.config import RemovedValues
from app.models import Comment as CommentModel
from app.models import Post as PostModel
from app.utils.exceptions import SubredditNotFound
from app.utils.print import p


class Scraper:
    def __init__(self, client: Reddit):
        """Initialize Scraper."""
        self.client = client

    def explore_posts_by_keyword(
        self,
        subreddit: str | Subreddit,
        keywords: list[str],
        limit: int = 1000,
        include_comments: bool = False,
    ) -> Generator[PostModel, None, None]:
        if isinstance(subreddit, str):
            if not self.validate_existence(subreddit):
                raise SubredditNotFound()
            sub: Subreddit = self.client.subreddit(subreddit)
        else:
            sub = subreddit

        query = (
            " ".join(keywords) if isinstance(keywords, (list, tuple)) else str(keywords)
        )

        for post in sub.search(query, limit=limit):
            post_info = PostModel(title=post.title, url=post.url, body=post.selftext)
            if include_comments:
                comments: list[CommentModel] = []
                for comment in post.comments.list():
                    built = self._build_comments(comment)
                    if built:
                        comments.append(built)
                post_info.comments = comments
            p.info(f"Scraped post: {post_info.title} from r/{sub.display_name}")
            yield post_info

    def _build_comments(
        self,
        reddit_comment: RedditComment | MoreComments,
        # whitelist: set
    ) -> CommentModel | None:
        if isinstance(reddit_comment, MoreComments):
            return None

        if not hasattr(reddit_comment, "body"):
            return None
        body = " ".join(reddit_comment.body.split())

        comment: CommentModel = CommentModel(body=body)
        if reddit_comment.replies:
            reddit_comment.replies.replace_more(limit=None)
            comment.comments = []

            for reply in reddit_comment.replies.list():
                built = self._build_comments(reply)
                if (built and built.body) and not (
                    (RemovedValues.REMOVED in built.body)
                    or (RemovedValues.DELETED in built.body)
                ):
                    comment.comments.append(built)

        if not comment.comments:
            comment.comments = None

        return comment

    def validate_existence(self, subreddit: str) -> bool:
        try:
            self.client.subreddit(subreddit).id
            return True
        except Exception:
            return False

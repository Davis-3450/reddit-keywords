from praw import Reddit

from app.client.scraper import Scraper
from app.config import RedditAccount
from app.utils.print import p

client = Reddit(
    client_id=RedditAccount.client_id,
    client_secret=RedditAccount.client_secret,
    user_agent=RedditAccount.user_agent,
    username=RedditAccount.username,
    password=RedditAccount.password,
)

p.info(f"Reddit Client initialized with user {str(client.user.me())}")
scraper = Scraper(client=client)  # TODO move this

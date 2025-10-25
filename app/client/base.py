import os

from dotenv import load_dotenv
from praw import Reddit

from app.client.scraper import Scraper
from app.utils.print import printer as p

load_dotenv()

client = Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
)

p.info(f"Reddit Client initialized with user {client.user.me()}")
scraper = Scraper(client=client)

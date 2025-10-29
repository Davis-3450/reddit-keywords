from app.models import UiMode


class Config:
    mode: UiMode = UiMode.TYPER
    debug: bool = False
    verbose: bool = False

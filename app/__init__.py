from app.config import Config
from app.models import UiMode
from app.UI.CLI import app as cli_app


def main():
    if Config.mode == UiMode.TYPER:
        cli_app()


if __name__ == "__main__":
    main()

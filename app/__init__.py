from app.models import UiMode
from app.UI.CLI import app as cli_app

app_mode: UiMode = UiMode.TYPER


def main():
    if app_mode == UiMode.TYPER:
        cli_app()


if __name__ == "__main__":
    main()

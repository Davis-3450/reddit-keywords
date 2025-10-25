from typer import secho
from typer.colors import BLUE, GREEN, MAGENTA, RED, YELLOW

from app.models import UiMode
from app import app_mode


class Printer:
    def __init__(self):
        self.enable = True

    def _print(self, text: str, color):
        if not self.enable:
            return
        if app_mode == UiMode.TYPER:
            secho(text, fg=color, bold=True)
        elif app_mode == UiMode.GRADIO:
            print(text)

    def info(self, text: str):
        self._print(text, GREEN)

    def warning(self, text: str):
        self._print(text, YELLOW)

    def error(self, text: str):
        self._print(text, RED)

    def success(self, text: str):
        self._print(text, GREEN)

    def debug(self, text: str):
        self._print(text, BLUE)

    def fatal(self, text: str):
        self._print(text, RED)

    def trace(self, text: str):
        self._print(text, MAGENTA)


printer = Printer()

from pathlib import Path

from app.utils.exceptions import SourcesNotFound


class Source:
    def __init__(self, path: str | Path):
        self.path = self._get_path(str(path))
        self.keywords = self._read_keywords()

    def _get_path(self, path_str: str) -> Path:
        try:
            path = Path(path_str)
            if path.exists() and path.is_file() and path.suffix == ".txt":
                return path

        except Exception:
            raise SourcesNotFound()

        return

    def _read_keywords(self) -> list[str]:
        if not self.path:
            return
        with self.path.open("r", encoding="utf-8") as file:
            keywords = [line.strip() for line in file if line.strip()]
            return keywords

    def __repr__(self) -> str:
        return f"Source(path={self.path}, keywords_count={len(self.keywords)})"

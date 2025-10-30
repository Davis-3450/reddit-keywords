from pathlib import Path

from app.utils.exceptions import SourcesNotFound


class Source:
    def __init__(self, path: str | Path):
        self.path = self._get_path(str(path))
        self.keywords = self._read_keywords()

    def _get_path(self, path_str: str) -> Path:
        path = Path(path_str)
        if path.exists() and path.is_file() and path.suffix == ".txt":
            return path
        raise SourcesNotFound()

    def _read_keywords(self) -> list[str]:
        try:
            with self.path.open("r", encoding="utf-8") as file:
                keywords = [line.strip() for line in file if line.strip()]
                return keywords
        except (OSError, IOError) as e:
            raise SourcesNotFound(f"Failed to read keywords file: {e}") from e

    def __repr__(self) -> str:
        return f"Source(path={self.path}, keywords_count={len(self.keywords)})"

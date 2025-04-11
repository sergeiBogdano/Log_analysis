import re
from pathlib import Path
from typing import Iterator, Tuple

LOG_LINE_REGEX = re.compile(
    r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+\s+'
    r'(?P<level>[A-Z]+)\s+django\.request:\s+'
    r'(?:GET|POST|PUT|PATCH|DELETE)\s+(?P<handler>/\S+)'
)

def parse_log_file(file_path: Path) -> Iterator[Tuple[str, str]]:
    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            match = LOG_LINE_REGEX.match(line)
            if match:
                level = match.group("level")
                handler = match.group("handler")
                yield handler, level

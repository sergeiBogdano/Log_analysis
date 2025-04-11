from collections import defaultdict
from pathlib import Path
from typing import List

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def generate(log_paths: List[Path]) -> str:
    total_requests = 0
    handler_counter = defaultdict(lambda: defaultdict(int))

    for path in log_paths:
        with open(path, encoding="utf-8") as file:
            for line in file:
                if "django.request" not in line:
                    continue

                parts = line.strip().split()
                if len(parts) < 6:
                    continue

                level = parts[2]
                handler = parts[5]

                if level in LOG_LEVELS and handler.startswith("/"):
                    handler_counter[handler][level] += 1
                    total_requests += 1

    header = (
        f"{'HANDLER':<24}"
        f"{'DEBUG':>7}"
        f"{'INFO':>8}"
        f"{'WARNING':>9}"
        f"{'ERROR':>8}"
        f"{'CRITICAL':>10}"
    )

    lines = [f"Total requests: {total_requests}", "", header]

    for handler in sorted(handler_counter):
        line = f"{handler:<24}"
        for level in LOG_LEVELS:
            line += f"{handler_counter[handler][level]:>{len(level)+2}}"
        lines.append(line)

    return "\n".join(lines)

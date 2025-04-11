from pathlib import Path
from typing import Callable, List, Dict
from reports.handlers import generate as generate_handlers_report

ReportFunction = Callable[[List[Path]], str]

REPORTS: Dict[str, ReportFunction] = {
    "handlers": generate_handlers_report,
}

AVAILABLE_REPORTS = list(REPORTS.keys())


def generate_report(name: str, log_paths: List[Path]) -> str:
    if name not in REPORTS:
        raise ValueError(f"Unknown report type: {name}")
    return REPORTS[name](log_paths)

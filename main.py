import argparse
import sys
from pathlib import Path
from report_generator import generate_report, AVAILABLE_REPORTS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Django Log Analyzer CLI"
    )
    parser.add_argument(
        "logfiles",
        nargs="+", type=Path,
        help="Paths to Django log files"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=AVAILABLE_REPORTS,
        help="Report type to generate"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    for log_file in args.logfiles:
        if not log_file.is_file():
            print(f"Error: file {log_file} does not exist.", file=sys.stderr)
            sys.exit(1)

    report_text = generate_report(args.report, args.logfiles)
    print(report_text)


if __name__ == "__main__":
    main()

import os
from pathlib import Path
from tempfile import NamedTemporaryFile
import pytest
from report_generator import generate_report


def test_generate_report():
    log_content = (
        "2025-03-28 12:44:46,000 INFO django.request:"
        " GET /api/v1/test/ 204 OK [192.168.1.59]\n"
        "2025-03-28 12:21:51,000 INFO django.request:"
        " GET /api/v1/another_test/ 200 OK [192.168.1.68]\n"
        "2025-03-28 12:05:13,000 INFO django.request:"
        " GET /api/v1/test/ 201 OK [192.168.1.97]\n"
        "2025-03-28 12:11:57,000 ERROR django.request:"
        " GET /api/v1/another_test/ 500 Error [192.168.1.29]\n"
    )
    with NamedTemporaryFile(delete=False, mode="w", suffix=".log") as temp_log_file:
        temp_log_file.write(log_content)
        temp_log_file_path = Path(temp_log_file.name)

    expected_output = (
        "Total requests: 4\n\n"
        "HANDLER                DEBUG   INFO    WARNING  ERROR   CRITICAL\n"
        "/api/v1/another_test/      0      1         0      1         0\n"
        "/api/v1/test/              0      2         0      0         0"
    )

    result = generate_report("handlers", [temp_log_file_path])
    os.remove(temp_log_file_path)
    assert result == expected_output


def test_generate_report_invalid_type():
    with pytest.raises(ValueError, match="Unknown report type: invalid_type"):
        generate_report("invalid_type", [Path("dummy.log")])

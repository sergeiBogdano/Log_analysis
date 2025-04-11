def print_table(data: dict, log_levels: list) -> str:
    header = f"{'HANDLER':<24}" + "".join(
        f"{level:>7}" for level in log_levels
    )
    lines = [header]

    for handler in sorted(data.keys()):
        row = f"{handler:<24}"
        for level in log_levels:
            row += f"{data[handler].get(level, 0):>7}"
        lines.append(row)

    return "\n".join(lines)

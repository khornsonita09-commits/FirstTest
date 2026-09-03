import os

def analyze_log(filename="logs/server.log"):
    if not filename.strip():
        filename = "logs/server.log"

    if not os.path.exists(filename):
        return f"Log file not found: {filename}"

    info_count = 0
    warning_count = 0
    error_count = 0
    errors = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line.startswith("INFO"):
                    info_count += 1
                elif line.startswith("WARNING"):
                    warning_count += 1
                elif line.startswith("ERROR"):
                    error_count += 1
                    error_message = line.replace("ERROR ", "", 1)
                    errors.append(error_message)

        lines = [
            "===== LOG ANALYZER =====",
            f"\nINFO     : {info_count}",
            f"WARNING  : {warning_count}",
            f"ERROR    : {error_count}",
            "\nErrors found:"
        ]

        if len(errors) == 0:
            lines.append("No errors found.")
        else:
            for number, error in enumerate(errors, start=1):
                lines.append(f"{number}. {error}")

        return "\n".join(lines)

    except Exception as error:
        return f"Error reading log file: {error}"
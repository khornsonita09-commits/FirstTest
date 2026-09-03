import psutil

def show_processes():
    lines = [
        f"{'PID':<10}{'NAME':<30}{'CPU %':<10}",
        "-" * 50
    ]

    count = 0
    for process in psutil.process_iter(["pid", "name", "cpu_percent"]):
        try:
            pid = process.info["pid"]
            name = process.info["name"]
            cpu = process.info["cpu_percent"]

            lines.append(f"{pid:<10}{str(name):<30}{cpu:<10}")
            count += 1

            if count >= 20:
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return "\n".join(lines)
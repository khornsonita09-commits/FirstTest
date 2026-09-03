import psutil

def show_disk_space():
    lines = []
    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total = usage.total / (1024 ** 3)
            used = usage.used / (1024 ** 3)
            free = usage.free / (1024 ** 3)

            lines.append(f"Drive : {partition.mountpoint}")
            lines.append(f"Total : {total:.2f} GB")
            lines.append(f"Used  : {used:.2f} GB")
            lines.append(f"Free  : {free:.2f} GB")
            lines.append(f"Usage : {usage.percent}%")

            if usage.percent >= 90:
                lines.append("WARNING: Disk space is very low!")
            lines.append("-" * 30)

        except PermissionError:
            continue

    return "\n".join(lines)
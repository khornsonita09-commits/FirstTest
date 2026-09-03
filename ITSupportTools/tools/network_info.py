import socket

def show_ip_info():
    lines = []
    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
        lines.append(f"Computer Name : {hostname}")
        lines.append(f"Local IP      : {local_ip}")
    except socket.error:
        lines.append("Unable to get IP information.")

    return "\n".join(lines)
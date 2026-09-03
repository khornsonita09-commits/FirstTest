import subprocess
import platform

def ping_host(host):
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "4", host]
    else:
        command = ["ping", "-c", "4", host]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout

        if result.returncode == 0:
            status = "Host is reachable."
        else:
            status = "Host is NOT reachable."

        return f"{output}\n{status}"

    except Exception as error:
        return f"Ping error: {error}"
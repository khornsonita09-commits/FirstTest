import socket

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            return f"Port {port} on {host} is OPEN."
        else:
            return f"Port {port} on {host} is CLOSED."

    except socket.gaierror:
        return f"Could not resolve host: {host}"
    except Exception as error:
        return f"Error: {error}"
import platform
import socket
import os


def show_system_info():

    system_info = f"""
========================================
        SYSTEM INFORMATION
========================================

Operating System : {platform.system()}
OS Version       : {platform.version()}
Machine          : {platform.machine()}
Processor        : {platform.processor()}
Computer Name    : {socket.gethostname()}
Python Version   : {platform.python_version()}
CPU Cores        : {os.cpu_count()}

========================================
"""

    return system_info
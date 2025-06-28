# daemon.py

import socket
import subprocess
from modules.monitor import handle
from modules.utils import get_socket_path

def run_daemon(rules):
    sock = get_socket_path()
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(sock)
        buf = b""
        while True:
            buf += s.recv(1024)
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                handle(line.decode(), rules)


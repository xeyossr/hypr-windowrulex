# utils.py

import os
from colorama import Fore, init
import subprocess
import json
import re
# Initialize colorama for cross-platform compatibility
init(autoreset=True)


def print_error(message):
    print(Fore.RED + f"[windowrulex] Error: {message}")


def print_success(message):
    print(Fore.GREEN + f"[windowrulex] Success: {message}")


def get_socket_path():
    base = f"/run/user/{os.getuid()}/hypr"
    for f in os.listdir(base):
        sock = os.path.join(base, f, ".socket2.sock")
        if os.path.exists(sock):
            return sock
    raise RuntimeError("Hyprland socket not found")


def get_monitor_info():
    monitors = json.loads(subprocess.check_output(
        ["hyprctl", "monitors", "-j"]))
    return monitors[0]["width"], monitors[0]["height"]


def get_client_info(addr):
    clients = json.loads(subprocess.check_output(["hyprctl", "clients", "-j"]))
    for client in clients:
        if client["address"] == addr:
            return client
    return None


def get_clients():
    return json.loads(subprocess.check_output(["hyprctl", "clients", "-j"]))


def matches(client, rule):
    for key, pattern in rule.match.items():
        val = ""
        if key == "title":
            val = client.get("title", "")
        if key == "class":
            val = client.get("class", "")
        if key == "initialTitle":
            val = client.get("initialTitle", "")
        if key == "initialClass":
            val = client.get("initialClass", "")
        if "*" in pattern:
            regex = re.escape(pattern).replace(r"\*", ".*")
        else:
            regex = pattern
        if not re.search(regex, val):
            return False
    return True

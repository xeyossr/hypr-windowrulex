# monitor.py

import time
import json
from threading import Thread
from modules.actions import dispatch_resize, dispatch_move
from modules.utils import get_clients, matches
import subprocess

def apply_actions(client, rule):
    addr = client["address"]
    for k, v in rule.actions.items():
        if k == "floating" and v:
            subprocess.call([
                "hyprctl", "dispatch", "setfloating", f"address:{addr}"
                ])

        elif k == "size":
            dispatch_resize(addr, v[0], v[1])

        elif k == "move":
            dispatch_move(addr, v[0], v[1])

    print(f"[windowrulex] Applied rule to {addr}")

def monitor(client_addr, rule):
    total = 0
    while total <= rule.timeout:
        clients = get_clients()
        client = next((c for c in clients if c["address"] == client_addr), None)
        if client and matches(client, rule):
            apply_actions(client, rule)
            return
        time.sleep(rule.interval)
        total += rule.interval

def handle(line, rules):
    if not line.startswith("openwindow"):
        return
    time.sleep(0.5)
    clients = get_clients()
    if not clients:
        return
    last = clients[-1]
    for rule in rules:
        Thread(target=monitor, args=(last["address"], rule), daemon=True).start()


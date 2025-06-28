# actions.py

import time
import subprocess
from modules.utils import get_monitor_info, get_client_info

def dispatch_resize(addr, target_w, target_h):
    client = get_client_info(addr)
    cur_w, cur_h = client["size"]
    diff_w = target_w - cur_w
    diff_h = target_h - cur_h
    subprocess.call([
        "hyprctl", "dispatch", "resizewindowpixel",
        "--", f"{diff_w}", f"{diff_h},address:{addr}"
    ])
    time.sleep(0.05)

def dispatch_move(addr, move_x, move_y):
    screen_w, screen_h = get_monitor_info()
    client = get_client_info(addr)
    win_w, win_h = client["size"]
    cur_x, cur_y = client["at"]

    if move_x == "center":
        target_x = int(screen_w / 2 - win_w / 2)
    else:
        target_x = int(move_x)

    if move_y == "center":
        target_y = int(screen_h / 2 - win_h / 2)
    else:
        target_y = int(move_y)

    diff_x = target_x - cur_x
    diff_y = target_y - cur_y

    subprocess.call([
        "hyprctl", "dispatch", "movewindowpixel",
        "--", f"{diff_x}", f"{diff_y},address:{addr}"
    ])
    time.sleep(0.05)


# config.py

import re
import os
import json
from modules.rules import Rule
from modules.utils import print_error

DEFAULT_INTERVAL = 0.1
DEFAULT_TIMEOUT = 3

def parse_config(path):
    rules = []
    with open(os.path.expanduser(path)) as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if not line.startswith("windowrulex"):
                raise ValueError(f"Syntax error at line {lineno}: must start with 'windowrulex'")

            rule = line.split("=", 1)[1].strip()
            parts = [p.strip() for p in re.split(r',(?![^\[]*\])', rule)]
            match, actions = {}, {}
            interval, timeout = DEFAULT_INTERVAL, DEFAULT_TIMEOUT

            for part in parts:
                if ':' not in part:
                    raise ValueError(f"Syntax error at line {lineno}: Missing ':' in '{part}'")
                key, val = part.split(':', 1)
                key = key.strip()
                val = val.strip()

                if key in {"title", "class", "initialTitle", "initialClass"}:
                    match[key] = val
                elif key == "floating":
                    actions["floating"] = val.lower() == "true"
                
                elif key == "size":
                    size = val.split()
                    if len(size) != 2:
                        raise ValueError(f"Invalid size at line {lineno}")
                    actions["size"] = [int(size[0]), int(size[1])]
                
                elif key == "move":
                    move = val.split()
                    if len(move) != 2:
                        raise ValueError(f"Invalid move at line {lineno}")
                    actions["move"] = move
                
                elif key == "interval":
                    interval = float(val)
                
                elif key == "timeout":
                    timeout = float(val)
                
                else:
                    raise ValueError(f"Unknown key '{key}' at line {lineno}")

            if not match:
                raise ValueError(f"No match fields found at line {lineno}")
            if not actions:
                raise ValueError(f"No actions defined at line {lineno}")
            
            rules.append(Rule(match, actions, interval, timeout))
    return rules


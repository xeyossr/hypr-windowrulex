# rules.py

class Rule:
    def __init__(self, match, actions, interval, timeout):
        self.match = match  # dict: {title, class, initialTitle, initialClass}
        self.actions = actions  # dict: {floating, size, move, opacity}
        self.interval = interval
        self.timeout = timeout


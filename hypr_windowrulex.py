# main.py

import argparse
import os
from modules.utils import print_error, print_success
from modules.config import parse_config
from modules.daemon import run_daemon
from colorama import Fore, init


def main():
    parser = argparse.ArgumentParser(
        description="Hyprland window rules handler")
    parser.add_argument('--daemon', action='store_true',
                        help="Run the script as a daemon")
    parser.add_argument('--config', type=str, help="Path to the config file")

    args = parser.parse_args()

    config_path = args.config or os.path.expandvars(
        os.path.expanduser("~/.config/hypr/windowrulex.conf"))
    if not args.daemon:
        print(Fore.YELLOW +
              "[windowrulex] No --daemon flag provided. Displaying help message.")
        parser.print_help()
        return

    try:
        rules = parse_config(config_path)
        print_success("[windowrulex] Config loaded. Listening for windows...")
        run_daemon(rules)
    except Exception as e:
        print_error(f"Error loading config or running daemon: {e}")


if __name__ == '__main__':
    main()

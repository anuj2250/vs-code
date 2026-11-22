import os
import sys
import time
import random

# ANSI Color Codes for Neon Cyberpunk Look
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Rotating Radar Sweep Frames
radar_frames = [
    r"""
         . - ~ ~ ~ - .
      /        |        \

     |         |         |   [TARGET]: LOCKED
     |         O - - - - |   [SIGNAL]: 99.8%
     |                   |   [MODE]  : ORBITAL SCAN
      \                 /
         ' - . _ . - '
    """,
    r"""
         . - ~ ~ ~ - .
      /           /     \

     |          /        |   [TARGET]: LOCKED
     |         O         |   [SIGNAL]: 99.8%
     |                   |   [MODE]  : ORBITAL SCAN
      \                 /
         ' - . _ . - '
    """,
    r"""
         . - ~ ~ ~ - .
      /                 \

     |                   |   [TARGET]: LOCKED
     |         O         |   [SIGNAL]: 99.8%
     |          \        |   [MODE]  : ORBITAL SCAN
      \           \     /
         ' - . _ . - '
    """,
    r"""
         . - ~ ~ ~ - .
      /                 \

     |                   |   [TARGET]: LOCKED
     |         O         |   [SIGNAL]: 99.8%
     |        /          |   [MODE]  : ORBITAL SCAN
      \      /          /
         ' - . _ . - '
    """,
    r"""
         . - ~ ~ ~ - .
      /                 \

     |                   |   [TARGET]: LOCKED
     | - - - - O         |   [SIGNAL]: 99.8%
     |                   |   [MODE]  : ORBITAL SCAN
      \                 /
         ' - . _ . - '
    """,
    r"""
         . - ~ ~ ~ - .
      /     \           \

     |        \          |   [TARGET]: LOCKED
     |         O         |   [SIGNAL]: 99.8%
     |                   |   [MODE]  : ORBITAL SCAN
      \                 /
         ' - . _ . - '
    """
]

def generate_hex_line():
    chars = "0123456789ABCDEF"
    return " ".join("".join(random.choices(chars, k=4)) for _ in range(8))

def infinite_cyber_loop():
    # Enable ANSI colors on Windows CMD
    if os.name == 'nt':
        os.system('')

    try:
        while True:
            # PHASE 1: SEARCHING & DECRYPTING
            for i in range(15):
                clear()
                print(f"{MAGENTA}{BOLD}=== NEURAL SATELLITE INTERFACE v4.2 ==={RESET}\n")
                print(f"{YELLOW}[*] SCANNING ORBITAL FREQUENCIES...{RESET}")
                print(f"{CYAN}{generate_hex_line()}{RESET}")
                print(f"{CYAN}{generate_hex_line()}{RESET}")
                print(f"\n{RED}[!] ACCESS: PENDING VERIFICATION...{RESET}")
                time.sleep(0.12)

            # PHASE 2: ACCESS GRANTED FLASH
            for _ in range(3):
                clear()
                print(f"\n\n{GREEN}{BOLD}   ########################################")
                print(f"   #   PERMISSION & ACCESS GRANTED [OK]   #")
                print(f"   ########################################{RESET}\n")
                time.sleep(0.25)
                clear()
                time.sleep(0.15)

            # PHASE 3: CONTINUOUS RADAR & SATELLITE TELEMETRY
            for cycle in range(3):
                for frame in radar_frames:
                    clear()
                    lat = round(random.uniform(25.0, 29.0), 4)
                    lon = round(random.uniform(80.0, 84.0), 4)
                    print(f"{MAGENTA}{BOLD}=== LIVE ORBITAL RADAR & SATELLITE FEED ==={RESET}")
                    print(f"{GREEN}STATUS: PERMISSION GRANTED | ENCRYPTION: AES-512{RESET}")
                    print(f"{CYAN}{frame}{RESET}")
                    print(f"{YELLOW}LIVE COORDS : {lat}° N, {lon}° E{RESET}")
                    print(f"{MAGENTA}PACKET STREAM: {generate_hex_line()}{RESET}")
                    print(f"\n{BOLD}Press Ctrl+C to exit loop...{RESET}")
                    time.sleep(0.18)

    except KeyboardInterrupt:
        clear()
        print(f"{RED}{BOLD}>>> SESSION TERMINATED BY USER.{RESET}")

if __name__ == "__main__":
    infinite_cyber_loop()

import os
import sys
import time
import random
import math

# ANSI Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- THEME 1: BIO-LAB RETINA & DNA SCANNER ---
def theme_biolab():
    bases = [("A", "T", CYAN), ("T", "A", GREEN), ("C", "G", YELLOW), ("G", "C", MAGENTA)]
    subject_id = f"SUBJ-{random.randint(1000, 9999)}"
    for i in range(28):
        clear()
        print(f"{CYAN}{BOLD}=== [THEME 01] BIO-SECURITY & GENOME ACCESS ==={RESET}")
        print(f"{WHITE}SCANNING SUBJECT: {subject_id} | RETINA MATCH: {min(100, i*4)}%{RESET}\n")
        for row in range(10):
            offset = int(math.sin((i + row) * 0.6) * 8) + 10
            b1, b2, col = random.choice(bases)
            strand = " " * offset + f"{col}{b1}---{b2}{RESET}"
            print(strand)
        if i > 20:
            print(f"\n{GREEN}{BOLD}>>> BIOMETRIC PERMISSION GRANTED <<<{RESET}")
        time.sleep(0.1)

# --- THEME 2: DEEP SPACE STARFIELD & WARP JUMP ---
def theme_spaceship():
    sector = f"SECTOR-{random.choice(['ALPHA', 'OMEGA', 'CYGNUS', 'ORION'])}-{random.randint(10,99)}"
    stars = [[random.randint(1, 55), random.randint(1, 12), random.choice(['.', '*', '+', 'o'])] for _ in range(25)]
    for frame in range(30):
        clear()
        speed = (frame + 1) * 320
        print(f"{BLUE}{BOLD}=== [THEME 02] STARSHIP NAVIGATION & WARP UPLINK ==={RESET}")
        print(f"{YELLOW}DESTINATION: {sector} | VELOCITY: {speed} KM/S{RESET}\n")
        grid = [[" " for _ in range(58)] for _ in range(14)]
        for s in stars:
            s[0] -= random.randint(1, 3)
            if s[0] < 0:
                s[0] = 57
                s[1] = random.randint(0, 13)
            grid[s[1]][s[0]] = s[2]
        for row in grid:
            print(f"{CYAN}" + "".join(row) + f"{RESET}")
        if frame > 22:
            print(f"\n{GREEN}{BOLD}>>> JUMP CLEARANCE GRANTED: ENGAGING HYPERDRIVE <<<{RESET}")
        time.sleep(0.09)

# --- THEME 3: RETRO 1980s AMBER MAINFRAME ---
def theme_retro_mainframe():
    node = f"NODE-0{random.randint(1,9)}-USR"
    mem_addr = random.randint(10000, 99999)
    for step in range(25):
        clear()
        print(f"{YELLOW}{BOLD}**************************************************")
        print(f"*   ARPANET MAINFRAME TERMINAL // {node}   *")
        print(f"**************************************************{RESET}\n")
        print(f"{YELLOW}SEARCHING MAGNETIC TAPE SECTORS...{RESET}")
        for r in range(6):
            blocks = "".join(random.choice(["[##]", "[  ]", "[**]", "[::]"]) for _ in range(10))
            print(f"{YELLOW}ADDR {mem_addr + r*16}: {blocks}{RESET}")
        if step > 18:
            print(f"\n{YELLOW}{BOLD}[OK] OVERRIDE CODE ACCEPTED - ACCESS GRANTED{RESET}")
        time.sleep(0.11)

# --- THEME 4: GLOBAL SATELLITE ORBITAL GRID ---
def theme_satellite_grid():
    sat_name = f"SAT-{random.choice(['INSAT', 'LANDSAT', 'SENTINEL', 'NOAA'])}-{random.randint(10,99)}"
    lat = round(random.uniform(10.0, 35.0), 4)
    lon = round(random.uniform(70.0, 90.0), 4)
    for t in range(28):
        clear()
        print(f"{GREEN}{BOLD}=== [THEME 04] ORBITAL TELEMETRY & SATELLITE LOCK ==={RESET}")
        print(f"{WHITE}TRACKING: {sat_name} | TARGET COORDS: {lat}° N, {lon}° E{RESET}\n")
        scan_col = t % 45
        for r in range(10):
            line = ""
            for c in range(45):
                if c == scan_col:
                    line += f"{RED}|{RESET}"
                elif (r + c + t) % 11 == 0:
                    line += f"{GREEN}+{RESET}"
                else:
                    line += f"{CYAN}.{RESET}"
            print("  " + line)
        if t > 20:
            print(f"\n{GREEN}{BOLD}>>> SATELLITE DOWNLINK PERMISSION GRANTED <<<{RESET}")
        time.sleep(0.09)

# --- THEME 5: QUANTUM WAVEFORM & FREQUENCY DECRYPTOR ---
def theme_quantum_wave():
    freq = round(random.uniform(100.0, 999.9), 2)
    for tick in range(30):
        clear()
        print(f"{MAGENTA}{BOLD}=== [THEME 05] QUANTUM FREQUENCY & CIPHER LOCK ==={RESET}")
        print(f"{CYAN}CARRIER WAVE: {freq} THz | ENTANGLEMENT: STABLE{RESET}\n")
        for row in range(-5, 6):
            line = ""
            for col in range(50):
                wave = int(math.sin((col * 0.25) + (tick * 0.5)) * 4)
                if wave == row:
                    line += f"{MAGENTA}█{RESET}"
                elif row == 0:
                    line += f"{WHITE}-{RESET}"
                else:
                    line += " "
            print(line)
        if tick > 22:
            print(f"\n{GREEN}{BOLD}>>> QUANTUM KEY VERIFIED: ACCESS GRANTED <<<{RESET}")
        time.sleep(0.08)

# --- THEME 6: SEISMIC & THERMAL CORE MONITOR ---
def theme_thermal_core():
    reactor = f"CORE-{random.choice(['DELTA', 'SIGMA', 'TITAN'])}-{random.randint(1,9)}"
    for step in range(26):
        clear()
        temp = random.randint(1200, 4500)
        print(f"{RED}{BOLD}=== [THEME 06] GEOTHERMAL & CORE CONTAINMENT ==={RESET}")
        print(f"{YELLOW}CHAMBER: {reactor} | CORE TEMP: {temp}°K{RESET}\n")
        for _ in range(8):
            bar_len = random.randint(5, 45)
            color = RED if bar_len > 32 else (YELLOW if bar_len > 18 else GREEN)
            print(f"  {color}{'▓' * bar_len}{'░' * (45 - bar_len)}{RESET}")
        if step > 19:
            print(f"\n{GREEN}{BOLD}>>> CONTAINMENT SHIELD PERMISSION GRANTED <<<{RESET}")
        time.sleep(0.1)

def run_endless_unique_loop():
    if os.name == 'nt':
        os.system('')  # Enable ANSI escape colors in Windows CMD

    themes = [
        theme_biolab,
        theme_spaceship,
        theme_retro_mainframe,
        theme_satellite_grid,
        theme_quantum_wave,
        theme_thermal_core
    ]
    
    last_theme = None
    try:
        while True:
            # Pick a random theme that wasn't just played
            available = [t for t in themes if t != last_theme]
            current_theme = random.choice(available)
            last_theme = current_theme
            
            current_theme()
            time.sleep(0.6)
            
    except KeyboardInterrupt:
        clear()
        print(f"{RED}{BOLD}>>> INFINITE LOOP TERMINATED BY USER.{RESET}")

if __name__ == "__main__":
    run_endless_unique_loop()

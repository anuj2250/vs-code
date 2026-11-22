import os
import sys
import time

# Clear terminal helper
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Typewriter effect
def type_text(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Loading bar animation
def loading_bar(label, steps=25, delay=0.06):
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        bar = '█' * i + '-' * (steps - i)
        sys.stdout.write(f'\r{label} [{bar}] {percent}%')
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ASCII Globe / Satellite frames
frames = [
    r"""
          .  *  .       .   *
       .    _..._    .
          .'     '.      [SAT-01: LOCKED]
         /  .-.    \     LAT: 28.6139° N

        |  (   )    |    LON: 77.2090° E
         \  '-'    /     ALT: 408 KM
          '.     .'
            '---'
    """,
    r"""
       *     .     *   .
          . _..._ .
          .'  _  '.      [SAT-01: SCANNING...]
         /   / \   \     LAT: 28.6139° N

        |   |   |   |    LON: 77.2090° E
         \   \_/   /     ALT: 408 KM
          '.     .'
            '---'
    """,
    r"""
          .     *     .
       .    _..._   *
          .'   _ '.      [SAT-01: TRACKING]
         /    ( )  \     LAT: 28.6139° N

        |      '    |    LON: 77.2090° E
         \         /     ALT: 408 KM
          '.     .'
            '---'
    """
]

def run_animation():
    clear()
    # Set terminal text to green (Windows CMD)
    if os.name == 'nt':
        os.system('color 0A')

    type_text(">>> INITIALIZING SATELLITE UPLINK...")
    time.sleep(0.5)
    loading_bar("SEARCHING FREQUENCY", steps=20, delay=0.05)
    
    type_text(">>> VERIFYING SECURITY CREDENTIALS...")
    time.sleep(0.5)
    loading_bar("BYPASSING FIREWALL ", steps=20, delay=0.05)
    
    print("\n" + "="*38)
    type_text("   [✓] PERMISSION & ACCESS GRANTED", delay=0.03)
    print("="*38 + "\n")
    time.sleep(1)

    # Loop satellite animation
    try:
        for _ in range(15):
            for frame in frames:
                clear()
                print("=== LIVE SATELLITE TELEMETRY VIEW ===")
                print(frame)
                print("Press Ctrl+C to terminate uplink...")
                time.sleep(0.25)
    except KeyboardInterrupt:
        print("\n>>> UPLINK TERMINATED.")

if __name__ == "__main__":
    run_animation()

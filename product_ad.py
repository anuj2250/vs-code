import os
import time

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"

LOGO = r"""
   ______      __              _____ __    _      __    __
  / ____/_  __/ /_  ___  _____/ ___// /_  (_)__  / /___/ /
 / /   / / / / __ \/ _ \/ ___/\__ \/ __ \/ / _ \/ / __  / 
/ /___/ /_/ / /_/ /  __/ /   ___/ / / / / /  __/ / /_/ /  
\____/\__, /_.___/\___/_/   /____/_/ /_/_/\___/_/\__,_/   
     /____/                                               
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, color=GREEN, delay=0.03):
    for ch in text:
        print(color + ch + RESET, end="", flush=True)
        time.sleep(delay)
    print()

while True:
    # SCENE 1: Product Intro & Glowing Logo
    clear()
    print(CYAN + "═" * 62 + RESET)
    print(MAGENTA + LOGO + RESET)
    print(CYAN + "═" * 62 + RESET)
    time.sleep(0.5)
    type_text("  >>> INTRODUCING: CYBER-SHIELD PRO (AI FIREWALL) <<<", YELLOW, 0.03)
    time.sleep(0.8)

    # SCENE 2: Product Features Reveal
    features = [
        "[✓] 100% Real-Time Ransomware & Malware Blocker",
        "[✓] Military-Grade AES-256 Quantum Encryption",
        "[✓] Zero-Latency Dark Web Threat Scanner",
        "[✓] Built by Future IIT B.Cyber. Security Engineers!"
    ]
    print()
    for feat in features:
        type_text("   " + feat, GREEN, 0.025)
        time.sleep(0.4)

    # SCENE 3: Flashing Special Offer Banner
    print()
    for i in range(6):
        border_color = YELLOW if i % 2 == 0 else MAGENTA
        print(f"\r{border_color}   ★ LIMITED LAUNCH OFFER: FREE FOR STUDENTS! ★   {RESET}", end="", flush=True)
        time.sleep(0.35)
    print("\n")

    # SCENE 4: Scrolling Bottom News/Ad Ticker
    ticker = "   🔥 DOWNLOAD NOW AT GITHUB.COM | PROTECT YOUR SYSTEM TODAY | 24/7 AI DEFENSE ACTIVE 🔥   "
    for _ in range(2):
        for i in range(len(ticker) - 55):
            print(f"\r{CYAN}[AD] {WHITE}{ticker[i:i+55]}{RESET}", end="", flush=True)
            time.sleep(0.06)

    time.sleep(1)

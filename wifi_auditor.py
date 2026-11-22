import subprocess
import re

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(CYAN + "\n[*] SCANNING SAVED WI-FI PROFILES ON THIS SYSTEM...\n" + RESET)

# Windows ke sabhi saved Wi-Fi profiles nikalne ki command
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode('utf-8', errors='ignore')
profile_names = re.findall("All User Profile     : (.*)\r", command_output)

if len(profile_names) == 0:
    print(YELLOW + "[!] Koi saved Wi-Fi profile nahi mili." + RESET)
else:
    print(f"{GREEN}{'WI-FI NAME (SSID)':<30} | {'SAVED PASSWORD'}{RESET}")
    print("-" * 55)
    
    for name in profile_names:
        # Har Wi-Fi ka password check karne ke liye
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode('utf-8', errors='ignore')
        password = re.search("Key Content            : (.*)\r", profile_info)
        
        if password is None:
            print(f"{name:<30} | {YELLOW}[No Password / Open]{RESET}")
        else:
            print(f"{name:<30} | {GREEN}{password[1]}{RESET}")

print("\n" + CYAN + "[✓] Wi-Fi Audit Complete!" + RESET)

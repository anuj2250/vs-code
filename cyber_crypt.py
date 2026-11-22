import time
import random
import string

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def radar_animation():
    spinner = ["|", "/", "-", "\\"]
    print(CYAN + "\n[*] ACTIVATING QUANTUM ENCRYPTION ENGINE..." + RESET)
    for i in range(25):
        rand_hex = "".join(random.choices("0123456789ABCDEF", k=16))
        print(f"\r{GREEN}[{spinner[i % 4]}] Generating Secure Key: 0x{rand_hex}{RESET}", end="")
        time.sleep(0.08)
    print("\n" + GREEN + "[✓] Secure Channel Established!\n" + RESET)

def matrix_reveal(text):
    # Text ko hacker style mein decode karke dikhane ka animation
    chars = string.ascii_letters + string.digits + "@#$%&*"
    current = [" "] * len(text)
    for i in range(len(text)):
        for _ in range(4):
            current[i] = random.choice(chars)
            print(f"\r{YELLOW}OUTPUT: {''.join(current)}{RESET}", end="")
            time.sleep(0.02)
        current[i] = text[i]
    print(f"\r{GREEN}OUTPUT: {''.join(current)}{RESET}\n")

def encrypt_decrypt(message, shift, mode):
    result = ""
    if mode == "D":
        shift = -shift
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Main Program Start
radar_animation()
choice = input(CYAN + "Kya karna hai? (E = Encrypt / D = Decrypt): " + RESET).upper()
msg = input(CYAN + "Apna Secret Message likhein: " + RESET)
key = int(input(CYAN + "Secret Key Number dalein (1-25): " + RESET))

print(CYAN + "\n[*] Processing Data..." + RESET)
time.sleep(0.8)

final_text = encrypt_decrypt(msg, key, choice)
matrix_reveal(final_text)

import socket

target = input("Target website dalein (jaise scanme.nmap.org): ")
print(f"\n[*] Scanning {target} for open ports...\n")

# Common ports: 21(FTP), 22(SSH), 80(HTTP), 443(HTTPS)
ports = [21, 22, 80, 443]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN!")
    else:
        print(f"[-] Port {port} is closed")
    s.close()

print("\n[✓] Scan Complete!")

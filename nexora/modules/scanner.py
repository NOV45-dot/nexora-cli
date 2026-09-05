import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP-Alt"
}

def scan_host(target=None):
    if target is None:
        target = input("Enter authorized host/IP: ").strip()

    if not target:
        print("[!] Host cannot be empty.")
        return

    try:
        ip = socket.gethostbyname(target)

        print("\n==========================================")
        print("          NEXORA HOST SCANNER")
        print("==========================================")
        print("[+] Target :", target)
        print("[+] IP     :", ip)
        print("------------------------------------------")

        for port, service in COMMON_PORTS.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))
            sock.close()

            if result == 0:
                print(f"[OPEN]   {port:<5} {service}")
            else:
                print(f"[CLOSED] {port:<5} {service}")

        print("------------------------------------------")
        print("[+] Scan complete.")

    except socket.gaierror:
        print("[!] Could not resolve host.")
    except Exception as e:
        print("[!] Error:", e)

    input("\nPress ENTER...")

def scanner_menu():
    while True:
        print("""
==========================================
          NEXORA HOST SCANNER
==========================================

[1] Scan authorized host
[0] Back
""")

        choice = input("SCANNER > ").strip()

        if choice == "1":
            scan_host()
        elif choice == "0":
            break
        else:
            print("[!] Invalid option.")

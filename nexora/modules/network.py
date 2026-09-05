import socket
import urllib.request
import json


def public_ip():
    try:
        with urllib.request.urlopen(
            "https://api.ipify.org?format=json", timeout=5
        ) as response:
            data = json.loads(response.read().decode())
            print("[+] Public IP:", data["ip"])
    except Exception:
        print("[!] Unable to retrieve public IP.")


def get_local_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print("[+] Hostname:", hostname)
        print("[+] Local IP:", ip)
    except Exception:
        print("[!] Unable to retrieve local network information.")


def dns_lookup(domain=None):
    if not domain:
        domain = input("Enter domain: ").strip()

    if not domain:
        print("[!] Domain cannot be empty.")
        return

    try:
        ip = socket.gethostbyname(domain)
        print("[+] Domain:", domain)
        print("[+] IP:", ip)
    except socket.gaierror:
        print("[!] Could not resolve domain.")


def network_menu():
    while True:
        print("""
==========================================
          NEXORA NETWORK TOOLS
==========================================

[1] Public IP
[2] Local Network Information
[3] DNS Lookup
[0] Back
""")

        choice = input("NETWORK > ").strip()

        if choice == "1":
            public_ip()
            input("\nPress ENTER...")

        elif choice == "2":
            get_local_ip()
            input("\nPress ENTER...")

        elif choice == "3":
            dns_lookup()
            input("\nPress ENTER...")

        elif choice == "0":
            break

        else:
            print("[!] Invalid option.")

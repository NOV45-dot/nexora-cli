import os
import sys
import socket

def run_doctor():
    print("""
==========================================
             NEXORA DOCTOR
==========================================
""")

    checks = []

    checks.append(("Python", sys.version.split()[0]))

    try:
        socket.gethostbyname("example.com")
        checks.append(("Internet/DNS", "OK"))
    except Exception:
        checks.append(("Internet/DNS", "Unavailable"))

    folders = [
        "nexora",
        "nexora/modules",
        "nexora/data",
        "tests"
    ]

    for folder in folders:
        if os.path.isdir(folder):
            checks.append((folder, "OK"))
        else:
            checks.append((folder, "Missing"))

    files = [
        "nexora/main.py",
        "nexora/modules/network.py",
        "nexora/modules/security.py",
        "nexora/modules/linux.py",
        "nexora/modules/learning.py",
        "nexora/modules/scanner.py",
        "nexora/modules/status.py"
    ]

    for file in files:
        if os.path.isfile(file):
            checks.append((file, "OK"))
        else:
            checks.append((file, "Missing"))

    print("COMPONENT STATUS")
    print("------------------------------------------")

    for name, status in checks:
        print(f"[+] {name:<30} {status}")

    print("------------------------------------------")
    print("[+] NEXORA diagnostic complete.")

    input("\nPress ENTER...")


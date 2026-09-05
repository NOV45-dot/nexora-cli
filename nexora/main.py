import os
import platform
import sys
from datetime import datetime
from colorama import Fore, Style, init

from modules.network import network_menu, public_ip, dns_lookup
from modules.security import security_menu, file_hash
from modules.linux import linux_menu
from modules.learning import learning_menu
from modules.scanner import scanner_menu
from modules.status import system_status
from config import VERSION, APP_NAME, TAGLINE
from modules.doctor import run_doctor

init(autoreset=True)



def banner():
    print(Fore.CYAN + "==========================================")
    print(Fore.CYAN + "              N E X O R A")
    print(Fore.CYAN + "==========================================")
    print(Fore.WHITE + "     CYBERSECURITY & NETWORK INTELLIGENCE")
    print(Fore.YELLOW + "              Version 1.0.0")
    print(Fore.CYAN + "     Security. Intelligence. Control.")
    print(Fore.CYAN + "==========================================")
    print()

def system_info():
    print(Fore.CYAN + "\nNEXORA SYSTEM INFORMATION")
    print("--------------------------------")
    print("OS      :", platform.system())
    print("Release :", platform.release())
    print("Machine :", platform.machine())
    print("Python  :", platform.python_version())
    print("Time    :", datetime.now().strftime("%H:%M:%S"))
    input("\nPress ENTER...")

def command_mode():
    if len(sys.argv) < 2:
        return False

    command = sys.argv[1].lower()

    if command in ["--version", "-v"]:
        print(Fore.CYAN + "NEXORA v" + VERSION)

    elif command in ["--help", "-h", "help"]:
        print("""
NEXORA COMMANDS

nexora                 Open menu
nexora help            Show help
nexora --version       Show version
nexora system          System information
nexora ip              Show public IP
nexora dns <domain>    DNS lookup
nexora hash            SHA-256 file hash
nexora network         Network tools
nexora security        Security tools
nexora linux           Linux assistant
nexora learn           Learning center
nexora scan            Authorized host scanner
nexora status          System status dashboard
nexora doctor          Run NEXORA diagnostics
""")

    elif command == "ip":
        public_ip()

    elif command == "dns":
        domain = sys.argv[2] if len(sys.argv) > 2 else None
        dns_lookup(domain)

    elif command == "hash":
        file_hash()

    elif command == "system":
        system_info()

    elif command == "network":
        network_menu()

    elif command == "security":
        security_menu()

    elif command == "linux":
        linux_menu()

    elif command == "learn":
        learning_menu()

    elif command == "scan":
        if len(sys.argv) > 2:
            from modules.scanner import scan_host
            scan_host(sys.argv[2])
        else:
            scanner_menu()

    elif command == "status":
        system_status()

    elif command == "doctor":
        run_doctor()

    else:
        print(Fore.RED + "[!] Unknown command.")
        print("Use: nexora help")

    return True

def main():
    while True:
        os.system("clear")
        banner()

        print("[1] Network Intelligence")
        print("[2] Security Tools")
        print("[3] Linux Assistant")
        print("[4] Cybersecurity Learning")
        print("[5] System Information")
        print("[6] Host Scanner")
        print("[7] System Status")
        print("[8] NEXORA Doctor")
        print(Fore.RED + "[0] Exit")

        choice = input(Fore.GREEN + "\nNEXORA > " + Style.RESET_ALL).strip()

        if choice == "1":
            network_menu()
        elif choice == "2":
            security_menu()
        elif choice == "3":
            linux_menu()
        elif choice == "4":
            learning_menu()
        elif choice == "5":
            system_info()
        elif choice == "6":
            scanner_menu()
        elif choice == "7":
            system_status()
        elif choice == "8":
            run_doctor()
        elif choice == "0":
            print("\nNEXORA shutting down...")
            break
        else:
            print(Fore.RED + "\n[!] Invalid option.")
            input("Press ENTER...")

if __name__ == "__main__":
    if not command_mode():
        main()

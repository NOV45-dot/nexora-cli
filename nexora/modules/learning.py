def linux_basics():
    print("""
LINUX BASICS
------------
Linux is an operating system used widely in servers, security and development.

Important commands:
ls   - list files
pwd  - show current directory
cd   - change directory
mkdir - create a directory
cp   - copy files
mv   - move or rename files
rm   - remove files
cat  - display file contents
""")
    input("\nPress ENTER...")

def networking_basics():
    print("""
NETWORKING BASICS
-----------------
IP address  - identifies a device on a network.
DNS         - translates domain names into IP addresses.
TCP         - reliable network communication protocol.
UDP         - faster connectionless communication protocol.
Port        - identifies a network service.
Router      - forwards traffic between networks.
""")
    input("\nPress ENTER...")

def security_basics():
    print("""
CYBERSECURITY BASICS
--------------------
Authentication - verifies who you are.
Authorization  - determines what you can access.
Encryption     - protects information by encoding it.
Hashing        - creates a fixed-length representation of data.
Firewall       - controls network traffic.
MFA            - adds another authentication factor.

Always test security tools only on systems you own or have permission to test.
""")
    input("\nPress ENTER...")

def learning_menu():
    while True:
        print()
        print("==========================================")
        print("       NEXORA CYBERSECURITY ACADEMY")
        print("==========================================")
        print("[1] Linux Basics")
        print("[2] Networking Basics")
        print("[3] Cybersecurity Basics")
        print("[0] Back")
        choice = input("LEARN > ").strip()
        if choice == "1":
            linux_basics()
        elif choice == "2":
            networking_basics()
        elif choice == "3":
            security_basics()
        elif choice == "0":
            break
        else:
            print("[!] Invalid option.")

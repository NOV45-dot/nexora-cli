import hashlib
import getpass

def password_checker():
    password = getpass.getpass("Enter password: ")
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    print("[+] Strength:", levels[score])

def file_hash():
    path = input("Enter file path: ").strip()
    try:
        sha256 = hashlib.sha256()
        with open(path, "rb") as file:
            for block in iter(lambda: file.read(4096), b""):
                sha256.update(block)
        print("[+] SHA-256:", sha256.hexdigest())
    except FileNotFoundError:
        print("[!] File not found.")

def security_menu():
    while True:
        print()
        print("==========================================")
        print("           NEXORA SECURITY TOOLS")
        print("==========================================")
        print("[1] Password Strength Checker")
        print("[2] SHA-256 File Hash")
        print("[0] Back")
        choice = input("SECURITY > ").strip()

        if choice == "1":
            password_checker()
            input("Press ENTER...")
        elif choice == "2":
            file_hash()
            input("Press ENTER...")
        elif choice == "0":
            break
        else:
            print("[!] Invalid option.")

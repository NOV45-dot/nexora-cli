def linux_menu():
    while True:
        print()
        print("==========================================")
        print("          NEXORA LINUX ASSISTANT")
        print("==========================================")
        print("[1] ls      - List files")
        print("[2] pwd     - Show current directory")
        print("[3] cd      - Change directory")
        print("[4] mkdir   - Create directory")
        print("[5] cp      - Copy files")
        print("[6] mv      - Move or rename files")
        print("[7] rm      - Remove files")
        print("[8] grep    - Search text")
        print("[9] chmod   - Change permissions")
        print("[0] Back")
        choice = input("LINUX > ").strip()
        commands = {
            "1": ("ls", "Lists files and directories."),
            "2": ("pwd", "Shows your current working directory."),
            "3": ("cd <directory>", "Changes to another directory."),
            "4": ("mkdir <name>", "Creates a new directory."),
            "5": ("cp <source> <destination>", "Copies a file or directory."),
            "6": ("mv <source> <destination>", "Moves or renames a file."),
            "7": ("rm <file>", "Removes a file. Use carefully."),
            "8": ("grep <text> <file>", "Searches for text inside a file."),
            "9": ("chmod <permissions> <file>", "Changes file permissions.")
        }
        if choice == "0":
            break
        elif choice in commands:
            command, explanation = commands[choice]
            print()
            print("[+] Command:", command)
            print("[+] Description:", explanation)
            input("\nPress ENTER...")
        else:
            print("[!] Invalid option.")

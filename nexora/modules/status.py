import platform
import socket
import shutil

def system_status():
    print("""
==========================================
          NEXORA SYSTEM STATUS
==========================================
""")

    print("[+] OS       :", platform.system())
    print("[+] Release  :", platform.release())
    print("[+] Machine  :", platform.machine())
    print("[+] Python   :", platform.python_version())

    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print("[+] Hostname :", hostname)
        print("[+] Local IP :", local_ip)
    except Exception:
        print("[!] Network information unavailable.")

    try:
        total, used, free = shutil.disk_usage("/")
        print("[+] Storage  :", round(used / (1024**3), 2), "GB used")
        print("[+] Free     :", round(free / (1024**3), 2), "GB free")
    except Exception:
        print("[!] Storage information unavailable.")

    print("\n[+] NEXORA status check complete.")
    input("\nPress ENTER...")

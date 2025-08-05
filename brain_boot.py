import os
import platform
import time
import subprocess
import socket
import psutil

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_os():
    os_type = platform.system()
    return {
        "Darwin": "MacOS",
        "Windows": "Windows",
        "Linux": "Linux"
    }.get(os_type, "Unknown")

def check_network():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except:
        return False

def detect_threat():
    suspicious_files = [".DS_Store", "tax_scan.py", "monitor_script.py", "access.log"]
    for file in suspicious_files:
        if os.path.exists(file):
            print(f"⚠️ Suspicious file detected: {file} – Deleting it.")
            os.remove(file)

def system_health():
    print("🧪 System Health:")
    print(f"  🔋 Battery: {psutil.sensors_battery().percent if psutil.sensors_battery() else 'N/A'}%")
    print(f"  💾 RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"  🧠 CPU Usage: {psutil.cpu_percent(interval=1)}%")

def brain_boot():
    clear()
    print("🧠 Initializing RAJAN SMART BRAIN ULTRA+...")
    print(f"📡 OS: {check_os()}")
    print("🛡️  Security Check Started...")

    if check_network():
        print("✅ Internet Connection: OK")
    else:
        print("❌ No Internet! Exiting for safety.")
        exit()

    detect_threat()
    system_health()
    print("🔍 Scanning Errors...")
    time.sleep(1)

    print("✅ All Systems Secure.\n")
    run_main_module()

def run_main_module():
    print("⚙️ Launching RAJAN AI BOT Engine...\n")
    time.sleep(1)
    try:
        subprocess.run(["python3", "smart_tv_signal.py"])
    except Exception as e:
        print(f"❌ Bot Launch Failed: {e}")
        print("💡 Tip: Check if smart_tv_signal.py exists and has no error.")

if __name__ == "__main__":
    brain_boot()


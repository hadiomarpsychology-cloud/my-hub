import time
import subprocess
import os

print("⚡ Hub Auto-Sync Bridge Active. Waiting for updates...")

while True:
    if os.path.exists("pending_update.py"):
        print("🔄 Applying new changes automatically...")
        subprocess.run(["python3", "pending_update.py"])
        os.remove("pending_update.py")
        subprocess.run(["git", "add", "index.html"])
        subprocess.run(["git", "commit", "-m", "Auto-sync update from Gemini collaboration"])
        subprocess.run(["git", "push", "origin", "main"])
        print("✅ Changes pushed live successfully!")
    time.sleep(2)

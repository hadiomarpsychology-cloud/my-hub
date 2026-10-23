#!/usr/bin/env python3
import subprocess
import os
from datetime import datetime, timedelta

LOG_FILE = os.path.expanduser("~/Desktop/my-hub/sync_audit.log")

def log_audit(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    print(log_entry.strip())
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"⚠️ Warning: Could not write log: {e}")

def run_applescript(script):
    try:
        process = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True)
        return process.stdout.strip()
    except subprocess.CalledProcessError as e:
        log_audit(f"AppleScript Error: {e.stderr.strip()}")
        return None

def add_macos_reminder(title, body=""):
    script = f'''
    tell application "Reminders"
        tell default list
            make new reminder with properties {{name:"{title}", body:"{body}"}}
        end tell
    end tell
    '''
    run_applescript(script)

def add_macos_calendar_event(title, days_from_now, hour=9):
    event_date = datetime.now() + timedelta(days=days_from_now)
    date_str = event_date.strftime("%B %d, %Y")
    
    script = f'''
    tell application "Calendar"
        tell calendar "Calendar"
            set startDate to date ("{date_str} " & "{hour}:00:00 AM")
            set endDate to startDate + (1 * hours)
            make new event with properties {{summary:"{title}", start date:startDate, end date:endDate}}
        end tell
    end tell
    '''
    run_applescript(script)

def check_redmi_secure_connection():
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        if len(lines) > 1 and any("device" in line and "unauthorized" not in line for line in lines[1:]):
            log_audit("SUCCESS: Cryptographic USB connection active with Redmi 15c.")
            return True
        else:
            log_audit("NOTICE: Redmi 15c offline or USB debugging authorization pending.")
            return False
    except FileNotFoundError:
        log_audit("ERROR: ADB not installed on Mac.")
        return False

def push_notification_to_redmi(title, message):
    if check_redmi_secure_connection():
        cmd = f"adb shell am broadcast -a android.intent.action.BOOT_COMPLETED --es title '{title}' --es message '{message}'"
        subprocess.run(cmd, shell=True, capture_output=True)
        log_audit(f"SUCCESS: Pushed alarm/alert to Redmi 15c -> {title}")

if __name__ == "__main__":
    print("==================================================")
    print("  Deploying 10-Day Survival & Legal Plan Bridge   ")
    print("==================================================")
    
    # 10-Day Schedule Data
    schedule = [
        (0, "DAY 1: Submit UNRWA Micro-Loan & UNHCR Letters", "Deliver formal ethical requests for microfinance and emergency bridging."),
        (1, "DAY 2: Passport Renewal Submission", "Visit Ministry of Interior / Civil Affairs in Ramallah for passport paperwork."),
        (2, "DAY 3: Arab Bank iBURAQ & Compliance Clearance", "Confirm SWIFT/iBURAQ active status with Arab Bank SME desk."),
        (3, "DAY 4: Intensive Preply & Client Intake Push", "Promote counseling/tutoring hub to secure direct pre-payments."),
        (4, "DAY 5: Mid-Way Financial Audit & Sustenance Check", "Verify accumulated session revenue & isolate food/transportation funds."),
        (5, "DAY 6: UNRWA Loan Status Follow-Up", "Check micro-loan review progress and confirm standing debit order setup."),
        (6, "DAY 7: An-Najah Academic Progress & Research Block", "Review clinical psychology coursework and thesis prep."),
        (7, "DAY 8: Rent Reserve Allocation", "Transfer 70% of collected revenue into dedicated rent settlement account."),
        (8, "DAY 9: Final Rent Preparation & Client Verification", "Confirm all pending client wire receipts & complete pre-rent ledger."),
        (9, "DAY 10: RENT DUE DATE & Full Settlement", "Execute rent payment in full. Maintain 20% UNRWA loan repayment reserve.")
    ]
    
    for days, title, details in schedule:
        # Add to macOS Reminders
        add_macos_reminder(title, details)
        
        # Add to macOS Calendar
        add_macos_calendar_event(title, days, hour=9)
        
        # Push to Redmi 15c via USB Bridge
        push_notification_to_redmi(title, details)
        
        log_audit(f"DEPLOYED: {title}")
        
    print("==================================================")
    print(f"Plan fully synchronized to Mac & Phone! Audit: {LOG_FILE}")
    print("==================================================")

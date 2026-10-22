#!/usr/bin/env python3
import json, subprocess, sys

DATA = {
    "1. Personal Info": {
        "First Name": "Hadi",
        "Last Name": "Omar",
        "Email": "hadiaugustpsychology@gmail.com",
        "Website": "https://hadiomarpsychology-cloud.github.io/my-hub/",
        "Country": "Autonomous Palestinian Territories",
        "Nationality": "Jordanian"
    },
    "2. Education": {
        "M.Sc. Title": "Master of Science in Clinical Psychology (Candidate)",
        "M.Sc. Org": "An-Najah National University",
        "M.Sc. Details": "Advanced clinical psychology, psychopathology, clinical assessment, research methodology, and supervised psychological counseling.",
        "B.A. Title": "Bachelor of Arts in Psychology",
        "B.A. Org": "Birzeit University",
        "UK Foundation": "Higher Education Studies in Psychology (FHEQ Levels 4 & 5) - University of Sussex / University of Sheffield"
    },
    "3. Work Experience": {
        "Counseling Role": "Psychological Counselor & Clinical Practitioner",
        "Counseling Org": "Global Resonance Practice / Private Practice",
        "Counseling Details": "Individual, couples, and group psychotherapy. Completed 480 supervised clinical hours at the Palestinian Counseling Center plus 100 field hours.",
        "Tutor Role": "Academic & Language Tutor",
        "Tutor Details": "Delivering language instruction and academic mentoring to international students ($30/hr)."
    },
    "4. Skills": {
        "Languages": "Arabic (Native), English (C2 - Proficient)",
        "Digital Skills": "Qualitative & Quantitative Research Design, Web Development (GitHub Pages / Git), Audio & Video Editing, Technical Writing"
    }
}

def copy_to_clipboard(text):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(text.encode('utf-8'))

def main():
    while True:
        print("\n================ EUROPASS AUTO-COPY TOOL ================")
        categories = list(DATA.keys())
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {cat}")
        print("0. Exit")
        
        choice = input("\nSelect section number (or 0 to quit): ").strip()
        if choice == '0':
            break
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(categories):
            continue
            
        selected_cat = categories[int(choice) - 1]
        items = list(DATA[selected_cat].items())
        
        while True:
            print(f"\n--- {selected_cat} ---")
            for idx, (label, val) in enumerate(items, 1):
                print(f"  {idx}. {label}: {val[:60]}...")
            print("  0. Back to Main Menu")
            
            sub_choice = input("\nSelect field number to COPY to clipboard: ").strip()
            if sub_choice == '0':
                break
            if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(items):
                label, val = items[int(sub_choice) - 1]
                copy_to_clipboard(val)
                print(f"\n✅ COPIED TO CLIPBOARD: '{val}'\n   (Now press Cmd+V in browser)")

if __name__ == "__main__":
    main()

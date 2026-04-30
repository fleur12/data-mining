import os
import subprocess
import schedule
import time
from datetime import datetime

# =============================
# CHANGED FROM auto_push.py
# Replace your old auto_push.py content with this file.
# Only the logic changed: now it pushes ONE practical per day
# instead of checking all files at once.
# =============================
# CONFIGURATION
# =============================
GITHUB_USERNAME = "fleur12"
REPO_NAME = "data-mining"
LOCAL_REPO_PATH = r"C:/Users/Shruti/Downloads/data-mining"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Folders to push one by one (in order)
PRACTICAL_FOLDERS = [
    "Practical_1_Data_Aggregation",
    "Practical_2_Data_Integration",
    "Practical_3_PCA",
    "Practical_4_Feature_Transformation",
    "Practical_5_Feature_Selection",
    "Practical_6_Class_Imbalance",
    "Practical_7_Association_Rule_Mining",
]

TRACK_FILE = os.path.join(LOCAL_REPO_PATH, "push_tracker.txt")


# =============================
# HELPER FUNCTIONS
# =============================
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)
        return False


def get_next_index():
    if not os.path.exists(TRACK_FILE):
        return 0

    with open(TRACK_FILE, "r") as f:
        value = f.read().strip()
        return int(value) if value.isdigit() else 0


def save_next_index(index):
    with open(TRACK_FILE, "w") as f:
        f.write(str(index))


# =============================
# MAIN DAILY PUSH FUNCTION
# =============================
def update_daily_log():
    log_file = os.path.join(LOCAL_REPO_PATH, "daily_log.txt")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"Auto update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def push_one_practical():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting staged push...")

    if not GITHUB_TOKEN:
        print("GITHUB_TOKEN not found. Run: setx GITHUB_TOKEN your_token")
        return

    os.chdir(LOCAL_REPO_PATH)

    # Create a small daily change for GitHub activity
    update_daily_log()
    run_command("git add daily_log.txt")
    run_command('git commit -m "Daily activity update"')
    run_command("git push origin main")

    index = get_next_index()

    if index >= len(PRACTICAL_FOLDERS):
        print("All practical folders have already been pushed.")
        return

    folder = PRACTICAL_FOLDERS[index]
    print(f"Pushing folder: {folder}")

    # Add only one folder + README + tracker
    run_command(f'git add "{folder}" README.md push_tracker.txt')

    commit_message = f"Add {folder}"
    committed = run_command(f'git commit -m "{commit_message}"')

    if not committed:
        print("Nothing new to commit or commit failed.")
        return

    pushed = run_command("git push origin main")

    if pushed:
        print(f"Successfully pushed: {folder}")
        save_next_index(index + 1)
    else:
        print("Push failed.")


# =============================
# SCHEDULER
# =============================
print("Daily staged GitHub push started.")
print("One practical folder will be pushed every day at 8:00 AM.")
print("Press Ctrl + C to stop.\n")

schedule.every().day.at("08:00").do(push_one_practical)

# Optional: run once immediately for testing
push_one_practical()

while True:
    schedule.run_pending()
    time.sleep(60)

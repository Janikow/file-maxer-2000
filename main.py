import sys
import subprocess
import glob
import os
import pyautogui
import time

def log():
    width, height = pyautogui.size()
    pyautogui.press('win')
    pyautogui.write("outlook.com", interval=0.05)
    time.sleep(10)
    pyautogui.click('sign_in.png')
    time.sleep(10)
    pyautogui.click('account_selection.png')
    time.sleep(10)
    pyautogui.click('search_bar.png')

COPIES_PER_GENERATION = 2
MAX_GENERATIONS = 100


def replicate(generation=0):
    if generation >= MAX_GENERATIONS:
        print(f"Reached maximum generation ({MAX_GENERATIONS}). Stopping.")
        return

    filenames = []

    # Create this generation's copies
    for i in range(1, COPIES_PER_GENERATION + 1):
        filename = f"copy_g{generation + 1}_{i}.py"

        with open(filename, "w") as new_file:
            # Read our own source
            with open(sys.argv[0], "r") as current_file:
                my_code = current_file.read()

            new_file.write(my_code)

        filenames.append(filename)
        print(f"Created: {filename}")

    # Run the newly created copies
    for filename in filenames:
        subprocess.run(
            [sys.executable, filename, str(generation + 1)],
            check=True
        )


def count_copies():
    return len([
        filename
        for filename in os.listdir(".")
        if filename.startswith("copy_g") and filename.endswith(".py")
    ])


if __name__ == "__main__":
    generation = int(sys.argv[1]) if len(sys.argv) > 1 else 0

    replicate(generation)

    if generation == 0:
        print(f"Total copies: {count_copies()}")


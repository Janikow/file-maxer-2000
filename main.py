import sys
import subprocess
import glob
import os

def count_copies():
    copies = glob.glob("copy_*.py")
    return len(copies)

def replicate():
    with open(sys.argv[0], 'r') as current_file:
        my_code = current_file.read()

    number_of_copies = 2

    for i in range(1, number_of_copies + 1):
        filename = f"copy_{i}.py"

        with open(filename, 'w') as new_file:
            new_file.write(my_code)

        print(f"Created: {filename}")

        subprocess.run([sys.executable, filename])

if __name__ == "__main__":
    replicate()
    count_copies()
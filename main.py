import sys
import subprocess

def replicate():
    with open(sys.argv[0], "r") as current_file:
        my_code = current_file.read()

    number_of_copies = 2
    filenames = []

    # Phase 1: create all copies
    for i in range(1, number_of_copies + 1):
        filename = f"copy_{i}.py"

        with open(filename, "w") as new_file:
            new_file.write(my_code)

        filenames.append(filename)
        print(f"Created: {filename}")

    # Phase 2: run all copies
    for filename in filenames:
        subprocess.run([sys.executable, filename])

if __name__ == "__main__":
    replicate()

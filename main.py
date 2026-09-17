import sys
import subprocess
import glob
import os

MAX_STORAGE = 100 * 1024 * 1024  # 100 MB


def storage_used():
    """Return total bytes used by copy_*.py files."""
    return sum(
        os.path.getsize(filename)
        for filename in glob.glob("copy_*.py")
        if os.path.isfile(filename)
    )


def replicate():
    with open(sys.argv[0], "r") as current_file:
        my_code = current_file.read()

    copy_number = 1

    while storage_used() < MAX_STORAGE:
        filename = f"copy_{copy_number}.py"

        # Don't create a copy if it would exceed the limit.
        code_size = len(my_code.encode("utf-8"))

        if storage_used() + code_size > MAX_STORAGE:
            print("Storage limit reached. Stopping.")
            break

        with open(filename, "w") as new_file:
            new_file.write(my_code)

        print(f"Created: {filename}")
        print(f"Storage used: {storage_used() / (1024 * 1024):.2f} MB")

        # Run the copy
        subprocess.run([sys.executable, filename])

        copy_number += 1


if __name__ == "__main__":
    replicate()

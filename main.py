import sys

def replicate():
    # Open the current running script file and read its contents
    with open(sys.argv[0], 'r') as current_file:
        my_code = current_file.read()
    
    # Define how many new copies you want to make
    number_of_copies = 3
    
    # Loop to write the exact same code into new files
    for i in range(1, number_of_copies + 1):
        filename = f"copy_{i}.py"
        with open(filename, 'w') as new_file:
            new_file.write(my_code)
        print(f"Created: {filename}")

if __name__ == "__main__":
    replicate()

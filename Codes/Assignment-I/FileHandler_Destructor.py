# Problem Statement:
# Create a Python class named FileHandler that represents a simple file handler. The class should have the following features:

# The class should have an initializer (__init__) that takes a filename and a mode as parameters and opens the file in the specified mode.
# Implement a method write_data(self, data) to write data to the file.
# Include a destructor (__del__) that ensures the file is closed when the object is destroyed.

# Sample Input:
# No direct input is required for this code. It demonstrates the usage of the FileHandler class.

# Sample Output:
# File 'example.txt' opened in 'w' mode.
# Data written to 'example.txt'.
# File 'example.txt' closed.



class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)
        print(f"File '{filename}' opened in '{mode}' mode.")

    def write_data(self, data):
        self.file.write(data)
        print(f"Data written to '{self.filename}'.")

    def __del__(self):
        # Destructor to close the file when the object is destroyed
        if hasattr(self, 'file') and not self.file.closed:
            self.file.close()
            print(f"File '{self.filename}' closed.")

file_writer = FileHandler("example1.txt", "w")
file_writer.write_data("Hello, this is a sample text.")
# The object goes out of scope here, and the destructor is automatically called.





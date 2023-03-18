# File Deletion Program

This is a simple Python program that deletes files from specific directories on your computer. The program uses a graphical user interface (GUI) created with the tkinter library to display the results of the file deletion.

## Usage

To use the program, simply run the `main.py` file in a Python environment. The program will delete files from the following directories:

- C:\Windows\Prefetch
- C:\Windows\Temp
- C:\Users\user\AppData\Local\Temp

After the program has finished deleting files, a GUI window will appear showing the number of files that were successfully deleted.

## Installation

To install the program, you can either clone this repository or download the source code as a ZIP file. Then, you can run the program by navigating to the directory where the code is saved and running the command `python main.py`.

Alternatively, you can use the PyInstaller library to create an executable file from the code. To do this, simply run the command `pyinstaller --onefile --icon=myicon.ico main.py` in the terminal. This will create an executable file in the `dist` directory.

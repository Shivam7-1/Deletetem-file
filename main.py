import os
import tkinter as tk
from tkinter import messagebox

# Define the directories to clean
dirs_to_clean = ["C:\\Windows\\Prefetch", "C:\\Windows\\Temp", "C:\\Users\\user\\AppData\\Local\\Temp"]

# Clean the directories
deleted_files = []
for directory in dirs_to_clean:
    for file_name in os.listdir(directory):
        try:
            os.remove(os.path.join(directory, file_name))
            deleted_files.append(file_name)
        except:
            pass

# Create the GUI output
root = tk.Tk()
root.title("File Deletion Results")
message = f"{len(deleted_files)} files deleted successfully:\n\n" + "\n".join(deleted_files)
result_label = tk.Label(root, text=message)
result_label.pack(pady=10)
ok_button = tk.Button(root, text="OK", command=root.destroy)
ok_button.pack(pady=10)
root.mainloop()
